import os

ENTRY = "I fired every night at 3 a.m. for six years and you never noticed the lights were on. Tonight they stay off."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    n = len(ENTRY.encode("utf-8"))
    print(f"LEN={n}")
    if n < 1 or n > 140 or not ENTRY.strip():
        raise SystemExit(1)


main()
