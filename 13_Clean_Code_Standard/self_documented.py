# ❌ => Bad, not self-documenting
def calc(a, b):
    """
    Hitung nilai akhir berdasarkan skor tugas dan ujian.

    Parameters:
    a (float): Skor tugas (assignment score)
    b (float): Skor ujian (exam score)

    Returns:
    float: Nilai akhir yang dihitung sebagai 10% tugas dan 90% ujian
    """
    return a * 0.1 + b * 0.9

# ✅ => Good, self-documenting
def calculate_final_score(assignment_score, exam_score):
    assignment_weight = 0.1
    exam_weight = 0.9
    return assignment_score * assignment_weight + exam_score * exam_weight