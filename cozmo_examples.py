#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 22:41:15 2017

@author: bjorland
"""

import cozmo


import time

import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id


def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Hello World").wait_for_completed()





def cozmo_program(robot: cozmo.robot.Robot):
    cube1 = robot.world.get_light_cube(LightCube1Id)  # looks like a paperclip
    cube2 = robot.world.get_light_cube(LightCube2Id)  # looks like a lamp / heart
    cube3 = robot.world.get_light_cube(LightCube3Id)  # looks like the letters 'ab' over 'T'

    if cube1 is not None:
        cube1.set_lights(cozmo.lights.red_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")

    if cube2 is not None:
        cube2.set_lights(cozmo.lights.green_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube2Id cube - check the battery.")

    if cube3 is not None:
        cube3.set_lights(cozmo.lights.blue_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube3Id cube - check the battery.")

    # Keep the lights on for 10 seconds until the program exits
    time.sleep(10)






def cozmo_program(robot: cozmo.robot.Robot):
    # Play an animation via a Trigger - see:
    # http://cozmosdk.anki.com/docs/generated/cozmo.anim.html#cozmo.anim.Triggers
    # for a list of available triggers.
    # A trigger can pick from several appropriate animations for variety.
    robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession).wait_for_completed()

    # Play an animation via its Name.
    # Warning: Future versions of the app might change these, so for future-proofing
    # we recommend using play_anim_trigger above instead.
    # See the remote_control_cozmo.py example in apps for an easy way to see
    # the available animations.
    robot.play_anim(name="id_poked_giggle").wait_for_completed()

async def dock_with_cube(robot: cozmo.robot.Robot):
    print("Cozmo is waiting until he sees a cube")

    cube = await robot.world.wait_for_observed_light_cube()

    # Cozmo will approach the cube he has seen
    # using a 180 approach angle will cause him to drive past the cube and approach from the opposite side
    # num_retries allows us to specify how many times Cozmo will retry the action in the event of it failing
    await robot.dock_with_cube(cube, approach_angle=cozmo.util.degrees(180), num_retries=2).wait_for_completed()



cozmo.run_program(cozmo_program)
