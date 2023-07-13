subjects = ['science', 'math', 'bangla', 'english']

marks = [0, 0, 0, 0]
for i in range(4):

    marks[i] = int(input("Enter the mark of " + subjects[i] +": "))

total= 0
avg= 0
for i in range(4):
    total = total+ marks[i]

avg = total/4

if avg >100:
    print("Error!")
elif avg >= 91:
    print("Your grade is A+")
elif avg>=81:
    print("Your grade is A")
elif avg>=71:
    print("Your grade is B")
elif avg>=61:
    print("Your grade is C")
elif avg>=41:
    print("Your grade is D")
elif avg<=40 and avg>=0:
    print("Your grade is F")
elif avg<0:
    print("impossible")


