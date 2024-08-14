import gym
import numpy as np
import gym
from ns3gym import ns3env
from gym import spaces
import os
import csv
import json
reward1=[]
reward2=[]
reward3=[]
global reward3_t
global reward4_t
reward3_t=[]
reward4_t=[]
class multi_level_env(gym.Env):
    def __init__(self,Agent_ID,PRT):#Agent_ID should Match the one in the Simulator 
        super(multi_level_env, self).__init__()
        port=PRT
        simTime= 2
        stepTime=0.2
        startSim=0
        seed=3
        simArgs = {"--duration": simTime,}
        debug=True
        self.ID=Agent_ID
        max_env_steps = 250
        self.env = ns3env.Ns3Env(port=port, stepTime=stepTime, startSim=startSim, simSeed=seed, simArgs=simArgs, debug=debug)
        self.env._max_episode_steps = max_env_steps
        self.Cell_num=6
        self.max_throu=5
        self.Users=8
        self.state_dim=4
        self.action_dim =  self.env.action_space.shape[0]
        self.action_bound =  self.env.action_space.high
        self.action_space = spaces.Box(low=-1, high=1,
                                        shape=(self.action_dim,), dtype=np.float32)
        self.observation_space = spaces.Box(low=0, high=self.Users,
                                        shape=(self.state_dim,), dtype=np.float32)



    def reset(self):
        if self.ID==0:
            state=self.env.reset()
            return self.get_state(state)
        else:
            x = [0 for i in range(self.action_dim)]
            state, reward, done, info = self.env.step(x)
            return self.get_state(state)
    def step(self,action):
        action=action*self.action_bound
        next_state, reward, done, info = self.env.step(action)
        while (next_state == None):
            next_state, reward, done, info = self.env.step(action)
        self.reportReward(reward)
        self.action_print(action,reward)
        return np.array(self.get_state(next_state)),reward, done,info

    def group_state(self,state):
        
        state1 = np.reshape(state['rbUtil'], [self.Cell_num, 1])#Reshape the matrix
        state2 = np.reshape(state['dlThroughput'],[self.Cell_num,1])
        state2_norm=state2/30
        state3 = np.reshape(state['UserCount'], [self.Cell_num, 1])#Reshape the matrix
        state3_norm=state3/40
        MCS_t=np.array(state['MCSPen'])
        state4=np.sum(MCS_t[:,:10], axis=1)
        state4=np.reshape(state4,[self.Cell_num,1])
        state1_1=np.sum(state1[self.cluster1])/3
        state1_2=np.sum(state1[self.cluster2])/3
        state2_1=np.sum(state2_norm[self.cluster1])/3
        state2_2=np.sum(state2_norm[self.cluster2])/3
        state3_1=np.sum(state3_norm[self.cluster1])/3
        state3_2=np.sum(state3_norm[self.cluster2])/3
        state4_1=np.sum(state4[self.cluster1])/3
        state4_2=np.sum(state4[self.cluster2])/3
       	state5=np.reshape(state['CIO'],[11,1])
       	state5_norm=state5/6
       	state5_cluster_action=np.concatenate((state5_norm[0],state5_norm[2],state5_norm[3],state5_norm[5],state5_norm[9],state5_norm[10]))
        reward_shaped=np.reshape(state['rewards'], [5, 1])
        reward3_t.append(reward_shaped[0][0])
        reward4_t.append(reward_shaped[4][0])
        state=np.concatenate((state1_1,state1_2,state2_1,state2_2,state3_1,state3_2,state4_1,state4_2,state1[1],state2_norm[1],state3_norm[1],state4[1]),axis=None)
        state=np.reshape(state,[18,])
        return np.array(state)
    def reportReward(self,reward):
        global reward1
        global reward2
        global reward3
        Result_row=[]
        rwd=[]
        if (len(rwd) % 1000== 0) and (len(rwd)!=0):
            with open('Rewards_' + 'Thr_opt' + str(self.ID)+'.csv','w', newline='') as rewardcsv:
                results_writer = csv.writer(rewardcsv, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                Result_row.clear()
                Result_row=Result_row+rwd
                results_writer.writerow(Result_row)
            rewardcsv.close()

        if len(reward3_t)%1000==0:
            with open('Report_'+str(self.ID)+'.csv','w',newline='') as reportcsv:
                results_writer=csv.writer(reportcsv, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                Result_row.clear()
                Result_row=Result_row+reward3_t
                results_writer.writerow(Result_row)
                Result_row.clear()
                Result_row=Result_row+reward4_t
                results_writer.writerow(Result_row)
    def get_state(self,next_state):
        state1 = np.reshape(next_state['rbUtil'], [self.Cell_num, 1])[self.ID]#Reshape the matrix (do we need that?)
        state2 = np.reshape(next_state['dlThroughput'],[self.Cell_num,1])[self.ID]
        state2_norm=state2/self.max_throu
        state3 = np.reshape(next_state['UserCount'], [self.Cell_num, 1])[self.ID]#Reshape the matrix (do we need that?)
        state3_norm=state3/self.Users
        MCS_t=np.array(next_state['MCSPen'])
        state4=np.sum(MCS_t[:,:10], axis=1)
        state4=np.reshape(state4,[self.Cell_num,1])[self.ID]
        #state5=np.reshape(next_state['CIO'],[11,1]) #GET CIO INFO
        #state5_norm=state5/6
        #state5_intercluster_action=np.concatenate((state5_norm[1],state5_norm[4],state5_norm[6],state5_norm[7],state5_norm[8]))
        reward_shaped=np.reshape(next_state['rewards'], [5, 1])
        next_state  = np.concatenate((state1,state2_norm,state3_norm,state4),axis=None)  
        next_state = np.reshape(next_state, [self.state_dim,])
        reward3_t.append(reward_shaped[0][0])
        reward4_t.append(reward_shaped[4][0])
        
        return next_state
    def action_print(self,action,reward):
        print("action:{}".format((action)))
        print("Reward:{}".format((reward)))
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
