import random


class Box:
    """Just a box."""

    def __init__(self, choices):
        self.state = []
        self.choices = choices

    def uniform(self, sizes):
        self.state = []
        for choice in self.choices:
            for item in range(sizes):
                self.state.append(choice)

    def random(self, length):
        self.state = []
        for i in range(length):
            self.state.append(random.choice(self.choices))

    def add(self, item):
        self.state.append(item)

    def remove(self, item):
        self.state.remove(item)

    def choose(self):
        if len(self.state) == 0:
            # print('dead choice')
            return -1
        return random.choice(self.state)

    def __len__(self):
        return len(self.state)

    def __str__(self):
        return str(self.state)


if __name__ == '__main__':
    space = [0, 1, 2, 3]
    mybox = Box(space)
    mybox.uniform(2)
    print(mybox.state)
    mybox.random(8)
    print(mybox.state)
