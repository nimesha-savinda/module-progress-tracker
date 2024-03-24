#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources id referenced within my code solution.
#Student ID:20530956
#Date: 10/12/2023

def range_check(x):
    """to check the range of the entered value"""
    while x not in range(0,140,20):
        print("Out of range")
        x = int(input("Enter a valid mark : "))
    return (x)

progress_list = [] #lists for Part B
credits_list = []
end_respond = "y"

while end_respond == "y":
    try:
        cr_pass = int(input("Please enter your credits at pass : "))
        checked_pass = range_check(cr_pass)
        cr_defer = int(input("Please enter your credits at defer : "))
        checked_defer = range_check(cr_defer)
        cr_fail = int(input("Please enter your credits at fail : "))
        checked_fail = range_check(cr_fail)
        print()
        if checked_pass + checked_defer + checked_fail != 120:
            print("Total Incorrect")
        else:

            credits_list.append(checked_pass)
            credits_list.append(checked_defer)
            credits_list.append(checked_fail)

            if 80 <= checked_fail:
                print("Exclude")
                progress_list.append("Exclude")
            elif checked_pass == 100:
                print("Progress (module trailer)")
                progress_list.append("Progress (module trailer)")
            elif checked_pass == 120:
                print("Progress")
                progress_list.append("Progress")
            else:
                print("Module retriever")
                progress_list.append("Module retriever")
        print()
        end_respond = str(input("Would you like to enter another set of data?: \n q = Quit y = Continue : "))
        end_respond = end_respond.lower()
        while end_respond != "q" and end_respond != "y":
            end_respond = str(input("Would you like to enter another set of data?: \n q = Quit y = Continue : "))
            end_respond = end_respond.lower()
        print()
    except ValueError:
        print("Integer required")

if not credits_list:  #Part_2
    print()
else:
    print("Part 2")
    starting_index = 0
    ending_index = 3
    for item in progress_list:
        print(item, end=" - ")
        marks_to_write = credits_list[starting_index:ending_index]
        print(str(marks_to_write).replace("[", "").replace("]", ""))
        starting_index += 3
        ending_index += 3

if not credits_list:  #Part 3
    print()
else:
    print()
    print("Part 3")
    f = open("part 3.txt", 'w')
    starting_index = 0
    ending_index = 3
    for item in progress_list:
        marks_to_write = (credits_list[starting_index:ending_index])
        f.write(item)
        f.write(" - ")
        f.write(str(marks_to_write).replace("[","").replace("]",""))
        f.write("\n")
        starting_index += 3
        ending_index += 3
    f = open("Part 3.txt" , 'r')
    data = f.read()
    f.readline()
    print(data)
    f.close()

#lists for the histrogram
progress_count = progress_list.count("Progress")
retriever_count = progress_list.count("Module retriever")
trailer_count = progress_list.count("Progress (module trailer)")
exclude_count = progress_list.count("Exclude")
total = progress_count + retriever_count + trailer_count + exclude_count
total_count = [progress_count,retriever_count,trailer_count,exclude_count]
max_count = max(total_count)

from graphics import *
import random

x_axis_elements = ["Progress","Retriever","Trailer","Exclude"]
colours = ["lightgreen","lightcyan","sandybrown","lightpink"]
random.shuffle(colours)
height_list = []

win = GraphWin("Histogram",710,500)
win.setBackground("white")

try:
    pixels_per_entry = 380 // max_count
    progress_height = pixels_per_entry * progress_count
    retriever_height = pixels_per_entry * retriever_count
    trailer_height = pixels_per_entry * trailer_count
    exclude_height = pixels_per_entry * exclude_count

    height_list.append(progress_height)
    height_list.append(retriever_height)
    height_list.append(trailer_height)
    height_list.append(exclude_height)

    line = Line(Point(10, win.getHeight() - 60), Point(700, win.getHeight() - 60))
    line.setOutline("black")
    line.draw(win)

    element = 0
    colour_pick = 0
    height_index = 0
    ending_x_point = 30
    starting_x_point = 0
    element_count = 0

    while ending_x_point != 670:
        starting_x_point = ending_x_point + 10 #this calculates the starting X point of the bar
        ending_x_point = starting_x_point + 150
        bar = Rectangle(Point(starting_x_point, win.getHeight() - 60), Point(ending_x_point, win.getHeight() - height_list[height_index] -60))
        Text(Point(starting_x_point + 75, win.getHeight() - 45), x_axis_elements[element]).draw(win)
        Text(Point(starting_x_point + 75, win.getHeight() - height_list[height_index] -60-10), str(total_count[element_count])).draw(win)
        bar.setFill(colours[colour_pick])
        colour_pick += 1
        element_count += 1
        height_index += 1
        element += 1
        bar.draw(win)

    footer = Text(Point(110, win.getHeight() - 15), f"{total} outcomes in total").draw(win)
    heading = Text(Point(100, 15), str("Histogram Results")).draw(win)

    win.getMouse()
    win.close()
except ZeroDivisionError:
    print()