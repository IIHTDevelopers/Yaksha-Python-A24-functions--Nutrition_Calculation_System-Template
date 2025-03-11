"""
Functional tests for the Nutrition Calculator System.
"""

import pytest
from test.TestUtils import TestUtils
from nutrition_calculation_system import (
    calculate_bmi,
    get_bmi_category,
    calculate_calories,
    calculate_protein_needs,
    calculate_water_intake,
    format_nutrition_result
)


class TestFunctional:
    """Test class for functional tests of the Nutrition Calculator System."""
    
    def test_basic_calculations(self):
        """Test BMI, BMI category, and calorie calculations."""
        try:
            # Test BMI calculation with different inputs
            assert calculate_bmi(70, 1.75) == 22.86
            assert calculate_bmi(65.5, 1.68) == 23.21
            assert calculate_bmi(100, 2.0) == 25.0
            
            # Test BMI category determination
            assert get_bmi_category(17.5) == "Underweight"
            assert get_bmi_category(22.0) == "Normal weight"
            assert get_bmi_category(27.5) == "Overweight"
            assert get_bmi_category(32.0) == "Obese"
            
            # Test calorie calculation
            male_calories = calculate_calories(70, 1.75, 30, "male", "moderate")
            assert isinstance(male_calories, int)
            assert male_calories > 2000
            
            female_calories = calculate_calories(60, 1.65, 30, "female", "moderate")
            assert isinstance(female_calories, int)
            assert female_calories > 1800
            
            # Test activity level impact
            sedentary_calories = calculate_calories(70, 1.75, 30, "male", "sedentary")
            active_calories = calculate_calories(70, 1.75, 30, "male", "active")
            assert active_calories > sedentary_calories
            
            TestUtils.yakshaAssert("TestBasicCalculations", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("TestBasicCalculations", False, "functional")
            pytest.fail(f"Basic calculations test failed: {str(e)}")
    
    def test_nutrition_calculations(self):
        """Test protein needs and water intake calculations."""
        try:
            # Test protein needs with default activity level
            assert calculate_protein_needs(70) == 112.0
            
            # Test with explicit activity levels
            assert calculate_protein_needs(70, "light") == 84.0
            assert calculate_protein_needs(70, "intense") == 140.0
            
            # Test weight proportionality
            assert calculate_protein_needs(35, "moderate") == 56.0
            
            # Test water intake with default activity
            assert calculate_water_intake(70) == 2.33
            
            # Test with different activity factors
            assert calculate_water_intake(70, 1.2) == 2.8
            assert calculate_water_intake(70, 1.5) == 3.5
            assert calculate_water_intake(70, 2.0) == 4.66
            
            # Test with different weight
            assert calculate_water_intake(100) == 3.33
            
            TestUtils.yakshaAssert("TestNutritionCalculations", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("TestNutritionCalculations", False, "functional")
            pytest.fail(f"Nutrition calculations test failed: {str(e)}")
    
    def test_formatting_and_function_usage(self):
        """Test formatting and advanced function usage patterns."""
        try:
            # Test formatting
            expected_output = (
                "Nutrition Summary:\n"
                "- Calories: 2000 kcal\n"
                "- Protein: 150 g\n"
                "- Carbohydrates: 200 g\n"
                "- Fat: 50 g"
            )
            formatted_result = format_nutrition_result(2000, 150, 200, 50)
            assert formatted_result == expected_output
            
            # Test different values
            different_output = format_nutrition_result(1800, 120, 180, 60)
            assert "Calories: 1800" in different_output
            assert "Protein: 120" in different_output
            
            # Test function calling patterns
            weight = 70
            height = 1.75
            
            # Chaining functions
            direct_category = get_bmi_category(calculate_bmi(weight, height))
            assert direct_category == "Normal weight"
            
            # Keyword arguments
            keyword_bmi = calculate_bmi(weight_kg=weight, height_m=height)
            assert keyword_bmi == 22.86
            
            # Mixed arguments
            protein = calculate_protein_needs(weight, activity_level="intense")
            assert protein == 140.0
            
            TestUtils.yakshaAssert("TestFormattingAndFunctionUsage", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("TestFormattingAndFunctionUsage", False, "functional")
            pytest.fail(f"Formatting and function usage test failed: {str(e)}")


if __name__ == '__main__':
    pytest.main(['-v'])