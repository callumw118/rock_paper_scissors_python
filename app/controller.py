from app import app
from flask import render_template
from app.models.game import play_game
from app.models.player import Player

@app.route("/")
def index():
    return "Hello World"

@app.route("/<player_1_choice>/<player_2_choice>")
def display_winner(player_1_choice, player_2_choice):

    player_1 = Player("Callum", player_1_choice)
    player_2 = Player("Niijor", player_2_choice)

    players = [player_1, player_2]

    winner = play_game(player_1, player_2)
    return render_template("index.html", title="Home", players=players, winner=winner)