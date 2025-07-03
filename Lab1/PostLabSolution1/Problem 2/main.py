
def main():
    try:
        path = input("Filename: ")
        lines = open(path).read().splitlines()
    except Exception:
        print("Cannot open file.")
        return

    print(f"Loaded {len(lines)} lines.")
    while True:
        idx = input("Line # (0 to exit): ")
        if not idx.isdigit():
            print("Enter a number.")
            continue
        i = int(idx)
        if i == 0:
            print("Goodbye.")
            break
        if 1 <= i <= len(lines):
            print(lines[i-1])
        else:
            print(f"Pick 1–{len(lines)}.")

if __name__ == '__main__':
    main()
