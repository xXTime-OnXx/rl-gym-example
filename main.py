import gymnasium as gym
import time

env = gym.make("CartPole-v1", render_mode='human')
observation = env.reset()

steps = 0
while True:
    env.render()
    action = 0
    if steps % 2 == 0:
        action = 1

    obs, reward, terminated, truncated, info = env.step(action)

    steps += 1

    if terminated:
        print('game over!!')
        env.reset()
        break
        
env.close()