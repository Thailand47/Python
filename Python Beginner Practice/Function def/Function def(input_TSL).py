def calculate_numbers():    # กำหนดฟังชั่น และตั้งชื่อ "calculate_numbers"
    
    choice_numbers = input("โปรดป้อนตัวเลขโดยเว้นช่องว่าง คือการ เคาะ 1ที: ") # รับค่าตัวเลข
    float_numbers = choice_numbers.split()  # สร้างตัวแปล เพื่อนำค่า input มาแยก 10, 20, 30
    float_numbers = [float(num) for num in float_numbers] # เอาตัวแปรมาแปลงเป็น ทศนิยม และ 
    sum_numbers = sum(float_numbers)    # สร้างตัวแปลเพื่อเก็บ ค่าผลรวมของ ตัวแปร float_numbers โดยใช้ Sum
    print(f"ผลรวมก็คือ: {sum_numbers}")   # แสดงผล ผลรวม โดยดึงตัวแปร sum_numbers มาไว้ในปีกกาให้มันแสดงผล


calculate_numbers() # เรียกใช้ block code ฟังชั่น def calculate_numbers():    
    