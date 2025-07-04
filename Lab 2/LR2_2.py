def main():
    filename = input("Enter filename: ")
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        while True:
            print(f"\nTotal lines: {len(lines)}")
            line_num = int(input("Enter line number (0 to quit): "))

            if line_num == 0:
                break
            elif 1 <= line_num <= len(lines):
                print("Line", line_num, ":", lines[line_num - 1].strip())
            else:
                print("Invalid line number.")
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

if __name__ == "__main__":
    main()
