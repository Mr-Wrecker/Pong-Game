import turtle
import time
import random
import os


def start(screen):

    def change_value():
        os.system("aplay ref/sound/Select.wav&")
        selector.value = not selector.value

    def call_method():
        if selector.value:
            os.system("aplay ref/sound/Menu.wav&")
            selector.turn = 5
        else:
            os.system("aplay ref/sound/Select.wav&")
            pass

    selector = turtle.Turtle()
    selector.value = True
    selector.turn = 0
    selector.speed(0)
    selector.color('#301a17')
    selector.shape("classic")
    selector.penup()

    screen.bgpic("ref/Part-1.png")
    Text = turtle.Turtle()
    Text.speed(0)
    Text.hideturtle()
    Text.color('#301a17')
    Text.penup()
    Text.goto(320, -140)
    dis = "Start Game\n\nSet Player Name"
    Text.write(dis, align="right", font=("calibri", 18, "bold"))

    screen.listen()
    screen.onkeypress(change_value, "Up")
    screen.onkeypress(change_value, "Down")
    screen.onkeypress(call_method, "Return")

    while True:
        if selector.value:
            selector.setpos(80, -65)
            if selector.turn == 5:
                break
        else:
            selector.setpos(80, -125)
        screen.update()
        time.sleep(.1)


def end(screen):
    time.sleep(1)
    screen.clear()
    screen.tracer(0)
    screen.bgpic('ref/Part-3.png')

    win = 'ref/Part-4.gif'
    screen.addshape(win)
    cup = turtle.Turtle()
    cup.speed(0)
    cup.shape(win)
    cup.penup()
    cup.goto(-100, -20)
    os.system('aplay ref/sound/Win.wav&')

    while True:
        time.sleep(.01)
        screen.update()
        cup.left(1)
        cup.forward(.3)


def main(screen):
    time.sleep(1)

    # Function
    def move_up_a():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def move_down_a():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def move_up_b():
        y = paddle_b.ycor()
        y += 6
        paddle_b.sety(y)

    def move_down_b():
        y = paddle_b.ycor()
        y -= 6
        paddle_b.sety(y)

    def print_score_a():
        score_board_a = 'ref/rank/Asset {}.gif'.format(score_a)
        screen.addshape(score_board_a)
        sb_a = turtle.Turtle()
        sb_a.shape(score_board_a)
        sb_a.speed(0)
        sb_a.penup()
        sb_a.goto(-200, 180)

    def print_score_b():
        score_board_b = 'ref/rank/Asset {}.gif'.format(score_b + 10)
        screen.addshape(score_board_b)
        sb_b = turtle.Turtle()
        sb_b.shape(score_board_b)
        sb_b.speed(0)
        sb_b.penup()
        sb_b.goto(200, 180)

    screen.clear()
    screen.tracer(0)
    screen.bgpic("ref/Part-2.png")

    score_a = 1
    score_b = 1

    # Show Screen Board
    print_score_a()
    print_score_b()

    # Ball
    game_speed = 2
    Ball = 'ref/Ball.gif'
    screen.addshape(Ball)
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape(Ball)
    ball.penup()
    ball.goto(0, 0)
    ball.dx = random.choice((1, -1)) * game_speed
    ball.dy = game_speed

    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(10)
    paddle_a.shape("square")
    paddle_a.color("green")
    paddle_a.shapesize(stretch_wid=4, stretch_len=.5)
    paddle_a.penup()
    paddle_a.goto(-380, 0)

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("green")
    paddle_b.shapesize(stretch_wid=4, stretch_len=.5)
    paddle_b.penup()
    paddle_b.goto(380, 0)

    screen.listen()
    screen.onkeypress(move_up_a, "w")
    screen.onkeypress(move_down_a, "s")

    start_time = time.perf_counter()
    goal = False
    while_speed = .004

    while True:
        time.sleep(while_speed)
        screen.update()

        if goal:
            time.sleep(2)
            goal = False

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Computer Player
        if (ball.ycor() > paddle_b.ycor() - 55) and (ball.xcor() > 55):
            if random.choice((0, 1, 0)):
                move_up_b()
        elif (ball.ycor() < paddle_b.ycor() + 55) and (ball.xcor() > 55):
            if random.choice((1, 0, 0)):
                move_down_b()

        # Check Player Out
        if paddle_b.ycor() > 165:
            paddle_b.sety(165)
        if paddle_b.ycor() < -165:
            paddle_b.sety(-165)
        if paddle_a.ycor() > 165:
            paddle_a.sety(165)
        if paddle_a.ycor() < -165:
            paddle_a.sety(-165)

        # Border Checking
        if ball.ycor() > 210:
            ball.sety(210)
            os.system('aplay ref/sound/Hurt.wav&')
            ball.dy *= -1

        if ball.ycor() < -210:
            ball.sety(-210)
            os.system('aplay ref/sound/Hurt.wav&')
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx = random.choice((2, -2))
            score_a += 1
            os.system("aplay ref/sound/Goal.wav&")
            while_speed = .004
            game_speed = 4
            print_score_a()
            goal = True

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx = random.choice((2, -2))
            score_b += 1
            os.system("aplay ref/sound/Goal.wav&")
            while_speed = .004
            game_speed = 4
            print_score_b()
            goal = True

        # Paddle and Ball Collisions
        if (ball.xcor() > 345) and (ball.ycor() < paddle_b.ycor() + 45 and ball.ycor() > paddle_b.ycor() - 51):
            ball.setx(345)
            ball.dx *= -1
            os.system("aplay ref/sound/Hurt.wav&")

        if (ball.xcor() < -345) and (ball.ycor() < paddle_a.ycor() + 45 and ball.ycor() > paddle_a.ycor() - 51):
            ball.setx(-345)
            ball.dx *= -1
            os.system("aplay ref/sound/Hurt.wav&")

        # Speed Up
        if time.perf_counter() > (start_time + 10):
            game_speed += 2
            while_speed -= .0008
            start_time = time.perf_counter()

        # Win The Game
        if (score_a > 5 or score_b > 5):
            break


if __name__ == "__main__":
    window = turtle.Screen()
    window.setup(width=800, height=460)
    window.title("Black Board Football")
    start(window)
    del(start)
    main(window)
    del(main)
    end(window)
