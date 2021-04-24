import random

def simulate_monty_hall_adjusted(n=1000):

    def monty_hall():
        doors = [True, False, False] # generate doors
        random.shuffle(doors)
        c1 = random.randint(0,2)
        chosen_door = doors[c1] # choose first door
        doors.pop(c1) 
        c2 = random.randint(0,1) # the host reveals a random door
        doors.pop(c2)
        alternative_door = doors[0] # the remaining door
        return chosen_door, alternative_door

    results = []
    for _ in range(n):
        results.append(monty_hall())

    relevant_results = [result for result in results if True in result] # if the host reveals True then the experiment is not relevant
    counter_for_chosen = 0
    for result in relevant_results:
        if result[0] == True:
            counter_for_chosen += 1

    n_relevant = len(relevant_results)
    return counter_for_chosen/n_relevant

if __name__ == '__main__':
    print(simulate_monty_hall_adjusted())