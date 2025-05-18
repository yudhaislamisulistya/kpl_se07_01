# ❌ Bad, Not Maintainable
def p(x, y):
    return x * 3.14 * y * y

# ✅ Good, Maintainable
# This function is simple and clear, making it easy to maintain.
import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

def print_area_info(name, radius):
    area = calculate_circle_area(radius)
    print(f"{name} memiliki luas {area:.2f} m²")