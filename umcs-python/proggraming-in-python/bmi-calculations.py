def calculate_user_bmi(mass: float, height: float) -> float:
    """Calculates and returns the BMI."""
    bmi = mass / (height * height)
    return bmi


def ask_for_input() -> tuple[float, float]:
    """Prompts the user for mass and height."""
    user_mass = float(input("What is your mass in kilograms? "))
    user_height = float(input("What is your height in meters? "))
    return user_mass, user_height


if __name__ == "__main__":
    user_mass, user_height = ask_for_input()
    total_bmi = calculate_user_bmi(user_mass, user_height)
    print(f"Your BMI is: {total_bmi:.2f}")
