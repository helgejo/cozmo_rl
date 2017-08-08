#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:05:27 2017

@author: bjorland
"""
import numpy as np

class agent():
    
    def __init__(self, num_states, num_actions):
        self.s = num_states
        self.a = num_actions
        #Initialize table with all zeros
        self.Q = np.zeros([self.s,self.a])
        # Set learning parameters
        self.lr = .8
        self.y = .95
        self.i = 0
        self.state = 0
        
    def get_action(self):
         #Choose an action by greedily (with noise) picking from Q table
         a = np.argmax(self.Q[self.state,:] + np.random.randn(1,self.a)*(1./(self.i+1)))
         return a
         
         
    def update(self, s1, a, r):
        s = self.state
        #Update Q-Table with new knowledge
        self.Q[s,a] = self.Q[s,a] + self.lr*(r + self.y*np.max(self.Q[s1,:]) - self.Q[s,a])
        self.state = s1

    def get_qtable(self):
        return self.Q
