def getBodyShape(bust, waist, hip):
    waistHipRatio = waist / hip
    bustWaistRatio = bust / waist

    #Nested if statements
    if waistHipRatio < 0.8 and bustWaistRatio > 1.05:
        return "Hourglass"
    elif waistHipRatio >= 0.8 and bustWaistRatio < 1.05:
        return "Pear"
    elif waistHipRatio >= 0.8 and bustWaistRatio >= 1.05:
        return "Apple"
    elif waistHipRatio < 0.8 and bustWaistRatio <= 1.05:
        return "Rectangle"
    else:
        return "Undefined"

if __name__ == "__main__":
  #Data type validation 
  import sys 
  
  try:
    bust = float(input("Enter bust measurement in inches:"))
    #Range Validation
    if bust <= 0:
       raise ValueError("Bust measurement must be greater than zero.")

    hip = float(input("Enter hip measurement in inches: "))
    #Range Validation
    if hip <= 0:
       raise ValueError("Hip measurement must be greater than zero.") 
    
    waist = float(input("Enter waist measurement in inches:"))
    #Range Validation
    if waist <= 0:
       raise ValueError("Waist measurement must be greater than zero.")
  

  except ValueError as e:
   print(f"Invalid input: {e}")
   sys.exit()

  bodyShape = getBodyShape(bust, waist, hip)
  print(f"You've entered {bust}in. for bust measurement. ")
  print(f"You've entered {waist}in. for waist measurement.")
  print(f"You've entered {hip}in for the hip measurement.")
  print(f"Given the measurements above, body shape is {bodyShape}.")

