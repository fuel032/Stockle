import stocks
import random

possible_stocks = stocks.stocks
chosen_stock = random.choice(possible_stocks)
possible_stock = stocks.currentStock
current_stock = 0
        
finalStock = stocks.chooseStock(chosen_stock)

guess1 = input()
guess1x = stocks.chooseStock(guess1)

if guess1 == chosen_stock:
    print(str(chosen_stock) + " - " + str(stocks.chooseStock(chosen_stock)) + " Correct!")
else:
    if guess1x < stocks.chooseStock(chosen_stock):
        final = "Higher"
    if guess1x > stocks.chooseStock(chosen_stock):
        final = "Lower"
    print(str(guess1) + " - " + str(guess1x) + " " + final)

guess2 = input()
guess2x = stocks.chooseStock(guess2)

if guess2 == chosen_stock:
    print(str(chosen_stock) + " - " + str(stocks.chooseStock(chosen_stock)) + " Correct!")
else:
    if guess2x < stocks.chooseStock(chosen_stock):
        final = "Higher"
    if guess2x > stocks.chooseStock(chosen_stock):
        final = "Lower"
    print(str(guess2) + " - " + str(guess2x) + " " + final)

guess3 = input()
guess3x = stocks.chooseStock(guess3)

if guess3 == chosen_stock:
    print(str(chosen_stock) + " - " + str(stocks.chooseStock(chosen_stock)) + " Correct!")
else:
    if guess3x < stocks.chooseStock(chosen_stock):
        final = "Higher"
    if guess3x > stocks.chooseStock(chosen_stock):
        final = "Lower"
    print(str(guess3) + " - " + str(guess3x) + " " + final)

guess4 = input()
guess4x = stocks.chooseStock(guess4)

if guess4 == chosen_stock:
    print(str(chosen_stock) + " - " + str(stocks.chooseStock(chosen_stock)) + " Correct!")
else:
    if guess4x < stocks.chooseStock(chosen_stock):
        final = "Higher"
    if guess4x > stocks.chooseStock(chosen_stock):
        final = "Lower"
    print(str(guess4) + " - " + str(guess4x) + " " + final)

guess5 = input()
guess5x = stocks.chooseStock(guess5)

if guess5 == chosen_stock:
    print(str(chosen_stock) + " - " + str(stocks.chooseStock(chosen_stock)) + " Correct!")
else:
    if guess5x < stocks.chooseStock(chosen_stock):
        final = "Higher"
    if guess5x > stocks.chooseStock(chosen_stock):
        final = "Lower"
    print(str(guess5) + " - " + str(guess5x) + " " + final)

guess6 = input()
guess6x = stocks.chooseStock(guess6)

if guess6 == chosen_stock:
    print(str(chosen_stock) + " - " + str(stocks.chooseStock(chosen_stock)) + " Correct!")
else:
    print("You failed! Nice try. The stock was: " + chosen_stock + " - " + str(stocks.chooseStock(chosen_stock)) + "!")