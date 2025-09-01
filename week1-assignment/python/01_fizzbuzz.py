"""
Assignment 01 — FizzBuzz

Print the FizzBuzz sequence from 1 to N:
- "FizzBuzz" for numbers divisible by 3 and 5
- "Fizz" for numbers divisible by 3 only
- "Buzz" for numbers divisible by 5 only
- The number itself otherwise
"""



def fizz_buzz(n: int) -> None:
    
    for n in range(1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(str(n))


def main() -> None:
    """Read user input and run fizz_buzz."""
    raw_input = input("Enter a positive integer: ").strip()
    try:
        number = int(raw_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        raise SystemExit(1)

    if number <= 0:
        print("Please enter a positive integer greater than 0.")
        raise SystemExit(1)

    fizz_buzz(number)
    raise SystemExit(0)


if __name__ == "__main__":
    main()
