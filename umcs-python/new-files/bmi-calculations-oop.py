class BMICalculator:
    def __init__(self):
        self.user_mass = 0.0
        self.user_height = 0.0

    def ask_for_input(self) -> None:
        """Prompts the user for mass and height."""
        self.user_mass = float(input("What is your mass in kilograms? "))
        self.user_height = float(input("What is your height in meters? "))

    def calculate_bmi(self) -> float:
        """Calculates and returns the BMI."""
        if self.user_height == 0:
            raise ValueError("Height cannot be zero.")
        bmi = self.user_mass / (self.user_height * self.user_height)
        return bmi


if __name__ == "__main__":
    calculator = BMICalculator()
    calculator.ask_for_input()
    total_bmi = calculator.calculate_bmi()
    print(f"Your BMI is: {total_bmi:.2f}")
