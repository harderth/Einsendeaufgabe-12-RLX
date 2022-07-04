import gym
import random

# Documentation: https://www.gymlibrary.ml/environments/classic_control/cart_pole/?highlight=cartpole

env = gym.make('CartPole-v1')
print('Observation', env.observation_space)
print('Action', env.action_space)

class Agent():
    def __init__(self, env):
        self.action_size = env.action_space.n
        print("Action size:", self.action_size)

    def get_random_action(self):
        action = random.choice(range(self.action_size))
        return action


agent = Agent(env)
env.reset()

for _ in range(200):
    # action = env.action_space.sample()
    action = agent.get_random_action()
    env.step(action)
    env.render()