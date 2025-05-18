# ❌ Bad, DRY (Don't Repeat Yourself)
# This function violates the DRY principle by repeating the area calculation logic.
def calculate_area_rectangle(length, width):
    return length * width

def calculate_floor_area(length, width):
    return length * width

# ✅ Good, DRY (Don't Repeat Yourself) -> Mematuhi Prinsip Jangan Ulangi Diri Sendiri
def calculate_area(length, width):
    return length * width

# Menggunakan fungsi tunggal sesuai konteks
rectangle_area = calculate_area(5, 3)
floor_area = calculate_area(10, 6)

print(f"Rectangle area: {rectangle_area}")
print(f"Floor area: {floor_area}")
