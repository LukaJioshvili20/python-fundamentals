if __name__ == "__main__":
    input_number: int = int(input("Enter a number: "))
    result = ["even", "odd"][input_number % 2]

    # result2 = "even" * (input_number % 2)

    print(f"The number {input_number} is {result}.")
