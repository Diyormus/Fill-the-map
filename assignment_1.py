# -----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment task for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 2, 2024.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 12155942
student_name = "Diyorbek Musaev"
#
#  NB: All files submitted for this assessable task will be subjected
#  to automated plagiarism analysis using a tool such as the Measure
#  of Software Similarity (http://theory.stanford.edu/~aiken/moss/).
#
# --------------------------------------------------------------------#


# -----Assessment Task 1 Description----------------------------------#
#
#  This assessment task tests your skills at processing large data
#  sets, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function.  You are required to complete this
#  function so that when the program runs it fills a grid with various
#  symbols, using data stored in a list to determine which symbols to
#  draw and where.  See the online video instructions for
#  full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts
#  and you will submit your final solution as this single Python 3
#  file only, whether or not you complete all requirements for the
#  assignment.
#
#  This file relies on other Python modules but all of your code
#  must appear in this file only.  You may not change any of the code
#  in the other modules and you should not submit the other modules
#  with your solution.  The markers will use their own copies of the
#  other modules to test your code, so your solution will not work
#  if it relies on changes made to any other files.
#
# --------------------------------------------------------------------#


# -----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()

# Import the functions for setting up the drawing canvas
config_file = 'assignment_1_config.py'
if isfile(config_file):
    print('\nConfiguration module found ...\n')
    from assignment_1_config import *
else:
    print(f"\nCannot find file '{config_file}', aborting!\n")
    abort()

# Define the function for generating data sets in Task 1B,
# using the imported raw data generation function if available,
# but otherwise creating a dummy function that just returns an
# empty list
data_file = 'assignment_1_data.py'
if isfile(data_file):
    print('Data generation module found ...\n')
    from assignment_1_data import raw_data


    def data_set(new_seed=randint(0, 99999)):
        return raw_data(new_seed)  # return the random data set
else:
    print('No data generation module available ...\n')


    def data_set(dummy_parameter=None):
        return []


#
# --------------------------------------------------------------------#


# -----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own function and any other functions needed to support it.
#  All of your solution code must appear in this section.  Do NOT put
#  any of your code in any other sections and do NOT change any of
#  the provided code except as allowed by the comments in the next
#  section.
#

# All of your code goes in, or is called from, this function.
# In Task 1B ensure that your code does NOT call functions data_set
# or raw_data because they're already called in the main program
# below.


def rectangular(horizontal, vertical, colour):
    pendown()
    pensize(1)
    color(colour)
    begin_fill()

    for _ in range(2):
        forward(horizontal)
        right(90)
        forward(vertical)
        right(90)
    end_fill()
    penup()


def triangle(colour):
    pendown()
    pencolor(colour)
    color(colour)
    begin_fill()
    for _ in range(3):
        forward(110)
        left(120)
    end_fill()
    penup()

    pendown()
    pensize(3)
    pencolor("black")
    color("black")
    for _ in range(3):
        forward(110)
        left(120)
    penup()


def reversed_triangle(colour):
    pendown()
    pencolor(colour)
    color(colour)
    begin_fill()
    for _ in range(3):
        forward(110)
        right(120)
    end_fill()
    penup()

    pendown()
    pensize(3)
    pencolor("black")
    color("black")
    for _ in range(3):
        forward(110)
        right(120)
    penup()


def write_instructions():
    grid_font = ('Arial', cell_width // (4 if platform == 'darwin' else 5),
                 'normal')
    goto((390, -100))
    write('''1-10 millions''',
          align='left', font=grid_font, )
    goto((390, -280))
    write('''more than 100 millions''',
          align='left', font=grid_font, )


