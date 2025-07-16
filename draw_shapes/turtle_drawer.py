import turtle
import math, tkinter.colorchooser, random


class TurtleDrawer():
    def __init__(self, file_name):
        self.wn = turtle.Screen()
        self.pd = 0
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.output_file = open(f"{file_name}.py", "w")

        self.output_file.write("""import turtle,math

def draw_right_triangle(side_length, angle_degrees):
    angle_radians = math.radians(angle_degrees)

    t.forward(side_length)

    t.left(90)
    t.forward(side_length)


    hypotenuse_length = side_length / math.cos(angle_radians)
    t.left(180 - angle_degrees)
    t.forward(hypotenuse_length)

def circlem():
    global y2, x2
    y2 = t.ycor()
    x2 = t.xcor()
    t.penup()
    t.goto(t.xcor(), y2 - 50)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    t.goto(x2 + 50, y2)
    t.pendown()


# Create a turtle object
t = turtle.Turtle()
t.speed(0)
                
def square():
    t.begin_fill()
    t.forward(50)
    t.setheading(270)
    t.forward(50)
    t.setheading(180)
    t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(360)
    t.end_fill()
                
                
                
def draw_fish():
    x = t.xcor()
    y = t.ycor()
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.left(135)
    t.forward(1)
    t.circle(400, 90)  # Double the radius from 200 to 400
    t.right(270)
    t.forward(1)
    t.circle(400, 90)  # Double the radius from 200 to 400
    t.forward(200)  # Double the length from 100 to 200
    t.right(135)
    t.forward(280)  # Double the length from 140 to 280
    t.right(135)
    t.forward(200)  # Double the length from 100 to 200
    t.setheading(180)

    t.penup()
    
    \n""")

    def goto_clicked_point(self, x, y):
        self.pen.goto(x, y)
        self.output_file.write("t.goto({}, {})\n".format(x, y))

    def square(self):
        self.pen.begin_fill()
        self.pen.forward(50)
        self.pen.setheading(270)
        self.pen.forward(50)
        self.pen.setheading(180)
        self.pen.forward(50)
        self.pen.setheading(90)
        self.pen.forward(50)
        self.pen.setheading(360)
        self.pen.end_fill()
        self.output_file.write("square()\n")

    def q(self):
        self.pen.setheading(135)
        self.output_file.write("t.setheading(135)\n")

    def e(self):
        self.pen.setheading(45)
        self.output_file.write("t.setheading(45)\n")

    def w(self):
        self.pen.setheading(90)
        self.output_file.write("t.setheading(90)\n")

    def a(self):
        self.pen.setheading(180)
        self.output_file.write("t.setheading(180)\n")

    def d(self):
        self.pen.setheading(360)
        self.output_file.write("t.setheading(360)\n")

    def z(self):
        self.pen.setheading(225)
        self.output_file.write("t.setheading(225)\n")

    def c(self):
        self.pen.setheading(315)
        self.output_file.write("t.setheading(315)\n")

    def x(self):
        self.pen.setheading(270)
        self.output_file.write("t.setheading(270)\n")

    def s(self):
        y = self.pen.ycor()
        self.pen.forward(50)
        self.output_file.write(f"t.forward(50)\n")

    def pud(self):
        if self.pd % 2 == 0:
            self.pen.penup()
            self.pd += 1
            self.output_file.write("t.penup()\n")
        else:
            self.pen.pendown()
            self.pd += 1
            self.output_file.write("t.pendown()\n")

    def short(self):
        self.pen.forward(25)
        self.output_file.write("t.forward(25)\n")

    def circlem(self):
        y2 = self.pen.ycor()
        x2 = self.pen.xcor()
        self.pen.penup()
        self.pen.goto(self.pen.xcor(), y2 - 50)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(random.randrange(30,50))
        self.pen.end_fill()
        self.pen.penup()
        self.pen.goto(x2 + 50, y2)
        self.output_file.write("circlem()\n")
        self.pen.pendown()

    def draw_right_triangle(self):
        side_length = 50
        angle_degrees = 45

        self.output_file.write(f"draw_right_triangle({side_length}, {angle_degrees})\n")

        angle_radians = math.radians(angle_degrees)

        self.pen.forward(side_length)
        self.pen.left(90)
        self.pen.forward(side_length)

        hypotenuse_length = side_length / math.cos(angle_radians)

        self.pen.left(180 - angle_degrees)
        self.pen.forward(hypotenuse_length)

    def open_color_chooser(self):
        # Open a color dialog box
        color = tkinter.colorchooser.askcolor()[1]

        # Check if a color is selected
        if color:
            # Set the turtle fill color
            self.pen.fillcolor(color)

        self.output_file.write('''t.fillcolor("{}")\n'''.format(color))

    def draw_fish(self):
        x = self.pen.xcor()
        y = self.pen.ycor()
        self.pen.penup()
        self.pen.goto(x, y)
        self.pen.pendown()

        self.pen.left(135)
        self.pen.forward(1)
        self.pen.circle(400, 90)  # Double the radius from 200 to 400
        self.pen.right(270)
        self.pen.forward(1)
        self.pen.circle(400, 90)  # Double the radius from 200 to 400
        self.pen.forward(200)  # Double the length from 100 to 200
        self.pen.right(135)
        self.pen.forward(280)  # Double the length from 140 to 280
        self.pen.right(135)
        self.pen.forward(200)  # Double the length from 100 to 200
        self.pen.setheading(180)

        self.pen.penup()

    def fill_shape(self):
        self.pen.begin_fill()
        self.output_file.write("t.begin_fill()\n")

    def end_fill_shape(self):
        self.pen.end_fill()
        self.output_file.write("t.end_fill()\n")

    def end_shape(self):
        self.output_file.write("# End of shape\n")

    def f(self):
        self.pen.forward(10)
        self.output_file.write("t.forward(10)\n")

    def close_program(self):
        self.output_file.write("t.done()\n")
        self.output_file.close()
        self.wn.bye()

    def run(self):
        self.pen.goto(0, 0)
        self.wn.onscreenclick(self.goto_clicked_point)
        self.wn.listen()
        self.wn.onkeypress(self.q, "q")
        self.wn.onkeypress(self.e, "e")
        self.wn.onkeypress(self.w, "w")
        self.wn.onkeypress(self.s, "s")
        self.wn.onkeypress(self.a, "a")
        self.wn.onkeypress(self.d, "d")
        self.wn.onkeypress(self.z, "z")
        self.wn.onkeypress(self.f, "f")
        self.wn.onkeypress(self.x, "x")
        self.wn.onkeypress(self.c, "c")
        self.wn.onkeypress(self.pud, "p")
        self.wn.onkeypress(self.circlem, "l")
        self.wn.onkeypress(self.draw_right_triangle, "o")
        self.wn.onkeypress(self.square, "r")
        self.wn.onkeypress(self.fill_shape, "n")  # 'n' key to start filling the shape
        self.wn.onkeypress(self.end_fill_shape, "b")  # 'b' key to end filling the shape
        self.wn.onkeypress(self.end_shape, "m")
        self.wn.onkeypress(self.open_color_chooser, 't')
        self.wn.onkeypress(self.draw_fish,"y")
