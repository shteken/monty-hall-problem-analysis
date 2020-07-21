import random
from matplotlib import pyplot as plt

def simulate_monty_hall(iter=1000):

    def monty_hall():
        doors = [True, False, False] # generate doors
        random.shuffle(doors)
        c1 = random.randint(0,2)
        chosen_door = doors[c1] # choose first door
        doors.pop(c1) 
        falses = [] # doors the host can show the participent
        for idx, val in enumerate(doors):
            if val == False:
                falses.append(idx)
        false_door = random.choice(falses) # the host show random false door to the participent
        doors.pop(false_door)
        alternative_door = doors[0] # the remaining door
        return chosen_door, alternative_door

    results = []
    for _ in range(iter):
        results.append(monty_hall())

    counter_for_chosen = 0
    for result in results:
        if result[0] == True:
            counter_for_chosen += 1

    return counter_for_chosen/iter

if __name__ == '__main__':
    print(simulate_monty_hall())