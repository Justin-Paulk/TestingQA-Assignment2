def bmi_calc(feet, inches, weight):
    kg = pound_to_kg(weight)
    inch_height = height_to_inches(feet, inches)
    meters = inches_to_meters(inch_height)
    bmi = kg / (meters * meters)
    bmi = round(bmi, 1)
    if bmi < 18.5:
        final_bmi = ['Underweight', bmi]
    elif bmi <= 24.9:
        final_bmi = ['Normal Weight', bmi]
    elif bmi <= 29.9:
        final_bmi = ['Overweight', bmi]
    else:
        final_bmi = ['Obese', bmi]

    return final_bmi


def pound_to_kg(pounds):
    kg = pounds * 0.45
    return kg


def height_to_inches(feet, inches):
    inches = (feet * 12) + inches
    return inches


def inches_to_meters(inches):
    meters = inches * 0.025
    return meters


def retirement_calc(age, salary, prcSaved, goal):
    yearly_saved = saved_per_year(salary, prcSaved)
    retire_age = years_to_goal(yearly_saved, goal) + age
    return retire_age


def saved_per_year(salary, prcSaved):
    saved = (salary * prcSaved) + ((salary * prcSaved) * 0.35)
    return saved


def years_to_goal(yearly_saved, goal):
    return goal / yearly_saved


def check_init_input(user_input):
    if user_input == '1' or user_input == '2' or user_input == '3':
        return True
    else:
        return False


def handle_bmi_input(user_input):
    newVal = user_input.split()
    result = bmi_calc(int(newVal[0]), int(newVal[1]), float(newVal[2]))
    return result


def handle_retirement_input(user_input):
    newVal = user_input.split()
    if float(newVal[2]) > 1.0:
        raise ValueError('Percent Cannot be Over 1.0')
    result = retirement_calc(float(newVal[0]), float(newVal[1]), float(newVal[2]), float(newVal[3]))
    return result

if __name__ == '__main__':
    run = True
    while run:
        print("Please enter the integer value beside the function you wish to use")
        print("1. BMI Calculator")
        print("2. Retirement Savings Calculator")
        print('3. Exit')

        val = input()

        if not check_init_input(val):
            print("Invalid Input. Please enter a valid integer")


        if val == '1':
            print("Please enter the height in feet and inches followed by the weight in pounds")
            print("Ex: 5 8 150")
            val = input()

            result = handle_bmi_input(val)

            print(result[0], ": ", result[1])
        elif val == '2':
            print("Please enter the current age, salary, percent saved, and retirement goal")
            print("Ex: 21 100000 0.15 500000")
            val = input()
            result = round(handle_retirement_input(val), 1)

            print("Goal will be met at ", result, " years old.")

            if result >= 100:
                print("The savings goal will not be met.")

        elif val == '3':
            print("Closing software")
            run = False
