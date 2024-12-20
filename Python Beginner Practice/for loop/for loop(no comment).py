# โจทย์ ผลรวมของตัวเลขในช่วง
# รับตัวเลขจากผู้ใช้ แล้วคำนวณผลรวมของตัวเลขทั้งหมดในช่วง 

n1 = int(input("ใส่เลขตัวแรก: "))
n2 = int(input("ใส่เลขตัวที่สอง: "))
total = 0
for i in range(n1, n2 + 1):
    total += i
print("ผลรวมคือ:", total)

# -----------------------------------------------------------------------------

# โจทย์ นับจำนวนเลขคู่ในช่วง
# ให้รับตัวเลข 2 ตัว แล้วนับว่ามีจำนวนเลขคู่ในช่วงนั้นกี่ตัว

n1 = int(input("ใส่เลขตัวแรก: "))
n2 = int(input("ใส่เลขตัวที่สอง: "))
count = 0
for i in range(n1, n2 + 1):
    if i % 2 == 0:
        count += 1
print("จำนวนเลขคู่คือ:", count)

# ---------------------------------------------------------------------------

# โจทย์ ตารางสูตรคูณ
# ให้พิมพ์ตารางสูตรคูณของตัวเลขที่ผู้ใช้กำหนด (1-12)

num = int(input("ใส่ตัวเลขสำหรับตารางสูตรคูณ: "))
for i in range(1, 13):
    print(f"{num} x {i} = {num * i}")

# ----------------------------------------------------------------------------

# โจทย์ วาดสามเหลี่ยมด้วยดอกจัน
# ให้ผู้ใช้ใส่ความสูงของสามเหลี่ยม แล้ววาดสามเหลี่ยมด้วยดอกจัน   

height = int(input("ใส่ความสูงของสามเหลี่ยม: "))
for i in range(1, height + 1):
    print("*" * i)

# -----------------------------------------------------------------------------

# โจทย์ ผลรวมของเลขกำลังสอง
# คำนวณผลรวมของเลขกำลังสองในช่วงที่ผู้ใช้กำหนด

n1 = int(input("ใส่เลขเริ่มต้น: "))
n2 = int(input("ใส่เลขสุดท้าย: "))
total = 0
for i in range(n1, n2 + 1):
    total += i ** 2
print("ผลรวมกำลังสองคือ:", total)

# -----------------------------------------------------------------------------

# โจทย์ คำนวณตัวหารร่วมของตัวเลข
# ให้ผู้ใช้ใส่ตัวเลข 2 ตัว จากนั้นแสดงตัวหารร่วมทั้งหมด

a = int(input("ใส่เลขตัวแรก: "))
b = int(input("ใส่เลขตัวที่สอง: "))
min_num = min(a, b)
print("ตัวหารร่วมคือ:")
for i in range(1, min_num + 1):
    if a % i == 0 and b % i == 0:
        print(i)

# ------------------------------------------------------------------------------


