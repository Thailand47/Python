count = 1

while count <= 50:
    if count % 2 == 0 and count % 5 == 0:
        count += 10
        print(f"Count is: {count}")
    elif count % 2 != 0 and count % 3 == 0:
        count += 5
        print(f"Count is: {count}")
    elif count % 2 == 0 and count % 7 == 0:
        count += 15
        print(f"Count is: {count}")  
    else:
        count += 3
        print(f"Count is: {count}")

print("ลูปสิ้นสุดแล้ว!")