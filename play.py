from PlayManager import PlayManager
import os.path
import pickle

manager = None
if os.path.isfile('./instance.p'):
    data = pickle.load(open('./instance.p', 'rb'))
    manager = PlayManager(prev_player=data)
else:
    raise Exception("Must train model first!")

while manager.check_win() == 0:
    manager.simulate()
    print(manager)
    if manager.check_win() != 0:
        break
    while True:
        x = int(input("Enter the X coordinate (1-3) of your move: ")) - 1
        y = int(input("Enter the Y coordinate (1-3) of your move: ")) - 1
        if manager.move(x, y):
            break
        else:
            print("Invalid coordinates. Please try again.")

    print(manager)

winner = manager.check_win()

if winner == -1:
    print("The match ended in a draw.")
else:
    print("The winner is: Player", winner)
