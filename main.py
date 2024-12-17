import math 
 
def calculate_bmi(weight, height): 
    # Convert height from cm to meters 
    height_in_meters = height / 100 
    # BMI Calculation: BMI = weight / (height_in_meters^2) 
    bmi = weight / (height_in_meters ** 2) 
    return bmi 
 
def bmi_interpretation(bmi): 
    if bmi < 18.5: 
        return "Underweight" 
    elif 18.5 <= bmi < 25: 
        return "Normal weight" 
    elif 25 <= bmi < 30: 
        return "Overweight" 
    else: 
        return "Obese" 
 
def main(): 
    # Input from the user 
    try: 
        weight = float(input("Enter your weight in kilograms: ")) 
        height = float(input("Enter your height in centimeters: ")) 
 
        # Ensure valid input 
        if weight <= 0 or height <= 0: 
            print("Weight and height must be positive values.") 
            return 
 
        # Calculate BMI 
        bmi = calculate_bmi(weight, height) 
 
        # Print results 
        print(f"Your BMI is: {bmi:.2f}") 
        print(f"Interpretation: {bmi_interpretation(bmi)}") 
 
    except ValueError: 
        print("Please enter valid numeric values for weight and height.") 
if __name__ == "__main__": 
main()
