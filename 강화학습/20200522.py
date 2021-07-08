#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import gym
from gym.envs.registration import register
import msvcrt


# In[2]:

"""
env = gym.make("FrozenLake-v0")
observation = env.reset()

for _ in range(1000):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
"""

# In[4]:


class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

            inkey = _Getch()


# In[5]:


# MACROS
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3


# In[6]:


# Key mapping
arrow_keys = {
    '\x1b[A': UP,
    '\x1b[B': DOWN,
    '\x1b[C': RIGHT,
    '\x1b[D': LEFT
}


# In[7]:


def getkey():
    return msvcrt.getch()


# In[8]:


register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4', 'is_slippery':False}
)


# In[9]:


env = gym.make('FrozenLake-v3')
env.render()


# In[ ]:


while True:
    key = getkey()
    if key not in arrow_keys.keys():
        print("Game aborted!")
        break
        
    action = arrow_keys[key]
    state, reward, done, info = env.step(action)
    env.render()
    print("State: ", state, "Action: ", action, "Reward:", reward, "Info: ", info)
    
    if done:
        print("Finished with reward", reward)
        break


# In[ ]:





# In[ ]:




