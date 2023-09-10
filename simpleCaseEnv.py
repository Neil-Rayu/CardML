import os
from typing import Optional

import numpy as np

import gymnasium as gym
from gymnasium import spaces
from gymnasium.error import DependencyNotInstalled
import random


class simpleEnv(gym.Env):
    def __init__(self):
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Discrete(
            2)  # use a box space for president
        self.number = random.randint(0, 1)

    def step(self, action):
        assert self.action_space.contains(action)
        if (action):
            if (self.number == 1):
                reward = 1
            else:
                reward = 0
        else:
            if (self.number == 0):
                reward = 1
            else:
                reward = 0

        info = {}

        return self.number, reward, True, info

    def render(self):
        pass

    def reset(self, seed=1):
        self.number = random.randint(0, 1)
        info = {}
        return self.number, info
