
import gym
import gym_mupen64plus
from Rider import DeepQNetwork
import numpy as np

def run_maze():
    step = 0
    for episode in range(300):
        # initial observation
        observation = env.reset().ravel()[::2000]

        while True:
            # fresh env
            env.render()
	    
	    print observation.shape

            # Rider choose action based on observation
            action = RL.choose_action(observation)
	    action = [(int(round(item))) for sublist in action for item in sublist]	    	  
	    print action 
	    index = np.argmax(action)

 
	    if action[2]>0:
		action[2]=1
	    else:
		action[2]

            if action[3]>0:
                action[3]=1
            else:
                action[3]=0

            if action[4]>0:
                action[4]=1
            else:
                action[4]=0


            # RL take action and get next observation and reward
            observation_, reward, end_episode, done = env.step(action)
	    observation_ = observation_.ravel()[::2000]
	    print observation[0::2000].shape

	    #print observation.shape
	    print ("index->",index)
	    print ("reward->",reward)
            #print observation_.shape

            RL.store_transition(observation,index, reward, observation_)

            if (step > 200) and (step % 5 == 0):
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
    RL = DeepQNetwork(5,461,
                      learning_rate=0.01,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      replace_target_iter=200,
                      memory_size=20000,
                      # output_graph=True
                      )
    run_maze()

'''
if __name__ == "__main__":
	env = gym.make('Mario-Kart-Royal-Raceway-v0')

	obs = env.reset()
	action = [0, 0, 0, 0, 0, 0]
	end_episode = False
	prev=0  
	 
	while not end_episode:

	
		#action[random.randint(0,5)]=1
		action[0]=100
		print action
		obs, reward, end_episode, info = env.step(action)
		#print (obs.shape)
		#print (reward)
		#print (end_episode)
		#print info 
		env.render()
	    
	obs = env.reset()
	env.close()
'''
