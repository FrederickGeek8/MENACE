from AdversarialManager import AdversarialManager
import os.path
import pickle

train = False
players = [None, None]
init_method = ['random', 'uniform']
sizes = [10, 10]
if os.path.isfile('./instance.p') and os.path.isfile(
        './instance2.p') and input('Load players? (y/n) ') == 'y':
    data = pickle.load(open('./instance.p', 'rb'))
    players[0] = data

    data2 = pickle.load(open('./instance2.p', 'rb'))
    players[1] = data2

    if input('Do you want to train or test the model? (train/test) '
             ) == 'train':
        train = True
else:
    train = True
    if input('Init P1? (random or uniform) [random]: ') != '':
        init_method[0] = 'uniform'

    lsizes = input('Init P1 size? [10]: ')
    if lsizes != '':
        sizes[0] = int(lsizes)

    if input('Init P2? (random or uniform) [uniform]: ') != '':
        init_method[1] = 'random'

    lsizes = input('Init P2 size? [10]: ')
    if lsizes != '':
        sizes[1] = int(lsizes)

manager = AdversarialManager(
    players=players, train=train, init_method=init_method, sizes=sizes)

trials = int(input('Enter number of trials: '))

player1 = 0
player2 = 0
draw = 0
while trials > 0:
    manager.simulate()

    check = manager.check_win()
    if check == 2:
        player2 += 1
    elif check == 1:
        player1 += 1
    else:
        draw += 1
    manager.reset()
    trials -= 1

print("Player 1 exited with a",
      str((player1 / (player1 + player2)) * 100) + "% winrate.")
print("Player 2 exited with a",
      str((player2 / (player1 + player2)) * 100) + "% winrate.")
print(str(draw / (draw + player1 + player2)) + "% of games were drawn.")

if train and input("Do you want to dump this instance to disk? (y/n) ") == 'y':
    loc = input('P1 Location [./instance.p]: ')
    if loc == '':
        manager.player.dump()
    else:
        manager.player.dump(loc)

    loc = input('P2 Location [./instance2.p]: ')
    if loc == '':
        manager.player2.dump('./instance2.p')
    else:
        manager.player2.dump(loc)
