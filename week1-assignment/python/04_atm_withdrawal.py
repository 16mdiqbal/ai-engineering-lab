"""
Assignment 04 — ATM Withdrawal

Prompts for a withdrawal amount; accepts multiples of 100 only.
"""



def atm_withdrawal() -> None:
    amount = int(input("Enter withdrawal amount: ").strip())

    if amount % 100 == 0:
        print(f"Dispensing {amount}")
    else:
        print("Invalid amount")

if __name__ == "__main__":
    atm_withdrawal()        
