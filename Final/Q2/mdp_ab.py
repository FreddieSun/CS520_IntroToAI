import math
import pdb

# 0 - start, 1~8 - used, 9 - dead
utility = [0 for i in range(10)]
# probs of transfering to next state
probs_trans = [0.1 * i for i in range(10)]
probs_trans[0] = 1
# probs of staying in current state
probs_stay = [1 - i for i in probs_trans]
# probs of replacing
probs_replace = [1 for i in range(10)]
probs_replace[0] = 0
# reward of transfer to next state
reward = [100 - i * 10 for i in range(10)]
reward[-1] = 0
# pdb.set_trace()
cost_replace = 250
beta = 0.9
epsilon = 0.001
epochs = 0
optimal_policy = []
action_choice = ['use', 'replace']
# value iterate
while (True):
    utility_update = []
    actions = []
    delta = 0
    epochs += 1
    # update utility of new and used states
    for i in range(9):
        v = [reward[i] + beta * (probs_stay[i] * utility[i] + probs_trans[i] * utility[i + 1]),
             -cost_replace + probs_replace[i] * beta * utility[0]]
        u_update = max(v)
        actions.append(v.index(u_update))
        # pdb.set_trace()
        utility_update.append(u_update)
        if abs(u_update - utility[i]) > delta:
            delta = abs(u_update - utility[i])
    # update utility of dead state
    u_update = -cost_replace + beta * utility[0]
    utility_update.append(u_update)
    actions.append(1)
    if abs(u_update - utility[-1]) > delta:
        delta = abs(u_update - utility[-1])

    utility = utility_update
    optimal_policy = actions
    # terminate?
    if delta < epsilon * (1 - beta) / beta:
        break

optimal_policy = [action_choice[i] for i in optimal_policy]
print(utility)
print(optimal_policy)
print('epochs = ', epochs)
