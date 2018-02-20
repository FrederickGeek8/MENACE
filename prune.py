import pickle
import math

loc = input('Enter the path to the file you want to prune: ')
data = None
try:
    data = open(loc, 'rb')
except Exception as e:
    raise Exception("Could not read file")

menance = pickle.load(data)
done = 0
length = len(menance.moves)
for key in menance.moves:
    done += 1
    print("Pruning Box " + str(done) + "/" + str(length))
    state = menance.moves[key].state
    if len(state) > 0:
        unique = list(set(state))
        unique_count = [state.count(num) for num in unique]
        mmin = min(unique_count)
        new_count = [math.ceil(count / mmin) for count in unique_count]

        tmp = []
        for i in range(len(new_count)):
            orig = unique[i]
            for j in range(new_count[i]):
                tmp.append(orig)

        menance.moves[key].state = tmp

pickle.dump(menance, open(loc, "wb"))
