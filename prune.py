import pickle
import math
import progressbar

loc = input('Enter the path to the file you want to prune: ')
data = None
try:
    data = open(loc, 'rb')
except Exception as e:
    raise Exception("Could not read file")

menance = pickle.load(data)
done = 0
length = len(menance.moves)
pbartmp = progressbar.ProgressBar(maxval=1).default_widgets()
pbar = progressbar.ProgressBar(
    widgets=pbartmp[:], maxval=length)
del pbartmp
for key in menance.moves:
    done += 1
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
    pbar.update(done)
pbar.finish()
pickle.dump(menance, open(loc, "wb"))
