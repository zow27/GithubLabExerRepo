import random
from itertools import count

def main():
    try:
        low, high = map(int, (input("Enter the smaller number: "),
                              input("Enter the larger number: ")))
    except ValueError:
        print("⚠️ Please enter valid integers.")
        return

    if low >= high:
        print("⚠️ Lower bound must be less than upper bound.")
        return

    target = random.randint(low, high)

    for tries in count(1):
        try:
            guess = int(input(f"Guess a number between {low} and {high}: "))
        except ValueError:
            print("⚠️ That's not an integer.")
            continue

        if guess < target:
            print("Too small.")
        elif guess > target:
            print("Too large.")
        else:
            print(f"🎉 Correct! You got it in {tries} tries.")
            break
    else:
        # (This block only runs if you add a max in range, e.g. `for tries in range(1, max+1):`)
        print(f"Game over – the number was {target}.")

if __name__ == "__main__":
    main()
