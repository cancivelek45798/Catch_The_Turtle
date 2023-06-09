import turtle
import time
import random
import threading

game_board = turtle.Screen()
game_board.bgcolor("ivory")
game_board.title("Turtle Python")
game_board.listen()

#Score Board
turtle_scoreboard = turtle.Turtle()
turtle_scoreboard.color("blue")
turtle_scoreboard.speed(0)
turtle_scoreboard.hideturtle()

score = 0

def update_score():
    turtle_scoreboard.clear()
    turtle_scoreboard.penup()
    score_board_x = 0
    score_board_y = game_board.window_height() // 2 - 30
    turtle_scoreboard.goto(score_board_x, score_board_y)
    turtle_scoreboard.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

def increase_score():
    global score
    score += 1
    update_score()


#Countdown
turtle_countdown = turtle.Turtle()
turtle_countdown.color("light blue")
turtle_countdown.speed(0)
turtle_countdown.hideturtle()

def update_countdown(sec):
    turtle_countdown.clear()
    turtle_countdown.penup()
    score_board_x = 0
    score_board_y = game_board.window_height() // 2 - 50
    turtle_countdown.goto(score_board_x, score_board_y)
    turtle_countdown.write(f"Time: {sec}", align="center", font=("Arial", 16, "bold"))

def countdowner():
    sec = 30
    while sec >=0:
        update_countdown(sec)
        time.sleep(1)
        sec -= 1

    turtle_countdown.clear()
    turtle_countdown.goto(0, 0)
    turtle_countdown.write("GAME OVER!", align="center", font=("Arial", 24, "bold"))

    game_board.onkey(game_board.bye, "q")  # Eğer 'e' tuşuna basılırsa programı sonlandır


#Turtle
turtle_turtle = turtle.Turtle()
turtle_turtle.color("green")
turtle_turtle.speed()
turtle_turtle.shape("turtle")
turtle_turtle.shapesize(3)
turtle_turtle.penup()

#Turtle Movement
def turtle_movement():
    while True:
        turtle_x = random.randint(-350, 350)
        turtle_y = random.randint(-350, 350)
        turtle_turtle.goto(turtle_x, turtle_y)

movement_thread = threading.Thread(target=lambda: turtle_movement())
score_thread = threading.Thread(target=lambda: update_score())
countdown_thread = threading.Thread(target=lambda: countdowner())

movement_thread.start()
score_thread.start()
countdown_thread.start()

game_board.onkey(increase_score, "e")
game_board.mainloop()

