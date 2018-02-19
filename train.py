from GameManager import GameManager
import os.path
import pickle

manager = None
testing = False
if os.path.isfile('./instance.p') and input(
        'Do you want to load the previous instance? (y/n) ') == 'y':
    data = pickle.load(open('./instance.p', 'rb'))
    if input(
            'Do you want to train or test the model? (train/test) ') == 'test':
        manager = GameManager(prev_player=data, train=False)
        testing = True
    else:
        manager = GameManager(prev_player=data)
else:
    manager = GameManager()
trials = int(input('Enter number of trials: '))

wins = 0
loss = 0
while trials > 0:
    try:
        manager.simulate()
    except Exception as e:
        print("MENANCE has died")
        break

    if manager.check_win() == 2:
        loss += 1
    else:
        wins += 1
    manager.reset()
    trials -= 1

print("Exited with", str((wins / (wins + loss)) * 100) + "% winrate")

if not testing and input(
        "Do you want to dump this instance to disk? (y/n) ") == 'y':
    manager.player.dump()
