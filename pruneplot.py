import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import asyncio
from GameManager import GameManager
from helpers import prune
from concurrent.futures import ProcessPoolExecutor

manager = GameManager(sizes=10)
manager2 = GameManager(sizes=10)

repeat = 1000
trial_length = 1000


def stage1():
    graph = []
    for i in range(repeat):
        trials = trial_length
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
        if i % 100 == 0:
            print("NTrial", i)
    return graph


def stage2():
    graph2 = []
    for i in range(repeat):
        trials = trial_length
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
        prune(manager2.player)
        if i % 100 == 0:
            print("PTrial", i)
    return graph2


executor = ProcessPoolExecutor(2)
loop = asyncio.get_event_loop()

graph, graph2 = loop.run_until_complete(
    asyncio.gather(
        asyncio.ensure_future(loop.run_in_executor(executor, stage1)),
        asyncio.ensure_future(loop.run_in_executor(executor, stage2))))
loop.close()

X = [i for i in range(0, trial_length * repeat, trial_length)]
fig, ax = plt.subplots()
uniform, = plt.plot(X, graph, 'r', label='Normal')
random, = plt.plot(X, graph2, 'b', label='Pruned')
mmin, mmax = min(min(graph), min(graph2)), max(max(graph), max(graph2))
loc = plticker.MultipleLocator(base=(mmax - mmin) // 10)
ax.yaxis.set_major_locator(loc)
plt.legend(handles=[uniform, random])
plt.show()
