from app import app
from flask import render_template, request, redirect
from app.models.game import play_game
from app.models.player import Player
import random

@app.route("/")
def index():
    return render_template("welcome_page.html", title="Home")

@app.route("/<player_1_choice>/<player_2_choice>")
def display_winner(player_1_choice, player_2_choice):

    player_1 = Player("Callum", player_1_choice)
    player_2 = Player("James", player_2_choice)

    players = [player_1, player_2]

    winner = play_game(player_1, player_2)
    return render_template("index.html", title=f"{winner} wins!", players=players, winner=winner)

@app.route("/play", methods=["GET", "POST"])
def play_page():
    return render_template("play.html", title="Play Against Computer")

@app.route("/play_computer", methods=["POST"])
def play_against_computer():
    player_name = request.form["player_name"]
    player_move = request.form["choice"]

    player_1 = Player(player_name, player_move)

    choices = ["rock", "paper", "scissors"]
    computer_move = choices[random.randint(0,2)]
    computer = Player("Computer", computer_move)

    winner = play_game(player_1, computer)
    print(winner)
    return render_template("/play.html", player_move=player_move, computer_move=computer_move, winner=winner, title=f"{winner} wins!")