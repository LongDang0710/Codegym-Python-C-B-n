import turtle
import datetime

class Clock:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Continuous Clock - PythonTurtleAcademy")
        self.screen.bgcolor("lightblue")
        self.screen.setup(width=600, height=600)

        self.clock_face = turtle.Turtle()
        self.hour_hand = turtle.Turtle()
        self.minute_hand = turtle.Turtle()
        self.second_hand = turtle.Turtle()

        self.setup_clock_face()
        self.setup_hands()

    def setup_clock_face(self):
        self.clock_face.speed(0)
        self.clock_face.penup()
        self.clock_face.goto(0, -250)
        self.clock_face.pendown()
        self.clock_face.circle(250)

        for _ in range(12):
            self.clock_face.penup()
            self.clock_face.goto(0, 0)
            self.clock_face.setheading((self.clock_face.heading() - 30) % 360)
            self.clock_face.forward(200)
            self.clock_face.pendown()
            self.clock_face.forward(30)
            self.clock_face.penup()
            self.clock_face.forward(20)
            self.clock_face.stamp()
            self.clock_face.penup()
            self.clock_face.goto(0, 0)

        self.clock_face.hideturtle()

    def setup_hands(self):
        for hand in [self.hour_hand, self.minute_hand, self.second_hand]:
            hand.shape('arrow')
            hand.speed(0)
            hand.penup()
            hand.goto(0, 0)
            hand.pendown()

        self.hour_hand.color("black")
        self.hour_hand.width(7)
        self.minute_hand.color("black")
        self.minute_hand.width(5)
        self.second_hand.color("red")
        self.second_hand.width(3)

    def update_hands(self):
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        microsecond = now.microsecond

        second_angle = (second + microsecond / 1_000_000) * 6
        minute_angle = (minute + second / 60) * 6
        hour_angle = ((hour % 12) + minute / 60) * 30

        self.draw_hand(self.second_hand, 200, second_angle)
        self.draw_hand(self.minute_hand, 150, minute_angle)
        self.draw_hand(self.hour_hand, 100, hour_angle)

        self.screen.update()
        self.screen.ontimer(self.update_hands, 50)

    def draw_hand(self, hand, length, angle):
        hand.clear()
        hand.penup()
        hand.goto(0, 0)
        hand.setheading(90 - angle)
        hand.pendown()
        hand.forward(length)

if __name__ == "__main__":
    clock = Clock()
    turtle.tracer(0, 0)
    clock.update_hands()
    turtle.mainloop()