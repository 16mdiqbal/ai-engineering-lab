"""
program to print the names of all the employess along with their serial numbers stored in list. 
"""
def get_employee_name() -> None:
    employees = ["Alice", "Bob", "Charlie", "David", "Eve"]

    for index, name in enumerate(employees, start=1):
        print(f"{index}. {name}")



if __name__ == "__main__":
    get_employee_name()       