from Game2Manager import Game2Manager
import os.path
import pickle
import progressbar
from helpers import prune

manager = None
data = None
train = True
sizes = 10
prune_length = -1
init = 'uniform'

if os.path.isfile('./instance2.p') and input(
        'Do you want to load the previous instance? (y/n) ') == 'y':
    data = pickle.load(open('./instance2.p', 'rb'))
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


manager = Game2Manager(
    prev_player=data, train=train, sizes=sizes, init_method=init)
trials_ = int(input('Enter number of trials: '))
trials = trials_
pbartmp = progressbar.ProgressBar(maxval=1).default_widgets()
pbar = progressbar.ProgressBar(
    widgets=pbartmp[:], maxval=trials)
del pbartmp
wins = 0
loss = 0
while trials > 0:
    manager.simulate()

    if manager.check_win() == 1:
        loss += 1
    else:
        wins += 1
    manager.reset()

    if prune_length != -1 and trials % prune_length == 0:
        prune(manager.player)
    pbar.update(trials_ - trials)
    trials -= 1
pbar.finish()
print("Exited with", str((wins / (wins + loss)) * 100) + "% winrate")

if train and input("Do you want to dump this instance to disk? (y/n) ") == 'y':
    loc = input('Location [./instance2.p]: ')
    if loc == '':
        manager.player.dump('./instance2.p')
    else:
        manager.player.dump(loc)
