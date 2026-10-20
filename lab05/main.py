from logstats import parse_event, count_levels, top_errors, format_report

path = input().strip()

total = errors = broken = 0
with open(path, encoding="utf-8") as log:
    for line in log:
        if not line.strip():
            continue
        total += 1
        try:
            event = parse_event(line)
        except ValueError:
            broken += 1
        else:
            if event["level"] == "ERROR":
                errors += 1

print(total)
print(errors)
print(broken)

with open(path, encoding="utf-8") as log:
    counts = count_levels(log)ss
with open(path, encoding="utf-8") as log:
    top = top_errors(log, 3)

with open("report.txt", "w", encoding="utf-8") as out:
    out.write(format_report(counts, top))