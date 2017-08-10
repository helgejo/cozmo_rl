#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:05:11 2017

@author: bjorland
"""
from AI import Agent
import numpy as np
#import Rob
# import Cozmo
#import Simulator

#
# def cozmo_app():
#     states = 8
#     actions = 2
#     simulator = Simulator.Simulator()
#     cozmo = Rob.Rob()
#     agent = AI.Agent(states, actions)
#     action = -1
#     # Get the first state (color) that appears
#     state = simulator.get_state(action)
#     prev_state = 0
#     reward = 0
#     episode = 0
#     iterations = 10
#     i = 0
#
#     while i < iterations:
#         # The agent gets the necessary state info from the simulator
#         action = agent.get_action(state)
#         cozmo.set_cubelight(state)
#         cozmo.do_action(action)
#         reward = reward + simulator.get_reward(action)
#         agent.update(state, action, reward)
#         state = simulator.get_new_state(action)
#
#         # if terminal state then restart cozmo and add on episode
#         if state == -1:
#             cozmo.restart_sad()
#             episode += 1
#             reward = 0
#         elif state == -2:
#             cozmo.restart_happy()
#             episode += 1
#             reward = 0
#
#         print("Episode reward: " + reward)
#         i += 1

class Dog:
    def __init__(self, qtable = np.ones((8, 2))):
        self.qtable = qtable
        print(self.qtable)



def debug():
    # test agent
    states = 8
    actions = 2
    print("creating AI")
    agent = Agent(states, actions)
    print(agent)
    print(agent.qtable)
    #print(agent.qtable())
    #print(agent.__getattribute__("qtable"))
    print("creating dog")
    dog = Dog()

    #a = agent.get_action()
    #print(type(a))
    #print(a)
    #print(agent.get_qtable())

    #print(agent.qtable())
    #print(get_dict_attr(_qtable)
    #test = np.ones((8, 2))
    #print(test)
    #print(test[7, :])
    #rando = np.random.randn(1, 2)
    #print(rando)
    #noise = rando * (1./(10+1))
    #print(noise)
    #test2 = test + noise
    #print("test2")
    #print(test2)
    #print("argmax")
    #print(np.argmax(test2))
# Running the whole thing
if __name__ == '__main__':
    debug()
