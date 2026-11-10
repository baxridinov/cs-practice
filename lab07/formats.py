import json


def _to_scalar(value: str):
    """Приводит значение из учебного YAML к типу."""
    value = value.strip()
    low = value.lower()

    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        return value


def csv_to_records(text: str) -> list[dict]:
    """CSV с заголовком -> список словарей. Значения остаются строками."""
    if not text or not text.strip():
        return []

    lines = text.splitlines()
    if not lines:
        return []

    header = [cell.strip() for cell in lines[0].split(",")]
    records = []

    for line in lines[1:]:
        if not line.strip():
            continue
        values = [cell.strip() for cell in line.split(",")]
        records.append({name: value for name, value in zip(header, values)})

    return records


def parse_settings(lines: list[str]) -> dict:
    """Простой YAML -> словарь."""
    result = {}
    current_list_key = None

    for raw in lines:
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue

        if line.startswith("- "):
            if current_list_key is not None:
                item = line[2:].strip()
                result[current_list_key].append(_to_scalar(item))
            continue

        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if value == "":
                result[key] = []
                current_list_key = key
            else:
                result[key] = _to_scalar(value)
                current_list_key = None
        else:
            current_list_key = None

    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    """Дополняет записи сведениями из справочника по ключу key."""
    merged_rows = []

    for row in rows:
        info = {}
        if key in row:
            row_key = row[key]
            if row_key in extra:
                info = extra[row_key]
            elif str(row_key) in extra:
                info = extra[str(row_key)]

        merged = dict(info) if isinstance(info, dict) else {}
        merged.update(row)
        merged_rows.append(merged)

    return merged_rows


def records_to_json(records: list[dict]) -> str:
    """Список словарей -> JSON: отступ 2, ключи по алфавиту, кириллица как есть."""
    return json.dumps(
        records,
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    )
