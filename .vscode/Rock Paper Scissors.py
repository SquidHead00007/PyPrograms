print("Welcome to rock paper scissors!!!")
player1 = input("If you would like to pick rock, please type in Rock, if you would like to pick paper please type in Paper, and if you pick scissors please type in Scissors[CASE SENSITIVE]: ")
player2 = input("If you would like to pick rock, please type in Rock, if you would like to pick paper please type in Paper, and if you pick scissors please type in Scissors[CASE SENSITIVE]: ")
if player1 == "Rock" and player2 == "Scissors":
    print("Player 1 Wins!!!")

elif player1 == "Scissors" and player2 == "Paper":
    print("Player 1 Wins!!!")

elif player1 == "Paper" and player2 == "Rock":
    print("Player 1 Wins!!!")



elif player1 == "Scissors" and player2 == "Rock":
    print("Player 2 Wins!!!")

elif player1 == "Paper" and player2 == "Scissors":
    print("Player 2 Wins!!!")

elif player1 == "Rock" and player2 == "Paper":
    print("Player 2 Wins!!!")


else:
    print("It's a tie!!!")