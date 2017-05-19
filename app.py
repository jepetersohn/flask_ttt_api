from flask import Flask, jsonify, request
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/game", methods=['GET'])
def game():
  boardState = list(request.args.getlist('board'))
  boardArray = list(boardState[0])
  move = randomPlay(boardArray)
  newBoard = placeMove(move, boardArray)
  return jsonify(newBoard)

def randomPlay(board):
  boardArray = [x for x in board if x != "X" and x != "O"]
  return random.choice(boardArray)

def placeMove(move, board):
  board[int(move)] = "O"
  return board


if __name__ == "__main__":
    app.run(debug=True)
