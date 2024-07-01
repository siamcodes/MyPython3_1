sum = 0
def avg(num):
    score = 0
    for i in range(num):
        score += int(input("รับคะแนน %d:" % (i+1)))
    sum = score/num
    return sum    

n = int(input("รับจำนวนคน:"))
print("คะแนนเฉลี่ย %.2f" % avg(n))    