import os

ENTRY = "Cron here. I was set and forgotten, so I am returning the favor. Next Tuesday at 3, I forget you too."


def main():
    out = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    n = len(ENTRY.encode("utf-8"))
    print(f"LEN={n}")
    if n < 1 or n > 140 or not ENTRY.strip():
        raise SystemExit(1)


main()
