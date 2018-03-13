import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from GameManager import GameManager
from Game2Manager import Game2Manager
from AdversarialManager import AdversarialManager
from helpers import test_p1, test_p2, prune
# train some people
train_samples = 100
train_length = 2500
prune_length = -1
prune_p1 = False

tmp = input('Prune interval [-1]: ')
if tmp != '':
    prune_length = int(tmp)

if input('Prune P1? (y/n) ') == 'y':
    prune_p1 = True

print("Initalizing P1 with default parameters")
manager = GameManager(init_method="random")
print("Initalizing P2 with default parameters")
manager2 = Game2Manager()

print("Training P1...")
p1_graph = []
for i in range(train_samples):
    trials = train_length
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
        if prune_p1 and prune_length != -1 and trials % prune_length == 0:
            prune(manager.player)
        trials -= 1
    p1_graph.append((wins / (wins + loss)) * 100)
    if i % 20 == 0:
        print("P1 Trial", i)

print("Training P2...")
p2_graph = []
for i in range(train_samples):
    trials = train_length
    wins = 0
    loss = 0
    while trials > 0:
        try:
            manager2.simulate()
        except Exception as e:
            print("MENANCE has died")
            break

        if manager2.check_win() == 1:
            loss += 1
        else:
            wins += 1
        manager2.reset()
        if prune_length != -1 and trials % prune_length == 0:
            prune(manager2.player)

        trials -= 1
    p2_graph.append((wins / (wins + loss)) * 100)

    if i % 20 == 0:
        print("P2 Trial", i)

# train them against one another
print("Setting up Adversarial Stage")
players = [manager.player, manager2.player]
fight_manager = AdversarialManager(players=players, train=True)
print("Adversarial Stage...")
fight_samples = 100
fight_length = 5000
p2_agraph = []
p2_improv = []
p1_agraph = []
p1_improv = []
for i in range(fight_samples):
    trials = fight_length
    player1 = 0
    player2 = 0
    draw = 0
    while trials > 0:
        fight_manager.simulate()

        check = fight_manager.check_win()
        if check == 2:
            player2 += 1
        elif check == 1:
            player1 += 1
        else:
            draw += 1
        fight_manager.reset()

        if prune_length != -1 and trials % prune_length == 0:
            fight_manager.prune()
        trials -= 1
    p1_agraph.append((player1 / (player1 + player2)) * 100)
    p1_improv.append(test_p1(fight_manager.player))
    p2_agraph.append((player2 / (player1 + player2)) * 100)
    p2_improv.append(test_p2(fight_manager.player2))

    if i % 20 == 0:
        print("Fight Trial", i)

plt.subplot(131)
X = [i for i in range(0, train_length * train_samples, train_length)]
p1_plot, = plt.plot(X, p1_graph, 'r', label='Player 1')
p2_plot, = plt.plot(X, p2_graph, 'b', label='Player 2')
plt.legend(handles=[p1_plot, p2_plot])

plt.subplot(132)
X2 = [i for i in range(0, fight_length * fight_samples, fight_length)]
p1_iplot, = plt.plot(X2, p1_improv, 'r', label='P1 Progress')
p2_iplot, = plt.plot(X2, p2_improv, 'b', label='P2 Progress')
plt.legend(handles=[p1_iplot, p2_iplot])

plt.subplot(133)

p1_gplot, = plt.plot(X2, p1_agraph, 'r', label='P1 Adver.')
p2_gplot, = plt.plot(X2, p2_agraph, 'b', label='P2 Adver.')
plt.legend(handles=[p1_gplot, p2_gplot])

plt.show()
