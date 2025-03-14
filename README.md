# Python Basics: Control Flow, Data Structures & Sets

This repository contains simple Python examples covering **Control Flow, Loops, Lists, Tuples, Dictionaries, Sets, and Frozensets**.

## 📌 Lessons Covered

### 📝 Lesson 05: Control Flow & Loops
Control flow statements allow conditional execution, while loops enable repeated execution of code blocks.

#### 🔹 **Examples**
```python
# If-Else Statement
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# For Loop
for i in range(1, 6):
    print(f"Number: {i}")

# While Loop
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1


📝 Lesson 06: Lists, Tuples & Dictionary
Python provides different data structures to store collections of data efficiently.

🔹 Lists (Mutable)
A list is an ordered, changeable collection that allows duplicate values.

python
Copy
Edit
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Mango")
print(fruits)  # ['Apple', 'Banana', 'Cherry', 'Mango']
🔹 Tuples (Immutable)
A tuple is similar to a list but immutable (cannot be changed after creation).

python
Copy
Edit
colors = ("Red", "Green", "Blue")
print(colors[1])  # Green
🔹 Dictionaries (Key-Value Pairs)
A dictionary stores data in key-value pairs, allowing efficient retrieval.

python
Copy
Edit
student = {"name": "Alice", "age": 20, "grade": "A"}
print(student["name"])  # Alice
student["age"] = 21  # Updating a value
📝 Lesson 07: The Set & Frozenset
Sets are unordered collections of unique elements.

🔹 Set (Mutable)
A set allows unique elements and supports operations like union, intersection, and difference.

python
Copy
Edit
numbers = {1, 2, 3, 4, 4, 5}
numbers.add(6)
print(numbers)  # {1, 2, 3, 4, 5, 6}
🔹 Frozenset (Immutable Set)
A frozenset is an immutable version of a set.

python
Copy
Edit
frozen_numbers = frozenset({10, 20, 30, 40})
print(frozen_numbers)  # frozenset({10, 20, 30, 40})


