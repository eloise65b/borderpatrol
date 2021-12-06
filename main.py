import pygame
import random
import time 
import sqlite3
import sys

pygame.init()
conn = sqlite3.connect('data.db') #note to self: this is NEEDED don't touch it, you'll break everything
clock = pygame.time.Clock()


def importperson():
    cursor = conn.cursor()
    #add random generation module here, for now, we'll be entering the refernece number by hand for debug purposes
    NameID = str("10")
    TaskID = str("04")
    TypeID = str("05")
    #these create our sql statements
    #TODO: needs to be correctly formatted it seems, use a larger (f?) string instead
    #cur.execute("select firstname, lastname from names where nameid like ?", (NameID,))
    namearray = ["select firstname, lastname from names where nameID like", NameID]
    namestatement = " ".join(namearray)
    NameValue = cursor.execute(namestatement)
    #not very efficient tbh
    taskarray = ["select TaskName, TaskDuration, TaskScore from Task where TaskID like", TaskID]
    taskstatement = " ".join(taskarray)
    TaskValue = cursor.execute(taskstatement)
    typearray = ["select TypeName from Type where TypeID like", TypeID]
    typestatement = " ".join(typearray)
    TypeValue = cursor.execute(typestatement)
    print(NameValue,TaskValue, TypeValue)


def longestfirst():
    #x = number of tasks waiting
    x = 0
    #timeval = import from main string, time left on task
    for i in range(0,x):
        lowest = 1
        if timeval < lowest:
            lowest = timeval
            todo = x
    return(todo,x)

def shortestfirst():
    #x = number of tasks waiting
    x = 0
    #timeval = import from main string, time left on task
    for i in range(0,x):
        highest = 1
        if timeval > highest:
            highest = timeval
            todo = x
    return(todo,x) #unsure if this is appropriate- run within the func.?

def roundrobin(sleeptime):
    #must be called multiple times using a for statment? probably should run within the function
    x = 0
    for i in range(0,x):
        time.sleep(sleeptime)
        return(x)
        #what the hell is this though


#bg = (255,255,255)
#width = 500
#height = 500
#initialise window
#win = pygame.display.set_mode((width, height))
#pygame.display.set_caption("Paperwork")
#win.fill(bg)
#font = pygame.font.SysFont(None, 24)
#img = font.render('Welcome to Paperwork', True, BLUE)
#you have to blit not print. format is [name of window thing].blit(text, (coords))
#win.blit(img, (20, 20))

screen = pygame.display.set_mode([600, 500])
  
# set font
base_font = pygame.font.Font(None, 32)
user_text = ''
  
# create rect for input
input_rect = pygame.Rect(200, 200, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
active = False

while True:
    screen.fill((255, 255, 255))
         
    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10)
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
                color = color_active
                inputparser()
             else:
                active = False
                color = color_passive
    
                
def inputparser():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode





importperson()



def startmenu(clientNumber):
    win.blit("Client Number",clientNumber)
    win.blit("Welcome to Paperwork!", (20,20))
    #TODO: how to take input from a pygame window. 
    # i'd rather only have one window open for professionalism
    # unless this part of the code gets intergrated into a "launcher" which is an option
    win.blit("Press N to start a new game, or J to join an existing one", (20,20))
    startnew = #input from pygame window
    if startnew != "N" and startnew != "J":
        win.blit("N to start a new game, J to join.",(20,20))
    if startnew == "N":
        pass
        #generate game number
    if startnew == "J":
        pass
        #recieve list of game numbers from server
        win.blit(listofgamenumbers)
        win.blit("select game number")
