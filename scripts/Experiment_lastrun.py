#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on March 10, 2017, at 15:37
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script -----------------------------------------------------------
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Experiment'  # from the Builder filename that created this script
expInfo = {'Participant':'', 'Proctor':'', 'session':'001', 'Time (##:##)':''}

expInfo = {'Participant':'', 'Proctor':'', 'session':'001', 'Time (##:##)':''}

dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel


expInfo['date'] = data.getDateStr()  # add a simple timestamp DATE--------
expInfo['expName'] = expName


# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\Arya\\Documents\\Research\\Stanford Psychophysiology Lab\\Experiment.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation






# ----------------------------------- START OF EXPERIMENT -----------------------------------



# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Welcome',
    font='Arial',
    pos=(0, 0), height=0.6, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Operator_Instructions"
Operator_InstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Simulation being prepared by Proctor. ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Block_1"
Block_1Clock = core.Clock()
neutral_view_Plus = visual.TextStim(win=win, name='neutral_view_Plus',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
neutral_view_VIEW = visual.TextStim(win=win, name='neutral_view_VIEW',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
neutral_view_Blank = visual.TextStim(win=win, name='neutral_view_Blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
neutral_view_Photo = visual.ImageStim(
    win=win, name='neutral_view_Photo',
    image='Neutral.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
neutral_view_Blank2 = visual.TextStim(win=win, name='neutral_view_Blank2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
neutral_view_Response = visual.TextStim(win=win, name='neutral_view_Response',
    text='How do you Feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
neutral_view_Plus2 = visual.TextStim(win=win, name='neutral_view_Plus2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
negative_view_Plus = visual.TextStim(win=win, name='negative_view_Plus',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
negative_view_VIEW = visual.TextStim(win=win, name='negative_view_VIEW',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.6, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
negative_view_Blank = visual.TextStim(win=win, name='negative_view_Blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
negative_view_image = visual.ImageStim(
    win=win, name='negative_view_image',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
negative_view_Blank2 = visual.TextStim(win=win, name='negative_view_Blank2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);
negative_view_Response = visual.TextStim(win=win, name='negative_view_Response',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-13.0);
negative_view_Plus2 = visual.TextStim(win=win, name='negative_view_Plus2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-15.0);
negative_distract_plus = visual.TextStim(win=win, name='negative_distract_plus',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-16.0);
negative_distract_DISTRACT = visual.TextStim(win=win, name='negative_distract_DISTRACT',
    text='DISTRACT',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-17.0);
negative_distract_Blank = visual.TextStim(win=win, name='negative_distract_Blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-18.0);
negative_distract_Photo = visual.ImageStim(
    win=win, name='negative_distract_Photo',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
negative_distract_Blank2 = visual.TextStim(win=win, name='negative_distract_Blank2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-20.0);
negative_distract_Response = visual.TextStim(win=win, name='negative_distract_Response',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-21.0);
negative_distract_Plus2 = visual.TextStim(win=win, name='negative_distract_Plus2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-23.0);
negative_reappraise_Plus = visual.TextStim(win=win, name='negative_reappraise_Plus',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-24.0);
negative_reappraise_REAPPRAISE = visual.TextStim(win=win, name='negative_reappraise_REAPPRAISE',
    text='REAPPRAISE',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-25.0);
negative_reappraise_Blank = visual.TextStim(win=win, name='negative_reappraise_Blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-26.0);
negative_reappraise_Photo = visual.ImageStim(
    win=win, name='negative_reappraise_Photo',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-27.0)
negative_reappraise_Blank2 = visual.TextStim(win=win, name='negative_reappraise_Blank2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-28.0);
negative_reappraise_Response = visual.TextStim(win=win, name='negative_reappraise_Response',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-29.0);
negative_reappraise_Plus2 = visual.TextStim(win=win, name='negative_reappraise_Plus2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-31.0);

# Initialize components for Routine "Block_2"
Block_2Clock = core.Clock()
neutral_view_Plus_2 = visual.TextStim(win=win, name='neutral_view_Plus_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
neutral_view_VIEW_2 = visual.TextStim(win=win, name='neutral_view_VIEW_2',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
neutral_view_Blank_2 = visual.TextStim(win=win, name='neutral_view_Blank_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
neutral_view_Photo_2 = visual.ImageStim(
    win=win, name='neutral_view_Photo_2',
    image='Neutral.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
neutral_view_Blank2_2 = visual.TextStim(win=win, name='neutral_view_Blank2_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
neutral_view_Response_2 = visual.TextStim(win=win, name='neutral_view_Response_2',
    text='How do you Feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
neutral_view_Plus2_2 = visual.TextStim(win=win, name='neutral_view_Plus2_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
negative_view_Plus_2 = visual.TextStim(win=win, name='negative_view_Plus_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
negative_view_VIEW_2 = visual.TextStim(win=win, name='negative_view_VIEW_2',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.6, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
negative_view_Blank_2 = visual.TextStim(win=win, name='negative_view_Blank_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
negative_view_image_2 = visual.ImageStim(
    win=win, name='negative_view_image_2',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
negative_view_Blank2_2 = visual.TextStim(win=win, name='negative_view_Blank2_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);
negative_view_Response_2 = visual.TextStim(win=win, name='negative_view_Response_2',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-13.0);
negative_view_Plus2_2 = visual.TextStim(win=win, name='negative_view_Plus2_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-15.0);
negative_distract_plus_2 = visual.TextStim(win=win, name='negative_distract_plus_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-16.0);
negative_distract_DISTRACT_2 = visual.TextStim(win=win, name='negative_distract_DISTRACT_2',
    text='DISTRACT',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-17.0);
negative_distract_Blank_2 = visual.TextStim(win=win, name='negative_distract_Blank_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-18.0);
negative_distract_Photo_2 = visual.ImageStim(
    win=win, name='negative_distract_Photo_2',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
negative_distract_Blank2_2 = visual.TextStim(win=win, name='negative_distract_Blank2_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-20.0);
negative_distract_Response_2 = visual.TextStim(win=win, name='negative_distract_Response_2',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-21.0);
negative_distract_Plus2_2 = visual.TextStim(win=win, name='negative_distract_Plus2_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-23.0);
negative_reappraise_Plus_2 = visual.TextStim(win=win, name='negative_reappraise_Plus_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-24.0);
negative_reappraise_REAPPRAISE_2 = visual.TextStim(win=win, name='negative_reappraise_REAPPRAISE_2',
    text='REAPPRAISE',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-25.0);
negative_reappraise_Blank_2 = visual.TextStim(win=win, name='negative_reappraise_Blank_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-26.0);
negative_reappraise_Photo_2 = visual.ImageStim(
    win=win, name='negative_reappraise_Photo_2',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-27.0)
negative_reappraise_Blank2_2 = visual.TextStim(win=win, name='negative_reappraise_Blank2_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-28.0);
negative_reappraise_Response_2 = visual.TextStim(win=win, name='negative_reappraise_Response_2',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-29.0);
negative_reappraise_Plus2_2 = visual.TextStim(win=win, name='negative_reappraise_Plus2_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-31.0);

# Initialize components for Routine "Block_3"
Block_3Clock = core.Clock()
neutral_view_Plus_3 = visual.TextStim(win=win, name='neutral_view_Plus_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
neutral_view_VIEW_3 = visual.TextStim(win=win, name='neutral_view_VIEW_3',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
neutral_view_Blank_3 = visual.TextStim(win=win, name='neutral_view_Blank_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
neutral_view_Photo_3 = visual.ImageStim(
    win=win, name='neutral_view_Photo_3',
    image='Neutral.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
neutral_view_Blank2_3 = visual.TextStim(win=win, name='neutral_view_Blank2_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
neutral_view_Response_3 = visual.TextStim(win=win, name='neutral_view_Response_3',
    text='How do you Feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
neutral_view_Plus2_3 = visual.TextStim(win=win, name='neutral_view_Plus2_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
negative_view_Plus_3 = visual.TextStim(win=win, name='negative_view_Plus_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
negative_view_VIEW_3 = visual.TextStim(win=win, name='negative_view_VIEW_3',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.6, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
negative_view_Blank_3 = visual.TextStim(win=win, name='negative_view_Blank_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
negative_view_image_3 = visual.ImageStim(
    win=win, name='negative_view_image_3',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
negative_view_Blank2_3 = visual.TextStim(win=win, name='negative_view_Blank2_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);
negative_view_Response_3 = visual.TextStim(win=win, name='negative_view_Response_3',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-13.0);
negative_view_Plus2_3 = visual.TextStim(win=win, name='negative_view_Plus2_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-15.0);
negative_distract_plus_3 = visual.TextStim(win=win, name='negative_distract_plus_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-16.0);
negative_distract_DISTRACT_3 = visual.TextStim(win=win, name='negative_distract_DISTRACT_3',
    text='DISTRACT',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-17.0);
negative_distract_Blank_3 = visual.TextStim(win=win, name='negative_distract_Blank_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-18.0);
negative_distract_Photo_3 = visual.ImageStim(
    win=win, name='negative_distract_Photo_3',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
negative_distract_Blank2_3 = visual.TextStim(win=win, name='negative_distract_Blank2_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-20.0);
negative_distract_Response_3 = visual.TextStim(win=win, name='negative_distract_Response_3',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-21.0);
negative_distract_Plus2_3 = visual.TextStim(win=win, name='negative_distract_Plus2_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-23.0);
negative_reappraise_Plus_3 = visual.TextStim(win=win, name='negative_reappraise_Plus_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-24.0);
negative_reappraise_REAPPRAISE_3 = visual.TextStim(win=win, name='negative_reappraise_REAPPRAISE_3',
    text='REAPPRAISE',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-25.0);
negative_reappraise_Blank_3 = visual.TextStim(win=win, name='negative_reappraise_Blank_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-26.0);
negative_reappraise_Photo_3 = visual.ImageStim(
    win=win, name='negative_reappraise_Photo_3',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-27.0)
negative_reappraise_Blank2_3 = visual.TextStim(win=win, name='negative_reappraise_Blank2_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-28.0);
negative_reappraise_Response_3 = visual.TextStim(win=win, name='negative_reappraise_Response_3',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-29.0);
negative_reappraise_Plus2_3 = visual.TextStim(win=win, name='negative_reappraise_Plus2_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-31.0);

# Initialize components for Routine "Block_4"
Block_4Clock = core.Clock()
neutral_view_Plus_4 = visual.TextStim(win=win, name='neutral_view_Plus_4',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
neutral_view_VIEW_4 = visual.TextStim(win=win, name='neutral_view_VIEW_4',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
neutral_view_Blank_4 = visual.TextStim(win=win, name='neutral_view_Blank_4',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
neutral_view_Photo_4 = visual.ImageStim(
    win=win, name='neutral_view_Photo_4',
    image='Neutral.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
neutral_view_Blank2_4 = visual.TextStim(win=win, name='neutral_view_Blank2_4',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
neutral_view_Response_4 = visual.TextStim(win=win, name='neutral_view_Response_4',
    text='How do you Feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
neutral_view_Plus2_4 = visual.TextStim(win=win, name='neutral_view_Plus2_4',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
negative_view_Plus_4 = visual.TextStim(win=win, name='negative_view_Plus_4',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
negative_view_VIEW_4 = visual.TextStim(win=win, name='negative_view_VIEW_4',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.6, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
negative_view_Blank_4 = visual.TextStim(win=win, name='negative_view_Blank_4',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
negative_view_image_4 = visual.ImageStim(
    win=win, name='negative_view_image_4',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
negative_view_Blank2_4 = visual.TextStim(win=win, name='negative_view_Blank2_4',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);
negative_view_Response_4 = visual.TextStim(win=win, name='negative_view_Response_4',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-13.0);
negative_view_Plus2_4 = visual.TextStim(win=win, name='negative_view_Plus2_4',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-15.0);
negative_distract_plus_4 = visual.TextStim(win=win, name='negative_distract_plus_4',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-16.0);
negative_distract_DISTRACT_4 = visual.TextStim(win=win, name='negative_distract_DISTRACT_4',
    text='DISTRACT',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-17.0);
negative_distract_Blank_4 = visual.TextStim(win=win, name='negative_distract_Blank_4',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-18.0);
negative_distract_Photo_4 = visual.ImageStim(
    win=win, name='negative_distract_Photo_4',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
negative_distract_Blank2_4 = visual.TextStim(win=win, name='negative_distract_Blank2_4',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-20.0);
negative_distract_Response_4 = visual.TextStim(win=win, name='negative_distract_Response_4',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-21.0);
negative_distract_Plus2_4 = visual.TextStim(win=win, name='negative_distract_Plus2_4',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-23.0);
negative_reappraise_Plus_4 = visual.TextStim(win=win, name='negative_reappraise_Plus_4',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-24.0);
negative_reappraise_REAPPRAISE_4 = visual.TextStim(win=win, name='negative_reappraise_REAPPRAISE_4',
    text='REAPPRAISE',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-25.0);
negative_reappraise_Blank_4 = visual.TextStim(win=win, name='negative_reappraise_Blank_4',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-26.0);
negative_reappraise_Photo_4 = visual.ImageStim(
    win=win, name='negative_reappraise_Photo_4',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-27.0)
negative_reappraise_Blank2_4 = visual.TextStim(win=win, name='negative_reappraise_Blank2_4',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-28.0);
negative_reappraise_Response_4 = visual.TextStim(win=win, name='negative_reappraise_Response_4',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-29.0);
negative_reappraise_Plus2_4 = visual.TextStim(win=win, name='negative_reappraise_Plus2_4',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-31.0);

# Initialize components for Routine "Block_5"
Block_5Clock = core.Clock()
neutral_view_Plus_5 = visual.TextStim(win=win, name='neutral_view_Plus_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
neutral_view_VIEW_5 = visual.TextStim(win=win, name='neutral_view_VIEW_5',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
neutral_view_Blank_5 = visual.TextStim(win=win, name='neutral_view_Blank_5',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
neutral_view_Photo_5 = visual.ImageStim(
    win=win, name='neutral_view_Photo_5',
    image='Neutral.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
neutral_view_Blank2_5 = visual.TextStim(win=win, name='neutral_view_Blank2_5',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
neutral_view_Response_5 = visual.TextStim(win=win, name='neutral_view_Response_5',
    text='How do you Feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
neutral_view_Plus2_5 = visual.TextStim(win=win, name='neutral_view_Plus2_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
negative_view_Plus_5 = visual.TextStim(win=win, name='negative_view_Plus_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
negative_view_VIEW_5 = visual.TextStim(win=win, name='negative_view_VIEW_5',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.6, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
negative_view_Blank_5 = visual.TextStim(win=win, name='negative_view_Blank_5',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
negative_view_image_5 = visual.ImageStim(
    win=win, name='negative_view_image_5',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
negative_view_Blank2_5 = visual.TextStim(win=win, name='negative_view_Blank2_5',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);
negative_view_Response_5 = visual.TextStim(win=win, name='negative_view_Response_5',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-13.0);
negative_view_Plus2_5 = visual.TextStim(win=win, name='negative_view_Plus2_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-15.0);
negative_distract_plus_5 = visual.TextStim(win=win, name='negative_distract_plus_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-16.0);
negative_distract_DISTRACT_5 = visual.TextStim(win=win, name='negative_distract_DISTRACT_5',
    text='DISTRACT',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-17.0);
negative_distract_Blank_5 = visual.TextStim(win=win, name='negative_distract_Blank_5',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-18.0);
negative_distract_Photo_5 = visual.ImageStim(
    win=win, name='negative_distract_Photo_5',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
negative_distract_Blank2_5 = visual.TextStim(win=win, name='negative_distract_Blank2_5',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-20.0);
negative_distract_Response_5 = visual.TextStim(win=win, name='negative_distract_Response_5',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-21.0);
negative_distract_Plus2_5 = visual.TextStim(win=win, name='negative_distract_Plus2_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-23.0);
negative_reappraise_Plus_5 = visual.TextStim(win=win, name='negative_reappraise_Plus_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-24.0);
negative_reappraise_REAPPRAISE_5 = visual.TextStim(win=win, name='negative_reappraise_REAPPRAISE_5',
    text='REAPPRAISE',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-25.0);
negative_reappraise_Blank_5 = visual.TextStim(win=win, name='negative_reappraise_Blank_5',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-26.0);
negative_reappraise_Photo_5 = visual.ImageStim(
    win=win, name='negative_reappraise_Photo_5',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-27.0)
negative_reappraise_Blank2_5 = visual.TextStim(win=win, name='negative_reappraise_Blank2_5',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-28.0);
negative_reappraise_Response_5 = visual.TextStim(win=win, name='negative_reappraise_Response_5',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-29.0);
negative_reappraise_Plus2_5 = visual.TextStim(win=win, name='negative_reappraise_Plus2_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-31.0);

# Initialize components for Routine "Block_6"
Block_6Clock = core.Clock()
neutral_view_Plus_6 = visual.TextStim(win=win, name='neutral_view_Plus_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
neutral_view_VIEW_6 = visual.TextStim(win=win, name='neutral_view_VIEW_6',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
neutral_view_Blank_6 = visual.TextStim(win=win, name='neutral_view_Blank_6',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
neutral_view_Photo_6 = visual.ImageStim(
    win=win, name='neutral_view_Photo_6',
    image='Neutral.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
neutral_view_Blank2_6 = visual.TextStim(win=win, name='neutral_view_Blank2_6',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
neutral_view_Response_6 = visual.TextStim(win=win, name='neutral_view_Response_6',
    text='How do you Feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
neutral_view_Plus2_6 = visual.TextStim(win=win, name='neutral_view_Plus2_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
negative_view_Plus_6 = visual.TextStim(win=win, name='negative_view_Plus_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
negative_view_VIEW_6 = visual.TextStim(win=win, name='negative_view_VIEW_6',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.6, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
negative_view_Blank_6 = visual.TextStim(win=win, name='negative_view_Blank_6',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
negative_view_image_6 = visual.ImageStim(
    win=win, name='negative_view_image_6',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
negative_view_Blank2_6 = visual.TextStim(win=win, name='negative_view_Blank2_6',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);
negative_view_Response_6 = visual.TextStim(win=win, name='negative_view_Response_6',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-13.0);
negative_view_Plus2_6 = visual.TextStim(win=win, name='negative_view_Plus2_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-15.0);
negative_distract_plus_6 = visual.TextStim(win=win, name='negative_distract_plus_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-16.0);
negative_distract_DISTRACT_6 = visual.TextStim(win=win, name='negative_distract_DISTRACT_6',
    text='DISTRACT',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-17.0);
negative_distract_Blank_6 = visual.TextStim(win=win, name='negative_distract_Blank_6',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-18.0);
negative_distract_Photo_6 = visual.ImageStim(
    win=win, name='negative_distract_Photo_6',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
negative_distract_Blank2_6 = visual.TextStim(win=win, name='negative_distract_Blank2_6',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-20.0);
negative_distract_Response_6 = visual.TextStim(win=win, name='negative_distract_Response_6',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-21.0);
negative_distract_Plus2_6 = visual.TextStim(win=win, name='negative_distract_Plus2_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-23.0);
negative_reappraise_Plus_6 = visual.TextStim(win=win, name='negative_reappraise_Plus_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-24.0);
negative_reappraise_REAPPRAISE_6 = visual.TextStim(win=win, name='negative_reappraise_REAPPRAISE_6',
    text='REAPPRAISE',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-25.0);
negative_reappraise_Blank_6 = visual.TextStim(win=win, name='negative_reappraise_Blank_6',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-26.0);
negative_reappraise_Photo_6 = visual.ImageStim(
    win=win, name='negative_reappraise_Photo_6',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-27.0)
negative_reappraise_Blank2_6 = visual.TextStim(win=win, name='negative_reappraise_Blank2_6',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-28.0);
negative_reappraise_Response_6 = visual.TextStim(win=win, name='negative_reappraise_Response_6',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-29.0);
negative_reappraise_Plus2_6 = visual.TextStim(win=win, name='negative_reappraise_Plus2_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-31.0);

# Initialize components for Routine "Block_7"
Block_7Clock = core.Clock()
neutral_view_Plus_7 = visual.TextStim(win=win, name='neutral_view_Plus_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
neutral_view_VIEW_7 = visual.TextStim(win=win, name='neutral_view_VIEW_7',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
neutral_view_Blank_7 = visual.TextStim(win=win, name='neutral_view_Blank_7',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
neutral_view_Photo_7 = visual.ImageStim(
    win=win, name='neutral_view_Photo_7',
    image='Neutral.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
neutral_view_Blank2_7 = visual.TextStim(win=win, name='neutral_view_Blank2_7',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
neutral_view_Response_7 = visual.TextStim(win=win, name='neutral_view_Response_7',
    text='How do you Feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
neutral_view_Plus2_7 = visual.TextStim(win=win, name='neutral_view_Plus2_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
negative_view_Plus_7 = visual.TextStim(win=win, name='negative_view_Plus_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
negative_view_VIEW_7 = visual.TextStim(win=win, name='negative_view_VIEW_7',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.6, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);
negative_view_Blank_7 = visual.TextStim(win=win, name='negative_view_Blank_7',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
negative_view_image_7 = visual.ImageStim(
    win=win, name='negative_view_image_7',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
negative_view_Blank2_7 = visual.TextStim(win=win, name='negative_view_Blank2_7',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);
negative_view_Response_7 = visual.TextStim(win=win, name='negative_view_Response_7',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-13.0);
negative_view_Plus2_7 = visual.TextStim(win=win, name='negative_view_Plus2_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-15.0);
negative_distract_plus_7 = visual.TextStim(win=win, name='negative_distract_plus_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-16.0);
negative_distract_DISTRACT_7 = visual.TextStim(win=win, name='negative_distract_DISTRACT_7',
    text='DISTRACT',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-17.0);
negative_distract_Blank_7 = visual.TextStim(win=win, name='negative_distract_Blank_7',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-18.0);
negative_distract_Photo_7 = visual.ImageStim(
    win=win, name='negative_distract_Photo_7',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
negative_distract_Blank2_7 = visual.TextStim(win=win, name='negative_distract_Blank2_7',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-20.0);
negative_distract_Response_7 = visual.TextStim(win=win, name='negative_distract_Response_7',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-21.0);
negative_distract_Plus2_7 = visual.TextStim(win=win, name='negative_distract_Plus2_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-23.0);
negative_reappraise_Plus_7 = visual.TextStim(win=win, name='negative_reappraise_Plus_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-24.0);
negative_reappraise_REAPPRAISE_7 = visual.TextStim(win=win, name='negative_reappraise_REAPPRAISE_7',
    text='REAPPRAISE',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-25.0);
negative_reappraise_Blank_7 = visual.TextStim(win=win, name='negative_reappraise_Blank_7',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-26.0);
negative_reappraise_Photo_7 = visual.ImageStim(
    win=win, name='negative_reappraise_Photo_7',
    image='Negative.png', mask=None,
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-27.0)
negative_reappraise_Blank2_7 = visual.TextStim(win=win, name='negative_reappraise_Blank2_7',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-28.0);
negative_reappraise_Response_7 = visual.TextStim(win=win, name='negative_reappraise_Response_7',
    text='How do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-29.0);
negative_reappraise_Plus2_7 = visual.TextStim(win=win, name='negative_reappraise_Plus2_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-31.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
t = 0
WelcomeClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
WelcomeComponents = [text]
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Welcome"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WelcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Operator_Instructions"-------
t = 0
Operator_InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
Operator_InstructionsComponents = [text_2]
for thisComponent in Operator_InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Operator_Instructions"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Operator_InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Operator_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Operator_Instructions"-------
for thisComponent in Operator_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "Block_1"-------
t = 0
Block_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(119.000000)
# update component parameters for each repeat
neutral_view_Key_Response = event.BuilderKeyResponse()
negative_view_Key_Resp_2 = event.BuilderKeyResponse()
negative_distract_key_resp_2 = event.BuilderKeyResponse()
negative_reappraise_key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
Block_1Components = [neutral_view_Plus, neutral_view_VIEW, neutral_view_Blank, neutral_view_Photo, neutral_view_Blank2, neutral_view_Response, neutral_view_Key_Response, neutral_view_Plus2, negative_view_Plus, negative_view_VIEW, negative_view_Blank, negative_view_image, negative_view_Blank2, negative_view_Response, negative_view_Key_Resp_2, negative_view_Plus2, negative_distract_plus, negative_distract_DISTRACT, negative_distract_Blank, negative_distract_Photo, negative_distract_Blank2, negative_distract_Response, negative_distract_key_resp_2, negative_distract_Plus2, negative_reappraise_Plus, negative_reappraise_REAPPRAISE, negative_reappraise_Blank, negative_reappraise_Photo, negative_reappraise_Blank2, negative_reappraise_Response, negative_reappraise_key_resp_2, negative_reappraise_Plus2]
for thisComponent in Block_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block_1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Block_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *neutral_view_Plus* updates
    if t >= 0.0 and neutral_view_Plus.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus.tStart = t
        neutral_view_Plus.frameNStart = frameN  # exact frame index
        neutral_view_Plus.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus.status == STARTED and t >= frameRemains:
        neutral_view_Plus.setAutoDraw(False)
    
    # *neutral_view_VIEW* updates
    if t >= 0.5 and neutral_view_VIEW.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_VIEW.tStart = t
        neutral_view_VIEW.frameNStart = frameN  # exact frame index
        neutral_view_VIEW.setAutoDraw(True)
    frameRemains = 0.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_VIEW.status == STARTED and t >= frameRemains:
        neutral_view_VIEW.setAutoDraw(False)
    
    # *neutral_view_Blank* updates
    if t >= 2.5 and neutral_view_Blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank.tStart = t
        neutral_view_Blank.frameNStart = frameN  # exact frame index
        neutral_view_Blank.setAutoDraw(True)
    frameRemains = 2.5 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank.status == STARTED and t >= frameRemains:
        neutral_view_Blank.setAutoDraw(False)
    
    # *neutral_view_Photo* updates
    if t >= 3 and neutral_view_Photo.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Photo.tStart = t
        neutral_view_Photo.frameNStart = frameN  # exact frame index
        neutral_view_Photo.setAutoDraw(True)
    frameRemains = 3 + 18- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Photo.status == STARTED and t >= frameRemains:
        neutral_view_Photo.setAutoDraw(False)
    
    # *neutral_view_Blank2* updates
    if t >= 21 and neutral_view_Blank2.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank2.tStart = t
        neutral_view_Blank2.frameNStart = frameN  # exact frame index
        neutral_view_Blank2.setAutoDraw(True)
    frameRemains = 21 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank2.status == STARTED and t >= frameRemains:
        neutral_view_Blank2.setAutoDraw(False)
    
    # *neutral_view_Response* updates
    if t >= 22 and neutral_view_Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Response.tStart = t
        neutral_view_Response.frameNStart = frameN  # exact frame index
        neutral_view_Response.setAutoDraw(True)
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Response.status == STARTED and t >= frameRemains:
        neutral_view_Response.setAutoDraw(False)
    
    # *neutral_view_Key_Response* updates
    if t >= 22 and neutral_view_Key_Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Key_Response.tStart = t
        neutral_view_Key_Response.frameNStart = frameN  # exact frame index
        neutral_view_Key_Response.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(neutral_view_Key_Response.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Key_Response.status == STARTED and t >= frameRemains:
        neutral_view_Key_Response.status = STOPPED
    if neutral_view_Key_Response.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            neutral_view_Key_Response.keys = theseKeys[-1]  # just the last key pressed
            neutral_view_Key_Response.rt = neutral_view_Key_Response.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *neutral_view_Plus2* updates
    if t >= 26 and neutral_view_Plus2.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus2.tStart = t
        neutral_view_Plus2.frameNStart = frameN  # exact frame index
        neutral_view_Plus2.setAutoDraw(True)
    frameRemains = 26 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus2.status == STARTED and t >= frameRemains:
        neutral_view_Plus2.setAutoDraw(False)
    
    # *negative_view_Plus* updates
    if t >= 34 and negative_view_Plus.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus.tStart = t
        negative_view_Plus.frameNStart = frameN  # exact frame index
        negative_view_Plus.setAutoDraw(True)
    frameRemains = 34 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus.status == STARTED and t >= frameRemains:
        negative_view_Plus.setAutoDraw(False)
    
    # *negative_view_VIEW* updates
    if t >= 34.5 and negative_view_VIEW.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_VIEW.tStart = t
        negative_view_VIEW.frameNStart = frameN  # exact frame index
        negative_view_VIEW.setAutoDraw(True)
    frameRemains = 34.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_VIEW.status == STARTED and t >= frameRemains:
        negative_view_VIEW.setAutoDraw(False)
    
    # *negative_view_Blank* updates
    if t >= 36.5 and negative_view_Blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank.tStart = t
        negative_view_Blank.frameNStart = frameN  # exact frame index
        negative_view_Blank.setAutoDraw(True)
    frameRemains = 36.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank.status == STARTED and t >= frameRemains:
        negative_view_Blank.setAutoDraw(False)
    
    # *negative_view_image* updates
    if t >= 37 and negative_view_image.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_image.tStart = t
        negative_view_image.frameNStart = frameN  # exact frame index
        negative_view_image.setAutoDraw(True)
    frameRemains = 37 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_image.status == STARTED and t >= frameRemains:
        negative_view_image.setAutoDraw(False)
    
    # *negative_view_Blank2* updates
    if t >= 52 and negative_view_Blank2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank2.tStart = t
        negative_view_Blank2.frameNStart = frameN  # exact frame index
        negative_view_Blank2.setAutoDraw(True)
    frameRemains = 52 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank2.status == STARTED and t >= frameRemains:
        negative_view_Blank2.setAutoDraw(False)
    
    # *negative_view_Response* updates
    if t >= 53 and negative_view_Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Response.tStart = t
        negative_view_Response.frameNStart = frameN  # exact frame index
        negative_view_Response.setAutoDraw(True)
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Response.status == STARTED and t >= frameRemains:
        negative_view_Response.setAutoDraw(False)
    
    # *negative_view_Key_Resp_2* updates
    if t >= 53 and negative_view_Key_Resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Key_Resp_2.tStart = t
        negative_view_Key_Resp_2.frameNStart = frameN  # exact frame index
        negative_view_Key_Resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_view_Key_Resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Key_Resp_2.status == STARTED and t >= frameRemains:
        negative_view_Key_Resp_2.status = STOPPED
    if negative_view_Key_Resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_view_Key_Resp_2.keys = theseKeys[-1]  # just the last key pressed
            negative_view_Key_Resp_2.rt = negative_view_Key_Resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_view_Plus2* updates
    if t >= 57 and negative_view_Plus2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus2.tStart = t
        negative_view_Plus2.frameNStart = frameN  # exact frame index
        negative_view_Plus2.setAutoDraw(True)
    frameRemains = 57 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus2.status == STARTED and t >= frameRemains:
        negative_view_Plus2.setAutoDraw(False)
    
    # *negative_distract_plus* updates
    if t >= 65 and negative_distract_plus.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_plus.tStart = t
        negative_distract_plus.frameNStart = frameN  # exact frame index
        negative_distract_plus.setAutoDraw(True)
    frameRemains = 65 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_plus.status == STARTED and t >= frameRemains:
        negative_distract_plus.setAutoDraw(False)
    
    # *negative_distract_DISTRACT* updates
    if t >= 65.5 and negative_distract_DISTRACT.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_DISTRACT.tStart = t
        negative_distract_DISTRACT.frameNStart = frameN  # exact frame index
        negative_distract_DISTRACT.setAutoDraw(True)
    frameRemains = 65.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_DISTRACT.status == STARTED and t >= frameRemains:
        negative_distract_DISTRACT.setAutoDraw(False)
    
    # *negative_distract_Blank* updates
    if t >= 67.5 and negative_distract_Blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank.tStart = t
        negative_distract_Blank.frameNStart = frameN  # exact frame index
        negative_distract_Blank.setAutoDraw(True)
    frameRemains = 67.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank.status == STARTED and t >= frameRemains:
        negative_distract_Blank.setAutoDraw(False)
    
    # *negative_distract_Photo* updates
    if t >= 68 and negative_distract_Photo.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Photo.tStart = t
        negative_distract_Photo.frameNStart = frameN  # exact frame index
        negative_distract_Photo.setAutoDraw(True)
    frameRemains = 68 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Photo.status == STARTED and t >= frameRemains:
        negative_distract_Photo.setAutoDraw(False)
    
    # *negative_distract_Blank2* updates
    if t >= 83 and negative_distract_Blank2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank2.tStart = t
        negative_distract_Blank2.frameNStart = frameN  # exact frame index
        negative_distract_Blank2.setAutoDraw(True)
    frameRemains = 83 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank2.status == STARTED and t >= frameRemains:
        negative_distract_Blank2.setAutoDraw(False)
    
    # *negative_distract_Response* updates
    if t >= 84 and negative_distract_Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Response.tStart = t
        negative_distract_Response.frameNStart = frameN  # exact frame index
        negative_distract_Response.setAutoDraw(True)
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Response.status == STARTED and t >= frameRemains:
        negative_distract_Response.setAutoDraw(False)
    
    # *negative_distract_key_resp_2* updates
    if t >= 84 and negative_distract_key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_key_resp_2.tStart = t
        negative_distract_key_resp_2.frameNStart = frameN  # exact frame index
        negative_distract_key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_distract_key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_key_resp_2.status == STARTED and t >= frameRemains:
        negative_distract_key_resp_2.status = STOPPED
    if negative_distract_key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_distract_key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            negative_distract_key_resp_2.rt = negative_distract_key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_distract_Plus2* updates
    if t >= 88 and negative_distract_Plus2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Plus2.tStart = t
        negative_distract_Plus2.frameNStart = frameN  # exact frame index
        negative_distract_Plus2.setAutoDraw(True)
    frameRemains = 88 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Plus2.status == STARTED and t >= frameRemains:
        negative_distract_Plus2.setAutoDraw(False)
    
    # *negative_reappraise_Plus* updates
    if t >= 92 and negative_reappraise_Plus.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus.tStart = t
        negative_reappraise_Plus.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus.setAutoDraw(True)
    frameRemains = 92 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus.setAutoDraw(False)
    
    # *negative_reappraise_REAPPRAISE* updates
    if t >= 92.5 and negative_reappraise_REAPPRAISE.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_REAPPRAISE.tStart = t
        negative_reappraise_REAPPRAISE.frameNStart = frameN  # exact frame index
        negative_reappraise_REAPPRAISE.setAutoDraw(True)
    frameRemains = 92.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_REAPPRAISE.status == STARTED and t >= frameRemains:
        negative_reappraise_REAPPRAISE.setAutoDraw(False)
    
    # *negative_reappraise_Blank* updates
    if t >= 94.5 and negative_reappraise_Blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank.tStart = t
        negative_reappraise_Blank.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank.setAutoDraw(True)
    frameRemains = 94.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank.setAutoDraw(False)
    
    # *negative_reappraise_Photo* updates
    if t >= 95 and negative_reappraise_Photo.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Photo.tStart = t
        negative_reappraise_Photo.frameNStart = frameN  # exact frame index
        negative_reappraise_Photo.setAutoDraw(True)
    frameRemains = 95 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Photo.status == STARTED and t >= frameRemains:
        negative_reappraise_Photo.setAutoDraw(False)
    
    # *negative_reappraise_Blank2* updates
    if t >= 110 and negative_reappraise_Blank2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank2.tStart = t
        negative_reappraise_Blank2.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank2.setAutoDraw(True)
    frameRemains = 110 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank2.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank2.setAutoDraw(False)
    
    # *negative_reappraise_Response* updates
    if t >= 111 and negative_reappraise_Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Response.tStart = t
        negative_reappraise_Response.frameNStart = frameN  # exact frame index
        negative_reappraise_Response.setAutoDraw(True)
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Response.status == STARTED and t >= frameRemains:
        negative_reappraise_Response.setAutoDraw(False)
    
    # *negative_reappraise_key_resp_2* updates
    if t >= 111 and negative_reappraise_key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_key_resp_2.tStart = t
        negative_reappraise_key_resp_2.frameNStart = frameN  # exact frame index
        negative_reappraise_key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_reappraise_key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_key_resp_2.status == STARTED and t >= frameRemains:
        negative_reappraise_key_resp_2.status = STOPPED
    if negative_reappraise_key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_reappraise_key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            negative_reappraise_key_resp_2.rt = negative_reappraise_key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_reappraise_Plus2* updates
    if t >= 115 and negative_reappraise_Plus2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus2.tStart = t
        negative_reappraise_Plus2.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus2.setAutoDraw(True)
    frameRemains = 115 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus2.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block_1"-------
for thisComponent in Block_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if neutral_view_Key_Response.keys in ['', [], None]:  # No response was made
    neutral_view_Key_Response.keys=None
thisExp.addData('neutral_view_Key_Response.keys',neutral_view_Key_Response.keys)
if neutral_view_Key_Response.keys != None:  # we had a response
    thisExp.addData('neutral_view_Key_Response.rt', neutral_view_Key_Response.rt)
thisExp.nextEntry()
# check responses
if negative_view_Key_Resp_2.keys in ['', [], None]:  # No response was made
    negative_view_Key_Resp_2.keys=None
thisExp.addData('negative_view_Key_Resp_2.keys',negative_view_Key_Resp_2.keys)
if negative_view_Key_Resp_2.keys != None:  # we had a response
    thisExp.addData('negative_view_Key_Resp_2.rt', negative_view_Key_Resp_2.rt)
thisExp.nextEntry()
# check responses
if negative_distract_key_resp_2.keys in ['', [], None]:  # No response was made
    negative_distract_key_resp_2.keys=None
thisExp.addData('negative_distract_key_resp_2.keys',negative_distract_key_resp_2.keys)
if negative_distract_key_resp_2.keys != None:  # we had a response
    thisExp.addData('negative_distract_key_resp_2.rt', negative_distract_key_resp_2.rt)
thisExp.nextEntry()
# check responses
if negative_reappraise_key_resp_2.keys in ['', [], None]:  # No response was made
    negative_reappraise_key_resp_2.keys=None
thisExp.addData('negative_reappraise_key_resp_2.keys',negative_reappraise_key_resp_2.keys)
if negative_reappraise_key_resp_2.keys != None:  # we had a response
    thisExp.addData('negative_reappraise_key_resp_2.rt', negative_reappraise_key_resp_2.rt)
thisExp.nextEntry()

# ------Prepare to start Routine "Block_2"-------
t = 0
Block_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(119.000000)
# update component parameters for each repeat
neutral_view_Key_Response_2 = event.BuilderKeyResponse()
negative_view_Key_Resp = event.BuilderKeyResponse()
negative_distract_key_resp = event.BuilderKeyResponse()
negative_reappraise_key_resp = event.BuilderKeyResponse()
# keep track of which components have finished
Block_2Components = [neutral_view_Plus_2, neutral_view_VIEW_2, neutral_view_Blank_2, neutral_view_Photo_2, neutral_view_Blank2_2, neutral_view_Response_2, neutral_view_Key_Response_2, neutral_view_Plus2_2, negative_view_Plus_2, negative_view_VIEW_2, negative_view_Blank_2, negative_view_image_2, negative_view_Blank2_2, negative_view_Response_2, negative_view_Key_Resp, negative_view_Plus2_2, negative_distract_plus_2, negative_distract_DISTRACT_2, negative_distract_Blank_2, negative_distract_Photo_2, negative_distract_Blank2_2, negative_distract_Response_2, negative_distract_key_resp, negative_distract_Plus2_2, negative_reappraise_Plus_2, negative_reappraise_REAPPRAISE_2, negative_reappraise_Blank_2, negative_reappraise_Photo_2, negative_reappraise_Blank2_2, negative_reappraise_Response_2, negative_reappraise_key_resp, negative_reappraise_Plus2_2]
for thisComponent in Block_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Block_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *neutral_view_Plus_2* updates
    if t >= 0.0 and neutral_view_Plus_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus_2.tStart = t
        neutral_view_Plus_2.frameNStart = frameN  # exact frame index
        neutral_view_Plus_2.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus_2.status == STARTED and t >= frameRemains:
        neutral_view_Plus_2.setAutoDraw(False)
    
    # *neutral_view_VIEW_2* updates
    if t >= 0.5 and neutral_view_VIEW_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_VIEW_2.tStart = t
        neutral_view_VIEW_2.frameNStart = frameN  # exact frame index
        neutral_view_VIEW_2.setAutoDraw(True)
    frameRemains = 0.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_VIEW_2.status == STARTED and t >= frameRemains:
        neutral_view_VIEW_2.setAutoDraw(False)
    
    # *neutral_view_Blank_2* updates
    if t >= 2.5 and neutral_view_Blank_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank_2.tStart = t
        neutral_view_Blank_2.frameNStart = frameN  # exact frame index
        neutral_view_Blank_2.setAutoDraw(True)
    frameRemains = 2.5 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank_2.status == STARTED and t >= frameRemains:
        neutral_view_Blank_2.setAutoDraw(False)
    
    # *neutral_view_Photo_2* updates
    if t >= 3 and neutral_view_Photo_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Photo_2.tStart = t
        neutral_view_Photo_2.frameNStart = frameN  # exact frame index
        neutral_view_Photo_2.setAutoDraw(True)
    frameRemains = 3 + 18- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Photo_2.status == STARTED and t >= frameRemains:
        neutral_view_Photo_2.setAutoDraw(False)
    
    # *neutral_view_Blank2_2* updates
    if t >= 21 and neutral_view_Blank2_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank2_2.tStart = t
        neutral_view_Blank2_2.frameNStart = frameN  # exact frame index
        neutral_view_Blank2_2.setAutoDraw(True)
    frameRemains = 21 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank2_2.status == STARTED and t >= frameRemains:
        neutral_view_Blank2_2.setAutoDraw(False)
    
    # *neutral_view_Response_2* updates
    if t >= 22 and neutral_view_Response_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Response_2.tStart = t
        neutral_view_Response_2.frameNStart = frameN  # exact frame index
        neutral_view_Response_2.setAutoDraw(True)
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Response_2.status == STARTED and t >= frameRemains:
        neutral_view_Response_2.setAutoDraw(False)
    
    # *neutral_view_Key_Response_2* updates
    if t >= 22 and neutral_view_Key_Response_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Key_Response_2.tStart = t
        neutral_view_Key_Response_2.frameNStart = frameN  # exact frame index
        neutral_view_Key_Response_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(neutral_view_Key_Response_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Key_Response_2.status == STARTED and t >= frameRemains:
        neutral_view_Key_Response_2.status = STOPPED
    if neutral_view_Key_Response_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            neutral_view_Key_Response_2.keys = theseKeys[-1]  # just the last key pressed
            neutral_view_Key_Response_2.rt = neutral_view_Key_Response_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *neutral_view_Plus2_2* updates
    if t >= 26 and neutral_view_Plus2_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus2_2.tStart = t
        neutral_view_Plus2_2.frameNStart = frameN  # exact frame index
        neutral_view_Plus2_2.setAutoDraw(True)
    frameRemains = 26 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus2_2.status == STARTED and t >= frameRemains:
        neutral_view_Plus2_2.setAutoDraw(False)
    
    # *negative_view_Plus_2* updates
    if t >= 34 and negative_view_Plus_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus_2.tStart = t
        negative_view_Plus_2.frameNStart = frameN  # exact frame index
        negative_view_Plus_2.setAutoDraw(True)
    frameRemains = 34 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus_2.status == STARTED and t >= frameRemains:
        negative_view_Plus_2.setAutoDraw(False)
    
    # *negative_view_VIEW_2* updates
    if t >= 34.5 and negative_view_VIEW_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_VIEW_2.tStart = t
        negative_view_VIEW_2.frameNStart = frameN  # exact frame index
        negative_view_VIEW_2.setAutoDraw(True)
    frameRemains = 34.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_VIEW_2.status == STARTED and t >= frameRemains:
        negative_view_VIEW_2.setAutoDraw(False)
    
    # *negative_view_Blank_2* updates
    if t >= 36.5 and negative_view_Blank_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank_2.tStart = t
        negative_view_Blank_2.frameNStart = frameN  # exact frame index
        negative_view_Blank_2.setAutoDraw(True)
    frameRemains = 36.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank_2.status == STARTED and t >= frameRemains:
        negative_view_Blank_2.setAutoDraw(False)
    
    # *negative_view_image_2* updates
    if t >= 37 and negative_view_image_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_image_2.tStart = t
        negative_view_image_2.frameNStart = frameN  # exact frame index
        negative_view_image_2.setAutoDraw(True)
    frameRemains = 37 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_image_2.status == STARTED and t >= frameRemains:
        negative_view_image_2.setAutoDraw(False)
    
    # *negative_view_Blank2_2* updates
    if t >= 52 and negative_view_Blank2_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank2_2.tStart = t
        negative_view_Blank2_2.frameNStart = frameN  # exact frame index
        negative_view_Blank2_2.setAutoDraw(True)
    frameRemains = 52 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank2_2.status == STARTED and t >= frameRemains:
        negative_view_Blank2_2.setAutoDraw(False)
    
    # *negative_view_Response_2* updates
    if t >= 53 and negative_view_Response_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Response_2.tStart = t
        negative_view_Response_2.frameNStart = frameN  # exact frame index
        negative_view_Response_2.setAutoDraw(True)
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Response_2.status == STARTED and t >= frameRemains:
        negative_view_Response_2.setAutoDraw(False)
    
    # *negative_view_Key_Resp* updates
    if t >= 53 and negative_view_Key_Resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Key_Resp.tStart = t
        negative_view_Key_Resp.frameNStart = frameN  # exact frame index
        negative_view_Key_Resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_view_Key_Resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Key_Resp.status == STARTED and t >= frameRemains:
        negative_view_Key_Resp.status = STOPPED
    if negative_view_Key_Resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_view_Key_Resp.keys = theseKeys[-1]  # just the last key pressed
            negative_view_Key_Resp.rt = negative_view_Key_Resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_view_Plus2_2* updates
    if t >= 57 and negative_view_Plus2_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus2_2.tStart = t
        negative_view_Plus2_2.frameNStart = frameN  # exact frame index
        negative_view_Plus2_2.setAutoDraw(True)
    frameRemains = 57 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus2_2.status == STARTED and t >= frameRemains:
        negative_view_Plus2_2.setAutoDraw(False)
    
    # *negative_distract_plus_2* updates
    if t >= 65 and negative_distract_plus_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_plus_2.tStart = t
        negative_distract_plus_2.frameNStart = frameN  # exact frame index
        negative_distract_plus_2.setAutoDraw(True)
    frameRemains = 65 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_plus_2.status == STARTED and t >= frameRemains:
        negative_distract_plus_2.setAutoDraw(False)
    
    # *negative_distract_DISTRACT_2* updates
    if t >= 65.5 and negative_distract_DISTRACT_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_DISTRACT_2.tStart = t
        negative_distract_DISTRACT_2.frameNStart = frameN  # exact frame index
        negative_distract_DISTRACT_2.setAutoDraw(True)
    frameRemains = 65.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_DISTRACT_2.status == STARTED and t >= frameRemains:
        negative_distract_DISTRACT_2.setAutoDraw(False)
    
    # *negative_distract_Blank_2* updates
    if t >= 67.5 and negative_distract_Blank_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank_2.tStart = t
        negative_distract_Blank_2.frameNStart = frameN  # exact frame index
        negative_distract_Blank_2.setAutoDraw(True)
    frameRemains = 67.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank_2.status == STARTED and t >= frameRemains:
        negative_distract_Blank_2.setAutoDraw(False)
    
    # *negative_distract_Photo_2* updates
    if t >= 68 and negative_distract_Photo_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Photo_2.tStart = t
        negative_distract_Photo_2.frameNStart = frameN  # exact frame index
        negative_distract_Photo_2.setAutoDraw(True)
    frameRemains = 68 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Photo_2.status == STARTED and t >= frameRemains:
        negative_distract_Photo_2.setAutoDraw(False)
    
    # *negative_distract_Blank2_2* updates
    if t >= 83 and negative_distract_Blank2_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank2_2.tStart = t
        negative_distract_Blank2_2.frameNStart = frameN  # exact frame index
        negative_distract_Blank2_2.setAutoDraw(True)
    frameRemains = 83 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank2_2.status == STARTED and t >= frameRemains:
        negative_distract_Blank2_2.setAutoDraw(False)
    
    # *negative_distract_Response_2* updates
    if t >= 84 and negative_distract_Response_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Response_2.tStart = t
        negative_distract_Response_2.frameNStart = frameN  # exact frame index
        negative_distract_Response_2.setAutoDraw(True)
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Response_2.status == STARTED and t >= frameRemains:
        negative_distract_Response_2.setAutoDraw(False)
    
    # *negative_distract_key_resp* updates
    if t >= 84 and negative_distract_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_key_resp.tStart = t
        negative_distract_key_resp.frameNStart = frameN  # exact frame index
        negative_distract_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_distract_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_key_resp.status == STARTED and t >= frameRemains:
        negative_distract_key_resp.status = STOPPED
    if negative_distract_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_distract_key_resp.keys = theseKeys[-1]  # just the last key pressed
            negative_distract_key_resp.rt = negative_distract_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_distract_Plus2_2* updates
    if t >= 88 and negative_distract_Plus2_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Plus2_2.tStart = t
        negative_distract_Plus2_2.frameNStart = frameN  # exact frame index
        negative_distract_Plus2_2.setAutoDraw(True)
    frameRemains = 88 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Plus2_2.status == STARTED and t >= frameRemains:
        negative_distract_Plus2_2.setAutoDraw(False)
    
    # *negative_reappraise_Plus_2* updates
    if t >= 92 and negative_reappraise_Plus_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus_2.tStart = t
        negative_reappraise_Plus_2.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus_2.setAutoDraw(True)
    frameRemains = 92 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus_2.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus_2.setAutoDraw(False)
    
    # *negative_reappraise_REAPPRAISE_2* updates
    if t >= 92.5 and negative_reappraise_REAPPRAISE_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_REAPPRAISE_2.tStart = t
        negative_reappraise_REAPPRAISE_2.frameNStart = frameN  # exact frame index
        negative_reappraise_REAPPRAISE_2.setAutoDraw(True)
    frameRemains = 92.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_REAPPRAISE_2.status == STARTED and t >= frameRemains:
        negative_reappraise_REAPPRAISE_2.setAutoDraw(False)
    
    # *negative_reappraise_Blank_2* updates
    if t >= 94.5 and negative_reappraise_Blank_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank_2.tStart = t
        negative_reappraise_Blank_2.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank_2.setAutoDraw(True)
    frameRemains = 94.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank_2.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank_2.setAutoDraw(False)
    
    # *negative_reappraise_Photo_2* updates
    if t >= 95 and negative_reappraise_Photo_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Photo_2.tStart = t
        negative_reappraise_Photo_2.frameNStart = frameN  # exact frame index
        negative_reappraise_Photo_2.setAutoDraw(True)
    frameRemains = 95 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Photo_2.status == STARTED and t >= frameRemains:
        negative_reappraise_Photo_2.setAutoDraw(False)
    
    # *negative_reappraise_Blank2_2* updates
    if t >= 110 and negative_reappraise_Blank2_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank2_2.tStart = t
        negative_reappraise_Blank2_2.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank2_2.setAutoDraw(True)
    frameRemains = 110 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank2_2.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank2_2.setAutoDraw(False)
    
    # *negative_reappraise_Response_2* updates
    if t >= 111 and negative_reappraise_Response_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Response_2.tStart = t
        negative_reappraise_Response_2.frameNStart = frameN  # exact frame index
        negative_reappraise_Response_2.setAutoDraw(True)
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Response_2.status == STARTED and t >= frameRemains:
        negative_reappraise_Response_2.setAutoDraw(False)
    
    # *negative_reappraise_key_resp* updates
    if t >= 111 and negative_reappraise_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_key_resp.tStart = t
        negative_reappraise_key_resp.frameNStart = frameN  # exact frame index
        negative_reappraise_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_reappraise_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_key_resp.status == STARTED and t >= frameRemains:
        negative_reappraise_key_resp.status = STOPPED
    if negative_reappraise_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_reappraise_key_resp.keys = theseKeys[-1]  # just the last key pressed
            negative_reappraise_key_resp.rt = negative_reappraise_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_reappraise_Plus2_2* updates
    if t >= 115 and negative_reappraise_Plus2_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus2_2.tStart = t
        negative_reappraise_Plus2_2.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus2_2.setAutoDraw(True)
    frameRemains = 115 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus2_2.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus2_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block_2"-------
for thisComponent in Block_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if neutral_view_Key_Response_2.keys in ['', [], None]:  # No response was made
    neutral_view_Key_Response_2.keys=None
thisExp.addData('neutral_view_Key_Response_2.keys',neutral_view_Key_Response_2.keys)
if neutral_view_Key_Response_2.keys != None:  # we had a response
    thisExp.addData('neutral_view_Key_Response_2.rt', neutral_view_Key_Response_2.rt)
thisExp.nextEntry()
# check responses
if negative_view_Key_Resp.keys in ['', [], None]:  # No response was made
    negative_view_Key_Resp.keys=None
thisExp.addData('negative_view_Key_Resp.keys',negative_view_Key_Resp.keys)
if negative_view_Key_Resp.keys != None:  # we had a response
    thisExp.addData('negative_view_Key_Resp.rt', negative_view_Key_Resp.rt)
thisExp.nextEntry()
# check responses
if negative_distract_key_resp.keys in ['', [], None]:  # No response was made
    negative_distract_key_resp.keys=None
thisExp.addData('negative_distract_key_resp.keys',negative_distract_key_resp.keys)
if negative_distract_key_resp.keys != None:  # we had a response
    thisExp.addData('negative_distract_key_resp.rt', negative_distract_key_resp.rt)
thisExp.nextEntry()
# check responses
if negative_reappraise_key_resp.keys in ['', [], None]:  # No response was made
    negative_reappraise_key_resp.keys=None
thisExp.addData('negative_reappraise_key_resp.keys',negative_reappraise_key_resp.keys)
if negative_reappraise_key_resp.keys != None:  # we had a response
    thisExp.addData('negative_reappraise_key_resp.rt', negative_reappraise_key_resp.rt)
thisExp.nextEntry()

# ------Prepare to start Routine "Block_3"-------
t = 0
Block_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(119.000000)
# update component parameters for each repeat
neutral_view_Key_Response_3 = event.BuilderKeyResponse()
negative_view_Key_Resp_3 = event.BuilderKeyResponse()
negative_distract_key_resp_3 = event.BuilderKeyResponse()
negative_reappraise_key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
Block_3Components = [neutral_view_Plus_3, neutral_view_VIEW_3, neutral_view_Blank_3, neutral_view_Photo_3, neutral_view_Blank2_3, neutral_view_Response_3, neutral_view_Key_Response_3, neutral_view_Plus2_3, negative_view_Plus_3, negative_view_VIEW_3, negative_view_Blank_3, negative_view_image_3, negative_view_Blank2_3, negative_view_Response_3, negative_view_Key_Resp_3, negative_view_Plus2_3, negative_distract_plus_3, negative_distract_DISTRACT_3, negative_distract_Blank_3, negative_distract_Photo_3, negative_distract_Blank2_3, negative_distract_Response_3, negative_distract_key_resp_3, negative_distract_Plus2_3, negative_reappraise_Plus_3, negative_reappraise_REAPPRAISE_3, negative_reappraise_Blank_3, negative_reappraise_Photo_3, negative_reappraise_Blank2_3, negative_reappraise_Response_3, negative_reappraise_key_resp_3, negative_reappraise_Plus2_3]
for thisComponent in Block_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Block_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *neutral_view_Plus_3* updates
    if t >= 0.0 and neutral_view_Plus_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus_3.tStart = t
        neutral_view_Plus_3.frameNStart = frameN  # exact frame index
        neutral_view_Plus_3.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus_3.status == STARTED and t >= frameRemains:
        neutral_view_Plus_3.setAutoDraw(False)
    
    # *neutral_view_VIEW_3* updates
    if t >= 0.5 and neutral_view_VIEW_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_VIEW_3.tStart = t
        neutral_view_VIEW_3.frameNStart = frameN  # exact frame index
        neutral_view_VIEW_3.setAutoDraw(True)
    frameRemains = 0.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_VIEW_3.status == STARTED and t >= frameRemains:
        neutral_view_VIEW_3.setAutoDraw(False)
    
    # *neutral_view_Blank_3* updates
    if t >= 2.5 and neutral_view_Blank_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank_3.tStart = t
        neutral_view_Blank_3.frameNStart = frameN  # exact frame index
        neutral_view_Blank_3.setAutoDraw(True)
    frameRemains = 2.5 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank_3.status == STARTED and t >= frameRemains:
        neutral_view_Blank_3.setAutoDraw(False)
    
    # *neutral_view_Photo_3* updates
    if t >= 3 and neutral_view_Photo_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Photo_3.tStart = t
        neutral_view_Photo_3.frameNStart = frameN  # exact frame index
        neutral_view_Photo_3.setAutoDraw(True)
    frameRemains = 3 + 18- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Photo_3.status == STARTED and t >= frameRemains:
        neutral_view_Photo_3.setAutoDraw(False)
    
    # *neutral_view_Blank2_3* updates
    if t >= 21 and neutral_view_Blank2_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank2_3.tStart = t
        neutral_view_Blank2_3.frameNStart = frameN  # exact frame index
        neutral_view_Blank2_3.setAutoDraw(True)
    frameRemains = 21 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank2_3.status == STARTED and t >= frameRemains:
        neutral_view_Blank2_3.setAutoDraw(False)
    
    # *neutral_view_Response_3* updates
    if t >= 22 and neutral_view_Response_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Response_3.tStart = t
        neutral_view_Response_3.frameNStart = frameN  # exact frame index
        neutral_view_Response_3.setAutoDraw(True)
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Response_3.status == STARTED and t >= frameRemains:
        neutral_view_Response_3.setAutoDraw(False)
    
    # *neutral_view_Key_Response_3* updates
    if t >= 22 and neutral_view_Key_Response_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Key_Response_3.tStart = t
        neutral_view_Key_Response_3.frameNStart = frameN  # exact frame index
        neutral_view_Key_Response_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(neutral_view_Key_Response_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Key_Response_3.status == STARTED and t >= frameRemains:
        neutral_view_Key_Response_3.status = STOPPED
    if neutral_view_Key_Response_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            neutral_view_Key_Response_3.keys = theseKeys[-1]  # just the last key pressed
            neutral_view_Key_Response_3.rt = neutral_view_Key_Response_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *neutral_view_Plus2_3* updates
    if t >= 26 and neutral_view_Plus2_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus2_3.tStart = t
        neutral_view_Plus2_3.frameNStart = frameN  # exact frame index
        neutral_view_Plus2_3.setAutoDraw(True)
    frameRemains = 26 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus2_3.status == STARTED and t >= frameRemains:
        neutral_view_Plus2_3.setAutoDraw(False)
    
    # *negative_view_Plus_3* updates
    if t >= 34 and negative_view_Plus_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus_3.tStart = t
        negative_view_Plus_3.frameNStart = frameN  # exact frame index
        negative_view_Plus_3.setAutoDraw(True)
    frameRemains = 34 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus_3.status == STARTED and t >= frameRemains:
        negative_view_Plus_3.setAutoDraw(False)
    
    # *negative_view_VIEW_3* updates
    if t >= 34.5 and negative_view_VIEW_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_VIEW_3.tStart = t
        negative_view_VIEW_3.frameNStart = frameN  # exact frame index
        negative_view_VIEW_3.setAutoDraw(True)
    frameRemains = 34.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_VIEW_3.status == STARTED and t >= frameRemains:
        negative_view_VIEW_3.setAutoDraw(False)
    
    # *negative_view_Blank_3* updates
    if t >= 36.5 and negative_view_Blank_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank_3.tStart = t
        negative_view_Blank_3.frameNStart = frameN  # exact frame index
        negative_view_Blank_3.setAutoDraw(True)
    frameRemains = 36.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank_3.status == STARTED and t >= frameRemains:
        negative_view_Blank_3.setAutoDraw(False)
    
    # *negative_view_image_3* updates
    if t >= 37 and negative_view_image_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_image_3.tStart = t
        negative_view_image_3.frameNStart = frameN  # exact frame index
        negative_view_image_3.setAutoDraw(True)
    frameRemains = 37 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_image_3.status == STARTED and t >= frameRemains:
        negative_view_image_3.setAutoDraw(False)
    
    # *negative_view_Blank2_3* updates
    if t >= 52 and negative_view_Blank2_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank2_3.tStart = t
        negative_view_Blank2_3.frameNStart = frameN  # exact frame index
        negative_view_Blank2_3.setAutoDraw(True)
    frameRemains = 52 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank2_3.status == STARTED and t >= frameRemains:
        negative_view_Blank2_3.setAutoDraw(False)
    
    # *negative_view_Response_3* updates
    if t >= 53 and negative_view_Response_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Response_3.tStart = t
        negative_view_Response_3.frameNStart = frameN  # exact frame index
        negative_view_Response_3.setAutoDraw(True)
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Response_3.status == STARTED and t >= frameRemains:
        negative_view_Response_3.setAutoDraw(False)
    
    # *negative_view_Key_Resp_3* updates
    if t >= 53 and negative_view_Key_Resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Key_Resp_3.tStart = t
        negative_view_Key_Resp_3.frameNStart = frameN  # exact frame index
        negative_view_Key_Resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_view_Key_Resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Key_Resp_3.status == STARTED and t >= frameRemains:
        negative_view_Key_Resp_3.status = STOPPED
    if negative_view_Key_Resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_view_Key_Resp_3.keys = theseKeys[-1]  # just the last key pressed
            negative_view_Key_Resp_3.rt = negative_view_Key_Resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_view_Plus2_3* updates
    if t >= 57 and negative_view_Plus2_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus2_3.tStart = t
        negative_view_Plus2_3.frameNStart = frameN  # exact frame index
        negative_view_Plus2_3.setAutoDraw(True)
    frameRemains = 57 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus2_3.status == STARTED and t >= frameRemains:
        negative_view_Plus2_3.setAutoDraw(False)
    
    # *negative_distract_plus_3* updates
    if t >= 65 and negative_distract_plus_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_plus_3.tStart = t
        negative_distract_plus_3.frameNStart = frameN  # exact frame index
        negative_distract_plus_3.setAutoDraw(True)
    frameRemains = 65 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_plus_3.status == STARTED and t >= frameRemains:
        negative_distract_plus_3.setAutoDraw(False)
    
    # *negative_distract_DISTRACT_3* updates
    if t >= 65.5 and negative_distract_DISTRACT_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_DISTRACT_3.tStart = t
        negative_distract_DISTRACT_3.frameNStart = frameN  # exact frame index
        negative_distract_DISTRACT_3.setAutoDraw(True)
    frameRemains = 65.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_DISTRACT_3.status == STARTED and t >= frameRemains:
        negative_distract_DISTRACT_3.setAutoDraw(False)
    
    # *negative_distract_Blank_3* updates
    if t >= 67.5 and negative_distract_Blank_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank_3.tStart = t
        negative_distract_Blank_3.frameNStart = frameN  # exact frame index
        negative_distract_Blank_3.setAutoDraw(True)
    frameRemains = 67.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank_3.status == STARTED and t >= frameRemains:
        negative_distract_Blank_3.setAutoDraw(False)
    
    # *negative_distract_Photo_3* updates
    if t >= 68 and negative_distract_Photo_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Photo_3.tStart = t
        negative_distract_Photo_3.frameNStart = frameN  # exact frame index
        negative_distract_Photo_3.setAutoDraw(True)
    frameRemains = 68 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Photo_3.status == STARTED and t >= frameRemains:
        negative_distract_Photo_3.setAutoDraw(False)
    
    # *negative_distract_Blank2_3* updates
    if t >= 83 and negative_distract_Blank2_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank2_3.tStart = t
        negative_distract_Blank2_3.frameNStart = frameN  # exact frame index
        negative_distract_Blank2_3.setAutoDraw(True)
    frameRemains = 83 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank2_3.status == STARTED and t >= frameRemains:
        negative_distract_Blank2_3.setAutoDraw(False)
    
    # *negative_distract_Response_3* updates
    if t >= 84 and negative_distract_Response_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Response_3.tStart = t
        negative_distract_Response_3.frameNStart = frameN  # exact frame index
        negative_distract_Response_3.setAutoDraw(True)
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Response_3.status == STARTED and t >= frameRemains:
        negative_distract_Response_3.setAutoDraw(False)
    
    # *negative_distract_key_resp_3* updates
    if t >= 84 and negative_distract_key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_key_resp_3.tStart = t
        negative_distract_key_resp_3.frameNStart = frameN  # exact frame index
        negative_distract_key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_distract_key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_key_resp_3.status == STARTED and t >= frameRemains:
        negative_distract_key_resp_3.status = STOPPED
    if negative_distract_key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_distract_key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            negative_distract_key_resp_3.rt = negative_distract_key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_distract_Plus2_3* updates
    if t >= 88 and negative_distract_Plus2_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Plus2_3.tStart = t
        negative_distract_Plus2_3.frameNStart = frameN  # exact frame index
        negative_distract_Plus2_3.setAutoDraw(True)
    frameRemains = 88 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Plus2_3.status == STARTED and t >= frameRemains:
        negative_distract_Plus2_3.setAutoDraw(False)
    
    # *negative_reappraise_Plus_3* updates
    if t >= 92 and negative_reappraise_Plus_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus_3.tStart = t
        negative_reappraise_Plus_3.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus_3.setAutoDraw(True)
    frameRemains = 92 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus_3.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus_3.setAutoDraw(False)
    
    # *negative_reappraise_REAPPRAISE_3* updates
    if t >= 92.5 and negative_reappraise_REAPPRAISE_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_REAPPRAISE_3.tStart = t
        negative_reappraise_REAPPRAISE_3.frameNStart = frameN  # exact frame index
        negative_reappraise_REAPPRAISE_3.setAutoDraw(True)
    frameRemains = 92.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_REAPPRAISE_3.status == STARTED and t >= frameRemains:
        negative_reappraise_REAPPRAISE_3.setAutoDraw(False)
    
    # *negative_reappraise_Blank_3* updates
    if t >= 94.5 and negative_reappraise_Blank_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank_3.tStart = t
        negative_reappraise_Blank_3.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank_3.setAutoDraw(True)
    frameRemains = 94.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank_3.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank_3.setAutoDraw(False)
    
    # *negative_reappraise_Photo_3* updates
    if t >= 95 and negative_reappraise_Photo_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Photo_3.tStart = t
        negative_reappraise_Photo_3.frameNStart = frameN  # exact frame index
        negative_reappraise_Photo_3.setAutoDraw(True)
    frameRemains = 95 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Photo_3.status == STARTED and t >= frameRemains:
        negative_reappraise_Photo_3.setAutoDraw(False)
    
    # *negative_reappraise_Blank2_3* updates
    if t >= 110 and negative_reappraise_Blank2_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank2_3.tStart = t
        negative_reappraise_Blank2_3.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank2_3.setAutoDraw(True)
    frameRemains = 110 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank2_3.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank2_3.setAutoDraw(False)
    
    # *negative_reappraise_Response_3* updates
    if t >= 111 and negative_reappraise_Response_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Response_3.tStart = t
        negative_reappraise_Response_3.frameNStart = frameN  # exact frame index
        negative_reappraise_Response_3.setAutoDraw(True)
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Response_3.status == STARTED and t >= frameRemains:
        negative_reappraise_Response_3.setAutoDraw(False)
    
    # *negative_reappraise_key_resp_3* updates
    if t >= 111 and negative_reappraise_key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_key_resp_3.tStart = t
        negative_reappraise_key_resp_3.frameNStart = frameN  # exact frame index
        negative_reappraise_key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_reappraise_key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_key_resp_3.status == STARTED and t >= frameRemains:
        negative_reappraise_key_resp_3.status = STOPPED
    if negative_reappraise_key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_reappraise_key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            negative_reappraise_key_resp_3.rt = negative_reappraise_key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_reappraise_Plus2_3* updates
    if t >= 115 and negative_reappraise_Plus2_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus2_3.tStart = t
        negative_reappraise_Plus2_3.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus2_3.setAutoDraw(True)
    frameRemains = 115 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus2_3.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus2_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block_3"-------
for thisComponent in Block_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if neutral_view_Key_Response_3.keys in ['', [], None]:  # No response was made
    neutral_view_Key_Response_3.keys=None
thisExp.addData('neutral_view_Key_Response_3.keys',neutral_view_Key_Response_3.keys)
if neutral_view_Key_Response_3.keys != None:  # we had a response
    thisExp.addData('neutral_view_Key_Response_3.rt', neutral_view_Key_Response_3.rt)
thisExp.nextEntry()
# check responses
if negative_view_Key_Resp_3.keys in ['', [], None]:  # No response was made
    negative_view_Key_Resp_3.keys=None
thisExp.addData('negative_view_Key_Resp_3.keys',negative_view_Key_Resp_3.keys)
if negative_view_Key_Resp_3.keys != None:  # we had a response
    thisExp.addData('negative_view_Key_Resp_3.rt', negative_view_Key_Resp_3.rt)
thisExp.nextEntry()
# check responses
if negative_distract_key_resp_3.keys in ['', [], None]:  # No response was made
    negative_distract_key_resp_3.keys=None
thisExp.addData('negative_distract_key_resp_3.keys',negative_distract_key_resp_3.keys)
if negative_distract_key_resp_3.keys != None:  # we had a response
    thisExp.addData('negative_distract_key_resp_3.rt', negative_distract_key_resp_3.rt)
thisExp.nextEntry()
# check responses
if negative_reappraise_key_resp_3.keys in ['', [], None]:  # No response was made
    negative_reappraise_key_resp_3.keys=None
thisExp.addData('negative_reappraise_key_resp_3.keys',negative_reappraise_key_resp_3.keys)
if negative_reappraise_key_resp_3.keys != None:  # we had a response
    thisExp.addData('negative_reappraise_key_resp_3.rt', negative_reappraise_key_resp_3.rt)
thisExp.nextEntry()

# ------Prepare to start Routine "Block_4"-------
t = 0
Block_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(119.000000)
# update component parameters for each repeat
neutral_view_Key_Response_4 = event.BuilderKeyResponse()
negative_view_Key_Resp_4 = event.BuilderKeyResponse()
negative_distract_key_resp_4 = event.BuilderKeyResponse()
negative_reappraise_key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
Block_4Components = [neutral_view_Plus_4, neutral_view_VIEW_4, neutral_view_Blank_4, neutral_view_Photo_4, neutral_view_Blank2_4, neutral_view_Response_4, neutral_view_Key_Response_4, neutral_view_Plus2_4, negative_view_Plus_4, negative_view_VIEW_4, negative_view_Blank_4, negative_view_image_4, negative_view_Blank2_4, negative_view_Response_4, negative_view_Key_Resp_4, negative_view_Plus2_4, negative_distract_plus_4, negative_distract_DISTRACT_4, negative_distract_Blank_4, negative_distract_Photo_4, negative_distract_Blank2_4, negative_distract_Response_4, negative_distract_key_resp_4, negative_distract_Plus2_4, negative_reappraise_Plus_4, negative_reappraise_REAPPRAISE_4, negative_reappraise_Blank_4, negative_reappraise_Photo_4, negative_reappraise_Blank2_4, negative_reappraise_Response_4, negative_reappraise_key_resp_4, negative_reappraise_Plus2_4]
for thisComponent in Block_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block_4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Block_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *neutral_view_Plus_4* updates
    if t >= 0.0 and neutral_view_Plus_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus_4.tStart = t
        neutral_view_Plus_4.frameNStart = frameN  # exact frame index
        neutral_view_Plus_4.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus_4.status == STARTED and t >= frameRemains:
        neutral_view_Plus_4.setAutoDraw(False)
    
    # *neutral_view_VIEW_4* updates
    if t >= 0.5 and neutral_view_VIEW_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_VIEW_4.tStart = t
        neutral_view_VIEW_4.frameNStart = frameN  # exact frame index
        neutral_view_VIEW_4.setAutoDraw(True)
    frameRemains = 0.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_VIEW_4.status == STARTED and t >= frameRemains:
        neutral_view_VIEW_4.setAutoDraw(False)
    
    # *neutral_view_Blank_4* updates
    if t >= 2.5 and neutral_view_Blank_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank_4.tStart = t
        neutral_view_Blank_4.frameNStart = frameN  # exact frame index
        neutral_view_Blank_4.setAutoDraw(True)
    frameRemains = 2.5 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank_4.status == STARTED and t >= frameRemains:
        neutral_view_Blank_4.setAutoDraw(False)
    
    # *neutral_view_Photo_4* updates
    if t >= 3 and neutral_view_Photo_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Photo_4.tStart = t
        neutral_view_Photo_4.frameNStart = frameN  # exact frame index
        neutral_view_Photo_4.setAutoDraw(True)
    frameRemains = 3 + 18- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Photo_4.status == STARTED and t >= frameRemains:
        neutral_view_Photo_4.setAutoDraw(False)
    
    # *neutral_view_Blank2_4* updates
    if t >= 21 and neutral_view_Blank2_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank2_4.tStart = t
        neutral_view_Blank2_4.frameNStart = frameN  # exact frame index
        neutral_view_Blank2_4.setAutoDraw(True)
    frameRemains = 21 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank2_4.status == STARTED and t >= frameRemains:
        neutral_view_Blank2_4.setAutoDraw(False)
    
    # *neutral_view_Response_4* updates
    if t >= 22 and neutral_view_Response_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Response_4.tStart = t
        neutral_view_Response_4.frameNStart = frameN  # exact frame index
        neutral_view_Response_4.setAutoDraw(True)
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Response_4.status == STARTED and t >= frameRemains:
        neutral_view_Response_4.setAutoDraw(False)
    
    # *neutral_view_Key_Response_4* updates
    if t >= 22 and neutral_view_Key_Response_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Key_Response_4.tStart = t
        neutral_view_Key_Response_4.frameNStart = frameN  # exact frame index
        neutral_view_Key_Response_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(neutral_view_Key_Response_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Key_Response_4.status == STARTED and t >= frameRemains:
        neutral_view_Key_Response_4.status = STOPPED
    if neutral_view_Key_Response_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            neutral_view_Key_Response_4.keys = theseKeys[-1]  # just the last key pressed
            neutral_view_Key_Response_4.rt = neutral_view_Key_Response_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *neutral_view_Plus2_4* updates
    if t >= 26 and neutral_view_Plus2_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus2_4.tStart = t
        neutral_view_Plus2_4.frameNStart = frameN  # exact frame index
        neutral_view_Plus2_4.setAutoDraw(True)
    frameRemains = 26 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus2_4.status == STARTED and t >= frameRemains:
        neutral_view_Plus2_4.setAutoDraw(False)
    
    # *negative_view_Plus_4* updates
    if t >= 34 and negative_view_Plus_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus_4.tStart = t
        negative_view_Plus_4.frameNStart = frameN  # exact frame index
        negative_view_Plus_4.setAutoDraw(True)
    frameRemains = 34 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus_4.status == STARTED and t >= frameRemains:
        negative_view_Plus_4.setAutoDraw(False)
    
    # *negative_view_VIEW_4* updates
    if t >= 34.5 and negative_view_VIEW_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_VIEW_4.tStart = t
        negative_view_VIEW_4.frameNStart = frameN  # exact frame index
        negative_view_VIEW_4.setAutoDraw(True)
    frameRemains = 34.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_VIEW_4.status == STARTED and t >= frameRemains:
        negative_view_VIEW_4.setAutoDraw(False)
    
    # *negative_view_Blank_4* updates
    if t >= 36.5 and negative_view_Blank_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank_4.tStart = t
        negative_view_Blank_4.frameNStart = frameN  # exact frame index
        negative_view_Blank_4.setAutoDraw(True)
    frameRemains = 36.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank_4.status == STARTED and t >= frameRemains:
        negative_view_Blank_4.setAutoDraw(False)
    
    # *negative_view_image_4* updates
    if t >= 37 and negative_view_image_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_image_4.tStart = t
        negative_view_image_4.frameNStart = frameN  # exact frame index
        negative_view_image_4.setAutoDraw(True)
    frameRemains = 37 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_image_4.status == STARTED and t >= frameRemains:
        negative_view_image_4.setAutoDraw(False)
    
    # *negative_view_Blank2_4* updates
    if t >= 52 and negative_view_Blank2_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank2_4.tStart = t
        negative_view_Blank2_4.frameNStart = frameN  # exact frame index
        negative_view_Blank2_4.setAutoDraw(True)
    frameRemains = 52 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank2_4.status == STARTED and t >= frameRemains:
        negative_view_Blank2_4.setAutoDraw(False)
    
    # *negative_view_Response_4* updates
    if t >= 53 and negative_view_Response_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Response_4.tStart = t
        negative_view_Response_4.frameNStart = frameN  # exact frame index
        negative_view_Response_4.setAutoDraw(True)
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Response_4.status == STARTED and t >= frameRemains:
        negative_view_Response_4.setAutoDraw(False)
    
    # *negative_view_Key_Resp_4* updates
    if t >= 53 and negative_view_Key_Resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Key_Resp_4.tStart = t
        negative_view_Key_Resp_4.frameNStart = frameN  # exact frame index
        negative_view_Key_Resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_view_Key_Resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Key_Resp_4.status == STARTED and t >= frameRemains:
        negative_view_Key_Resp_4.status = STOPPED
    if negative_view_Key_Resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_view_Key_Resp_4.keys = theseKeys[-1]  # just the last key pressed
            negative_view_Key_Resp_4.rt = negative_view_Key_Resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_view_Plus2_4* updates
    if t >= 57 and negative_view_Plus2_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus2_4.tStart = t
        negative_view_Plus2_4.frameNStart = frameN  # exact frame index
        negative_view_Plus2_4.setAutoDraw(True)
    frameRemains = 57 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus2_4.status == STARTED and t >= frameRemains:
        negative_view_Plus2_4.setAutoDraw(False)
    
    # *negative_distract_plus_4* updates
    if t >= 65 and negative_distract_plus_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_plus_4.tStart = t
        negative_distract_plus_4.frameNStart = frameN  # exact frame index
        negative_distract_plus_4.setAutoDraw(True)
    frameRemains = 65 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_plus_4.status == STARTED and t >= frameRemains:
        negative_distract_plus_4.setAutoDraw(False)
    
    # *negative_distract_DISTRACT_4* updates
    if t >= 65.5 and negative_distract_DISTRACT_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_DISTRACT_4.tStart = t
        negative_distract_DISTRACT_4.frameNStart = frameN  # exact frame index
        negative_distract_DISTRACT_4.setAutoDraw(True)
    frameRemains = 65.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_DISTRACT_4.status == STARTED and t >= frameRemains:
        negative_distract_DISTRACT_4.setAutoDraw(False)
    
    # *negative_distract_Blank_4* updates
    if t >= 67.5 and negative_distract_Blank_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank_4.tStart = t
        negative_distract_Blank_4.frameNStart = frameN  # exact frame index
        negative_distract_Blank_4.setAutoDraw(True)
    frameRemains = 67.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank_4.status == STARTED and t >= frameRemains:
        negative_distract_Blank_4.setAutoDraw(False)
    
    # *negative_distract_Photo_4* updates
    if t >= 68 and negative_distract_Photo_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Photo_4.tStart = t
        negative_distract_Photo_4.frameNStart = frameN  # exact frame index
        negative_distract_Photo_4.setAutoDraw(True)
    frameRemains = 68 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Photo_4.status == STARTED and t >= frameRemains:
        negative_distract_Photo_4.setAutoDraw(False)
    
    # *negative_distract_Blank2_4* updates
    if t >= 83 and negative_distract_Blank2_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank2_4.tStart = t
        negative_distract_Blank2_4.frameNStart = frameN  # exact frame index
        negative_distract_Blank2_4.setAutoDraw(True)
    frameRemains = 83 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank2_4.status == STARTED and t >= frameRemains:
        negative_distract_Blank2_4.setAutoDraw(False)
    
    # *negative_distract_Response_4* updates
    if t >= 84 and negative_distract_Response_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Response_4.tStart = t
        negative_distract_Response_4.frameNStart = frameN  # exact frame index
        negative_distract_Response_4.setAutoDraw(True)
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Response_4.status == STARTED and t >= frameRemains:
        negative_distract_Response_4.setAutoDraw(False)
    
    # *negative_distract_key_resp_4* updates
    if t >= 84 and negative_distract_key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_key_resp_4.tStart = t
        negative_distract_key_resp_4.frameNStart = frameN  # exact frame index
        negative_distract_key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_distract_key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_key_resp_4.status == STARTED and t >= frameRemains:
        negative_distract_key_resp_4.status = STOPPED
    if negative_distract_key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_distract_key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            negative_distract_key_resp_4.rt = negative_distract_key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_distract_Plus2_4* updates
    if t >= 88 and negative_distract_Plus2_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Plus2_4.tStart = t
        negative_distract_Plus2_4.frameNStart = frameN  # exact frame index
        negative_distract_Plus2_4.setAutoDraw(True)
    frameRemains = 88 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Plus2_4.status == STARTED and t >= frameRemains:
        negative_distract_Plus2_4.setAutoDraw(False)
    
    # *negative_reappraise_Plus_4* updates
    if t >= 92 and negative_reappraise_Plus_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus_4.tStart = t
        negative_reappraise_Plus_4.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus_4.setAutoDraw(True)
    frameRemains = 92 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus_4.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus_4.setAutoDraw(False)
    
    # *negative_reappraise_REAPPRAISE_4* updates
    if t >= 92.5 and negative_reappraise_REAPPRAISE_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_REAPPRAISE_4.tStart = t
        negative_reappraise_REAPPRAISE_4.frameNStart = frameN  # exact frame index
        negative_reappraise_REAPPRAISE_4.setAutoDraw(True)
    frameRemains = 92.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_REAPPRAISE_4.status == STARTED and t >= frameRemains:
        negative_reappraise_REAPPRAISE_4.setAutoDraw(False)
    
    # *negative_reappraise_Blank_4* updates
    if t >= 94.5 and negative_reappraise_Blank_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank_4.tStart = t
        negative_reappraise_Blank_4.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank_4.setAutoDraw(True)
    frameRemains = 94.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank_4.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank_4.setAutoDraw(False)
    
    # *negative_reappraise_Photo_4* updates
    if t >= 95 and negative_reappraise_Photo_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Photo_4.tStart = t
        negative_reappraise_Photo_4.frameNStart = frameN  # exact frame index
        negative_reappraise_Photo_4.setAutoDraw(True)
    frameRemains = 95 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Photo_4.status == STARTED and t >= frameRemains:
        negative_reappraise_Photo_4.setAutoDraw(False)
    
    # *negative_reappraise_Blank2_4* updates
    if t >= 110 and negative_reappraise_Blank2_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank2_4.tStart = t
        negative_reappraise_Blank2_4.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank2_4.setAutoDraw(True)
    frameRemains = 110 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank2_4.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank2_4.setAutoDraw(False)
    
    # *negative_reappraise_Response_4* updates
    if t >= 111 and negative_reappraise_Response_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Response_4.tStart = t
        negative_reappraise_Response_4.frameNStart = frameN  # exact frame index
        negative_reappraise_Response_4.setAutoDraw(True)
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Response_4.status == STARTED and t >= frameRemains:
        negative_reappraise_Response_4.setAutoDraw(False)
    
    # *negative_reappraise_key_resp_4* updates
    if t >= 111 and negative_reappraise_key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_key_resp_4.tStart = t
        negative_reappraise_key_resp_4.frameNStart = frameN  # exact frame index
        negative_reappraise_key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_reappraise_key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_key_resp_4.status == STARTED and t >= frameRemains:
        negative_reappraise_key_resp_4.status = STOPPED
    if negative_reappraise_key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_reappraise_key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            negative_reappraise_key_resp_4.rt = negative_reappraise_key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_reappraise_Plus2_4* updates
    if t >= 115 and negative_reappraise_Plus2_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus2_4.tStart = t
        negative_reappraise_Plus2_4.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus2_4.setAutoDraw(True)
    frameRemains = 115 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus2_4.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus2_4.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block_4"-------
for thisComponent in Block_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if neutral_view_Key_Response_4.keys in ['', [], None]:  # No response was made
    neutral_view_Key_Response_4.keys=None
thisExp.addData('neutral_view_Key_Response_4.keys',neutral_view_Key_Response_4.keys)
if neutral_view_Key_Response_4.keys != None:  # we had a response
    thisExp.addData('neutral_view_Key_Response_4.rt', neutral_view_Key_Response_4.rt)
thisExp.nextEntry()
# check responses
if negative_view_Key_Resp_4.keys in ['', [], None]:  # No response was made
    negative_view_Key_Resp_4.keys=None
thisExp.addData('negative_view_Key_Resp_4.keys',negative_view_Key_Resp_4.keys)
if negative_view_Key_Resp_4.keys != None:  # we had a response
    thisExp.addData('negative_view_Key_Resp_4.rt', negative_view_Key_Resp_4.rt)
thisExp.nextEntry()
# check responses
if negative_distract_key_resp_4.keys in ['', [], None]:  # No response was made
    negative_distract_key_resp_4.keys=None
thisExp.addData('negative_distract_key_resp_4.keys',negative_distract_key_resp_4.keys)
if negative_distract_key_resp_4.keys != None:  # we had a response
    thisExp.addData('negative_distract_key_resp_4.rt', negative_distract_key_resp_4.rt)
thisExp.nextEntry()
# check responses
if negative_reappraise_key_resp_4.keys in ['', [], None]:  # No response was made
    negative_reappraise_key_resp_4.keys=None
thisExp.addData('negative_reappraise_key_resp_4.keys',negative_reappraise_key_resp_4.keys)
if negative_reappraise_key_resp_4.keys != None:  # we had a response
    thisExp.addData('negative_reappraise_key_resp_4.rt', negative_reappraise_key_resp_4.rt)
thisExp.nextEntry()

# ------Prepare to start Routine "Block_5"-------
t = 0
Block_5Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(119.000000)
# update component parameters for each repeat
neutral_view_Key_Response_5 = event.BuilderKeyResponse()
negative_view_Key_Resp_5 = event.BuilderKeyResponse()
negative_distract_key_resp_5 = event.BuilderKeyResponse()
negative_reappraise_key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
Block_5Components = [neutral_view_Plus_5, neutral_view_VIEW_5, neutral_view_Blank_5, neutral_view_Photo_5, neutral_view_Blank2_5, neutral_view_Response_5, neutral_view_Key_Response_5, neutral_view_Plus2_5, negative_view_Plus_5, negative_view_VIEW_5, negative_view_Blank_5, negative_view_image_5, negative_view_Blank2_5, negative_view_Response_5, negative_view_Key_Resp_5, negative_view_Plus2_5, negative_distract_plus_5, negative_distract_DISTRACT_5, negative_distract_Blank_5, negative_distract_Photo_5, negative_distract_Blank2_5, negative_distract_Response_5, negative_distract_key_resp_5, negative_distract_Plus2_5, negative_reappraise_Plus_5, negative_reappraise_REAPPRAISE_5, negative_reappraise_Blank_5, negative_reappraise_Photo_5, negative_reappraise_Blank2_5, negative_reappraise_Response_5, negative_reappraise_key_resp_5, negative_reappraise_Plus2_5]
for thisComponent in Block_5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block_5"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Block_5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *neutral_view_Plus_5* updates
    if t >= 0.0 and neutral_view_Plus_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus_5.tStart = t
        neutral_view_Plus_5.frameNStart = frameN  # exact frame index
        neutral_view_Plus_5.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus_5.status == STARTED and t >= frameRemains:
        neutral_view_Plus_5.setAutoDraw(False)
    
    # *neutral_view_VIEW_5* updates
    if t >= 0.5 and neutral_view_VIEW_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_VIEW_5.tStart = t
        neutral_view_VIEW_5.frameNStart = frameN  # exact frame index
        neutral_view_VIEW_5.setAutoDraw(True)
    frameRemains = 0.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_VIEW_5.status == STARTED and t >= frameRemains:
        neutral_view_VIEW_5.setAutoDraw(False)
    
    # *neutral_view_Blank_5* updates
    if t >= 2.5 and neutral_view_Blank_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank_5.tStart = t
        neutral_view_Blank_5.frameNStart = frameN  # exact frame index
        neutral_view_Blank_5.setAutoDraw(True)
    frameRemains = 2.5 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank_5.status == STARTED and t >= frameRemains:
        neutral_view_Blank_5.setAutoDraw(False)
    
    # *neutral_view_Photo_5* updates
    if t >= 3 and neutral_view_Photo_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Photo_5.tStart = t
        neutral_view_Photo_5.frameNStart = frameN  # exact frame index
        neutral_view_Photo_5.setAutoDraw(True)
    frameRemains = 3 + 18- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Photo_5.status == STARTED and t >= frameRemains:
        neutral_view_Photo_5.setAutoDraw(False)
    
    # *neutral_view_Blank2_5* updates
    if t >= 21 and neutral_view_Blank2_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank2_5.tStart = t
        neutral_view_Blank2_5.frameNStart = frameN  # exact frame index
        neutral_view_Blank2_5.setAutoDraw(True)
    frameRemains = 21 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank2_5.status == STARTED and t >= frameRemains:
        neutral_view_Blank2_5.setAutoDraw(False)
    
    # *neutral_view_Response_5* updates
    if t >= 22 and neutral_view_Response_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Response_5.tStart = t
        neutral_view_Response_5.frameNStart = frameN  # exact frame index
        neutral_view_Response_5.setAutoDraw(True)
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Response_5.status == STARTED and t >= frameRemains:
        neutral_view_Response_5.setAutoDraw(False)
    
    # *neutral_view_Key_Response_5* updates
    if t >= 22 and neutral_view_Key_Response_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Key_Response_5.tStart = t
        neutral_view_Key_Response_5.frameNStart = frameN  # exact frame index
        neutral_view_Key_Response_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(neutral_view_Key_Response_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Key_Response_5.status == STARTED and t >= frameRemains:
        neutral_view_Key_Response_5.status = STOPPED
    if neutral_view_Key_Response_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            neutral_view_Key_Response_5.keys = theseKeys[-1]  # just the last key pressed
            neutral_view_Key_Response_5.rt = neutral_view_Key_Response_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *neutral_view_Plus2_5* updates
    if t >= 26 and neutral_view_Plus2_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus2_5.tStart = t
        neutral_view_Plus2_5.frameNStart = frameN  # exact frame index
        neutral_view_Plus2_5.setAutoDraw(True)
    frameRemains = 26 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus2_5.status == STARTED and t >= frameRemains:
        neutral_view_Plus2_5.setAutoDraw(False)
    
    # *negative_view_Plus_5* updates
    if t >= 34 and negative_view_Plus_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus_5.tStart = t
        negative_view_Plus_5.frameNStart = frameN  # exact frame index
        negative_view_Plus_5.setAutoDraw(True)
    frameRemains = 34 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus_5.status == STARTED and t >= frameRemains:
        negative_view_Plus_5.setAutoDraw(False)
    
    # *negative_view_VIEW_5* updates
    if t >= 34.5 and negative_view_VIEW_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_VIEW_5.tStart = t
        negative_view_VIEW_5.frameNStart = frameN  # exact frame index
        negative_view_VIEW_5.setAutoDraw(True)
    frameRemains = 34.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_VIEW_5.status == STARTED and t >= frameRemains:
        negative_view_VIEW_5.setAutoDraw(False)
    
    # *negative_view_Blank_5* updates
    if t >= 36.5 and negative_view_Blank_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank_5.tStart = t
        negative_view_Blank_5.frameNStart = frameN  # exact frame index
        negative_view_Blank_5.setAutoDraw(True)
    frameRemains = 36.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank_5.status == STARTED and t >= frameRemains:
        negative_view_Blank_5.setAutoDraw(False)
    
    # *negative_view_image_5* updates
    if t >= 37 and negative_view_image_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_image_5.tStart = t
        negative_view_image_5.frameNStart = frameN  # exact frame index
        negative_view_image_5.setAutoDraw(True)
    frameRemains = 37 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_image_5.status == STARTED and t >= frameRemains:
        negative_view_image_5.setAutoDraw(False)
    
    # *negative_view_Blank2_5* updates
    if t >= 52 and negative_view_Blank2_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank2_5.tStart = t
        negative_view_Blank2_5.frameNStart = frameN  # exact frame index
        negative_view_Blank2_5.setAutoDraw(True)
    frameRemains = 52 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank2_5.status == STARTED and t >= frameRemains:
        negative_view_Blank2_5.setAutoDraw(False)
    
    # *negative_view_Response_5* updates
    if t >= 53 and negative_view_Response_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Response_5.tStart = t
        negative_view_Response_5.frameNStart = frameN  # exact frame index
        negative_view_Response_5.setAutoDraw(True)
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Response_5.status == STARTED and t >= frameRemains:
        negative_view_Response_5.setAutoDraw(False)
    
    # *negative_view_Key_Resp_5* updates
    if t >= 53 and negative_view_Key_Resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Key_Resp_5.tStart = t
        negative_view_Key_Resp_5.frameNStart = frameN  # exact frame index
        negative_view_Key_Resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_view_Key_Resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Key_Resp_5.status == STARTED and t >= frameRemains:
        negative_view_Key_Resp_5.status = STOPPED
    if negative_view_Key_Resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_view_Key_Resp_5.keys = theseKeys[-1]  # just the last key pressed
            negative_view_Key_Resp_5.rt = negative_view_Key_Resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_view_Plus2_5* updates
    if t >= 57 and negative_view_Plus2_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus2_5.tStart = t
        negative_view_Plus2_5.frameNStart = frameN  # exact frame index
        negative_view_Plus2_5.setAutoDraw(True)
    frameRemains = 57 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus2_5.status == STARTED and t >= frameRemains:
        negative_view_Plus2_5.setAutoDraw(False)
    
    # *negative_distract_plus_5* updates
    if t >= 65 and negative_distract_plus_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_plus_5.tStart = t
        negative_distract_plus_5.frameNStart = frameN  # exact frame index
        negative_distract_plus_5.setAutoDraw(True)
    frameRemains = 65 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_plus_5.status == STARTED and t >= frameRemains:
        negative_distract_plus_5.setAutoDraw(False)
    
    # *negative_distract_DISTRACT_5* updates
    if t >= 65.5 and negative_distract_DISTRACT_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_DISTRACT_5.tStart = t
        negative_distract_DISTRACT_5.frameNStart = frameN  # exact frame index
        negative_distract_DISTRACT_5.setAutoDraw(True)
    frameRemains = 65.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_DISTRACT_5.status == STARTED and t >= frameRemains:
        negative_distract_DISTRACT_5.setAutoDraw(False)
    
    # *negative_distract_Blank_5* updates
    if t >= 67.5 and negative_distract_Blank_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank_5.tStart = t
        negative_distract_Blank_5.frameNStart = frameN  # exact frame index
        negative_distract_Blank_5.setAutoDraw(True)
    frameRemains = 67.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank_5.status == STARTED and t >= frameRemains:
        negative_distract_Blank_5.setAutoDraw(False)
    
    # *negative_distract_Photo_5* updates
    if t >= 68 and negative_distract_Photo_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Photo_5.tStart = t
        negative_distract_Photo_5.frameNStart = frameN  # exact frame index
        negative_distract_Photo_5.setAutoDraw(True)
    frameRemains = 68 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Photo_5.status == STARTED and t >= frameRemains:
        negative_distract_Photo_5.setAutoDraw(False)
    
    # *negative_distract_Blank2_5* updates
    if t >= 83 and negative_distract_Blank2_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank2_5.tStart = t
        negative_distract_Blank2_5.frameNStart = frameN  # exact frame index
        negative_distract_Blank2_5.setAutoDraw(True)
    frameRemains = 83 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank2_5.status == STARTED and t >= frameRemains:
        negative_distract_Blank2_5.setAutoDraw(False)
    
    # *negative_distract_Response_5* updates
    if t >= 84 and negative_distract_Response_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Response_5.tStart = t
        negative_distract_Response_5.frameNStart = frameN  # exact frame index
        negative_distract_Response_5.setAutoDraw(True)
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Response_5.status == STARTED and t >= frameRemains:
        negative_distract_Response_5.setAutoDraw(False)
    
    # *negative_distract_key_resp_5* updates
    if t >= 84 and negative_distract_key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_key_resp_5.tStart = t
        negative_distract_key_resp_5.frameNStart = frameN  # exact frame index
        negative_distract_key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_distract_key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_key_resp_5.status == STARTED and t >= frameRemains:
        negative_distract_key_resp_5.status = STOPPED
    if negative_distract_key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_distract_key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            negative_distract_key_resp_5.rt = negative_distract_key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_distract_Plus2_5* updates
    if t >= 88 and negative_distract_Plus2_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Plus2_5.tStart = t
        negative_distract_Plus2_5.frameNStart = frameN  # exact frame index
        negative_distract_Plus2_5.setAutoDraw(True)
    frameRemains = 88 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Plus2_5.status == STARTED and t >= frameRemains:
        negative_distract_Plus2_5.setAutoDraw(False)
    
    # *negative_reappraise_Plus_5* updates
    if t >= 92 and negative_reappraise_Plus_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus_5.tStart = t
        negative_reappraise_Plus_5.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus_5.setAutoDraw(True)
    frameRemains = 92 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus_5.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus_5.setAutoDraw(False)
    
    # *negative_reappraise_REAPPRAISE_5* updates
    if t >= 92.5 and negative_reappraise_REAPPRAISE_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_REAPPRAISE_5.tStart = t
        negative_reappraise_REAPPRAISE_5.frameNStart = frameN  # exact frame index
        negative_reappraise_REAPPRAISE_5.setAutoDraw(True)
    frameRemains = 92.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_REAPPRAISE_5.status == STARTED and t >= frameRemains:
        negative_reappraise_REAPPRAISE_5.setAutoDraw(False)
    
    # *negative_reappraise_Blank_5* updates
    if t >= 94.5 and negative_reappraise_Blank_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank_5.tStart = t
        negative_reappraise_Blank_5.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank_5.setAutoDraw(True)
    frameRemains = 94.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank_5.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank_5.setAutoDraw(False)
    
    # *negative_reappraise_Photo_5* updates
    if t >= 95 and negative_reappraise_Photo_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Photo_5.tStart = t
        negative_reappraise_Photo_5.frameNStart = frameN  # exact frame index
        negative_reappraise_Photo_5.setAutoDraw(True)
    frameRemains = 95 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Photo_5.status == STARTED and t >= frameRemains:
        negative_reappraise_Photo_5.setAutoDraw(False)
    
    # *negative_reappraise_Blank2_5* updates
    if t >= 110 and negative_reappraise_Blank2_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank2_5.tStart = t
        negative_reappraise_Blank2_5.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank2_5.setAutoDraw(True)
    frameRemains = 110 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank2_5.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank2_5.setAutoDraw(False)
    
    # *negative_reappraise_Response_5* updates
    if t >= 111 and negative_reappraise_Response_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Response_5.tStart = t
        negative_reappraise_Response_5.frameNStart = frameN  # exact frame index
        negative_reappraise_Response_5.setAutoDraw(True)
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Response_5.status == STARTED and t >= frameRemains:
        negative_reappraise_Response_5.setAutoDraw(False)
    
    # *negative_reappraise_key_resp_5* updates
    if t >= 111 and negative_reappraise_key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_key_resp_5.tStart = t
        negative_reappraise_key_resp_5.frameNStart = frameN  # exact frame index
        negative_reappraise_key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_reappraise_key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_key_resp_5.status == STARTED and t >= frameRemains:
        negative_reappraise_key_resp_5.status = STOPPED
    if negative_reappraise_key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_reappraise_key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            negative_reappraise_key_resp_5.rt = negative_reappraise_key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_reappraise_Plus2_5* updates
    if t >= 115 and negative_reappraise_Plus2_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus2_5.tStart = t
        negative_reappraise_Plus2_5.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus2_5.setAutoDraw(True)
    frameRemains = 115 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus2_5.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus2_5.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block_5"-------
for thisComponent in Block_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if neutral_view_Key_Response_5.keys in ['', [], None]:  # No response was made
    neutral_view_Key_Response_5.keys=None
thisExp.addData('neutral_view_Key_Response_5.keys',neutral_view_Key_Response_5.keys)
if neutral_view_Key_Response_5.keys != None:  # we had a response
    thisExp.addData('neutral_view_Key_Response_5.rt', neutral_view_Key_Response_5.rt)
thisExp.nextEntry()
# check responses
if negative_view_Key_Resp_5.keys in ['', [], None]:  # No response was made
    negative_view_Key_Resp_5.keys=None
thisExp.addData('negative_view_Key_Resp_5.keys',negative_view_Key_Resp_5.keys)
if negative_view_Key_Resp_5.keys != None:  # we had a response
    thisExp.addData('negative_view_Key_Resp_5.rt', negative_view_Key_Resp_5.rt)
thisExp.nextEntry()
# check responses
if negative_distract_key_resp_5.keys in ['', [], None]:  # No response was made
    negative_distract_key_resp_5.keys=None
thisExp.addData('negative_distract_key_resp_5.keys',negative_distract_key_resp_5.keys)
if negative_distract_key_resp_5.keys != None:  # we had a response
    thisExp.addData('negative_distract_key_resp_5.rt', negative_distract_key_resp_5.rt)
thisExp.nextEntry()
# check responses
if negative_reappraise_key_resp_5.keys in ['', [], None]:  # No response was made
    negative_reappraise_key_resp_5.keys=None
thisExp.addData('negative_reappraise_key_resp_5.keys',negative_reappraise_key_resp_5.keys)
if negative_reappraise_key_resp_5.keys != None:  # we had a response
    thisExp.addData('negative_reappraise_key_resp_5.rt', negative_reappraise_key_resp_5.rt)
thisExp.nextEntry()

# ------Prepare to start Routine "Block_6"-------
t = 0
Block_6Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(119.000000)
# update component parameters for each repeat
neutral_view_Key_Response_6 = event.BuilderKeyResponse()
negative_view_Key_Resp_6 = event.BuilderKeyResponse()
negative_distract_key_resp_6 = event.BuilderKeyResponse()
negative_reappraise_key_resp_6 = event.BuilderKeyResponse()
# keep track of which components have finished
Block_6Components = [neutral_view_Plus_6, neutral_view_VIEW_6, neutral_view_Blank_6, neutral_view_Photo_6, neutral_view_Blank2_6, neutral_view_Response_6, neutral_view_Key_Response_6, neutral_view_Plus2_6, negative_view_Plus_6, negative_view_VIEW_6, negative_view_Blank_6, negative_view_image_6, negative_view_Blank2_6, negative_view_Response_6, negative_view_Key_Resp_6, negative_view_Plus2_6, negative_distract_plus_6, negative_distract_DISTRACT_6, negative_distract_Blank_6, negative_distract_Photo_6, negative_distract_Blank2_6, negative_distract_Response_6, negative_distract_key_resp_6, negative_distract_Plus2_6, negative_reappraise_Plus_6, negative_reappraise_REAPPRAISE_6, negative_reappraise_Blank_6, negative_reappraise_Photo_6, negative_reappraise_Blank2_6, negative_reappraise_Response_6, negative_reappraise_key_resp_6, negative_reappraise_Plus2_6]
for thisComponent in Block_6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block_6"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Block_6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *neutral_view_Plus_6* updates
    if t >= 0.0 and neutral_view_Plus_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus_6.tStart = t
        neutral_view_Plus_6.frameNStart = frameN  # exact frame index
        neutral_view_Plus_6.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus_6.status == STARTED and t >= frameRemains:
        neutral_view_Plus_6.setAutoDraw(False)
    
    # *neutral_view_VIEW_6* updates
    if t >= 0.5 and neutral_view_VIEW_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_VIEW_6.tStart = t
        neutral_view_VIEW_6.frameNStart = frameN  # exact frame index
        neutral_view_VIEW_6.setAutoDraw(True)
    frameRemains = 0.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_VIEW_6.status == STARTED and t >= frameRemains:
        neutral_view_VIEW_6.setAutoDraw(False)
    
    # *neutral_view_Blank_6* updates
    if t >= 2.5 and neutral_view_Blank_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank_6.tStart = t
        neutral_view_Blank_6.frameNStart = frameN  # exact frame index
        neutral_view_Blank_6.setAutoDraw(True)
    frameRemains = 2.5 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank_6.status == STARTED and t >= frameRemains:
        neutral_view_Blank_6.setAutoDraw(False)
    
    # *neutral_view_Photo_6* updates
    if t >= 3 and neutral_view_Photo_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Photo_6.tStart = t
        neutral_view_Photo_6.frameNStart = frameN  # exact frame index
        neutral_view_Photo_6.setAutoDraw(True)
    frameRemains = 3 + 18- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Photo_6.status == STARTED and t >= frameRemains:
        neutral_view_Photo_6.setAutoDraw(False)
    
    # *neutral_view_Blank2_6* updates
    if t >= 21 and neutral_view_Blank2_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank2_6.tStart = t
        neutral_view_Blank2_6.frameNStart = frameN  # exact frame index
        neutral_view_Blank2_6.setAutoDraw(True)
    frameRemains = 21 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank2_6.status == STARTED and t >= frameRemains:
        neutral_view_Blank2_6.setAutoDraw(False)
    
    # *neutral_view_Response_6* updates
    if t >= 22 and neutral_view_Response_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Response_6.tStart = t
        neutral_view_Response_6.frameNStart = frameN  # exact frame index
        neutral_view_Response_6.setAutoDraw(True)
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Response_6.status == STARTED and t >= frameRemains:
        neutral_view_Response_6.setAutoDraw(False)
    
    # *neutral_view_Key_Response_6* updates
    if t >= 22 and neutral_view_Key_Response_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Key_Response_6.tStart = t
        neutral_view_Key_Response_6.frameNStart = frameN  # exact frame index
        neutral_view_Key_Response_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(neutral_view_Key_Response_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Key_Response_6.status == STARTED and t >= frameRemains:
        neutral_view_Key_Response_6.status = STOPPED
    if neutral_view_Key_Response_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            neutral_view_Key_Response_6.keys = theseKeys[-1]  # just the last key pressed
            neutral_view_Key_Response_6.rt = neutral_view_Key_Response_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *neutral_view_Plus2_6* updates
    if t >= 26 and neutral_view_Plus2_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus2_6.tStart = t
        neutral_view_Plus2_6.frameNStart = frameN  # exact frame index
        neutral_view_Plus2_6.setAutoDraw(True)
    frameRemains = 26 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus2_6.status == STARTED and t >= frameRemains:
        neutral_view_Plus2_6.setAutoDraw(False)
    
    # *negative_view_Plus_6* updates
    if t >= 34 and negative_view_Plus_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus_6.tStart = t
        negative_view_Plus_6.frameNStart = frameN  # exact frame index
        negative_view_Plus_6.setAutoDraw(True)
    frameRemains = 34 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus_6.status == STARTED and t >= frameRemains:
        negative_view_Plus_6.setAutoDraw(False)
    
    # *negative_view_VIEW_6* updates
    if t >= 34.5 and negative_view_VIEW_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_VIEW_6.tStart = t
        negative_view_VIEW_6.frameNStart = frameN  # exact frame index
        negative_view_VIEW_6.setAutoDraw(True)
    frameRemains = 34.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_VIEW_6.status == STARTED and t >= frameRemains:
        negative_view_VIEW_6.setAutoDraw(False)
    
    # *negative_view_Blank_6* updates
    if t >= 36.5 and negative_view_Blank_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank_6.tStart = t
        negative_view_Blank_6.frameNStart = frameN  # exact frame index
        negative_view_Blank_6.setAutoDraw(True)
    frameRemains = 36.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank_6.status == STARTED and t >= frameRemains:
        negative_view_Blank_6.setAutoDraw(False)
    
    # *negative_view_image_6* updates
    if t >= 37 and negative_view_image_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_image_6.tStart = t
        negative_view_image_6.frameNStart = frameN  # exact frame index
        negative_view_image_6.setAutoDraw(True)
    frameRemains = 37 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_image_6.status == STARTED and t >= frameRemains:
        negative_view_image_6.setAutoDraw(False)
    
    # *negative_view_Blank2_6* updates
    if t >= 52 and negative_view_Blank2_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank2_6.tStart = t
        negative_view_Blank2_6.frameNStart = frameN  # exact frame index
        negative_view_Blank2_6.setAutoDraw(True)
    frameRemains = 52 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank2_6.status == STARTED and t >= frameRemains:
        negative_view_Blank2_6.setAutoDraw(False)
    
    # *negative_view_Response_6* updates
    if t >= 53 and negative_view_Response_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Response_6.tStart = t
        negative_view_Response_6.frameNStart = frameN  # exact frame index
        negative_view_Response_6.setAutoDraw(True)
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Response_6.status == STARTED and t >= frameRemains:
        negative_view_Response_6.setAutoDraw(False)
    
    # *negative_view_Key_Resp_6* updates
    if t >= 53 and negative_view_Key_Resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Key_Resp_6.tStart = t
        negative_view_Key_Resp_6.frameNStart = frameN  # exact frame index
        negative_view_Key_Resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_view_Key_Resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Key_Resp_6.status == STARTED and t >= frameRemains:
        negative_view_Key_Resp_6.status = STOPPED
    if negative_view_Key_Resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_view_Key_Resp_6.keys = theseKeys[-1]  # just the last key pressed
            negative_view_Key_Resp_6.rt = negative_view_Key_Resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_view_Plus2_6* updates
    if t >= 57 and negative_view_Plus2_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus2_6.tStart = t
        negative_view_Plus2_6.frameNStart = frameN  # exact frame index
        negative_view_Plus2_6.setAutoDraw(True)
    frameRemains = 57 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus2_6.status == STARTED and t >= frameRemains:
        negative_view_Plus2_6.setAutoDraw(False)
    
    # *negative_distract_plus_6* updates
    if t >= 65 and negative_distract_plus_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_plus_6.tStart = t
        negative_distract_plus_6.frameNStart = frameN  # exact frame index
        negative_distract_plus_6.setAutoDraw(True)
    frameRemains = 65 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_plus_6.status == STARTED and t >= frameRemains:
        negative_distract_plus_6.setAutoDraw(False)
    
    # *negative_distract_DISTRACT_6* updates
    if t >= 65.5 and negative_distract_DISTRACT_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_DISTRACT_6.tStart = t
        negative_distract_DISTRACT_6.frameNStart = frameN  # exact frame index
        negative_distract_DISTRACT_6.setAutoDraw(True)
    frameRemains = 65.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_DISTRACT_6.status == STARTED and t >= frameRemains:
        negative_distract_DISTRACT_6.setAutoDraw(False)
    
    # *negative_distract_Blank_6* updates
    if t >= 67.5 and negative_distract_Blank_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank_6.tStart = t
        negative_distract_Blank_6.frameNStart = frameN  # exact frame index
        negative_distract_Blank_6.setAutoDraw(True)
    frameRemains = 67.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank_6.status == STARTED and t >= frameRemains:
        negative_distract_Blank_6.setAutoDraw(False)
    
    # *negative_distract_Photo_6* updates
    if t >= 68 and negative_distract_Photo_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Photo_6.tStart = t
        negative_distract_Photo_6.frameNStart = frameN  # exact frame index
        negative_distract_Photo_6.setAutoDraw(True)
    frameRemains = 68 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Photo_6.status == STARTED and t >= frameRemains:
        negative_distract_Photo_6.setAutoDraw(False)
    
    # *negative_distract_Blank2_6* updates
    if t >= 83 and negative_distract_Blank2_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank2_6.tStart = t
        negative_distract_Blank2_6.frameNStart = frameN  # exact frame index
        negative_distract_Blank2_6.setAutoDraw(True)
    frameRemains = 83 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank2_6.status == STARTED and t >= frameRemains:
        negative_distract_Blank2_6.setAutoDraw(False)
    
    # *negative_distract_Response_6* updates
    if t >= 84 and negative_distract_Response_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Response_6.tStart = t
        negative_distract_Response_6.frameNStart = frameN  # exact frame index
        negative_distract_Response_6.setAutoDraw(True)
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Response_6.status == STARTED and t >= frameRemains:
        negative_distract_Response_6.setAutoDraw(False)
    
    # *negative_distract_key_resp_6* updates
    if t >= 84 and negative_distract_key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_key_resp_6.tStart = t
        negative_distract_key_resp_6.frameNStart = frameN  # exact frame index
        negative_distract_key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_distract_key_resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_key_resp_6.status == STARTED and t >= frameRemains:
        negative_distract_key_resp_6.status = STOPPED
    if negative_distract_key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_distract_key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            negative_distract_key_resp_6.rt = negative_distract_key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_distract_Plus2_6* updates
    if t >= 88 and negative_distract_Plus2_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Plus2_6.tStart = t
        negative_distract_Plus2_6.frameNStart = frameN  # exact frame index
        negative_distract_Plus2_6.setAutoDraw(True)
    frameRemains = 88 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Plus2_6.status == STARTED and t >= frameRemains:
        negative_distract_Plus2_6.setAutoDraw(False)
    
    # *negative_reappraise_Plus_6* updates
    if t >= 92 and negative_reappraise_Plus_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus_6.tStart = t
        negative_reappraise_Plus_6.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus_6.setAutoDraw(True)
    frameRemains = 92 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus_6.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus_6.setAutoDraw(False)
    
    # *negative_reappraise_REAPPRAISE_6* updates
    if t >= 92.5 and negative_reappraise_REAPPRAISE_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_REAPPRAISE_6.tStart = t
        negative_reappraise_REAPPRAISE_6.frameNStart = frameN  # exact frame index
        negative_reappraise_REAPPRAISE_6.setAutoDraw(True)
    frameRemains = 92.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_REAPPRAISE_6.status == STARTED and t >= frameRemains:
        negative_reappraise_REAPPRAISE_6.setAutoDraw(False)
    
    # *negative_reappraise_Blank_6* updates
    if t >= 94.5 and negative_reappraise_Blank_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank_6.tStart = t
        negative_reappraise_Blank_6.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank_6.setAutoDraw(True)
    frameRemains = 94.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank_6.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank_6.setAutoDraw(False)
    
    # *negative_reappraise_Photo_6* updates
    if t >= 95 and negative_reappraise_Photo_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Photo_6.tStart = t
        negative_reappraise_Photo_6.frameNStart = frameN  # exact frame index
        negative_reappraise_Photo_6.setAutoDraw(True)
    frameRemains = 95 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Photo_6.status == STARTED and t >= frameRemains:
        negative_reappraise_Photo_6.setAutoDraw(False)
    
    # *negative_reappraise_Blank2_6* updates
    if t >= 110 and negative_reappraise_Blank2_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank2_6.tStart = t
        negative_reappraise_Blank2_6.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank2_6.setAutoDraw(True)
    frameRemains = 110 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank2_6.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank2_6.setAutoDraw(False)
    
    # *negative_reappraise_Response_6* updates
    if t >= 111 and negative_reappraise_Response_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Response_6.tStart = t
        negative_reappraise_Response_6.frameNStart = frameN  # exact frame index
        negative_reappraise_Response_6.setAutoDraw(True)
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Response_6.status == STARTED and t >= frameRemains:
        negative_reappraise_Response_6.setAutoDraw(False)
    
    # *negative_reappraise_key_resp_6* updates
    if t >= 111 and negative_reappraise_key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_key_resp_6.tStart = t
        negative_reappraise_key_resp_6.frameNStart = frameN  # exact frame index
        negative_reappraise_key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_reappraise_key_resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_key_resp_6.status == STARTED and t >= frameRemains:
        negative_reappraise_key_resp_6.status = STOPPED
    if negative_reappraise_key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_reappraise_key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            negative_reappraise_key_resp_6.rt = negative_reappraise_key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_reappraise_Plus2_6* updates
    if t >= 115 and negative_reappraise_Plus2_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus2_6.tStart = t
        negative_reappraise_Plus2_6.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus2_6.setAutoDraw(True)
    frameRemains = 115 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus2_6.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus2_6.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block_6"-------
for thisComponent in Block_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if neutral_view_Key_Response_6.keys in ['', [], None]:  # No response was made
    neutral_view_Key_Response_6.keys=None
thisExp.addData('neutral_view_Key_Response_6.keys',neutral_view_Key_Response_6.keys)
if neutral_view_Key_Response_6.keys != None:  # we had a response
    thisExp.addData('neutral_view_Key_Response_6.rt', neutral_view_Key_Response_6.rt)
thisExp.nextEntry()
# check responses
if negative_view_Key_Resp_6.keys in ['', [], None]:  # No response was made
    negative_view_Key_Resp_6.keys=None
thisExp.addData('negative_view_Key_Resp_6.keys',negative_view_Key_Resp_6.keys)
if negative_view_Key_Resp_6.keys != None:  # we had a response
    thisExp.addData('negative_view_Key_Resp_6.rt', negative_view_Key_Resp_6.rt)
thisExp.nextEntry()
# check responses
if negative_distract_key_resp_6.keys in ['', [], None]:  # No response was made
    negative_distract_key_resp_6.keys=None
thisExp.addData('negative_distract_key_resp_6.keys',negative_distract_key_resp_6.keys)
if negative_distract_key_resp_6.keys != None:  # we had a response
    thisExp.addData('negative_distract_key_resp_6.rt', negative_distract_key_resp_6.rt)
thisExp.nextEntry()
# check responses
if negative_reappraise_key_resp_6.keys in ['', [], None]:  # No response was made
    negative_reappraise_key_resp_6.keys=None
thisExp.addData('negative_reappraise_key_resp_6.keys',negative_reappraise_key_resp_6.keys)
if negative_reappraise_key_resp_6.keys != None:  # we had a response
    thisExp.addData('negative_reappraise_key_resp_6.rt', negative_reappraise_key_resp_6.rt)
thisExp.nextEntry()

# ------Prepare to start Routine "Block_7"-------
t = 0
Block_7Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(119.000000)
# update component parameters for each repeat
neutral_view_Key_Response_7 = event.BuilderKeyResponse()
negative_view_Key_Resp_7 = event.BuilderKeyResponse()
negative_distract_key_resp_7 = event.BuilderKeyResponse()
negative_reappraise_key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
Block_7Components = [neutral_view_Plus_7, neutral_view_VIEW_7, neutral_view_Blank_7, neutral_view_Photo_7, neutral_view_Blank2_7, neutral_view_Response_7, neutral_view_Key_Response_7, neutral_view_Plus2_7, negative_view_Plus_7, negative_view_VIEW_7, negative_view_Blank_7, negative_view_image_7, negative_view_Blank2_7, negative_view_Response_7, negative_view_Key_Resp_7, negative_view_Plus2_7, negative_distract_plus_7, negative_distract_DISTRACT_7, negative_distract_Blank_7, negative_distract_Photo_7, negative_distract_Blank2_7, negative_distract_Response_7, negative_distract_key_resp_7, negative_distract_Plus2_7, negative_reappraise_Plus_7, negative_reappraise_REAPPRAISE_7, negative_reappraise_Blank_7, negative_reappraise_Photo_7, negative_reappraise_Blank2_7, negative_reappraise_Response_7, negative_reappraise_key_resp_7, negative_reappraise_Plus2_7]
for thisComponent in Block_7Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Block_7"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Block_7Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *neutral_view_Plus_7* updates
    if t >= 0.0 and neutral_view_Plus_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus_7.tStart = t
        neutral_view_Plus_7.frameNStart = frameN  # exact frame index
        neutral_view_Plus_7.setAutoDraw(True)
    frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus_7.status == STARTED and t >= frameRemains:
        neutral_view_Plus_7.setAutoDraw(False)
    
    # *neutral_view_VIEW_7* updates
    if t >= 0.5 and neutral_view_VIEW_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_VIEW_7.tStart = t
        neutral_view_VIEW_7.frameNStart = frameN  # exact frame index
        neutral_view_VIEW_7.setAutoDraw(True)
    frameRemains = 0.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_VIEW_7.status == STARTED and t >= frameRemains:
        neutral_view_VIEW_7.setAutoDraw(False)
    
    # *neutral_view_Blank_7* updates
    if t >= 2.5 and neutral_view_Blank_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank_7.tStart = t
        neutral_view_Blank_7.frameNStart = frameN  # exact frame index
        neutral_view_Blank_7.setAutoDraw(True)
    frameRemains = 2.5 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank_7.status == STARTED and t >= frameRemains:
        neutral_view_Blank_7.setAutoDraw(False)
    
    # *neutral_view_Photo_7* updates
    if t >= 3 and neutral_view_Photo_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Photo_7.tStart = t
        neutral_view_Photo_7.frameNStart = frameN  # exact frame index
        neutral_view_Photo_7.setAutoDraw(True)
    frameRemains = 3 + 18- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Photo_7.status == STARTED and t >= frameRemains:
        neutral_view_Photo_7.setAutoDraw(False)
    
    # *neutral_view_Blank2_7* updates
    if t >= 21 and neutral_view_Blank2_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Blank2_7.tStart = t
        neutral_view_Blank2_7.frameNStart = frameN  # exact frame index
        neutral_view_Blank2_7.setAutoDraw(True)
    frameRemains = 21 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Blank2_7.status == STARTED and t >= frameRemains:
        neutral_view_Blank2_7.setAutoDraw(False)
    
    # *neutral_view_Response_7* updates
    if t >= 22 and neutral_view_Response_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Response_7.tStart = t
        neutral_view_Response_7.frameNStart = frameN  # exact frame index
        neutral_view_Response_7.setAutoDraw(True)
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Response_7.status == STARTED and t >= frameRemains:
        neutral_view_Response_7.setAutoDraw(False)
    
    # *neutral_view_Key_Response_7* updates
    if t >= 22 and neutral_view_Key_Response_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Key_Response_7.tStart = t
        neutral_view_Key_Response_7.frameNStart = frameN  # exact frame index
        neutral_view_Key_Response_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(neutral_view_Key_Response_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 22 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Key_Response_7.status == STARTED and t >= frameRemains:
        neutral_view_Key_Response_7.status = STOPPED
    if neutral_view_Key_Response_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            neutral_view_Key_Response_7.keys = theseKeys[-1]  # just the last key pressed
            neutral_view_Key_Response_7.rt = neutral_view_Key_Response_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *neutral_view_Plus2_7* updates
    if t >= 26 and neutral_view_Plus2_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        neutral_view_Plus2_7.tStart = t
        neutral_view_Plus2_7.frameNStart = frameN  # exact frame index
        neutral_view_Plus2_7.setAutoDraw(True)
    frameRemains = 26 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if neutral_view_Plus2_7.status == STARTED and t >= frameRemains:
        neutral_view_Plus2_7.setAutoDraw(False)
    
    # *negative_view_Plus_7* updates
    if t >= 34 and negative_view_Plus_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus_7.tStart = t
        negative_view_Plus_7.frameNStart = frameN  # exact frame index
        negative_view_Plus_7.setAutoDraw(True)
    frameRemains = 34 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus_7.status == STARTED and t >= frameRemains:
        negative_view_Plus_7.setAutoDraw(False)
    
    # *negative_view_VIEW_7* updates
    if t >= 34.5 and negative_view_VIEW_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_VIEW_7.tStart = t
        negative_view_VIEW_7.frameNStart = frameN  # exact frame index
        negative_view_VIEW_7.setAutoDraw(True)
    frameRemains = 34.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_VIEW_7.status == STARTED and t >= frameRemains:
        negative_view_VIEW_7.setAutoDraw(False)
    
    # *negative_view_Blank_7* updates
    if t >= 36.5 and negative_view_Blank_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank_7.tStart = t
        negative_view_Blank_7.frameNStart = frameN  # exact frame index
        negative_view_Blank_7.setAutoDraw(True)
    frameRemains = 36.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank_7.status == STARTED and t >= frameRemains:
        negative_view_Blank_7.setAutoDraw(False)
    
    # *negative_view_image_7* updates
    if t >= 37 and negative_view_image_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_image_7.tStart = t
        negative_view_image_7.frameNStart = frameN  # exact frame index
        negative_view_image_7.setAutoDraw(True)
    frameRemains = 37 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_image_7.status == STARTED and t >= frameRemains:
        negative_view_image_7.setAutoDraw(False)
    
    # *negative_view_Blank2_7* updates
    if t >= 52 and negative_view_Blank2_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Blank2_7.tStart = t
        negative_view_Blank2_7.frameNStart = frameN  # exact frame index
        negative_view_Blank2_7.setAutoDraw(True)
    frameRemains = 52 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Blank2_7.status == STARTED and t >= frameRemains:
        negative_view_Blank2_7.setAutoDraw(False)
    
    # *negative_view_Response_7* updates
    if t >= 53 and negative_view_Response_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Response_7.tStart = t
        negative_view_Response_7.frameNStart = frameN  # exact frame index
        negative_view_Response_7.setAutoDraw(True)
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Response_7.status == STARTED and t >= frameRemains:
        negative_view_Response_7.setAutoDraw(False)
    
    # *negative_view_Key_Resp_7* updates
    if t >= 53 and negative_view_Key_Resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Key_Resp_7.tStart = t
        negative_view_Key_Resp_7.frameNStart = frameN  # exact frame index
        negative_view_Key_Resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_view_Key_Resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Key_Resp_7.status == STARTED and t >= frameRemains:
        negative_view_Key_Resp_7.status = STOPPED
    if negative_view_Key_Resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_view_Key_Resp_7.keys = theseKeys[-1]  # just the last key pressed
            negative_view_Key_Resp_7.rt = negative_view_Key_Resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_view_Plus2_7* updates
    if t >= 57 and negative_view_Plus2_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_view_Plus2_7.tStart = t
        negative_view_Plus2_7.frameNStart = frameN  # exact frame index
        negative_view_Plus2_7.setAutoDraw(True)
    frameRemains = 57 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_view_Plus2_7.status == STARTED and t >= frameRemains:
        negative_view_Plus2_7.setAutoDraw(False)
    
    # *negative_distract_plus_7* updates
    if t >= 65 and negative_distract_plus_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_plus_7.tStart = t
        negative_distract_plus_7.frameNStart = frameN  # exact frame index
        negative_distract_plus_7.setAutoDraw(True)
    frameRemains = 65 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_plus_7.status == STARTED and t >= frameRemains:
        negative_distract_plus_7.setAutoDraw(False)
    
    # *negative_distract_DISTRACT_7* updates
    if t >= 65.5 and negative_distract_DISTRACT_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_DISTRACT_7.tStart = t
        negative_distract_DISTRACT_7.frameNStart = frameN  # exact frame index
        negative_distract_DISTRACT_7.setAutoDraw(True)
    frameRemains = 65.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_DISTRACT_7.status == STARTED and t >= frameRemains:
        negative_distract_DISTRACT_7.setAutoDraw(False)
    
    # *negative_distract_Blank_7* updates
    if t >= 67.5 and negative_distract_Blank_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank_7.tStart = t
        negative_distract_Blank_7.frameNStart = frameN  # exact frame index
        negative_distract_Blank_7.setAutoDraw(True)
    frameRemains = 67.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank_7.status == STARTED and t >= frameRemains:
        negative_distract_Blank_7.setAutoDraw(False)
    
    # *negative_distract_Photo_7* updates
    if t >= 68 and negative_distract_Photo_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Photo_7.tStart = t
        negative_distract_Photo_7.frameNStart = frameN  # exact frame index
        negative_distract_Photo_7.setAutoDraw(True)
    frameRemains = 68 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Photo_7.status == STARTED and t >= frameRemains:
        negative_distract_Photo_7.setAutoDraw(False)
    
    # *negative_distract_Blank2_7* updates
    if t >= 83 and negative_distract_Blank2_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Blank2_7.tStart = t
        negative_distract_Blank2_7.frameNStart = frameN  # exact frame index
        negative_distract_Blank2_7.setAutoDraw(True)
    frameRemains = 83 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Blank2_7.status == STARTED and t >= frameRemains:
        negative_distract_Blank2_7.setAutoDraw(False)
    
    # *negative_distract_Response_7* updates
    if t >= 84 and negative_distract_Response_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Response_7.tStart = t
        negative_distract_Response_7.frameNStart = frameN  # exact frame index
        negative_distract_Response_7.setAutoDraw(True)
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Response_7.status == STARTED and t >= frameRemains:
        negative_distract_Response_7.setAutoDraw(False)
    
    # *negative_distract_key_resp_7* updates
    if t >= 84 and negative_distract_key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_key_resp_7.tStart = t
        negative_distract_key_resp_7.frameNStart = frameN  # exact frame index
        negative_distract_key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_distract_key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 84 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_key_resp_7.status == STARTED and t >= frameRemains:
        negative_distract_key_resp_7.status = STOPPED
    if negative_distract_key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_distract_key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            negative_distract_key_resp_7.rt = negative_distract_key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_distract_Plus2_7* updates
    if t >= 88 and negative_distract_Plus2_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_distract_Plus2_7.tStart = t
        negative_distract_Plus2_7.frameNStart = frameN  # exact frame index
        negative_distract_Plus2_7.setAutoDraw(True)
    frameRemains = 88 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_distract_Plus2_7.status == STARTED and t >= frameRemains:
        negative_distract_Plus2_7.setAutoDraw(False)
    
    # *negative_reappraise_Plus_7* updates
    if t >= 92 and negative_reappraise_Plus_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus_7.tStart = t
        negative_reappraise_Plus_7.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus_7.setAutoDraw(True)
    frameRemains = 92 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus_7.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus_7.setAutoDraw(False)
    
    # *negative_reappraise_REAPPRAISE_7* updates
    if t >= 92.5 and negative_reappraise_REAPPRAISE_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_REAPPRAISE_7.tStart = t
        negative_reappraise_REAPPRAISE_7.frameNStart = frameN  # exact frame index
        negative_reappraise_REAPPRAISE_7.setAutoDraw(True)
    frameRemains = 92.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_REAPPRAISE_7.status == STARTED and t >= frameRemains:
        negative_reappraise_REAPPRAISE_7.setAutoDraw(False)
    
    # *negative_reappraise_Blank_7* updates
    if t >= 94.5 and negative_reappraise_Blank_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank_7.tStart = t
        negative_reappraise_Blank_7.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank_7.setAutoDraw(True)
    frameRemains = 94.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank_7.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank_7.setAutoDraw(False)
    
    # *negative_reappraise_Photo_7* updates
    if t >= 95 and negative_reappraise_Photo_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Photo_7.tStart = t
        negative_reappraise_Photo_7.frameNStart = frameN  # exact frame index
        negative_reappraise_Photo_7.setAutoDraw(True)
    frameRemains = 95 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Photo_7.status == STARTED and t >= frameRemains:
        negative_reappraise_Photo_7.setAutoDraw(False)
    
    # *negative_reappraise_Blank2_7* updates
    if t >= 110 and negative_reappraise_Blank2_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Blank2_7.tStart = t
        negative_reappraise_Blank2_7.frameNStart = frameN  # exact frame index
        negative_reappraise_Blank2_7.setAutoDraw(True)
    frameRemains = 110 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Blank2_7.status == STARTED and t >= frameRemains:
        negative_reappraise_Blank2_7.setAutoDraw(False)
    
    # *negative_reappraise_Response_7* updates
    if t >= 111 and negative_reappraise_Response_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Response_7.tStart = t
        negative_reappraise_Response_7.frameNStart = frameN  # exact frame index
        negative_reappraise_Response_7.setAutoDraw(True)
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Response_7.status == STARTED and t >= frameRemains:
        negative_reappraise_Response_7.setAutoDraw(False)
    
    # *negative_reappraise_key_resp_7* updates
    if t >= 111 and negative_reappraise_key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_key_resp_7.tStart = t
        negative_reappraise_key_resp_7.frameNStart = frameN  # exact frame index
        negative_reappraise_key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(negative_reappraise_key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 111 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_key_resp_7.status == STARTED and t >= frameRemains:
        negative_reappraise_key_resp_7.status = STOPPED
    if negative_reappraise_key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            negative_reappraise_key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            negative_reappraise_key_resp_7.rt = negative_reappraise_key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *negative_reappraise_Plus2_7* updates
    if t >= 115 and negative_reappraise_Plus2_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        negative_reappraise_Plus2_7.tStart = t
        negative_reappraise_Plus2_7.frameNStart = frameN  # exact frame index
        negative_reappraise_Plus2_7.setAutoDraw(True)
    frameRemains = 115 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if negative_reappraise_Plus2_7.status == STARTED and t >= frameRemains:
        negative_reappraise_Plus2_7.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block_7"-------
for thisComponent in Block_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if neutral_view_Key_Response_7.keys in ['', [], None]:  # No response was made
    neutral_view_Key_Response_7.keys=None
thisExp.addData('neutral_view_Key_Response_7.keys',neutral_view_Key_Response_7.keys)
if neutral_view_Key_Response_7.keys != None:  # we had a response
    thisExp.addData('neutral_view_Key_Response_7.rt', neutral_view_Key_Response_7.rt)
thisExp.nextEntry()
# check responses
if negative_view_Key_Resp_7.keys in ['', [], None]:  # No response was made
    negative_view_Key_Resp_7.keys=None
thisExp.addData('negative_view_Key_Resp_7.keys',negative_view_Key_Resp_7.keys)
if negative_view_Key_Resp_7.keys != None:  # we had a response
    thisExp.addData('negative_view_Key_Resp_7.rt', negative_view_Key_Resp_7.rt)
thisExp.nextEntry()
# check responses
if negative_distract_key_resp_7.keys in ['', [], None]:  # No response was made
    negative_distract_key_resp_7.keys=None
thisExp.addData('negative_distract_key_resp_7.keys',negative_distract_key_resp_7.keys)
if negative_distract_key_resp_7.keys != None:  # we had a response
    thisExp.addData('negative_distract_key_resp_7.rt', negative_distract_key_resp_7.rt)
thisExp.nextEntry()
# check responses
if negative_reappraise_key_resp_7.keys in ['', [], None]:  # No response was made
    negative_reappraise_key_resp_7.keys=None
thisExp.addData('negative_reappraise_key_resp_7.keys',negative_reappraise_key_resp_7.keys)
if negative_reappraise_key_resp_7.keys != None:  # we had a response
    thisExp.addData('negative_reappraise_key_resp_7.rt', negative_reappraise_key_resp_7.rt)
thisExp.nextEntry()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
