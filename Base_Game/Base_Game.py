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
        print('you pressed w')
    elif(char=='a'):
        print('you pressed a')
    elif(char=='s'):
        print('you pressed s')
    elif(char=='d'):
        print('you pressed d')
    else:
        print('unknown character')

#Main Function/Testing functions
print('Game Start')
Map_Display(map_Medbay)
while True:
    input_char = msvcrt.getwch() #Only for windows
    Input_Handler(input_char)


