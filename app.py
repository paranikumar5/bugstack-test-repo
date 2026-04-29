
```python
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

result = divide_numbers(10, 0)
print(result)
```
