# ❌ => Bad, KISS (Keep It Simple, Stupid)
# This function is unnecessarily complex and could be simplified.
def is_even(n):
    return True if n % 2 == 0 else False

# ✅ => Good, KISS (Keep It Simple, Stupid) -> Sederhana dan Jelas
def is_even(n):
    return n % 2 == 0