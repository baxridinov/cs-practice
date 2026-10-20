def parse_event(line: str) -> dict:
    """Строка журнала -> {"time", "level", "message"} или ValueError."""
    parts = line.strip().split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("недостаточно частей в строке")
    time, level, message = parts
    if level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
        raise ValueError("незнакомый уровень")
    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    """Сколько строк каждого уровня; негодные -> BROKEN. Пустые пропускаем."""
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
        else:
            lvl = event["level"]
            counts[lvl] = counts.get(lvl, 0) + 1
    return counts


def top_errors(lines, n: int) -> list:
    """n самых частых сообщений ERROR: [сообщение, сколько раз], при равенстве — по алфавиту."""
    freq = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            msg = event["message"]
            freq[msg] = freq.get(msg, 0) + 1
    ordered = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return [[msg, cnt] for msg, cnt in ordered[:n]]


def format_report(counts: dict, errors: list) -> str:
    """Текст отчёта по готовым подсчётам. Уровни — по алфавиту, в конце перевод строки."""
    out = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        out.append(f"{level}: {counts[level]}")
    out.append("")
    out.append("Частые ошибки:")
    for msg, cnt in errors:
        out.append(f"- {msg} — {cnt}")
    return "\n".join(out) + "\n"