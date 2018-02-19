from Box import Box
import pickle


class MENANCE():
    """MENANCE instance."""

    def __init__(self, model, init_method='uniform', groups=9, sizes=10):
        self.moves = {}
        self.game = []
        self.init_method = init_method
        self.groups = groups
        self.sizes = sizes

        if model is not None:
            self.moves = model.moves
            self.init_method = model.init_method
            self.groups = model.groups
            self.sizes = model.sizes


    def move(self, state):
        joined = "".join(state)
        if joined not in self.moves:
            blank = [i for i, x in enumerate(state) if x == "0"]
            self.moves[joined] = Box(blank)

            if self.init_method == 'random':
                self.moves[joined].random(self.sizes)
            else:
                self.moves[joined].uniform(self.sizes)

        move = self.moves[joined].choose()
        if move != -1:
            self.game.append((joined, move))
        return move

    def regress(self, end):
        if end == 'win':
            for state, move in self.game:
                self.moves[state].add(move)
                self.moves[state].add(move)
                self.moves[state].add(move)
        elif end == 'draw':
            for state, move in self.game:
                self.moves[state].add(move)
        else:
            for state, move in self.game:
                self.moves[state].remove(move)

        if len(self.moves["".join(['0' for i in range(9)])]) == 0:
            raise Exception("MENANCE has died")

        self.game = []

    def dump(self, loc='./instance.p'):
        pickle.dump(self, open(loc, "wb"))
