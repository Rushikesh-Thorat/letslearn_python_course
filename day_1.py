def calculategrade(marks):
    if 90 <= marks <= 100:
        return "A+"
    elif 80 <= marks < 90:
        return "A"
    elif 70 <= marks < 80:
        return "B"
    elif 60 <= marks < 70:
        return "C"
    elif 50 <= marks < 60:
        return "D"
    elif 0 <= marks < 50:
        return "F"
    else:
        return "Invalid Input "


def main():
    while True:
        try:
            marks = float(input("Enter the marks of student 0 to 100: "))
            if 0 <= marks <= 100:
                grade = calculategrade(marks)
                print(f"The grade for the student is: {grade}")
            else:
                print("  enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input! ")
        
        exit_choice = input(" calculate grade for another student? (yes/no): ")
        if exit_choice.lower() != "yes":
            print("Exit.")
            break


if __name__ == "__main__":
    main()
