#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on March 17, 2017, at 15:50
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

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Training'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\Arya\\Documents\\Research\\Stanford Psychophysiology Lab\\Training.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
Start = visual.TextStim(win=win, name='Start',
    text=u'Ready to begin Training Simulation.\n\nPress SPACE to start. ',
    font=u'Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
text = visual.TextStim(win=win, name='text',
    text=u"In this task you are going to see a series of pictures. Some pictures might make you feel quite negative, while others won't make you feel much at all.\n\nBefore each picture, you will see an instruction that tells you what we want you to do while you are viewing the picture.\n\nPress SPACE to continue\n",
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Look at the picture and allow yourself to react to it naturally. \n\nPress SPACE to continue',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='Reinterpret the picture so it is less negative for you.\n\nPress SPACE to continue',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='After each picture is presented, please rate how negative you feel on a 1-5 scale.\n\nYou have only 4 seconds to rate a picture.\n\nPress SPACE to continue',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='You will see the following rating scale which lasts only 4 seconds\n\n\nHow do you feel?\n\n1 2 3 4 5\n\n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-10.0);
Plus = visual.TextStim(win=win, name='Plus',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-12.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='VIEW',
    font='Arial',
    pos=(0, 0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-13.0);
Blank = visual.TextStim(win=win, name='Blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-14.0);
image = visual.ImageStim(
    win=win, name='image',
    image='mario.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 1.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
Blank2 = visual.TextStim(win=win, name='Blank2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-16.0);
Response = visual.TextStim(win=win, name='Response',
    text='Ho Do you feel?\n\n1 2 3 4 5',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-17.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-19.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='Great Job!\n\nPress ENTER to try again.\n\nPress SPACE to continue',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-20.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(63.000000)
    # update component parameters for each repeat
    
    
    resp_8 = event.BuilderKeyResponse()
    key_resp_2 = event.BuilderKeyResponse()
    key_resp_3 = event.BuilderKeyResponse()
    key_resp_4 = event.BuilderKeyResponse()
    key_resp_5 = event.BuilderKeyResponse()
    key_resp_6 = event.BuilderKeyResponse()
    keyResponse = event.BuilderKeyResponse()
    key_resp_7 = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [Start, key_resp_8, text, key_resp_2, text_2, key_resp_3, text_3, key_resp_4, text_4, key_resp_5, text_5, key_resp_6, Plus, text_6, Blank, image, Blank2, Response, keyResponse, text_7, text_8, key_resp_7]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Start* updates
        if t >= 0 and Start.status == NOT_STARTED:
            # keep track of start time/frame for later
            Start.tStart = t
            Start.frameNStart = frameN  # exact frame index
            Start.setAutoDraw(True)
        frameRemains = 0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Start.status == STARTED and t >= frameRemains:
            Start.setAutoDraw(False)
        
        # *key_resp_8* updates
        if key_resp_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_8.tStart = t
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_8.status == STARTED and t >= frameRemains:
            key_resp_8.status = STOPPED
        if key_resp_8.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_8.keys = theseKeys[-1]  # just the last key pressed
                key_resp_8.rt = key_resp_8.clock.getTime()
                # was this 'correct'?
                if (key_resp_8.keys == str(u"'space'")) or (key_resp_8.keys == u"'space'"):
                    key_resp_8.corr = 1
                else:
                    key_resp_8.corr = 0
        
        # *text* updates
        if t >= 5 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 5 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # *key_resp_2* updates
        if key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 5 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_2.status == STARTED and t >= frameRemains:
            key_resp_2.status = STOPPED
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # was this 'correct'?
                if (key_resp_2.keys == str(u"'space'")) or (key_resp_2.keys == u"'space'"):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
        
        # *text_2* updates
        if t >= 13 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        frameRemains = 13 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_2.status == STARTED and t >= frameRemains:
            text_2.setAutoDraw(False)
        
        # *key_resp_3* updates
        if t >= 13 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 13 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_3.status == STARTED and t >= frameRemains:
            key_resp_3.status = STOPPED
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
        
        # *text_3* updates
        if t >= 17 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        frameRemains = 17 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_3.status == STARTED and t >= frameRemains:
            text_3.setAutoDraw(False)
        
        # *key_resp_4* updates
        if t >= 17 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 17 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_4.status == STARTED and t >= frameRemains:
            key_resp_4.status = STOPPED
        if key_resp_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_4.keys = theseKeys[-1]  # just the last key pressed
                key_resp_4.rt = key_resp_4.clock.getTime()
                # was this 'correct'?
                if (key_resp_4.keys == str(u"'space'")) or (key_resp_4.keys == u"'space'"):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
        
        # *text_4* updates
        if t >= 21 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        frameRemains = 21 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_4.status == STARTED and t >= frameRemains:
            text_4.setAutoDraw(False)
        
        # *key_resp_5* updates
        if t >= 21 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            key_resp_5.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        frameRemains = 21 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_5.status == STARTED and t >= frameRemains:
            key_resp_5.status = STOPPED
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_5.keys = theseKeys[-1]  # just the last key pressed
                key_resp_5.rt = key_resp_5.clock.getTime()
        
        # *text_5* updates
        if t >= 26 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        frameRemains = 26 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_5.status == STARTED and t >= frameRemains:
            text_5.setAutoDraw(False)
        
        # *key_resp_6* updates
        if t >= 26 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 26 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_6.status == STARTED and t >= frameRemains:
            key_resp_6.status = STOPPED
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6.rt = key_resp_6.clock.getTime()
                # was this 'correct'?
                if (key_resp_6.keys == str(u"'space'")) or (key_resp_6.keys == u"'space'"):
                    key_resp_6.corr = 1
                else:
                    key_resp_6.corr = 0
        
        # *Plus* updates
        if t >= 30 and Plus.status == NOT_STARTED:
            # keep track of start time/frame for later
            Plus.tStart = t
            Plus.frameNStart = frameN  # exact frame index
            Plus.setAutoDraw(True)
        frameRemains = 30 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Plus.status == STARTED and t >= frameRemains:
            Plus.setAutoDraw(False)
        
        # *text_6* updates
        if t >= 30.5 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        frameRemains = 30.5 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_6.status == STARTED and t >= frameRemains:
            text_6.setAutoDraw(False)
        
        # *Blank* updates
        if t >= 32.5 and Blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            Blank.tStart = t
            Blank.frameNStart = frameN  # exact frame index
            Blank.setAutoDraw(True)
        frameRemains = 32.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Blank.status == STARTED and t >= frameRemains:
            Blank.setAutoDraw(False)
        
        # *image* updates
        if t >= 33 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 33 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # *Blank2* updates
        if t >= 48 and Blank2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Blank2.tStart = t
            Blank2.frameNStart = frameN  # exact frame index
            Blank2.setAutoDraw(True)
        frameRemains = 48 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Blank2.status == STARTED and t >= frameRemains:
            Blank2.setAutoDraw(False)
        
        # *Response* updates
        if t >= 49 and Response.status == NOT_STARTED:
            # keep track of start time/frame for later
            Response.tStart = t
            Response.frameNStart = frameN  # exact frame index
            Response.setAutoDraw(True)
        frameRemains = 49 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Response.status == STARTED and t >= frameRemains:
            Response.setAutoDraw(False)
        
        # *keyResponse* updates
        if t >= 49 and keyResponse.status == NOT_STARTED:
            # keep track of start time/frame for later
            keyResponse.tStart = t
            keyResponse.frameNStart = frameN  # exact frame index
            keyResponse.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(keyResponse.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 49 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if keyResponse.status == STARTED and t >= frameRemains:
            keyResponse.status = STOPPED
        if keyResponse.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3', '4', '5'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                keyResponse.keys = theseKeys[-1]  # just the last key pressed
                keyResponse.rt = keyResponse.clock.getTime()
                # was this 'correct'?
                if (keyResponse.keys == str(u"'1','2','3','4','5'")) or (keyResponse.keys == u"'1','2','3','4','5'"):
                    keyResponse.corr = 1
                else:
                    keyResponse.corr = 0
        
        # *text_7* updates
        if t >= 53 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        frameRemains = 53 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_7.status == STARTED and t >= frameRemains:
            text_7.setAutoDraw(False)
        
        # *text_8* updates
        if t >= 57 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        frameRemains = 57 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_8.status == STARTED and t >= frameRemains:
            text_8.setAutoDraw(False)
        
        # *key_resp_7* updates
        if t >= 57 and key_resp_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_7.tStart = t
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 57 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_7.status == STARTED and t >= frameRemains:
            key_resp_7.status = STOPPED
        if key_resp_7.status == STARTED:
            theseKeys = event.getKeys(keyList=['enter', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_7.keys = theseKeys[-1]  # just the last key pressed
                key_resp_7.rt = key_resp_7.clock.getTime()
                # was this 'correct'?
                if (key_resp_7.keys == str(u"'enter','space'")) or (key_resp_7.keys == u"'enter','space'"):
                    key_resp_7.corr = 1
                else:
                    key_resp_7.corr = 0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys=None
        # was no response the correct answer?!
        if str(u"'space'").lower() == 'none':
           key_resp_8.corr = 1  # correct non-response
        else:
           key_resp_8.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_8.keys',key_resp_8.keys)
    trials.addData('key_resp_8.corr', key_resp_8.corr)
    if key_resp_8.keys != None:  # we had a response
        trials.addData('key_resp_8.rt', key_resp_8.rt)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
        # was no response the correct answer?!
        if str(u"'space'").lower() == 'none':
           key_resp_2.corr = 1  # correct non-response
        else:
           key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    trials.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys=None
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys=None
        # was no response the correct answer?!
        if str(u"'space'").lower() == 'none':
           key_resp_4.corr = 1  # correct non-response
        else:
           key_resp_4.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    trials.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys=None
    trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials.addData('key_resp_5.rt', key_resp_5.rt)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys=None
        # was no response the correct answer?!
        if str(u"'space'").lower() == 'none':
           key_resp_6.corr = 1  # correct non-response
        else:
           key_resp_6.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_6.keys',key_resp_6.keys)
    trials.addData('key_resp_6.corr', key_resp_6.corr)
    if key_resp_6.keys != None:  # we had a response
        trials.addData('key_resp_6.rt', key_resp_6.rt)
    # check responses
    if keyResponse.keys in ['', [], None]:  # No response was made
        keyResponse.keys=None
        # was no response the correct answer?!
        if str(u"'1','2','3','4','5'").lower() == 'none':
           keyResponse.corr = 1  # correct non-response
        else:
           keyResponse.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('keyResponse.keys',keyResponse.keys)
    trials.addData('keyResponse.corr', keyResponse.corr)
    if keyResponse.keys != None:  # we had a response
        trials.addData('keyResponse.rt', keyResponse.rt)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys=None
        # was no response the correct answer?!
        if str(u"'enter','space'").lower() == 'none':
           key_resp_7.corr = 1  # correct non-response
        else:
           key_resp_7.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_7.keys',key_resp_7.keys)
    trials.addData('key_resp_7.corr', key_resp_7.corr)
    if key_resp_7.keys != None:  # we had a response
        trials.addData('key_resp_7.rt', key_resp_7.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
