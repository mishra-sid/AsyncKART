import gym
import gym_mupen64plus
from Rider import DeepQNetwork
import numpy as np
from PIL import Image

ACTION_MAP = [
        # ("NO_OP",         [  0,   0, 0, 0, 0]),
        ("STRAIGHT",      [  0,   0, 1, 0, 0]),
        # ("BRAKE",         [  0,   0, 0, 1, 0]),
        ("BACK_UP",       [  0, -80, 0, 1, 0]),
        ("SOFT_LEFT",     [-20,   0, 1, 0, 0]),
        ("LEFT",          [-40,   0, 1, 0, 0]),
        # ("HARD_LEFT",     [-60,   0, 1, 0, 0]),
        # ("EXTREME_LEFT",  [-80,   0, 1, 0, 0]),
        ("SOFT_RIGHT",    [ 20,   0, 1, 0, 0]),
        ("RIGHT",         [ 40,   0, 1, 0, 0]),
        # ("HARD_RIGHT",    [ 60,   0, 1, 0, 0]),
        # ("EXTREME_RIGHT", [ 80,   0, 1, 0, 0]),
    ]

car_arr = np.full((50,150,3), 10)
def get_car_args(observation):
        fin_dist = 9999999999999999
        fin_i = None
        fin_j = None
        for i in xrange(0,430,10):
            for j in xrange(95,490,10):
                dist_r = np.linalg.norm(observation[i:i+50, j : j + 150, 0]-car_arr[:,:,0])
                dist_g = np.linalg.norm(observation[i:i+50, j : j + 150, 1]-car_arr[:,:,1])
                dist_b = np.linalg.norm(observation[i:i+50, j : j + 150, 2]-car_arr[:,:,2])
                dist = np.linalg.norm([dist_r, dist_g, dist_b])
                if dist < fin_dist:
                    fin_dist = dist
                    fin_i = i
                    fin_j = j

        rew = []
        for ind in range(3):
            temp = observation[fin_i+50: fin_i + 100, fin_j:fin_j + 150, ind]
            rew.append(np.linalg.norm(temp - np.full(temp.shape, 115)))
        reward = np.linalg.norm(rew)
        return reward, fin_i, fin_j

def run_maze():
    step = 0
    for episode in range(300):
        # initial observation
        observation = env.reset().ravel()[::2000]

        while True:
            # fresh env
            env.render()

          #print observation.shape

            # Rider choose action based on observation
            action = RL.choose_action(observation)
            action = [(int(round(item))) for sublist in action for item in sublist]
            index = np.argmax(action)

            new_action = ACTION_MAP[index][1]
            print "Action taken", ACTION_MAP[index][0]
            # RL take action and get next observation and reward
            observation_, reward, end_episode, done = env.step(new_action)
            if done:
                reward -= 10000
            fdist, fi, fj = get_car_args(observation_)
            observation_ = observation_.ravel()[::2000]
            #print observation[0::2000].shape

            #print observation.shape
            
            print "Args", fdist, fi, fj
            reward += (10000 - fdist) / 100
            print ("reward->",reward)
            #print observation_.shape

            RL.store_transition(observation,index, reward, observation_)

            #if (step > 200) and (step % 5 == 0):
            RL.learn()

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break
            step += 1

    # end of game
    print('END')
    env.destroy()

if __name__ == "__main__":
    # maze game
    env = gym.make('Mario-Kart-Royal-Raceway-v0')
    RL = DeepQNetwork(len(ACTION_MAP),461,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      replace_target_iter=200,
                      memory_size=20000,
                      # output_graph=True
                      )
    run_maze()



# if __name__ == "__main__":
#         env = gym.make('Mario-Kart-Royal-Raceway-v0')

#         obs = env.reset()
#         action = [0, 0, 1, 0, 0]  # rb lite, see this https://strategywiki.org/wiki/Mario_Kart_64/Controls
#         end_episode = False
#         prev=0
#         first_time = True
#         while not end_episode:

#                 import random

#                 obs, reward, end_episode, info = env.step(action)
#                 # print (obs.shape)
#                 #print (reward)
#                 #print (end_episode)

#                 #if first_time:
#                 #        car_arr = obs[250 : 400, 250 : 400, :]
#                 #        first_time = False
#                 fdist, fi, fj = get_car_args(obs)
#                 print fdist, fi, fj
#                 #im = Image.fromarray(arr)
#                 #im.save('try.png')
#                 #print info
#                 env.render()
#                 # action = [0, 0, 0, 0, 0, 0]
#         obs = env.reset()
#         env.close()

