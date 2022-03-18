# PROJECT:// Dark Water
# Code by: _SPECTRE
import numpy as np
import msvcrt #Only for windows

#Variables
#Maps
map_DockingHub1 = np.array([[11, 6, 0],
                            [11, 0, 1],
                            [11, 6, 2]])

map_PrepRoom1 = np.array([[1, 0, 1, 2, 1],
                          [2, 0, 3, 0, 2],
                          [4, 4, 0, 4, 4]])

map_Medbay = np.array([[6, 4, 0, 3, 4],
                       [1, 0, 3, 0, 5],
                       [2, 4, 0, 4, 0]])

map_LivingQuarters = np.array([[5, 1, 2],
                               [5, 0, 5],
                               [4, 0, 5],
                               [4, 0, 4],
                               [5, 0, 4],
                               [5, 1, 2]])

map_CIC = np.array([[0, 1, 2],
                    [8, 9, 7],
                    [3, 1, 2]])

map_LifeSupport = np.array([[0, 1, 2],
                            [6, 0, 6],
                            [6, 0, 4],
                            [6, 1, 2]])

map_PrepRoom2 = np.array([[4, 4, 0, 0, 0],
                          [2, 0, 0, 3, 2],
                          [1, 0, 1, 2, 1]])

map_BioChem = np.array([[4, 0, 0, 0],
                        [0, 4, 4, 1],
                        [4, 10, 0, 2]])

doors = [{'locked':False, 'f_room':1, 't_room':0, 'f_x':0, 'f_y':0, 't_x':1, 't_y':2}, #Prep1-Dock1
         {'locked':False, 'f_room':1, 't_room':3, 'f_x':0, 'f_y':2, 't_x':5, 't_y':1}, #Prep1-Living
         {'locked':False, 'f_room':1, 't_room':2, 'f_x':0, 'f_y':4, 't_x':1, 't_y':0}, #Prep1-MedBay
         {'locked':False, 'f_room':4, 't_room':3, 'f_x':2, 'f_y':1, 't_x':0, 't_y':1}, #CIC-Living
         {'locked':False, 'f_room':4, 't_room':5, 'f_x':0, 'f_y':1, 't_x':3, 't_y':1}, #CIC-LifeSupport
         {'locked':False, 'f_room':6, 't_room':5, 'f_x':2, 'f_y':2, 't_x':0, 't_y':1}, #Prep2-LifeSupport
         {'locked':False, 'f_room':6, 't_room':7, 'f_x':2, 'f_y':0, 't_x':1, 't_y':3}, #Prep2-BioChem
         {'locked':False, 'f_room':6, 't_room':8, 'f_x':2, 'f_y':4, 't_x':0, 't_y':0} #Prep2-Dock2 (Not to be used)
         ]

#Game Control Variables
player_Pos = {'row':0,'column':0}
currentRoom = 0
map_Current = map_Medbay
stay = False #For staying in the Room

#Functions and Classes

def Map_Display(map):
    '''Function for displaying the map state of the current room'''
    map_dimensions = map.shape
    #print(map_dimensions)
    s_map = ("_"*((map_dimensions[1]*2)+1))+"\n"
    for i in range(0,map_dimensions[0]):
        s_map = s_map+"|"
        for j in range(0,map_dimensions[1]):
            if((player_Pos['row']==i)and(player_Pos['column']==j)):
                s_map = s_map+'P|'
            else:
                s_map = s_map+str(map[i][j])+"|"
        s_map = s_map+"\n"
    s_map = s_map+(chr(8254)*((map_dimensions[1]*2)+1))+"\n"
    print(s_map)

def Input_Handler(char):
    '''Function for handling player input'''
    if (char=='w'):
        Movement_Controller(map_Current,'w')
    elif(char=='a'):
        Movement_Controller(map_Current,'a')
    elif(char=='s'):
        Movement_Controller(map_Current,'s')
    elif(char=='d'):
        Movement_Controller(map_Current,'d')
    elif(char=='e'):
        Use_Handler(map_Current)
    else:
        print('unknown character')

def Movement_Controller(map, char):
    '''Function for controlling the player movement'''
    map_dimensions = map.shape
    if (char=='w'):
        if(player_Pos['row']-1>=0): #W: for up
            player_Pos['row'] = player_Pos['row'] - 1;
    elif(char=='a'):
        if(player_Pos['column']-1>=0): #A: for left
            player_Pos['column'] = player_Pos['column'] - 1;
    elif(char=='s'):
        if(player_Pos['row']+1<map_dimensions[0]): #S: for down
            player_Pos['row'] = player_Pos['row'] + 1;
    elif(char=='d'):
        if(player_Pos['column']+1<map_dimensions[1]): #D: for right
            player_Pos['column'] = player_Pos['column'] + 1;

