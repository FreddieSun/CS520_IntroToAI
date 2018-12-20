

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


while (True):
    new_utility = []
    actions = []
    delta = 0
    epochs += 1

    for i in range(9):
        temp_value = [(remain_probability[i] * (reward[i] + beta * utility_list[i]) +
                       trans_probability[i] * (reward[i] + beta * utility_list[i + 1])),
                      replace_probability[i] * (-cost_replace + beta * utility_list[0])]
        utility_updated = max(temp_value)
        actions.append(temp_value.index(utility_updated))
        new_utility.append(utility_updated)
        if abs(utility_updated - utility_list[i]) > delta:
            delta = abs(utility_updated - utility_list[i])

    utility_updated = -cost_replace + beta * utility_list[0]
    new_utility.append(utility_updated)
    actions.append(1)
    if abs(utility_updated - utility_list[-1]) > delta:
        delta = abs(utility_updated - utility_list[-1])

    utility_list = new_utility
    optimal_policy_list = actions

    if delta < epsilon * (1 - beta) / beta:
        break

optimal_policy_list = [action_choice[i] for i in optimal_policy_list]
print(utility_list)
print(optimal_policy_list)
print('epochs = ', epochs)
