import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from GameManager import GameManager

manager = GameManager(sizes=20)
manager2 = GameManager(init_method='random', sizes=20)

graph = []
graph2 = []
for i in range(100):
    trials = 1000
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
    graph.append((wins / (wins + loss)) * 100)

for i in range(100):
    trials = 1000
    wins = 0
    loss = 0
    while trials > 0:
        try:
            manager2.simulate()
        except Exception as e:
            print("MENANCE has died")
            break

        if manager2.check_win() == 2:
            loss += 1
        else:
            wins += 1
        manager2.reset()
        trials -= 1
    graph2.append((wins / (wins + loss)) * 100)

X = [i for i in range(0, 1000 * 100, 1000)]
fig, ax = plt.subplots()
ax.plot(X, graph, 'r', X, graph2, 'b')
mmin, mmax = min(min(graph), min(graph2)), max(max(graph), max(graph2))
loc = plticker.MultipleLocator(base=(mmax - mmin) // 10)
ax.yaxis.set_major_locator(loc)
plt.show()
