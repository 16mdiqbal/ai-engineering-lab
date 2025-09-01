"""
Assignment 04 — ATM Withdrawal

Prompts for a withdrawal amount and validates that it is a multiple of 100.
- Prints "Dispensing {amount}" when valid.
- Prints "Invalid amount" otherwise.

"""



def atm_withdrawal() -> None:
    amount = int(input("Enter withdrawal amount: ").strip())

    if amount % 100 == 0:
        print(f"Dispensing {amount}")
    else:
        print("Invalid amount")

if __name__ == "__main__":
    atm_withdrawal()        
