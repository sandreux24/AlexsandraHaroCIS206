def calc_BMI(weight, heightFeet, heightInches):

    totalHeight = heightFeet * 12 + heightInches

    bmi = (weight / totalHeight ** 2) * 703

    return bmi


def interpretBMI(bmi):

    if bmi < 18.5:

        return "Underweight"

    elif 18.5 <= bmi < 25:

        return "Normal weight"

    elif  25 <= bmi < 30:

        return "Over weight"

    else:

        return "Obese"

   

if __name__ == "__main__":

    weight = float(input("Enter weight in pounds:"))

    heightFeet = float(input("Enter height in feet:"))

    heightInches = float(input("Enter height in inches:"))

   

    bmi = calc_BMI(weight, heightFeet, heightInches)
    interpretBMI_result = interpretBMI(bmi)

    print(f"Your BMI is {bmi:.2f}, which is considered {interpretBMI_result}.")
