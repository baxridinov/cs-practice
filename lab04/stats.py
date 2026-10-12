"""Функции обработки журнала наблюдений."""


def parse_record(line: str) -> dict:
    """Разбирает строку 'город;температура;дата'. Негодная строка → ValueError."""
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("Запись должна содержать ровно три поля: город;температура;дата")

    city, temp_str, date = parts
    city = city.strip()
    temp_str = temp_str.strip()
    date = date.strip()

    if not city or not date:
        raise ValueError("Город и дата не должны быть пустыми")

    try:
        temperature = float(temp_str)
    except ValueError as exc:
        raise ValueError(f"Температура не является числом: {temp_str!r}") from exc

    return {"city": city, "temperature": temperature, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records


def average_by_city(records: list[dict]) -> dict:
    sums = {}
    counts = {}
    for record in records:
        city = record["city"]
        temperature = record["temperature"]
        sums[city] = sums.get(city, 0.0) + temperature
        counts[city] = counts.get(city, 0) + 1
    return {city: round(sums[city] / counts[city], 1) for city in sums}


def warmest_city(records: list[dict]) -> str:
    sums = {}
    counts = {}
    for record in records:
        city = record["city"]
        temperature = record["temperature"]
        sums[city] = sums.get(city, 0.0) + temperature
        counts[city] = counts.get(city, 0) + 1

    if not sums:
        return ""

    max_avg = max(sums[city] / counts[city] for city in sums)
    candidates = [city for city in sums if sums[city] / counts[city] == max_avg]
    return min(candidates)