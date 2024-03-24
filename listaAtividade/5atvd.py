def calculate_imc(weight, height):
    #Calculates the Body Mass Index (IMC) given weight (in kilograms) and height (in meters).
    imc = weight / (height ** 2)
    return imc

def interpret_imc(imc):
    #Interprets the Body Mass Index (IMC) and returns the corresponding classification.
    if imc < IMC_UNDERWEIGHT:
        return "Underweight"
    elif imc < IMC_NORMAL:
        return "Normal weight"
    elif imc < IMC_OVERWEIGHT:
        return "Overweight"
    else:
        return "Obese"

# Constants for IMC classification thresholds
IMC_UNDERWEIGHT = 18.5
IMC_NORMAL = 24.9
IMC_OVERWEIGHT = 29.9

try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    imc = calculate_imc(weight, height)
    interpretation = interpret_imc(imc)

    print("Your IMC is:", imc)
    print("Interpretation:", interpretation)

except ValueError:
    print("Invalid input. Please enter valid numerical values for weight and height.")
