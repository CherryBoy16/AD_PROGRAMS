a1= 85
b1= 92
c1= 88
d1= (a1 + b1+ c1) / 3
if d1 >= 90:
    grade = "Grade: A"
elif 80 <= d1< 90:
    grade = "Grade: B"
elif 70 <= d1 < 80:
    grade = "Grade: C"
else:
    grade = "Grade: Fail"
print(f"Average Marks: {d1:.2f}")
print(grade)