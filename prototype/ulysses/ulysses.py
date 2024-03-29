from navigation import qlearning

# Needs to come from elsewhere
map = [
    [26, 26, 26, 26, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33],
    [26, 26, 15, 15, 26, 26, 26, 26, 33, 33, 33, 33, 33, 33, 33],
    [26, 26, 16, 15, 26, 26, 26, 26, 26, 26, 26, 33, 33, 33, 33],
    [25, 25, 25, 25, 25, 25, 25, 25, 15, 26, 26, 26, 33, 33, 33],
    [15, 25, 25, 25, 25, 25, 25, 25, 25, 15, 26, 33, 33, 33, 33],
    [26, 15, 15, 15, 25, 25, 25, 25, 15, 26, 33, 33, 33, 33, 33],
    [33, 26, 15, 26, 15, 25, 25, 15, 15, 26, 33, 33, 33, 33, 33],
    [33, 33, 33, 33, 26, 15, 25, 25, 15, 26, 33, 33, 33, 33, 33],
    [33, 33, 33, 33, 33, 26, 15, 25, 25, 15, 33, 33, 33, 33, 33],
    [33, 33, 33, 33, 33, 33, 26, 15, 15, 15, 33, 33, 33, 33, 33],
    [33, 33, 33, 33, 33, 33, 26, 26, 26, 26, 33, 33, 33, 33, 33],
    [33, 33, 33, 33, 33, 33, 26, 26, 26, 26, 26, 33, 33, 33, 33],
    [33, 33, 33, 33, 33, 26, 26, 26, 26, 26, 26, 33, 33, 33, 33]
]

alpha = 0.4
gamma = 0.999
epsilon = 0.9
episodes = 10000
max_steps = 2500
n_tests = 2
timestep_reward = qlearning(alpha, gamma, epsilon, episodes, max_steps, n_tests, test = True)
print(timestep_reward)
