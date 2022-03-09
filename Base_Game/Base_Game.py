# PROJECT:// Dark Water
# Code by: _SPECTRE
import numpy as np
import msvcrt #Only for windows

#Variables
map_Medbay = np.array([[0,0,0,0,0],
                       [0,0,0,0,0],
                       [0,0,0,0,0]])
player_Pos = {'row':0,'column':0}

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
        Movement_Controller(map_Medbay,'w')
    elif(char=='a'):
        Movement_Controller(map_Medbay,'a')
    elif(char=='s'):
        Movement_Controller(map_Medbay,'s')
    elif(char=='d'):
        Movement_Controller(map_Medbay,'d')
    elif(char=='e'):
        Use_Handler(map_Medbay, 'e')
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

def Use_Handler(map, char):
    '''Function for '''

#Main Function/Testing functions
print('Game Start')

while True:
    input_char = msvcrt.getwch() #Only for windows
    Input_Handler(input_char)
    Map_Display(map_Medbay)

