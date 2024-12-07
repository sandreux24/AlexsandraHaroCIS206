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

        return "Overweight"

    else:

        return "Obese"

def validateInput(prompt):
    while True:
        userInput = input(prompt)
        if userInput.lower() == "exit":
         return None
        try:
         value = float(userInput)
         if value < 0:
            print(f"Error: Value entered must be positive.")
            continue
         return value
        except ValueError:
           print(f"Error: Invalid input. Enter a valid number.")

def displayBMItable():
   
   print(r'{"Weight // Height":<15}', end="")
   for weight in range (100, 260, 10):
     print(f"{weight:<15}", end="")
     for totalHeight in range (58, 77, 2):
        heightFeet = totalHeight // 12
        heightInches = totalHeight % 12
        bmi = calc_BMI(weight, heightFeet, heightInches)
        print(f"{bmi:.1f}<10", end="")
        print()
    
        
       
   
if __name__ == "__main__":
 displayBMItable()

 while True:
    print(f"Type 'exit' at any point to exit.")

    weight = validateInput("Enter weight in pounds:")
    if weight is None:
       break

    heightFeet = validateInput("Enter height in feet:")
    if heightFeet is None:
       break

    heightInches = validateInput("Enter height in inches:")
    if heightFeet is None:
       break

    bmi = calc_BMI(weight, heightFeet, heightInches)
    interpretBMI_result = interpretBMI(bmi)

    print(f"Your BMI is {bmi:.2f}, which is considered {interpretBMI_result}.")
 
    continueInput = input(f"Would you like to calculate another BMI? Type 'yes' or 'exit' to exit program. ")
    if continueInput == "exit":
       break

 print(f"Thanks for using program.") 
