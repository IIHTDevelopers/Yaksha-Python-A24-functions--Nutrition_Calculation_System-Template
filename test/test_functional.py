"""
Functional tests for the Nutrition Calculator System - Unittest Version.
"""

import unittest
import os
import sys
import importlib
from test.TestUtils import TestUtils
from skeleton import *

class TestNutritionCalculator:
    def __init__(self, test_obj):
        self.test_obj = test_obj

    def test_calculate_bmi_expected(self):
        try:
            result = calculate_bmi(70, 1.75)  # → 22.86
            expected = 22.86
            self.test_obj.yakshaAssert("TestCalculateBmiExpected", result == expected, "functional")
            print("TestCalculateBmiExpected =", "Passed" if result == expected else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateBmiExpected", False, "functional")
            print("TestCalculateBmiExpected = Failed | Exception:", e)

    def test_get_bmi_category_expected(self):
        try:
            bmi = 22.86
            result = get_bmi_category(bmi)  # → "Normal weight"
            expected = "Normal weight"
            self.test_obj.yakshaAssert("TestGetBmiCategoryExpected", result == expected, "functional")
            print("TestGetBmiCategoryExpected =", "Passed" if result == expected else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestGetBmiCategoryExpected", False, "functional")
            print("TestGetBmiCategoryExpected = Failed | Exception:", e)

    def test_calculate_calories_expected(self):
        try:
            result = calculate_calories(70, 1.75, 30, "male", "moderate")
            expected = 2628
            self.test_obj.yakshaAssert("TestCalculateCaloriesExpected", result == expected, "functional")
            print("TestCalculateCaloriesExpected =", "Passed" if result == expected else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateCaloriesExpected", False, "functional")
            print("TestCalculateCaloriesExpected = Failed | Exception:", e)

    def test_calculate_protein_default_expected(self):
        try:
            result = calculate_protein_needs(70)
            expected = 112.0
            self.test_obj.yakshaAssert("TestCalculateProteinDefaultExpected", result == expected, "functional")
            print("TestCalculateProteinDefaultExpected =", "Passed" if result == expected else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateProteinDefaultExpected", False, "functional")
            print("TestCalculateProteinDefaultExpected = Failed | Exception:", e)

    def test_calculate_protein_override_expected(self):
        try:
            result = calculate_protein_needs(70, "intense")
            expected = 140.0
            self.test_obj.yakshaAssert("TestCalculateProteinOverrideExpected", result == expected, "functional")
            print("TestCalculateProteinOverrideExpected =", "Passed" if result == expected else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateProteinOverrideExpected", False, "functional")
            print("TestCalculateProteinOverrideExpected = Failed | Exception:", e)

    def test_water_intake_sedentary_expected(self):
        try:
            result = calculate_water_intake(70)
            expected = 2.33
            self.test_obj.yakshaAssert("TestWaterIntakeSedentaryExpected", result == expected, "functional")
            print("TestWaterIntakeSedentaryExpected =", "Passed" if result == expected else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestWaterIntakeSedentaryExpected", False, "functional")
            print("TestWaterIntakeSedentaryExpected = Failed | Exception:", e)

    def test_water_intake_moderate_expected(self):
        try:
            result = calculate_water_intake(70, 1.5)
            expected = 3.5
            self.test_obj.yakshaAssert("TestWaterIntakeModerateExpected", result == expected, "functional")
            print("TestWaterIntakeModerateExpected =", "Passed" if result == expected else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestWaterIntakeModerateExpected", False, "functional")
            print("TestWaterIntakeModerateExpected = Failed | Exception:", e)

    def test_water_intake_intense_expected(self):
        try:
            result = calculate_water_intake(70, activity_factor=2.0)
            expected = 4.66
            self.test_obj.yakshaAssert("TestWaterIntakeIntenseExpected", result == expected, "functional")
            print("TestWaterIntakeIntenseExpected =", "Passed" if result == expected else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestWaterIntakeIntenseExpected", False, "functional")
            print("TestWaterIntakeIntenseExpected = Failed | Exception:", e)

    def test_format_nutrition_summary_expected(self):
        try:
            calories = 2650
            protein = 112.0
            carbs = (calories * 0.5) / 4     # 331.25
            fat = (calories * 0.25) / 9      # 73.61
            result = format_nutrition_result(calories, protein, carbs, round(fat, 2))
            expected = (
                "Nutrition Summary:\n"
                "- Calories: 2650 kcal\n"
                "- Protein: 112.0 g\n"
                "- Carbohydrates: 331.25 g\n"
                "- Fat: 73.61 g"
            )
            self.test_obj.yakshaAssert("TestFormatNutritionSummaryExpected", result == expected, "functional")
            print("TestFormatNutritionSummaryExpected =", "Passed" if result == expected else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestFormatNutritionSummaryExpected", False, "functional")
            print("TestFormatNutritionSummaryExpected = Failed | Exception:", e)


# Add a main block to run all functional tests
if __name__ == "__main__":
    test_obj = TestUtils()
    tester = TestNutritionCalculator(test_obj)
    # List all callable test methods
    test_methods = [method for method in dir(tester) if method.startswith("test_") and callable(getattr(tester, method))]
    for method in test_methods:
        getattr(tester, method)()
