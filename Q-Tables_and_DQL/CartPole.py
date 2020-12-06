import gym
import numpy as np
import matplotlib.pyplot as plt

# Init Gym
env = gym.make("CartPole-v1")
state = env.reset()

### Constants ###

# General Settings
LEARNING_RATE = 0.5
DISCOUNT = 0.95
EPISODES = 50000
SHOW_EVERY = 5000

# Exploration
EPSILON = 0.1
START_EPSILON_DECAYING = 1
END_EPSILON_DICAYING = EPISODES // 2
EPSILON_DECAY_VALUE= EPSILON / (END_EPSILON_DICAYING - START_EPSILON_DECAYING)


# Window Size for the Q-Table and init Q-Table
DISCRETE_OS_SIZE = [40] * len(env.observation_space.high)
DISCRETE_OS_WIN_SIZE = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE
q_table = np.random.uniform(low=0, high=2, size=(DISCRETE_OS_SIZE + [env.action_space.n]))

ep_rewards = []
aggr_ep_rewards = {"ep": [], "avg": [], "min": [], "max": []}

# Helper Function to convert the continuous state into our discrete state
def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low) / DISCRETE_OS_WIN_SIZE
    return tuple(discrete_state.astype(np.int))

# Training
for episode in range(EPISODES):
    episode_reward = 0
    discrete_state = get_discrete_state(env.reset())
    done = False
    while not done:

        # Decide if the action in the Q-Table is taken or a random action
        if np.random.random() > EPSILON:
            action = np.argmax(q_table[discrete_state])
        else:
            action = np.random.randint(0, env.action_space.n)

        new_state, reward, done, _ = env.step(action)
        episode_reward += reward
        new_discrete_state = get_discrete_state(new_state)

        # Show us that you are still alive every now and then
        if not episode % SHOW_EVERY:
            print("Episode: ", episode)

        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
            current_q = q_table[discrete_state + (action, )]

            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            q_table[discrete_state + (action, )] = new_q

        discrete_state = new_discrete_state

    # Reduce EPSILON to take less random actions the more we have trained
    if END_EPSILON_DICAYING >= episode >= START_EPSILON_DECAYING:
        EPSILON -= EPSILON_DECAY_VALUE

    # Close the Environment if it has been rendered
    if not episode % SHOW_EVERY and episode != 0:
        env.close()

        average_reward = sum(ep_rewards[-SHOW_EVERY:])/len(ep_rewards[-SHOW_EVERY:])
        aggr_ep_rewards["ep"].append(episode)
        aggr_ep_rewards["avg"].append(average_reward)
        aggr_ep_rewards["min"].append(min(ep_rewards[-SHOW_EVERY:]))
        aggr_ep_rewards["max"].append(max(ep_rewards[-SHOW_EVERY:]))

    ep_rewards.append(episode_reward)

plt.plot(aggr_ep_rewards["ep"], aggr_ep_rewards["avg"], label="avg")
plt.plot(aggr_ep_rewards["ep"], aggr_ep_rewards["min"], label="min")
plt.plot(aggr_ep_rewards["ep"], aggr_ep_rewards["max"], label="max")
plt.legend(loc=4)
plt.show()

