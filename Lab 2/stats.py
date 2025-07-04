def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mode(numbers):
    if not numbers:
        return 0
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_freq]
    return modes[0] if len(modes) == 1 else modes  # Return the single mode or list

def main():
    sample = [4, 1, 2, 2, 3, 5, 4]
    print("Sample data:", sample)
    print("Mean:", mean(sample))
    print("Median:", median(sample))
    print("Mode:", mode(sample))

if __name__ == "__main__":
    main()
