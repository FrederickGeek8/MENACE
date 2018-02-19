import matplotlib.pyplot as plt
from GameManager import GameManager

manager = GameManager()

graph = []
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

X = [i for i in range (0,1000 * 100,1000)]
line1 = plt.plot(X,graph)
plt.show()
