import gymnasium as gym
import importlib

# # Specify the path to the environment file
# environment_file = '/home/neil/CardML/blackjack.py'

# # Load the environment from the file
# environment_module = importlib.import_module(environment_file)

# # Get the actual environment object
# env = environment_module.Environment()

env = gym.make("Blackjack-v1", render_mode="rgb_array")

# env = gym.make("LunarLander-v2", render_mode="human")

observation, info = env.reset()

for _ in range(1000):
    # agent policy that uses the observation and info
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()
