#Problem 1 Grading
# Get the student's score
#score = float(input("Enter the student's score (0-100): "))
#
## Determine the grade
#if score >= 90:
#    grade = 'A'
#elif score >= 80:
#    grade = 'B'
#elif score >= 70:
#    grade = 'C'
#elif score >= 60:
#    grade = 'D'
#else:
#    grade = 'F'
#
## Print the grade
#print(f"The student's grade is: {grade}")

#Problem 5 Days of the Week
#dow = int(input("Enter A Number (1-7) That Corresponds To The Day of The Week: "))
#
#if dow == 1:
#    day = 'Monday'
#elif dow == 2:
#    day = 'Tuesday'
#elif dow == 3:
#    day = 'Wednesday'
#elif dow == 4:
#    day = 'Thursday'
#elif dow == 5:
#    day = 'Friday'
#elif dow == 6:
#    day = 'Saturday'
#elif dow == 7:
#    day = 'Sunday'
#else:
##    day = 'You Must Enter A Number (1-7)'
##
##print(f"The day of the week: {day}")
#
##Problem 10 Color Mixer
## Prompt the user to enter two primary colors
#color1 = input("Enter the first primary color (red, blue, yellow): ").strip().lower()
#color2 = input("Enter the second primary color (red, blue, yellow): ").strip().lower()
#
## Check if both colors are primary colors
#primary_colors = {'red', 'blue', 'yellow'}
#color_mix = {
#    ('red', 'blue'): 'purple',
#    ('blue', 'red'): 'purple',
#    ('red', 'yellow'): 'orange',
#    ('yellow', 'red'): 'orange',
#    ('blue', 'yellow'): 'green',
#    ('yellow', 'blue'): 'green'
#}
#
#if color1 in primary_colors and color2 in primary_colors:
#    if color1 == color2:
#        result_color = color1
#    else:
#        result_color = color_mix.get((color1, color2), "unknown")
#    print(f"The color made by mixing {color1} and {color2} is {result_color}.")
#else:
#    if color1 not in primary_colors and color2 not in primary_colors:
#        print(f"Error: Both {color1} and {color2} are not primary colors.")
#    elif color1 not in primary_colors:
#        print(f"Error: {color1} is not a primary color.")
#    else:
#        print(f"Error: {color2} is not a primary color.")
#
#
#
#