# จงเขียนโปรแกรมรับค่าข้อความและตัวเลข จากนั้นนำเลขไปบวก 44.112 แล้วแสดงผลดังตัวอย่าง
# สร้างตัวแปรได้เพียง 2 ตัว
# ไม่อนุญาตให้ใช้ String Format ทุกรูปแบบ

text = input("Input text: ")
num  = float(input("Input number: "))
num  += 44.112
num  = str(num)
print("I can print string with another datatype like this -> " + text + " " + num)