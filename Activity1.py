grade_book = {"Raghav": 90, "Sam":75, "Chloe":69, "Tom":98}

for key, value in grade_book.items():
    grades = 0
    grades += grade_book[key]
avg = grades / len(grade_book)
print("Average:", avg)
print("Top scorer:", max(grade_book))
print("Lowest scorer:", min(grade_book))

print(grade_book.get(input("Enter student name:"), 'Student was not found'))