print("CGPA Calculator")
cl=int(input("\nHow many course are you trying to compute its CGPA?\nEnter total number: "))

tqp=0
tu=0
for i in range(1,cl +1):
    print("\n",i,"st course:")
    cc=input("Course code: ")
    score=int(input("Final score: "))
    unit=int(input("Course unit: "))
    if (score>=70 and score<=100):
        gp=5
        print("A")
    elif (score>=60 and score<=69):
        gp=4
        print("B")
    elif(score>=50 and score<=59):
        gp=3
        print("C")
    elif(score>=45 and score<=49):
        gp=2
        print("D")
    elif(score>=40 and score<=44):
        gp=1
        print("E")
    elif (score>=0 and score<=39):
        gp=0
        print("F")
    else:
        print("Invalid score. Try again")

#qp(quality point),gp(grade point)
qp=gp*unit


tqp=tqp+qp
tu=tu+unit
#print(tqp)
#tqp(total quality point),tu(total unit)
CGPA=tqp/tu
print("\nCGPA:",CGPA)


