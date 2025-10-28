"""
MODULE 1 PRACTICE QUESTIONS
===========================

This file contains practice questions for students to reinforce the concepts
learned in Module 1: Variables, Arithmetic Operations, and String Concatenation.

Instructions:
- Read each question carefully
- Write your code below each question
- Test your solutions by running the file
- Check your answers against the expected output when provided
"""

print("=" * 50)
print("MODULE 1 PRACTICE QUESTIONS")
print("=" * 50)

# =============================================================================
# SECTION 1: VARIABLE ASSIGNMENT
# =============================================================================

print("\n--- SECTION 1: Variable Assignment ---\n")

# Question 1.1
print("Question 1.1:")
print("Create a variable called 'age' and assign it the value 25.")
print("Then create a variable called 'city' and assign it the string 'Boston'.")
print("Print both variables.")
print("Expected output: 25, Boston")
print()

# Write your code here:
age = 25
city = 'boston'
print(age)
print(city)




print("=" * 30)

# Question 1.2
print("Question 1.2:")
print("Create three variables: 'first_name', 'last_name', and 'student_id'.")
print("Assign them appropriate values and print each one on a separate line.")
print()

# Write your code here:
first_name = 'Mingyuan'
last_name = 'Xin'
student_id = 12345678

print('\n',first_name,'\n',last_name,'\n',student_id)


print("=" * 30)

# Question 1.3
print("Question 1.3:")
print("Create a variable 'temperature' with the value 72.")
print("Then reassign it to 68 and print the new value.")
print("Expected output: 68")
print()

# Write your code here:
temperature = 72
temperature = 68
print(temperature)



# =============================================================================
# SECTION 2: ARITHMETIC OPERATIONS
# =============================================================================

print("\n--- SECTION 2: Arithmetic Operations ---\n")

# Question 2.1
print("Question 2.1:")
print("Given two numbers 15 and 4, calculate and print:")
print("- Their sum")
print("- Their difference (15 - 4)")
print("- Their product")
print("- Their quotient (15 / 4)")
print("- The remainder when 15 is divided by 4")
print("Expected output: 19, 11, 60, 3.75, 3")
print()

# Write your code here:
a= 15
b= 4
sum = a+b
diff = a-b
pro = a*b
quetient = a/b

rem =a % b
print(sum,diff,pro,quetient)




print("=" * 30)

# Question 2.2
print("Question 2.2:")
print("Calculate the area of a rectangle with length 12 and width 8.")
print("Store the result in a variable called 'area' and print it.")
print("Expected output: 96")
print()

# Write your code here:
area = 12*8
print(area)



print("=" * 30)

# Question 2.3
print("Question 2.3:")
print("You have $50. You buy 3 items that cost $12.99 each.")
print("Calculate how much money you have left.")
print("Expected output: 11.03")
print()

# Write your code here:
money = 50-3*12.99
print(money)



print("=" * 30)

# Question 2.4
print("Question 2.4:")
print("Calculate the average of these five test scores: 85, 92, 78, 96, 89")
print("Store the result in a variable called 'average' and print it.")
print("Expected output: 88.0")
print()

# Write your code here:
average =  (85+92+78+96+89)/5
print(average)




# =============================================================================
# SECTION 3: STRING CONCATENATION
# =============================================================================

print("\n--- SECTION 3: String Concatenation ---\n")

# Question 3.1
print("Question 3.1:")
print("Create variables for your first name, middle initial, and last name.")
print("Concatenate them to create your full name and print it.")
print("Example output: John Q. Smith")
print()

# Write your code here:

first_name = "Mingyuan"
last_name = "Xin"
print(first_name,"",last_name)


print("=" * 30)

# Question 3.2
print("Question 3.2:")
print("Create a greeting message that includes the user's name and age.")
print("Use variables: name = 'Sarah' and age = 20")
print("Expected output: Hello Sarah, you are 20 years old!")
print()

# Write your code here:

name = 'Sarah'
age = 20

print(f"Hello {name},you are {age}year's old")


print("=" * 30)

# Question 3.3
print("Question 3.3:")
print("Create variables for a book title and author.")
print("Print a message in the format: 'The book [title] was written by [author].'")
print("Example: 'The book To Kill a Mockingbird was written by Harper Lee.'")
print()

# Write your code here:
title = "To Kill a Mockingbird"
author = "Harper Lee"

