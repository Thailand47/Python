# สร้างระบบที่ให้ผู้ใช้กรอกชื่อผู้ใช้และรหัสผ่าน โดยให้ระบบตรวจสอบว่าเป็นข้อมูลที่ถูกต้องหรือไม่
# รับชื่อผู้ใช้และรหัสผ่าน
# ตรวจสอบว่าเข้ากันได้กับค่าที่กำหนดไว้หรือไม่ (สามารถใช้ค่าคงที่ในตอนแรก)
# แสดงข้อความว่าผู้ใช้เข้าสู่ระบบสำเร็จหรือไม่

username = input("โปรดป้อนชื่อของคุณ: ")            # รับชื่อผู้ใช้
lastname = input("โปรดป้อนนามสกุลของคุณ: ")        # รับรหัสผ่านจากผู้ใช้

if username == "root" and lastname == "admin":      # ใช้เงื่อนไขตรวจสอบ อินพุต ว่าถูกต้องไหม ถ้าเป็นจริงทั้ง 2 ก็จะทำงาน
    print("Access Grant")                           # ถ้าถูกต้อง จะแสดงผลลัพธ์ออกมา
else:                                               # ถ้าไม่มีเงื่อนไขใดตรง บรรทัดนี้จะทำงาน
    print("Access Denied")                          # และแสดงผลลัพธ์ออกมา

