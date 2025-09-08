class Student:

    def __init__(self, name: str, grade: str, department: str):
        self.name = name
        self.grade = grade
        self.department = department

    def print_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}, Department: {self.department}")    
        
    def update_grade(self, new_grade: str):
        self.grade = new_grade
        

if __name__ == "__main__":
    student1 = Student("Alice", "A", "Computer Science")
    student1.print_info()
    
    student2 = Student("Bob", "B", "Mathematics")
    student2.print_info()

    student3 = Student("Iqbal", "B", "AI Engineer")
    student3.print_info()
    
    # Update Iqbal's grade
    student3.update_grade("A")
    student3.print_info()        