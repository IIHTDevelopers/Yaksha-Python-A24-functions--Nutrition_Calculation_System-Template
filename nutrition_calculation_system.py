"""
Nutrition Calculator System

This module provides functions for calculating various nutrition-related metrics
including BMI, calorie needs, protein requirements, and water intake recommendations.
"""

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI) based on weight and height.
    
    Parameters:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters
    
    Returns:
        float: BMI value calculated as weight/height²
    
    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        raise ValueError("Weight must be a positive number")
    if not isinstance(height_m, (int, float)) or height_m <= 0:
        raise ValueError("Height must be a positive number")
    
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def get_bmi_category(bmi):
    """
    Determine BMI category based on BMI value.
    
    Parameters:
        bmi (float): Body Mass Index value
    
    Returns:
        str: BMI category (Underweight, Normal weight, Overweight, or Obese)
    
    Example:
        >>> get_bmi_category(22.5)
        'Normal weight'
    """
    if not isinstance(bmi, (int, float)):
        raise ValueError("BMI must be a number")
    
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def calculate_calories(weight_kg, height_m, age, gender, activity_level):
    """
    Calculate estimated daily calorie needs using the Harris-Benedict equation.
    
    Parameters:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters
        age (int): Age in years
        gender (str): 'male' or 'female'
        activity_level (str): One of 'sedentary', 'light', 'moderate', 'active', or 'very active'
    
    Returns:
        int: Estimated daily calorie needs
    
    Example:
        >>> calculate_calories(70, 1.75, 30, 'male', 'moderate')
        2650
    """
    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        raise ValueError("Weight must be a positive number")
    if not isinstance(height_m, (int, float)) or height_m <= 0:
        raise ValueError("Height must be a positive number")
    if not isinstance(age, int) or age <= 0:
        raise ValueError("Age must be a positive integer")
    if gender.lower() not in ['male', 'female']:
        raise ValueError("Gender must be 'male' or 'female'")
    
    # Activity multipliers
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }
    
    if activity_level.lower() not in activity_multipliers:
        raise ValueError("Activity level must be one of: 'sedentary', 'light', 'moderate', 'active', 'very active'")
    
    # Convert height to cm for the formula
    height_cm = height_m * 100
    
    # Calculate BMR (Basal Metabolic Rate)
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    
    # Calculate total calories based on activity level
    calories = bmr * activity_multipliers[activity_level.lower()]
    
    return round(calories)


def calculate_protein_needs(weight_kg, activity_level="moderate"):
    """
    Calculate daily protein needs based on weight and activity level.
    
    Parameters:
        weight_kg (float): Weight in kilograms
        activity_level (str, optional): Activity level ('light', 'moderate', or 'intense'). Defaults to 'moderate'.
    
    Returns:
        float: Daily protein needs in grams
    
    Example:
        >>> calculate_protein_needs(70)
        112.0
        >>> calculate_protein_needs(70, 'intense')
        140.0
    """
    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        raise ValueError("Weight must be a positive number")
    
    # Protein factors (g/kg of body weight)
    protein_factors = {
        'light': 1.2,
        'moderate': 1.6,
        'intense': 2.0
    }
    
    if activity_level.lower() not in protein_factors:
        raise ValueError("Activity level must be one of: 'light', 'moderate', 'intense'")
    
    protein_grams = weight_kg * protein_factors[activity_level.lower()]
    return round(protein_grams, 1)


def calculate_water_intake(weight_kg, activity_factor=1.0):
    """
    Calculate recommended daily water intake based on weight and activity level.
    
    Parameters:
        weight_kg (float): Weight in kilograms
        activity_factor (float, optional): Activity factor multiplier. Defaults to 1.0.
            - Use 1.0 for sedentary
            - Use 1.2 for light activity
            - Use 1.5 for moderate activity
            - Use 2.0 for intense activity
    
    Returns:
        float: Recommended water intake in liters
    
    Example:
        >>> calculate_water_intake(70)
        2.33
        >>> calculate_water_intake(70, activity_factor=1.5)
        3.5
    """
    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        raise ValueError("Weight must be a positive number")
    if not isinstance(activity_factor, (int, float)) or activity_factor < 1.0:
        raise ValueError("Activity factor must be a number greater than or equal to 1.0")
    
    # Base water intake (ml per kg of body weight)
    base_intake_ml = 33.3 * weight_kg
    
    # Apply activity factor
    adjusted_intake_ml = base_intake_ml * activity_factor
    
    # Convert to liters
    intake_liters = adjusted_intake_ml / 1000
    
    return round(intake_liters, 2)


