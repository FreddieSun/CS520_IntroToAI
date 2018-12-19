"""
Inputs, global variables
"""

'''0 - start, 1~8 - used, 9 - dead'''
utility = []
for i in range(10):
    utility.append(0)

'''probabilities of transfering to next state'''
transfer_probability = []
for i in range(10):
    transfer_probability.append(0.1 * i)
transfer_probability[0] = 1

'''probabilities of staying in current state'''
stay_probability = []
for i in transfer_probability:
    stay_probability.append(1 - i)

'''probabilities of replacing'''
replace_probability = []
for i in range(10):
    replace_probability.append(1)
replace_probability[0] = 0

'''reward of transfer to next state'''
reward = []
for i in range(10):
    reward.append(100 - i * 10)
reward[-1] = 0

'''cost of replacing to new'''
cost_replace = 250

'''
discount factor β
the maximum error allowed in the utility of any state ε
iteration times t
'''
beta = 0.9
epsilon = 0.001
epochs = 0

'''optimal policy and two actions'''
optimal_policy = []
action_choice = ['use', 'replace']

if __name__ == '__main__':
    # value iterate
    while True:
        utility_update = []
        actions = []

        '''the maximum change in the utility of any state in an iteration'''
        delta = 0
        epochs += 1

        '''update utility of new and used states'''
        for i in range(9):
            value = [(stay_probability[i] * (reward[i] + beta * utility[i]) + transfer_probability[i] * (
                    reward[i] + beta * utility[i + 1])), replace_probability[i] * (-cost_replace + beta * utility[0])]

            temp_update = max(value)
            actions.append(value.index(temp_update))
            utility_update.append(temp_update)
            if abs(temp_update - utility[i]) > delta:
                delta = abs(temp_update - utility[i])

        '''update utility of dead state'''
        temp_update = -cost_replace + beta * utility[0]
        utility_update.append(temp_update)
        actions.append(1)

        if abs(temp_update - utility[-1]) > delta:
            delta = abs(temp_update - utility[-1])

        utility = utility_update
        optimal_policy = actions

        '''terminate'''
        if delta < epsilon * (1 - beta) / beta:
            break

    optimal_policy = [action_choice[i] for i in optimal_policy]
    print(utility)
    print(optimal_policy)
    print('epochs =', epochs)