print(f"The book {title} was written by {author}.")





# =============================================================================
# SECTION 4: COMBINING CONCEPTS
# =============================================================================

print("\n--- SECTION 4: Combining All Concepts ---\n")

# Question 4.1
print("Question 4.1:")
print("Create a simple calculator program:")
print("- Create two number variables: num1 = 24, num2 = 6")
print("- Calculate all four basic operations")
print("- Print each result with a descriptive message")
print("Example: '24 + 6 = 30'")
print()

# Write your code here:
num1 = 24
num2 = 6

print(f'the sum is {num1 + num2}')



print("=" * 30)

# Question 4.2
print("Question 4.2:")
print("Create a program that calculates the tip for a restaurant bill:")
print("- Bill amount: $45.50")
print("- Tip percentage: 18%")
print("- Calculate the tip amount and total bill")
print("- Print both values with descriptive messages")
print("Expected: Tip: $8.19, Total: $53.69")
print()

# Write your code here:

bill = 45.5
percentage = 0.18
tip  = bill*percentage

total = tip + bill
print(f'Tip:{tip},total:{total}')




print("=" * 30)

# Question 4.3
print("Question 4.3:")
print("Create a student report card:")
print("- Student name: 'Alex Johnson'")
print("- Three test scores: 87, 92, 85")
print("- Calculate the average")
print("- Print a report showing the name, all scores, and average")
print("Format: 'Student: Alex Johnson | Scores: 87, 92, 85 | Average: 88.0'")
print()

# Write your code here:
student = 'Alex Johnson'
sc1 = 87
sc2 = 92
sc3 = 85
average =  (sc1+sc2+sc3)/3
print(f'Student: {student} | Scores: {sc1}, {sc2}, {sc3} | Average: {average}')


print("=" * 30)

# Question 4.4
print("Question 4.4:")
print("Create a shopping receipt:")
print("- Item 1: 'Apples' - $3.99")
print("- Item 2: 'Bread' - $2.50")
print("- Item 3: 'Milk' - $4.25")
print("- Calculate subtotal, tax (8.5%), and total")
print("- Print a formatted receipt")
print()

# Write your code here:
apples = 3.99
bread = 2.50
milk = 4.25

subtotal = apples + bread + milk
tax = subtotal * 0.085
total = subtotal + tax

print("Apples: $", apples)
print("Bread:  $", bread)
print("Milk:   $", milk)
print("Subtotal:", round(subtotal, 2))
print("Tax:", round(tax, 2))
print("Total:", round(total, 2))




# =============================================================================
# SECTION 5: CHALLENGE QUESTIONS - NOT GRADED (OPTIONAL)
# =============================================================================

print("\n--- SECTION 5: Challenge Questions ---\n")

# Challenge 5.1
print("Challenge 5.1:")
print("Temperature Converter:")
print("Convert 75 degrees Fahrenheit to Celsius using the formula:")
print("Celsius = (Fahrenheit - 32) * 5/9")
print("Print the result with a descriptive message.")
print("Expected: 75°F is equal to 23.89°C")
print()

# Write your code here:


fahrenheit = 75
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F is equal to {celsius}°C")



print("=" * 30)

# Challenge 5.2
print("Challenge 5.2:")
print("Time Calculator:")
print("You have 3847 seconds. Convert this to hours, minutes, and seconds.")
print("Print the result in the format: 'X hours, Y minutes, Z seconds'")
print("Hint: Use integer division (//) and modulus (%) operators")
print("Expected: 1 hours, 4 minutes, 7 seconds")
print()

# Write your code here:
seconds = 3847
hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

print(f"{hours} hours, {minutes} minutes, {secs} seconds")




print("=" * 30)

# Challenge 5.3
print("Challenge 5.3:")
print("Create a mad lib story:")
print("Create variables for: adjective, noun, verb, place, number")
print("Use them to create a funny story and print it.")
print("Be creative with your story structure!")
print()

# Write your code here:
adjective = "funny"
noun = "dog"
verb = "dance"
place = "park"
number = 3

print(f"One {adjective} {noun} decided to {verb} at the {place} for {number} hours nonstop!")



print("\n" + "=" * 50)
print("END OF PRACTICE QUESTIONS")
print("Great job practicing! Keep coding!")
print("=" * 50)
