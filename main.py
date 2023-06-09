import turtle
import time

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
    sec = 5
    while sec >=0:
        update_countdown(sec)
        time.sleep(1)
        sec -= 1

update_score()
game_board.onkey(increase_score, "e")
countdowner()
game_board.mainloop()