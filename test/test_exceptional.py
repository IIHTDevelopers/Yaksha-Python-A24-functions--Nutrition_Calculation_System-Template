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

class TestExceptional:
    """Test class for exception handling tests of the Nutrition Calculator System."""
    
    def test_error_handling(self):
        """Consolidated test for error handling across all functions"""
        try:
            # BMI error handling
            with pytest.raises(ValueError):
                calculate_bmi("seventy", 1.75)  # Non-numeric weight
            
            with pytest.raises(ValueError):
                calculate_bmi(70, 0)  # Zero height
            
            with pytest.raises(ValueError):
                calculate_bmi(-10, 1.75)  # Negative weight
            
            with pytest.raises(ValueError):
                get_bmi_category("twenty-two")  # Non-numeric BMI
            
            # Calorie calculation error handling
            with pytest.raises(ValueError):
                calculate_calories(70, 1.75, 30, "invalid", "moderate")  # Invalid gender
            
            with pytest.raises(ValueError):
                calculate_calories(70, 1.75, 30, "male", "super active")  # Invalid activity
            
            with pytest.raises(ValueError):
                calculate_calories(70, 1.75, -10, "male", "moderate")  # Negative age
            
            # Protein needs error handling
            with pytest.raises(ValueError):
                calculate_protein_needs(-50)  # Negative weight
            
            with pytest.raises(ValueError):
                calculate_protein_needs(70, "ultra intense")  # Invalid activity
            
            # Water intake error handling
            with pytest.raises(ValueError):
                calculate_water_intake(-70)  # Negative weight
            
            with pytest.raises(ValueError):
                calculate_water_intake(70, 0.5)  # Invalid activity factor
            
            # Nutrition formatting error handling
            with pytest.raises(ValueError):
                format_nutrition_result(-2000, 150, 200, 50)  # Negative calories
            
            with pytest.raises(ValueError):
                format_nutrition_result(2000, -150, 200, 50)  # Negative protein
            
            TestUtils.yakshaAssert("TestErrorHandling", True, "exception")
        except Exception as e:
            TestUtils.yakshaAssert("TestErrorHandling", False, "exception")
            pytest.fail(f"Error handling test failed: {str(e)}")


if __name__ == '__main__':
    pytest.main(['-v'])