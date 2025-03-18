# def maximum_int(a: int, b: int) -> int:
#     return a if a > b else b

# def maximum_float(a: float, b: float) -> float:
#     return a if a > b else b

# def maximum_str(a: str, b: str) -> str:
#     return a if a > b else b

# print(maximum_int(1, 2))
# print(maximum_float(1.0, 2.0))
# print(maximum_str('a', 'b'))

from typing import TypeVar

T = TypeVar('T')

def maximum(a: T, b: T) -> T:
    return a if a > b else b

print(maximum(1, 2))
print(maximum(1.0, 2.0))
print(maximum('a', 'b'))


def maximum_all(a, b):
    type_a = type(a)
    type_b = type(b)
    
    if type_a == "int" or type_b == "int":
        int_a = int(a)
        int_b = int(b)
        return int_a if int_a > int_b else int_b
    elif type_a == "float" or type_b == "float":
        float_a = float(a)
        float_b = float(b)
        return float_a if float_a > float_b else float_b
    else:
        return a if a > b else b
        