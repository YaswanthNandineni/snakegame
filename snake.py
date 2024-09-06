from turtle import *
y_values=[(0,0) ,(-20,0) ,(-40,0)]
move_distance=20
UP=90
LEFT=180
DOWN=270
RIGHT=0


class Snake:
    def __init__(self):
       self.segments=[]
       self.create_snake()
       self.head=self.segments[0]
    def create_snake(self):

        for i_position in y_values:
            self.add_segment(i_position)

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.segments.append(new_turtle)


    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)
    def up(self):
        if self.head.heading()!=DOWN:
          self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
          self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
          self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
          self.head.setheading(RIGHT)

