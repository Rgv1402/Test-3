grades = {"Jordan":67, "Raghav":98, "Holly":91, "Arjun":94}
print("\nGrades:",grades)
for key, value in grades.items():
    total = 0
    total+= grades[key]
avg = total/len(grades)
print("Average:", avg)
top = max(grades, key=grades.get)
lowest = min(grades, key=grades.get)
print("\nTop Scorer:",top)
print("Lowest Scorer", lowest)
print(grades.get(input("Enter a student's name: "), "Student wasn't found"))
