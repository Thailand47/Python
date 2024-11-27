# Simple Calculator
# สร้างโปรแกรมเครื่องคิดเลขที่สามารถทำการบวก, ลบ, คูณ, และหารได้
# รับค่าตัวเลข 2 ตัวจากผู้ใช้
# รับการเลือกการทำงาน เช่น บวก, ลบ, คูณ, หาร

num1 = float(input("โปรดป้อนตัวเลขแรกของคุณ: "))               # รับค่าตัวเลขแรกจากผู้ใช้งาน
operations = input("กรุณาใส่ บวก ลบ คูณ หาร (+, -, *, /): ")   # รับค่า + - * / จากผู้ใช้งาน
num2 = float(input("โปรดป้อนตัวเลขตัวที่สองของคุณ: "))            # รับค่าตัวที่สอง ตัวเลขจากผู้ใช้งาน

# Process
if operations == "+":       # ถ้าตัวแปรเป็น + คือ True บล๊อคโค๊ดนี้จะทำงาน
    total = num1 + num2     # เมื่อ บล๊อคโค๊ด if ทำงาน ตัวแปร total จะบวก ตัวแปร num1 และ num 2 และเก็บผลลัพธ์เอาไว้ที่ total
elif operations == "-":     # ถ้าหาก Block code If ด้านบนเป็น False และผู้ใช้ป้อน - เข้ามา จะเป็น True บล๊อคโค๊ดนี้จะทำงาน
    total = num1 - num2     # เมื่อ บล๊อคโค๊ดนี้ทำงาน ตัวแปร total จะลบ ตัวแปร num1 และ num 2 และเก็บผลลัพธ์เอาไว้ที่ total
elif operations == "*":     # ถ้าหาก Block code ด้านบนเป็น False และผู้ใช้ป้อน * เข้ามา จะเป็น True บล๊อคโค๊ดนี้จะทำงาน
    total = num1 * num2     # เมื่อ บล๊อคโค๊ดนี้ทำงาน ตัวแปร total จะคูณ ตัวแปร num1 และ num 2 และเก็บผลลัพธ์เอาไว้ที่ total
elif operations == "/":     # ถ้าหาก Block code ด้านบนเป็น False และผู้ใช้ป้อน / เข้ามา จะเป็น True บล๊อคโค๊ดนี้จะทำงาน
    total = num1 / num2     # เมื่อ บล๊อคโค๊ดนี้ทำงาน ตัวแปร total จะหาร ตัวแปร num1 และ num 2 และเก็บผลลัพธ์เอาไว้ที่ total
else:                               # เมื่อทุก block code ด้านบนเป็น false หมด บรรทัดนี้จะทำงาน
    total = "คุณป้อนผิด รบกวนป้อนใหม่"   # เมื่อ บล๊อคโค๊ดนี้ทำงาน ตัวแปร total จะเก็บค่า "string" เอาไว้ที่ total

# Output
print(total)    # แสดงผลลัพธ์   