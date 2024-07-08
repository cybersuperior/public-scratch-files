from turtle import *

def draw_prism():
    penup()
    goto(-150, -50)
    pendown()
    pencolor("white")
    fillcolor("black")
    pensize(5)
    begin_fill()
    goto(0, 200)
    goto(150, -50)
    goto(-150, -50)
    end_fill()

    penup()
    goto(-145, -48)
    pendown()
    pencolor("turquoise")
    pensize(3)
    goto(0, 195)
    goto(145, -48)
    goto(-145, -48)

def draw_rainbow():
    colors = ["#CC102D", "#E88514", "#FFFF28", "#7DC62C", "#71C0DE", "#634C8A"]
    start_x = 50
    start_y = 115
    end_y = 5
    for color in colors:
        penup()
        goto(start_x, start_y)
        pendown()
        pencolor(color)
        pensize(10)
        end_x = start_x + 500
        goto(end_x, end_y)
        end_y -= 10
        start_y -= 10
        start_x += 5

def draw_light():
    penup()
    goto(-450, 10)
    pendown()
    pencolor("white")
    pensize(4)
    goto(-60, 100)

def main():
    bgcolor("black")

    draw_rainbow()
    draw_prism()
    draw_light()

    hideturtle()
    done()

if __name__ == "__main__":
    main()