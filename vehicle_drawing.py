import turtle
import tkinter as tk
import random
from draw_flowers import draw_flowers

# turtle screen with desired dimensions and background color
turtle.setup(width=1450, height=700)
screen = turtle.Screen()
screen.bgcolor("light green") # background color red
screen.title('Vehicle Deawing')

# maximum animation speed
turtle.tracer(1, 0) # 1 is the delay and 0 is the number of frames to skip


car_details = """The following sedan is in inventory:
    Make: BMW
    Model: 2001
    Mileage: 70000
    Price: $15000.0
    Number of doors: 4"""

suv_details = """The following SUV is in inventory:
    Make: Volvo
    Model: 2000
    Mileage: 30000
    Price: $18500.0
    Passenger Capacity: 5"""

truck_details = """The following truck is in inventory:
    Make: Toyota
    Model: 2002
    Mileage: 40000
    Price: $12000.0
    Drive type: 4WD"""


# load screen
def draw_initial_details():
    global car_details, suv_details, truck_details
    turtle.penup()
    turtle.goto(0, 300) # setting the position of the text on the screen using goto method of turtle module
    turtle.write("Vehicle Listing", font=("Calibri", 14, "bold")) 
    turtle.goto(-60, 290) 
    turtle.write("_____________________________", font=("Calibri", 14, "bold")) 

    turtle.goto(-500, 190)
    turtle.write(car_details, align="left", font=("Arial", 11, "normal"))

    turtle.goto(-200, 190)
    turtle.write(suv_details, align="left", font=("Arial", 11, "normal"))

    turtle.goto(100, 190)
    turtle.write(truck_details, align="left", font=("Arial", 11, "normal"))
    turtle.hideturtle()


draw_initial_details()


def clear_screen():
    for turtle_object in turtle.Screen().turtles(): # loop through all the turtle objects on the screen
        turtle_object.clear() # clear the turtle object on the screen using clear method of turtle module


# functions to draw cars
def draw_car():
    global car_details
    clear_screen()
    turtle.penup()
    turtle.goto(-530, 300)
    turtle.write("SEDAN INVENTORY", font=("Calibri", 14, "bold"))
    turtle.goto(-530, 290)
    turtle.write("____________________________", font=("Calibri", 14, "bold"))
    turtle.goto(-530, 190)
    turtle.write(car_details, align="left", font=("Arial", 11, "normal"))

    # -----------------------------------------------CAR--------------------------------------------------------#
    # parameters
    a = 20 # minimum length of the car
    b = 80 # maximum length of the car
    u = random.random() # random number between 0 and 1 to generate random length of the car
    car_length = a + u * (b - a) # length is calculated using the formula

    # turtle object
    car = turtle.Turtle() 
    # hiding initial turtle
    turtle.ht()  

    # lifts the pen of the turtle (car) and moves to starting point, so no drawing occurs
    car.penup()
    car.goto(-100, 0) # setting the position of the car on the screen using goto method of turtle module

    # random rgb values for the car
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()

    # drawing flowers
    draw_flowers()

    # initialising drawing of car object
    car.speed(0) 
    car.pendown() 
    car.fillcolor(red_amount, green_amount, blue_amount) 
    car.begin_fill()
    car.forward(car_length * 4)  # length of the car is 4 times the width
    car.left(90) # turn left by 90 degrees 
    car.forward(car_length / 1.175)  # width is 1.175 times the length
    car.left(90)
    car.forward(car_length * 5) # length is 5 times the width
    car.left(90)
    car.forward(car_length / 1.175)
    car.end_fill()
    # first wheel
    car.left(90)
    car.forward(car_length / 1.25) 
    car.right(90)
    car.forward(car_length / 8)
    car.fillcolor('black')
    car.begin_fill()
    car.circle(car_length / 3.45) 
    car.end_fill()
    # second wheel
    car.back(car_length / 8) 
    car.left(90)
    car.forward(car_length * 2.75) # distance between the two wheels is 2.75 times the length of the car
    car.right(90)
    car.forward(car_length / 8) # distance between the two wheels is 1/8 times the length of the car
    car.fillcolor('black')
    car.begin_fill()
    car.circle(car_length / 3.45) # radius of the wheel is 1/3.45 times the length of the car
    car.end_fill()
    # --------upper body-----------
    car.back(car_length / 8)
    car.left(90)
    car.forward(car_length * 1.45)
    car.left(90)
    car.forward(car_length / 1.175)
    car.left(90)
    car.forward(car_length * 0.75)
    # trapezium
    car.right(60)
    car.forward(car_length * 1.35)
    car.left(60)
    car.forward(car_length * 2.15)
    car.left(60)
    car.forward(car_length * 1.35)
    # middle line
    car.left(120)
    car.forward(car_length * 1.7)
    car.left(90)
    car.forward(car_length * 1.185)
    car.right(90)

    car.hideturtle()
    turtle.update()


