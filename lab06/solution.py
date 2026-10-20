def count_by_extension(paths):
    """Словарь «расширение → сколько файлов»; расширение в нижнем регистре, без точки."""
    counts = {}
    for path in paths:
        name = path.rsplit("/", 1)[-1]
        if "." in name:
            ext = name.rsplit(".", 1)[-1].lower()
        else:
            ext = ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths):
    """Путь с наибольшей вложенностью; при равенстве — первый по алфавиту."""
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))


def human_size(n_bytes):
    """Размер в удобных единицах: 1536 -> «1.5 КБ»."""
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    value = float(n_bytes)
    idx = 0
    while value >= 1024 and idx < len(units) - 1:
        value /= 1024
        idx += 1
    return f"{value:.1f} {units[idx]}"