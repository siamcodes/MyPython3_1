kg = int(input("รับค่าน้ำหนัก:"))
cm = int(input("รับค่าส่วนสูง:"))
bmi = kg / pow(cm/100,2)
print("ค่า BMI = %.2f" % bmi)

if bmi < 18.50:
    print("น้ำหนักน้อย/ผอม")
elif bmi >=18.50 and bmi <=22.90:
    print("ปกติ  สุขภาพดี")
elif bmi >=23 and bmi <=24.90:
    print("ท้วม ระดับ 1")
elif bmi >=25 and bmi <=29.90:
    print("อ้วน ระดับ 2")
elif bmi >=30 :
    print("อ้วนมาก ระดับ 2")