def draw_suv():
    global suv_details
    clear_screen()
    turtle.penup()
    turtle.goto(-530, 300)
    turtle.write("TRUCK INVENTORY", font=("Calibri", 14, "bold"))
    turtle.goto(-530, 290)
    turtle.write("------------------------------", font=("Calibri", 14, "bold"))
    turtle.goto(-530, 190)
    turtle.write(suv_details, align="left", font=("Arial", 11, "normal"))

    
    # parameters
    a = 25
    b = 90
    u = random.random()
    suv_length = a + u * (b - a)

    # turtle object
    suv = turtle.Turtle()

    # hiding initial turtle
    turtle.ht()

    # random colors for vehicle
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()

    # drawing flowers
    draw_flowers()

    suv.penup()
    suv.goto(-100, 0)
    # ----------------initialise drawing of suv------------------- #
    suv.speed(0)
    suv.pendown()
    suv.fillcolor(red_amount, green_amount, blue_amount)
    suv.begin_fill()
    suv.forward(suv_length * 5)  # length
    suv.left(90)
    suv.forward(suv_length / 1.175)  # width
    suv.left(90)
    suv.forward(suv_length * 5)
    suv.left(90)
    suv.forward(suv_length / 1.175)
    suv.end_fill()
    # wheel1
    suv.left(90)
    suv.forward(suv_length / 1.25)
    suv.right(90)
    suv.forward(suv_length / 8)
    suv.fillcolor('black')
    suv.begin_fill()
    suv.circle(suv_length / 3.45)
    suv.end_fill()
    # wheel2
    suv.back(suv_length / 8)
    suv.left(90)
    suv.forward(suv_length * 2.75)
    suv.right(90)
    suv.forward(suv_length / 8)
    suv.fillcolor('black')
    suv.begin_fill()
    suv.circle(suv_length / 3.45)
    suv.end_fill()
    # -----------upper body-----------#
    suv.back(suv_length / 8)
    suv.left(90)
    suv.forward(suv_length * 1.45)
    suv.left(90)
    suv.forward(suv_length / 1.175)
    suv.left(90)
    suv.forward(suv_length * 1.6)
    # trapezium
    suv.right(60)
    suv.forward(suv_length * 1.2)
    suv.left(60)
    suv.forward(suv_length * 2.25)
    suv.left(63)
    suv.forward(suv_length * 1.2)
    # back-wheel
    suv.left(27)
    suv.forward(suv_length * 0.085)
    suv.right(90)
    suv.fillcolor('black')
    suv.begin_fill()
    suv.circle((suv_length / 2.95), extent=180)
    suv.end_fill()
    # middle line
    suv.left(90)
    suv.forward(suv_length * 0.785)
    suv.right(90)
    suv.forward(suv_length * 2.49)
    suv.left(90)
    suv.forward(suv_length * 1.075)

    turtle.update()
    suv.hideturtle()



def draw_truck():
    global truck_details
    clear_screen()
    turtle.penup()
    turtle.goto(-530, 300)
    turtle.write("Truck INVENTORY", font=("Calibri", 14, "bold"))
    turtle.goto(-530, 290)
    turtle.write("------------------------------", font=("Calibri", 14, "bold"))
    turtle.goto(-530, 190)
    turtle.write(truck_details, align="left", font=("Arial", 11, "normal"))


    # params
    a = 30
    b = 95
    u = random.random()
    truck_length = a + u * (b - a)

    # random colors for vehicle
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()

    # turtle object
    truck = turtle.Turtle()

    # hiding initial turtle
    turtle.ht()

    # drawing flowers
    draw_flowers()

    truck.penup()
    truck.goto(-200, 0)

    # initialising drawing of truck object
    truck.speed(0)
    truck.pendown()
    truck.fillcolor(red_amount, green_amount, blue_amount)
    truck.begin_fill()
    truck.forward(truck_length * 4.5)  # length
    truck.left(90)
    truck.forward(truck_length * 2.875)  # width
    truck.left(90)
    truck.forward(truck_length * 4.5)
    truck.left(90)
    truck.forward(truck_length * 2.875)
    truck.end_fill()
    # wheel1
    truck.left(90)
    truck.forward(truck_length / 1.975)
    truck.right(90)
    truck.forward(truck_length / 10.025)
    truck.fillcolor('black')
    truck.begin_fill()
    truck.circle(truck_length / 2.15) # radius of the wheel is 1/2.15 times the length of the truck 
    truck.end_fill()
    # wheel2
    truck.back(truck_length / 10.45)
    truck.left(90)
    truck.forward(truck_length * 1.285)
    truck.right(90)
    truck.forward(truck_length / 7)
    truck.fillcolor('black')
    truck.begin_fill()
    truck.circle(truck_length / 2.095)
    truck.end_fill()
    # trapezium
    truck.back(truck_length / 7.015)
    truck.left(90)
    truck.forward(truck_length * 2.7)
    truck.left(90)
    truck.forward(truck_length * 0.145)
    truck.right(90)
    truck.forward(truck_length * 1.15)
    truck.right(90)
    truck.fillcolor('black')
    truck.begin_fill()
    truck.circle(truck_length / 2.095)
    truck.end_fill()
    truck.left(90)
    truck.forward(truck_length * 1.75)
    truck.left(90)
    truck.forward(truck_length * 1.35)
    truck.left(60)
    truck.forward(truck_length * 1.75)
    truck.left(120)
    truck.forward(truck_length * 0.875)
    truck.left(90)
    truck.forward(truck_length * 1.5)
    truck.left(150)
    truck.forward(truck_length * 1.75)
    truck.left(30)
    truck.forward(truck_length * 1.425)

    truck.hideturtle()
    turtle.update()


def gencolors():
    blue_amount = random.random()
    green_amount = random.random()
    red_amount = random.random()
    # normalized RGB values (0 rep. absence of color and 1 represents the maximum intensity of that component)
    return red_amount,green_amount,blue_amount

draw_flowers()



# Create buttons using tkinter
root = tk.Tk()
root.geometry("280x100")  # Adjusting the window size
root.title("Buttons")

car_button = tk.Button(root, text="See Car", command=draw_car, width=10, height=2)  
car_button.pack(side=tk.LEFT,padx=6.5, pady=10)

suv_button = tk.Button(root, text="See SUV", command=draw_suv, width=10, height=2)  
suv_button.pack(side=tk.LEFT,padx=6.5, pady=10)

truck_button = tk.Button(root, text="See Truck", command=draw_truck, width=10, height=2)  
truck_button.pack(side=tk.LEFT,padx=6.5, pady=10)

root.mainloop()