def Use_Handler(map):
    '''Function for calling the correct use handler for the right tile'''
    tile = map[player_Pos['row']][player_Pos['column']]
    if(tile==0):
        print("There is nothing here.")
    elif(tile==1):
        print("You used the door")
        doorHandler()
    elif(tile==2):
        print("You used a terminal")
    elif(tile==3):
        print("You found something on the floor")
    elif(tile==4):
        print("You found a locker")
    elif(tile==5):
        print("You found a safe")
    elif(tile==6):
        print("You found something interesting")
    elif(tile==7):
        print("You found a Computer")
    elif(tile==8):
        print("You found the N.E.S.S.I.E Core")
        Nessie()
    elif(tile==9):
        print("You found Doris")
        Doris()
    elif(tile==10):
        print("You found Ellen")
        Ellen()
    elif(tile==11):
        print("You found the escape pod")

#Door Functions
def doorHandler():
    if(currentRoom==0):
        #Docking Hub 1
        #doors[0] | Dock1-Prep1 (inv)
        changeRoom(0, True);
    elif(currentRoom==1): 
        #Prep Room 1
        if(player_Pos['column'] == 0):
            #doors[0] | Prep1-Dock1
            changeRoom(0, False);
        elif(player_Pos['column'] == 2):
            #doors[1] | Prep1-Living
            changeRoom(1, False);
        elif(player_Pos['column'] == 4):
            #doors[2] | Prep1-MedBay
            changeRoom(2, False);
    elif(currentRoom==2):
        #Med Bay
        #doors[2] | MedBay-Prep1 (inv)
        changeRoom(2, True);
    elif(currentRoom==3): 
        #Living Quarters
        if (player_Pos['row'] == 5):
            #doors[1] | Living-Prep1 (inv)
            changeRoom(1, True);
            return;
        #doors[3] | Living-CIC (inv)
        changeRoom(3, True);
    elif(currentRoom==4):
        #CIC
        if (player_Pos['row'] == 2):
            #doors[3] | CIC-Living
            changeRoom(3, False);
            return;
        #doors[4] | CIC-LifeSupport
        changeRoom(4, False);
    elif(currentRoom==5):
        #Life Support
        if (player_Pos['row'] == 3):
            #doors[4] | LifeSupport-CIC (inv)
            changeRoom(4, True);
            return;
        #doors[5] | LifeSuppport-Prep2
        changeRoom(5, True);
    elif(currentRoom==6):
        #Prep Room 2
        if(player_Pos['column'] == 0):
            #doors[6] | Prep2-BioChem
            changeRoom(6, False);
        elif(player_Pos['column'] == 2):
            #doors[5] | Prep2-LifeSupport
            changeRoom(5, False);
        elif(player_Pos['column'] == 4):
            #To dev room/DockHub 2
            print("This door is sealed");
    elif(currentRoom==7):
        #BioChem
        #doors[6] | BioChem-Prep2 (inv)
        changeRoom(6, True);
def changeRoom(doorNo, invert):
  global currentRoom, stay, player_Pos
  if(doors[doorNo]['locked']):
    print("This room is locked!");
    return;
  #Invert is when you want to set the value to from values instead of to
  if (invert):
    currentRoom = doors[doorNo]['f_room'];
    player_Pos['row'] = doors[doorNo]['f_x'];
    player_Pos['column'] = doors[doorNo]['f_y'];
  else:
    currentRoom = doors[doorNo]['t_room'];
    player_Pos['row'] = doors[doorNo]['t_x'];
    player_Pos['column'] = doors[doorNo]['t_y'];
  stay = False

#Terminal Functions

def Doris():
    '''Function for the NPC Doris'''
    
def Ellen():
    '''Function for the NPC Ellen'''

def Nessie():
    '''Function for the NPC N.E.S.S.I.E'''

#Main Function/Testing functions
print('Game Start')
while True:
    if(currentRoom==0):
        map_Current = map_DockingHub1
    elif(currentRoom==1):
        map_Current = map_PrepRoom1
    elif(currentRoom==2):
        map_Current = map_Medbay
    elif(currentRoom==3):
        map_Current = map_LivingQuarters
    elif(currentRoom==4):
        map_Current = map_CIC
    elif(currentRoom==5):
        map_Current = map_LifeSupport
    elif(currentRoom==6):
        map_Current = map_PrepRoom2
    elif(currentRoom==7):
        map_Current = map_BioChem
    Map_Display(map_Current)
    stay = True
    while (stay):
        input_char = msvcrt.getwch() #Only for windows
        Input_Handler(input_char)
        Map_Display(map_Current)