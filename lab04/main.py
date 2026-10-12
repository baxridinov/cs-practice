import sys

from stats import average_by_city, read_valid, warmest_city


def main() -> None:
    lines = sys.stdin.read().splitlines()

    records = read_valid(lines)

        # пропущенные = все строки минус пустые минус корректные
    empty_count = sum(1 for line in lines if not line.strip())
    skipped = len(lines) - empty_count - len(records)

    print(len(records))
    print(skipped)

    if not records:
        print("0.0")
        return

    averages = average_by_city(records)
    best = warmest_city(records)

    print(f"{averages[best]:.1f}")


if __name__ == "__main__":
    main()