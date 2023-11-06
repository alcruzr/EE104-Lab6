# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:10:49 2023

@author: Marvin Andrew Librado

Original Code from CodingGamesInPython PDF

Edited by Marvin Andrew Librado
"""

import pgzrun
import pygame
import pgzero

'Window size of the game'
WIDTH = 1280
HEIGHT = 720

'Parameters for the boxes on the screen'
main_box = Rect(0, 0, 820, 240) #Original was (0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

'Globals'
score = 0 #Score keeps track of the number of answers you got correct
time_left = 10 #Time in seconds before the timer ends

'Questions for the quiz'
'There will be 10 questions total'
#How it works is the first line has the question
#The second line has the answers and the number corresponding to the correct answer
q1 = ["What is the capital of France?",
      "London", "Paris", "Berlin", "Tokyo", 2]

q2 = ["What is 5+7?",
      "12", "10", "14", "8", 1]

q3 = ["What is the seventh month of the year?",
      "April", "May", "June", "July", 4]

q4 = ["Which planet is closest to the Sun?",
      "Saturn", "Neptune", "Mercury", "Venus", 3]

q5 = ["Where are the pyramids?",
      "India", "Egypt", "Morocco", "Canada", 2]

'Hacks and Tweaks (More questions)'
q6 = ["What is a quarter of 200?",
      "50", "100", "25", "150", 1]

q7 = ["Which is the largest state in the USA?",
      "Wyoming", "Alaska", "Florida", "Texas", 2]

q8 = ["How many wives did Henry VIII have?",
      "Eight", "Four", "Six", "One", 3]

'My 2 own questions to have 10 questions in total'
q9 = ["How many sides does an octagon have?",
      "Seven", "Ten", "Two", "Eight", 4]

q10 = ["When did Christopher Columbus sail the ocean blue?",
      "1492", "1519", "1612", "1776", 1]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10] #Number of questions in a list
question = questions.pop(0)

def draw():
    'Hacks and Tweaks (Dash and Color)'
    #Change names into RGB color values
    #e.g. "sky blue" --> (255, 0, 0)
    'Indigo'
    screen.fill("indigo") #Was originally "dim grey"
    'Slate Blue'
    screen.draw.filled_rect(main_box, (106, 90, 205)) #Was originally "sky blue"
    'Slate Blue'
    screen.draw.filled_rect(timer_box, (106, 90, 205)) #Was originally "sky blue"
 
    for box in answer_boxes:
        'Slate Blue'
        screen.draw.filled_rect(box, (106, 90, 205)) #Was originally "orange"
 
    'Corn Silk'
    screen.draw.textbox(str(time_left), timer_box, color=("corn silk")) #Was originally "black"
    'Corn Silk'
    screen.draw.textbox(question[0], main_box, color=("corn silk")) #Was originally "black"
    
    'Used for the answer'
    index = 1
    for box in answer_boxes:
        'Corn Silk'
        screen.draw.textbox(question[index], box, color=("corn silk")) #Was originally "black"
        index = index + 1

'Shows a game over screen and a message pertaining to'
'how many question the user got correct'        
def game_over():
    global question, time_left
    message = "Game over. You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

'Calls function when the correct answer has been picked'
#Calculates score, moves to the next question, and resets the time    
def correct_answer():
    global question, score, time_left
        
    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        print("End of questions")
        game_over()
        'Print the total score'
        print("Total score =", str(score))

'Used to detect mouse clicks'            
def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                game_over()
        index = index + 1

'Hacks and Tweaks (Hints and Skip a Question)'
def on_key_up(key):
    global score
    if key == keys.H:
        print("The correct answer is box number %s " % question[5])
    if key == keys.SPACE:
        score = score - 1
        correct_answer()

'Updates the time or ends the game due to time out'
def update_time_left():
    global time_left
    
    if time_left:
        time_left = time_left - 1
    else:
        game_over()
        
clock.schedule_interval(update_time_left, 1.0)

'Runs the game'
pgzrun.go()