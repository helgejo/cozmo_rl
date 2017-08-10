#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:05:56 2017

@author: bjorland
"""

import cozmo
import time
from Rob.objects import LightCube1Id, LightCube2Id, LightCube3Id


class Rob(object):
    def __init__(self):
        self.cube = None
        self.state = 0
    
    def print_text(robot: cozmo.robot.Robot):
        robot.say_text("Hello World").wait_for_completed()

    async def dock_with_cube(robot: cozmo.robot.Robot):
        print("Cozmo is waiting until he sees a cube")
    
        cube = await robot.world.wait_for_observed_light_cube()
    
        # Cozmo will approach the cube he has seen
        # using a 180 approach angle will cause him to drive past the cube and approach from the opposite side
        # num_retries allows us to specify how many times Cozmo will retry the action in the event of it failing
        await robot.dock_with_cube(cube, approach_angle=cozmo.util.degrees(180), num_retries=2).wait_for_completed()
        return cube

    def sad_animation(robot: cozmo.robot.Robot):
        # Play an animation via a Trigger - see:
        # http://cozmosdk.anki.com/docs/generated/cozmo.anim.html#cozmo.anim.Triggers
        # for a list of available triggers.
        # A trigger can pick from several appropriate animations for variety.
        robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession).wait_for_completed()
        
    def happy_animation(robot: cozmo.robot.Robot):
        # Play an animation via a Trigger - see:
        # http://cozmosdk.anki.com/docs/generated/cozmo.anim.html#cozmo.anim.Triggers
        # for a list of available triggers.
        # A trigger can pick from several appropriate animations for variety.
        robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession).wait_for_completed()
    
    def numbers_to_strings(argument):
 
        switcher = {
            0: "cozmo.lights.green_light",
            1: "cozmo.lights.red_light",
            2: "cozmo.lights.blue_light",
            3: "cozmo.lights.white_light",
            4: "cozmo.lights.Color(rgb=(255,0,255))"
            
        }
        return switcher.get(argument, "nothing")

    def cubelight(self, robot: cozmo.robot.Robot):
        light =  self.numbers_to_strings(self.state)
        if self.cube is not None:
            self.cube.set_lights(light)
        else:
            Rob.logger.warning("Cozmo is not connected to a cube - check the battery.")
    
    def light_off(self, robot: cozmo.robot.Robot):
        self.cube.set_lights(Rob.lights.off_light)
    
        # Keep the lights on for 10 seconds until the program exits
        #time.sleep(10)
        
    def pounce_cube(robot: cozmo.robot.Robot):
        robot.play_anim_trigger(cozmo.anim.Triggers.CubePouncePounceNormal).wait_for_completed()
        
        
    def set_cubelight(self, state):
        self.state = state
        cozmo.run_program(self.cubelight)
        
    def do_action(self,action):
        if action == 1:
            cozmo.run_program(self.pounce_cube)
        
    def restart_sad(self):
        cozmo.run_program(self.sad_animation)
    def restart_happy(self):
        cozmo.run_program(self.happy_animation)
    def find_cube(self):
        self.cube = cozmo.run_program(self.dock_with_cube)
    def reset_cube(self):
        cozmo.run_program(self.light_off)