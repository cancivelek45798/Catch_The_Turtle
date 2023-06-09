import turtle

game_board = turtle.Screen()
game_board.bgcolor("ivory")
game_board.title("Turtle Python")

#Score Board
turtle_scoreboard = turtle.Turtle()
turtle_scoreboard.color("blue")
turtle_scoreboard.speed(0)

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

update_score()
game_board.onkey(increase_score, "e")

game_board.listen()

game_board.mainloop()
