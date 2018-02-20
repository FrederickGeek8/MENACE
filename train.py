from GameManager import GameManager
from helpers import prune
import os.path
import pickle

manager = None
data = None
train = True
sizes = 10
prune_length = -1
init = 'uniform'

if os.path.isfile('./instance.p') and input(
        'Do you want to load the previous instance? (y/n) ') == 'y':
    data = pickle.load(open('./instance.p', 'rb'))
    if input(
            'Do you want to train or test the model? (train/test) ') == 'test':
        train = False

if train and data is None:
    if input('Init? (random or uniform) [uniform]: ') != '':
        init = 'random'

    lsizes = input('Init size? [10]: ')
    if lsizes != '':
        sizes = int(lsizes)

if train:
    tmp = input('Prune interval [-1]: ')
    if tmp != '':
        prune_length = int(tmp)

manager = GameManager(
    prev_player=data, train=train, sizes=sizes, init_method=init)
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
    if prune_length != -1 and trials % prune_length == 0:
        prune(manager.player)
    trials -= 1

print("Exited with", str((wins / (wins + loss)) * 100) + "% winrate")

if train and input("Do you want to dump this instance to disk? (y/n) ") == 'y':
    loc = input('Location [./instance.p]: ')
    if loc == '':
        manager.player.dump()
    else:
        manager.player.dump(loc)
