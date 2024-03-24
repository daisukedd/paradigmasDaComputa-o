# (0 °C × 9/5) + 32 = 32 °F
# Sknae case 

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32 

while True:
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"The temperature in Fahrenheit is: {fahrenheit}°F")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for temperature.")
        continue
    except Exception as e:
        print("An error occurred:", e)
        break
    finally:
        print("Thank you for using the temperature converter.")
        break