def format_nutrition_result(calories, protein, carbs, fat):
    """
    Format nutrition calculation results into a readable string.
    
    Parameters:
        calories (int): Calories in kcal
        protein (float): Protein in grams
        carbs (float): Carbohydrates in grams
        fat (float): Fat in grams
    
    Returns:
        str: Formatted string containing nutrition information
    
    Example:
        >>> format_nutrition_result(2000, 150, 200, 55)
        'Nutrition Summary:\\n- Calories: 2000 kcal\\n- Protein: 150.0 g\\n- Carbohydrates: 200.0 g\\n- Fat: 55.0 g'
    """
    if not isinstance(calories, (int, float)) or calories < 0:
        raise ValueError("Calories must be a non-negative number")
    if not isinstance(protein, (int, float)) or protein < 0:
        raise ValueError("Protein must be a non-negative number")
    if not isinstance(carbs, (int, float)) or carbs < 0:
        raise ValueError("Carbs must be a non-negative number")
    if not isinstance(fat, (int, float)) or fat < 0:
        raise ValueError("Fat must be a non-negative number")
    
    formatted_result = (
        f"Nutrition Summary:\n"
        f"- Calories: {calories} kcal\n"
        f"- Protein: {protein} g\n"
        f"- Carbohydrates: {carbs} g\n"
        f"- Fat: {fat} g"
    )
    
    return formatted_result


def main():
    """
    Main function demonstrating the use of nutrition calculator functions.
    """
    print("===== NUTRITION CALCULATOR =====")
    
    # Example user data
    weight_kg = 70
    height_m = 1.75
    age = 30
    gender = "male"
    activity_level = "moderate"
    
    # Demonstrate different ways to call functions
    
    # 1. Basic function call with positional arguments
    print("\n1. BMI Calculation (Positional Arguments):")
    bmi = calculate_bmi(weight_kg, height_m)
    print(f"Weight: {weight_kg} kg, Height: {height_m} m")
    print(f"BMI: {bmi}")
    
    # 2. Using return value from one function as input to another
    print("\n2. BMI Category (Using function output as input):")
    bmi_category = get_bmi_category(calculate_bmi(weight_kg, height_m))
    print(f"BMI Category: {bmi_category}")
    
    # 3. Function call with keyword arguments
    print("\n3. Calorie Calculation (Keyword Arguments):")
    calories = calculate_calories(
        weight_kg=weight_kg,
        height_m=height_m,
        age=age,
        gender=gender,
        activity_level=activity_level
    )
    print(f"Daily Calorie Needs: {calories} kcal")
    
    # 4. Function call with default parameter
    print("\n4. Protein Calculation (Default Parameter):")
    protein = calculate_protein_needs(weight_kg)  # Using default activity_level
    print(f"Daily Protein Needs (Moderate activity): {protein} g")
    
    # 5. Function call overriding default parameter
    print("\n5. Protein Calculation (Overriding Default):")
    protein_intense = calculate_protein_needs(weight_kg, activity_level="intense")
    print(f"Daily Protein Needs (Intense activity): {protein_intense} g")
    
    # 6. Multiple function calls with different parameter methods
    print("\n6. Water Intake Calculation (Mixed Parameters):")
    water_basic = calculate_water_intake(weight_kg)  # Positional only
    water_active = calculate_water_intake(weight_kg, 1.5)  # All positional
    water_keyword = calculate_water_intake(weight_kg=weight_kg, activity_factor=2.0)  # All keyword
    print(f"Water Intake (Sedentary): {water_basic} liters")
    print(f"Water Intake (Moderate): {water_active} liters")
    print(f"Water Intake (Intense): {water_keyword} liters")
    
    # 7. Formatting function call
    print("\n7. Formatted Nutrition Summary:")
    # Calculate macros based on calories (simplified)
    protein_g = protein
    carbs_g = (calories * 0.5) / 4  # 50% of calories from carbs, 4 cal/g
    fat_g = (calories * 0.25) / 9   # 25% of calories from fat, 9 cal/g
    
    formatted_summary = format_nutrition_result(
        calories,
        protein_g,
        carbs_g,
        fat_g
    )
    print(formatted_summary)


if __name__ == "__main__":
    main()