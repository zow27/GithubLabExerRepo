def mean(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return None
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mode(numbers):
    if not numbers:
        return None
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    modes = [num for num, count in freq.items() if count == max_count]
    if len(modes) == 1:
        return modes[0]
    return modes
