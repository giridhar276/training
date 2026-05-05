
#Validate marks before calculating grade

def validate_marks(func):
    def wrapper(marks):
        if 0 <= marks <= 100:
            return func(marks)
        else:
            print("Invalid marks")
    return wrapper

@validate_marks
def calculate_grade(marks):
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    else:
        print("Grade C")

calculate_grade(85)
calculate_grade(120)