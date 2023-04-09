# GPA Calculator:

credits1 = [3, 3, 3, 3, 1.5, 1.5, 3, 1.5]
credits2 = [3, 3, 3, 3, 2, 1.5, 1, 1.5, 1.5]
credits3 = [3, 3, 3, 3, 3, 1.5, 1.5, 1.5, 2]

credits = credits1 + credits2 + credits3

points = {'A+':10, 'A':9, 'B':8, 'C':7, 'D':6, 'E':5, 'F':4}

print("Enter grades in capital letters: ")
grades1 = [points[x] for x in input("Sem1 grades: ").split(" ")]
grades2 = [points[x] for x in input("Sem2 grades: ").split(" ")]
grades3 = [points[x] for x in input("Sem3 grades: ").split(" ")]

grades = grades1 + grades2 + grades3

sgpa1 = 0
sgpa2 = 0
sgpa3 = 0
cgpa = 0

for i in range(len(credits)):
    cgpa += credits[i]*grades[i]
    
for i in range(len(credits1)):
    sgpa1 += credits1[i]*grades1[i]
    
for i in range(len(credits2)):
    sgpa2 += credits2[i]*grades2[i]
    
for i in range(len(credits3)):
    sgpa3 += credits3[i]*grades3[i]

cgpa /= sum(credits)
sgpa1 /= sum(credits1)
sgpa2 /= sum(credits2)
sgpa3 /= sum(credits3)

print("\nSGPA 1 = ", sgpa1)
print("SGPA 2 = ", sgpa2)
print("SGPA 3 = ", sgpa3)
print("CGPA   = ", cgpa)