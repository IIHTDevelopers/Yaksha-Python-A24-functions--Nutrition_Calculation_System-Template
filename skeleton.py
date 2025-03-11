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
    # TODO: Implement BMI calculation
    pass


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
    # TODO: Implement BMI category determination
    pass


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
    # TODO: Implement calorie calculation
    pass


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
    # TODO: Implement protein needs calculation
    pass


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
    # TODO: Implement water intake calculation
    pass


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
    # TODO: Implement nutrition result formatting
    pass


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
    
    # TODO: Demonstrate different ways to call the functions
    # 1. Basic function call with positional arguments
    
    # 2. Using return value from one function as input to another
    
    # 3. Function call with keyword arguments
    
    # 4. Function call with default parameter
    
    # 5. Function call overriding default parameter
    
    # 6. Multiple function calls with different parameter methods
    
    # 7. Formatting function call


if __name__ == "__main__":
    main()