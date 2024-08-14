import os
import time
import gym
import numpy as np
import matplotlib.pyplot as plt
from stable_baselines3 import TD3
from stable_baselines3.td3.policies import MlpPolicy
from stable_baselines3.common import results_plotter
from VecMonitor import VecMonitor
from stable_baselines3.common.results_plotter import load_results, ts2xy
from stable_baselines3.common.noise import NormalActionNoise
from stable_baselines3.common.vec_env import DummyVecEnv, VecNormalize
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.env_util import make_vec_env
from Multi_level_env import multi_level_env
import csv



class SaveOnBestTrainingRewardCallback(BaseCallback):
    """
    Callback for saving a model (the check is done every ``check_freq`` steps)
    based on the training reward (in practice, we recommend using ``EvalCallback``).

    :param check_freq: (int)
    :param log_dir: (str) Path to the folder where the model will be saved.
      It must contains the file created by the ``Monitor`` wrapper.
    :param verbose: (int)
    """
    def __init__(self, check_freq: int, log_dir: str, verbose=1):
        super(SaveOnBestTrainingRewardCallback, self).__init__(verbose)
        self.check_freq = check_freq
        self.log_dir = log_dir
        self.save_path = os.path.join(log_dir, 'best_model')
        self.best_mean_reward = -np.inf

    def _init_callback(self) -> None:
        # Create folder if needed
        if self.save_path is not None:
            os.makedirs(self.save_path, exist_ok=True)

    def _on_step(self) -> bool:
        print("Steps: {}".format(self.num_timesteps))

        if self.n_calls % self.check_freq == 0:

          # Retrieve training reward
          x, y = ts2xy(load_results(self.log_dir), 'timesteps')
          if len(x) > 0:
              # Mean training reward over the last 100 episodes
              mean_reward = np.mean(y[-100:])
              if self.verbose > 0:
                print("Num timesteps: {}".format(self.num_timesteps))
                print("Best mean reward: {:.2f} - Last mean reward per episode: {:.2f}".format(self.best_mean_reward, mean_reward))

              # New best model, you could save the agent here
              if mean_reward > self.best_mean_reward:
                  self.best_mean_reward = mean_reward
                  # Example for saving best model
                  if self.verbose > 0:
                    print("Saving new best model to {}".format(self.save_path))
                  self.model.save(self.save_path)
        return True
def main():
  
  
  #Custom Network Archeticure
  policy_kwargs=dict(net_arch=[64,64])
  #Making Directories
  log_dir_1 = "tmp_1{}/".format(int(time.time())-100)
  os.makedirs(log_dir_1, exist_ok=True)
  
  #Double environment
  env_1=multi_level_env(4,8005)

  env_1=make_vec_env(lambda: env_1, n_envs=1)

  env_1 =VecMonitor(env_1, log_dir_1)
  action_1= env_1.action_space.shape[-1]

  noise_action_1= NormalActionNoise(mean=np.zeros(action_1), sigma=0.1 * np.ones(action_1))

  model_1=TD3(MlpPolicy, env_1, action_noise=noise_action_1, verbose=1, tensorboard_log="./TD3_ped_veh_tensorboard_1/",learning_starts=10000,policy_kwargs=policy_kwargs)
  #actions

  callback_1 = SaveOnBestTrainingRewardCallback(check_freq=250, log_dir=log_dir_1)
  time_steps = 100002
  model_1.learn(total_timesteps=int(time_steps), callback=callback_1)
  model_1.save("TD3_ped_veh_r1_agent_1")

        
if __name__ == '__main__':
	main()
