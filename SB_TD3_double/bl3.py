import gym
import numpy as np
from Multi_level_env import multi_level_env

def main():
    episode_rewards_0 = []
    Step_rewards0 = []
    env_3=multi_level_env(3,8002)
    env_3=make_vec_env(lambda:env_3,n_envs=1)
    env_3 =VecMonitor(env_3,log_dir_3)
    for i in range(1):
        reward_sum0 = 0
        obs = env.reset()
        for j in range(episode_steps):
            action=[0,0,0,0,0]
            print("Baseline: Step : {} | Episode: {}".format(j, i))
            obs, rewards, dones, info = env.step([action])
            reward_sum0 += rewards
            Step_rewards0.append(rewards)
    Results=[]
    with open("agent3_BL.csv",'w',newline='') as blcsv:
        writer=csv.writer(blcsv, delimiter=';', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        Results.clear()
        Results=Results+Step_rewards0
        writer.writerow(Results)
    
if __name__ == '__main__':
	main()