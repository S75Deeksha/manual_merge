import turtle

def draw_star(size, color):
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title(f"Manual Merge Demo - Star Size {size}")
    
    t = turtle.Turtle()
    t.speed(3)
    t.color(color)
    t.pensize(2)
    
    for _ in range(5):
        t.forward(size)
        t.right(144)
    
    t.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    draw_star(100, "white")
