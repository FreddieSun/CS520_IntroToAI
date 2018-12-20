import math
import pdb



cost_replace = 250
beta = 0.9
epsilon = 0.001
epochs = 0
optimal_policy_list = []
action_choice = ['USE', 'REPLACE']


# init the utility for each state
utility_list = []
for i in range(10):
    utility_list.append(0)

# init the transfor probability for each state
trans_probability = []
for i in range(10):
    if i == 0:
        trans_probability.append(1)
        continue
    trans_probability.append(0.1 * i)

# init the remain probability for each state
remain_probability = []

for i in range(10):
    remain_probability.append(1 - trans_probability[i])


# init the replace probability for each state
replace_probability = []
for i in range(10):
    if i == 0:
        replace_probability.append(0)
        continue
    replace_probability.append(1)


# init the reward
reward = []
for i in range(10):
    reward.append(100 - i * 10)

reward[-1] = 0



# value iterate
while (True):
    utility_update = []
    actions = []
    delta = 0
    epochs += 1
    # update utility_list of new and used states
    for i in range(9):
        v = [(remain_probability[i] * (reward[i] + beta * utility_list[i]) + trans_probability[i] * (reward[i] + beta * utility_list[i + 1])),
             replace_probability[i] * (-cost_replace + beta * utility_list[0])]
        u_update = max(v)
        actions.append(v.index(u_update))
        # pdb.set_trace()
        utility_update.append(u_update)
        if abs(u_update - utility_list[i]) > delta:
            delta = abs(u_update - utility_list[i])
    # update utility_list of dead state
    u_update = -cost_replace + beta * utility_list[0]
    utility_update.append(u_update)
    actions.append(1)
    if abs(u_update - utility_list[-1]) > delta:
        delta = abs(u_update - utility_list[-1])

    utility_list = utility_update
    optimal_policy_list = actions
    # terminate?
    if delta < epsilon * (1 - beta) / beta:
        break

optimal_policy_list = [action_choice[i] for i in optimal_policy_list]
print(utility_list)
print(optimal_policy_list)
print('epochs = ', epochs)
