import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key in dict.keys(kwargs):
            for i in range(0, kwargs[key]):
                self.contents.append(key)

    def draw(self, quantity):
        remaining = quantity
        if quantity > len(self.contents):
            return self.contents
        removed_items = []
        for i in range(0, remaining):
            random_index = random.randint(0, len(self.contents) - 1)
            removed_items.append(self.contents[random_index])
            self.contents.pop(random_index)
        return removed_items


class ContinueLoop(Exception):
    pass


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    good = 0
    for i in range(0, num_experiments):
        temp_copy = copy.deepcopy(hat)
        result = temp_copy.draw(num_balls_drawn)
        try:
            for key in dict.keys(expected_balls):
                for i in range(0, expected_balls[key]):
                    if not key in result:
                        raise ContinueLoop()
                    result.remove(key)
            good += 1
        except ContinueLoop:
            pass
    return good / num_experiments
