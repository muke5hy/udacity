import sys
import pandas as pd
import numpy as np
from agents.agent import DDPG
from task import Task

runtime = 3.                                     # time limit of the episode
init_pose = np.array([0., 0., 0, 0., 0., 0.])  # initial pose
init_velocities = np.array([10., 10., 10.])         # initial velocities
init_angle_velocities = np.array([0., 0., 0.])   # initial angle velocities
file_output = 'data.txt'                         # file name for saved results

num_episodes = 1000
target_pos = np.array([0., 0., 10.])

task = Task(
    init_pose=init_pose,
    init_velocities=init_velocities,
    init_angle_velocities=init_angle_velocities, 
    target_pos=target_pos,
    runtime=runtime
)

labels = ['time', 'x', 'y', 'z', 'phi', 'theta', 'psi', 'x_velocity',
          'y_velocity', 'z_velocity', 'phi_velocity', 'theta_velocity',
          'psi_velocity', 'rotor_speed1', 'rotor_speed2', 'rotor_speed3', 'rotor_speed4']

results = {x : [] for x in labels}
agent = DDPG(task) 
rewards = []
for i_episode in range(1, num_episodes+1):
    state = agent.reset_episode() # start a new episode
    score = 0;
    while True:
        rotor_speeds = agent.act(state) 
        next_state, reward, done = task.step(rotor_speeds)
        agent.step(action, reward, next_state, done)
        score +=reward
        state = next_state
        rewards.append(reward)
        
        result = [task.sim.time] + list(task.sim.pose) + list(task.sim.v) + list(task.sim.angular_v) + list(rotor_speeds)
        for i in range(len(labels)):
            results[labels[i]].append(result[i])
            
        if done:
            print("\rEpisode = {:4d}, score = {:7.3f} (best = {:7.3f})".format(
                i_episode, score, max(rewards)), end="")  # [debug]
            break
    sys.stdout.flush()