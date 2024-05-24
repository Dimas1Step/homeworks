def calculator_decorator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception as e:
            return f"Error: {e}"
    return wrapper

@calculator_decorator
def calculate(expression):
    allowed_chars = "0123456789+-*/(). "
    if any(char not in allowed_chars for char in expression):
        raise ValueError("Invalid characters in expression")
    return eval(expression)

print(calculate("10 + 20"))
print(calculate("10 / 0"))
print(calculate("10 + (5 * 3)"))
print(calculate("10 + abc"))