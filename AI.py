#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:05:27 2017

@author: bjorland
"""
import numpy as np


class Agent:
    def __init__(self, num_states=0, num_actions=0, qtable = np.ones((8, 2))):
        self.s = num_states
        self.a = num_actions
        # Initialize table with all zeros
        self.qtable = qtable
        print(qtable)
        # Set learning parameters
        self.lr = .8
        self.y = .95
        self.i = 0
        self.state = 0

    # @property
    # def qtable(self):
    #     print("Getting Q table")
    #     return self._qtable
    #
    # @qtable.setter
    # def qtable(self, value):
    #     self._qtable = value




    def get_action(self):
        # Choose an action by greedily (with noise) picking from Q table
        a = np.argmax(self.Q[self.state, :] + np.random.randn(1, self.a) * (1. / (self.i + 1)))
        return a

    def update(self, s1, a, r):
        s = self.state
        # Update Q-Table with new knowledge
        self.Q[s, a] = self.Q[s, a] + self.lr * (r + self.y * np.max(self.Q[s1, :]) - self.Q[s, a])
        self.state = s1

    # def get_qtable(self):
    #     return self.Q
