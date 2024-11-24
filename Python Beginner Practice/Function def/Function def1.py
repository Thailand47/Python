# สร้างฟังก์ชันที่คำนวณค่าพื้นที่ของสามเหลี่ยม

# ชื่อฟังก์ชัน: calculate_triangle_area
# พารามิเตอร์: base (ฐาน), height (ความสูง)
# ผลลัพธ์: คืนค่าพื้นที่ของสามเหลี่ยม โดยใช้สูตร 0.5 × ฐาน × ความสูง

def calculate_triangle_area(base, height):
    return 0.5 * base * height
result = calculate_triangle_area(5, 3)
print(result)
