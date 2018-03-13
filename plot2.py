import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from Game2Manager import Game2Manager
import progressbar

manager = Game2Manager(sizes=10)
manager2 = Game2Manager(init_method='random', sizes=10)

graph = []
graph2 = []
repeat = 500
for i in range(repeat):
    trials = 1000
    wins = 0
    loss = 0
    while trials > 0:
        try:
            manager.simulate()
        except Exception as e:
            print("MENANCE has died")
            break

        if manager.check_win() == 1:
            loss += 1
        else:
            wins += 1
        manager.reset()
        trials -= 1
    graph.append((wins / (wins + loss)) * 100)
    if i % 100 == 0:
        print("Trial", i)

for i in range(repeat):
    trials = 1000
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
        trials -= 1
    graph2.append((wins / (wins + loss)) * 100)
    if i % 100 == 0:
        print("Trial", i)

X = [i for i in range(0, 1000 * repeat, 1000)]
fig, ax = plt.subplots()
uniform, = plt.plot(X, graph, 'r', label='Uniform')
random, = plt.plot(X, graph2, 'b', label='Random')
mmin, mmax = min(min(graph), min(graph2)), max(max(graph), max(graph2))
loc = plticker.MultipleLocator(base=(mmax - mmin) // 10)
ax.yaxis.set_major_locator(loc)
plt.legend(handles=[uniform, random])
plt.show()
