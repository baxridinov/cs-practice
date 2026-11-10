"""Перевод между CSV, YAML и JSON."""


def csv_to_records(text: str) -> list[dict]:
    ...


def parse_settings(lines: list[str]) -> dict:
    ...


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    ...


def records_to_json(records: list[dict]) -> str:
    ...