def draw_robot(position_x, position_y, reversed_or_not,
               triangle_colour, body_n_head_color, other_parts_color):
    # Draw triangle
    goto(position_x - 45, position_y - 40)  # Move to starting point for the triangle
    if reversed_or_not == 'yes':
        goto(position_x - 45, position_y + 25)  # Move to the top vertex of the reversed triangle
        pendown()  # Start drawing
        pencolor("black")  # Set the outline color
        reversed_triangle(triangle_colour)  # Draw the reversed triangle
    else:
        goto(position_x - 45, position_y - 45)  # Move to the starting point for the normal triangle
        triangle(triangle_colour)  # Draw the normal triangle

    # Draw body
    goto(position_x, position_y)  # Move to the center position
    rectangular(20, 20, body_n_head_color)  # Draw the body

    # Draw left hand
    goto(position_x, position_y)  # Move to the center
    right(90)  # Rotate to align with left hand position
    rectangular(5, 10, other_parts_color)  # Draw left hand (part 1)
    goto(position_x - 15, position_y)  # Move to the next position for the left hand
    left(90)  # Rotate to draw the second part of the left hand
    rectangular(5, 10, other_parts_color)  # Draw left hand (part 2)

    # Draw right hand
    goto(position_x + 30, position_y)  # Move to the center for the right hand
    right(90)  # Rotate to align with right hand position
    rectangular(5, 10, other_parts_color)  # Draw right hand (part 1)
    goto(position_x + 30, position_y)  # Move to the next position for the right hand
    left(90)  # Rotate to draw the second part of the right hand
    rectangular(5, 10, other_parts_color)  # Draw right hand (part 2)

    # Draw feet
    goto(position_x + 5, position_y - 30)  # Move to starting point for the feet
    right(90)  # Rotate to align with feet position
    rectangular(5, 10, other_parts_color)  # Draw foot (part 1)
    right(90)  # Rotate to draw the second part of the foot
    rectangular(5, 10, other_parts_color)  # Draw foot (part 2)
    goto(position_x + 20, position_y - 35)  # Move to the next position for the feet
    right(90)  # Rotate to draw the foot's additional parts
    rectangular(5, 5, other_parts_color)  # Draw foot (part 3)
    left(90)  # Rotate to draw the final part of the foot
    rectangular(5, 15, other_parts_color)  # Draw foot (part 4)

    # Draw head
    goto(position_x + 12.5, position_y)  # Move to starting point for the head
    rectangular(5, 5, other_parts_color)  # Draw head (part 1)
    goto(position_x + 17.5, position_y + 5)  # Move to the next position for the head
    rectangular(15, 15, body_n_head_color)  # Draw head (part 2)

    # Draw face
    goto(position_x + 6.5, position_y + 15)  # Move to the position for left eye
    dot(3, other_parts_color)  # Draw left eye
    goto(position_x + 14.5, position_y + 15)  # Move to the position for right eye
    dot(3, other_parts_color)  # Draw right eye
    goto(position_x + 8, position_y + 10)  # Move to the position for the mouth
    color(other_parts_color)  # Set the color for the mouth
    pendown()  # Start drawing the mouth
    pensize(2)  # Set the pen size
    left(90)  # Rotate to draw the mouth
    circle(4, 180)  # Draw the mouth as a semi-circle

    penup()  # Lift the pen
    home()  # Return to the origin


def visualise_data(data):
    # writing an instruction
    write_instructions()

    draw_robot(420, 30, 'yes', "misty rose", "red", "black")
    draw_robot(520, 0, 'no', "misty rose", "red", "black")
    draw_robot(420, -150, 'yes', "thistle", "light blue", "black")
    draw_robot(520, -180, 'no', "thistle", "light blue", "black")
    if data[0][0] == 'Start in Cell I3' and data[0][1] == 'Mark Low':
        x_start, y_start = -120, -50
        reversed_or_not = 'no'
        triangle_color = 'thistle'
        body_head_color = 'light blue'
        other_parts_color = 'black'
        draw_robot(x_start, y_start, reversed_or_not, triangle_color, body_head_color, other_parts_color)
    elif data[0][0] == 'Start in Cell I4' and data[0][1] == 'Mark Low':
        x_start, y_start = -120, 70
        reversed_or_not = 'yes'
        triangle_color = 'thistle'
        body_head_color = 'light blue'
        other_parts_color = 'black'
        draw_robot(x_start, y_start, reversed_or_not, triangle_color, body_head_color, other_parts_color)
    elif data[0][0] == 'Start in Cell I3' and data[0][1] == 'Mark High':
        x_start, y_start = -120, -50
        reversed_or_not = 'no'
        triangle_color = 'misty rose'
        body_head_color = 'red'
        other_parts_color = 'black'
        draw_robot(x_start, y_start, reversed_or_not, triangle_color, body_head_color, other_parts_color)
    elif data[0][0] == 'Start in Cell I4' and data[0][1] == 'Mark High':
        x_start, y_start = -120, 70
        reversed_or_not = 'yes'
        triangle_color = 'misty rose'
        body_head_color = 'red'
        other_parts_color = 'black'
        draw_robot(x_start, y_start, reversed_or_not, triangle_color, body_head_color, other_parts_color)

    x_curr, y_curr = x_start, y_start

    for move, instruction in data[1:]:

        # Update the position based on the move command
        if reversed_or_not == 'yes':
            if move == 'Go East':
                x_curr += 55
                y_curr -= 25
            elif move == 'Go West':
                x_curr -= 55
                y_curr -= 25
            elif move == 'Go North':
                y_curr += 70
            elif move == 'Go South':
                y_curr -= 120
        else:
            if move == 'Go East':
                x_curr += 55
                y_curr += 25
            elif move == 'Go West':
                x_curr -= 55
                y_curr += 25
            elif move == 'Go North':
                y_curr += 120
            elif move == 'Go South':
                y_curr -= 70

        if instruction != 'No Change':
            if instruction == 'Mark High':
                triangle_color = 'misty rose'
                body_head_color = 'red'
                other_parts_color = 'black'
            elif instruction == 'Mark Low':
                triangle_color = 'thistle'
                body_head_color = 'light blue'
                other_parts_color = 'black'

        reversed_or_not = 'yes' if reversed_or_not == 'no' else 'no'
        if instruction != 'No Change':
            # Make sure to draw the robot at the final position
            draw_robot(x_curr, y_curr, reversed_or_not, triangle_color, body_head_color, other_parts_color)


# Configure the drawing canvas
create_drawing_canvas(canvas_title="The density of robots in the world in 2070",
                      write_instructions=False)

# Create the data set and pass it to the student's function
visualise_data(data_set())  # <-- no argument for "data_set" when assessed

# Exit gracefully
release_drawing_canvas(student_name)
