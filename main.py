#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:05:11 2017

@author: bjorland
"""
import agent, cozmo, simulator

# Running the whole thing
if __name__ == '__main__':
    simulator = simulator()
    cozmo = cozmo()
    agent = agent()  
    action = -1
    #Get the first state (color) that appears
    state = simulator.get_state(action)
    prev_state = 0
    reward = 0
    episode = 0
    iterations = 10
    i = 0
    
    while i < iterations:
        #The agent gets the necessary state info from the simulator
        action = agent.get_action(state)
        cozmo.set_cubelight(state)
        cozmo.do_action(action)
        reward = reward + simulator.get_reward(action)
        agent.update(state, action, reward)
        state = simulator.get_new_state(action)
        
        # if terminal state then restart cozmo and add on episode
        if state == -1:
            cozmo.restart_sad()
            episode += 1
            reward = 0
        elif state == -2:
            cozmo.restart_happy()
            episode += 1
            reward = 0
        
        print("Episode reward: " + reward)
        i += 1
        
        
    