def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "🚫 Cannot divide by zero"
    return x / y

def calculator():
    print("🧮 Welcome to Dhanya’s Python Calculator!")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Choose operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        print("❌ Invalid operator selected.")
        return

    print(f"\n✅ Result: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()