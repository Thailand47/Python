# โจทย์ ฟังก์ชันตรวจสอบเลขคู่-คี่
# เขียนฟังก์ชันชื่อ is_even ที่รับตัวเลข n แล้วคืนค่า True ถ้าเลขนั้นเป็นเลขคู่ และคืนค่า False ถ้าเลขนั้นเป็นเลขคี่

def is_even(n):
    return n % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False
