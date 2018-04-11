
import gym
import gym_mupen64plus


if __name__ == "__main__":
    env = gym.make('Mario-Kart-Royal-Raceway-v0')

    obs = env.reset()

    end_episode = False
    while not end_episode:
        action = [63, 3, 3, 1, 1, 0]
        obs, reward, end_episode, info = env.step(action)
        print obs
        print reward
        print end_episode
        print info 
        env.render()
    
    obs = env.reset()
    env.close()
