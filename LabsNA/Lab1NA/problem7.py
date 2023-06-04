import sys


class DecimalToBinaryConverter:
    @staticmethod
    def convert(decimal):
        binary = ""
        while decimal > 0:
            remainder = decimal % 2
            decimal = decimal // 2
            binary = str(remainder) + binary
        return binary


class BinaryToDecimalConverter:
    @staticmethod
    def convert(binary):
        decimal = 0
        for i, digit in enumerate(reversed(binary)):
            decimal += int(digit) * (2 ** i)
        return decimal


class BinaryCalculator:
    @staticmethod
    def add(bin1, bin2):
        bin1_decimal = BinaryToDecimalConverter.convert(bin1)
        bin2_decimal = BinaryToDecimalConverter.convert(bin2)
        sum_decimal = bin1_decimal + bin2_decimal
        return DecimalToBinaryConverter.convert(sum_decimal)

    @staticmethod
    def subtract(bin1, bin2):
        bin1_decimal = BinaryToDecimalConverter.convert(bin1)
        bin2_decimal = BinaryToDecimalConverter.convert(bin2)
        difference_decimal = bin1_decimal - bin2_decimal
        return DecimalToBinaryConverter.convert(difference_decimal)

    @staticmethod
    def multiply(bin1, bin2):
        bin1_decimal = BinaryToDecimalConverter.convert(bin1)
        bin2_decimal = BinaryToDecimalConverter.convert(bin2)
        product_decimal = bin1_decimal * bin2_decimal
        return DecimalToBinaryConverter.convert(product_decimal)

    @staticmethod
    def divide(bin1, bin2):
        bin1_decimal = BinaryToDecimalConverter.convert(bin1)
        bin2_decimal = BinaryToDecimalConverter.convert(bin2)
        if bin2_decimal == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        quotient_decimal = bin1_decimal // bin2_decimal
        return DecimalToBinaryConverter.convert(quotient_decimal)


class ErrorCalculator:
    @staticmethod
    def calculate_absolute_error(approx_value, true_value):
        return abs(true_value - approx_value)

    @staticmethod
    def calculate_relative_error(approx_value, true_value):
        return abs((true_value - approx_value) / true_value)


class BinaryCalculatorApp:
    def __init__(self):
        self.binary_calculator = BinaryCalculator()
        self.error_calculator = ErrorCalculator()

    def run(self):
        while True:
            print("\nChoose an operation:")
            print("1. Convert decimal to binary")
            print("2. Convert binary to decimal")
            print("3. Add binary numbers")
            print("4. Subtract binary numbers")
            print("5. Multiply binary numbers")
            print("6. Divide binary numbers")
            print("7. Calculate absolute and relative error")
            print("8. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                decimal = int(input("Enter decimal number: "))
                print("Binary:", DecimalToBinaryConverter.convert(decimal))
            elif choice == 2:
                binary = input("Enter binary number: ")
                print("Decimal:", BinaryToDecimalConverter.convert(binary))
            elif choice == 3:
                bin1 = input("Enter 1st binary number: ")
                bin2 = input("Enter 2nd binary number: ")
                print("Sum:", self.binary_calculator.add(bin1, bin2))
            elif choice == 4:
                bin1 = input("Enter first binary number: ")
                bin2 = input("Enter 2nd binary number: ")
                print("Difference:", self.binary_calculator.subtract(bin1, bin2))
            elif choice == 5:
                bin1 = input("Enter first binary number: ")
                bin2 = input("Enter 2nd binary number: ")
                print("Product:", self.binary_calculator.multiply(bin1, bin2))
            elif choice == 6:
                bin1 = input("Enter first binary number: ")
                bin2 = input("Enter 2nd binary number: ")
                try:
                    print("Quotient:", self.binary_calculator.divide(bin1, bin2))
                except ZeroDivisionError as e:
                    print(e)
            elif choice == 7:
                approx_value = float(input("Enter the approximate value: "))
                true_value = float(input("Enter the true value: "))
                abs_error = self.error_calculator.calculate_absolute_error(approx_value, true_value)
                rel_error = self.error_calculator.calculate_relative_error(approx_value, true_value)
                print("Absolute error:", abs_error)
                print("Relative error:", rel_error)
            elif choice == 8:
                print("Exiting the program.")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")


calculator = BinaryCalculatorApp()
calculator.run()
