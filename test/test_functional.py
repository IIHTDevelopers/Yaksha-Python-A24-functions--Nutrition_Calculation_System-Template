import unittest
from test.TestUtils import TestUtils
from nutrition_calculation_system import *

class TestNutritionCalculator(unittest.TestCase):

    def setUp(self):
        self.test_obj = TestUtils()

    def test_calculate_bmi_expected(self):
        try:
            result = calculate_bmi(70, 1.75)
            expected = 22.86
            self.test_obj.yakshaAssert("TestCalculateBmiExpected", result == expected, "functional")
            print("TestCalculateBmiExpected =", "Passed" if result == expected else "Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateBmiExpected", False, "functional")
            print("TestCalculateBmiExpected = Failed | Exception:", e)

    def test_get_bmi_category_expected(self):
        try:
            bmi = 22.86
            result = get_bmi_category(bmi)
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
            fat = round((calories * 0.25) / 9, 2)  # 73.61
            result = format_nutrition_result(calories, protein, carbs, fat)
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


if __name__ == "__main__":
    unittest.main()
