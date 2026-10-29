# Program to find student marks in a class list
marks = [78, 85, 92, 67, 85, 90, 55, 85]

search_mark = int(input("Enter the marks you want to search for: "))

# Check if item exists in list
if search_mark in marks:
    print(f"Marks found at index position: {marks.index(search_mark)}")
    print(f"Number of students who scored this: {marks.count(search_mark)}")
else:
    print("Marks not found in the list.")
