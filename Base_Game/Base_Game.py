title='''
                                                                                                             
`7MM"""Yb.      db      `7MM"""Mq.  `7MMF' `YMM'     `7MMF'     A     `7MF' db   MMP""MM""YMM `7MM"""YMM  `7MM"""Mq.  
  MM    `Yb.   ;MM:       MM   `MM.   MM   .M'         `MA     ,MA     ,V  ;MM:  P'   MM   `7   MM    `7    MM   `MM. 
  MM     `Mb  ,V^MM.      MM   ,M9    MM .d"            VM:   ,VVM:   ,V  ,V^MM.      MM        MM   d      MM   ,M9  
  MM      MM ,M  `MM      MMmmdM9     MMMMM.             MM.  M' MM.  M' ,M  `MM      MM        MMmmMM      MMmmdM9   
  MM     ,MP AbmmmqMA     MM  YM.     MM  VMA            `MM A'  `MM A'  AbmmmqMA     MM        MM   Y  ,   MM  YM.   
  MM    ,dP'A'     VML    MM   `Mb.   MM   `MM.           :MM;    :MM;  A'     VML    MM        MM     ,M   MM   `Mb. 
.JMMmmmdP'.AMA.   .AMMA..JMML. .JMM..JMML.   MMb.          VF      VF .AMA.   .AMMA..JMML.    .JMMmmmmMMM .JMML. .JMM.

'''
credits='''
PROJECT:// Dark Water
Code by: _SPECTRE
'''

'''
Current Issues\Points to Consider:
*Functions that take in map as an argument, unnecessary with global variable map_Current
ASCII font is Georgia11
'''

import numpy as np
import msvcrt #Only for windows
import time
import sys
import os

#Variables
'''Maps:
There is a map for each room in the game, 7 maps in total.
Each map is divided into a grid, with each grid containing a Tile ID.
The Tile ID specify the behavior when the player presses E (Use Key) on a Tile.
'''
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

'''
Storage Objects
name: Defines what the object is
itemID: ItemID of the Item it holds
room: Which room the 
row: 
column: 
'''
storage = [
  {'name':"Equipment Locker",'itemID':0,'room':1,'row':2,'column':0},
  {'name':"Equipment Locker",'itemID':1,'room':1,'row':2,'column':1},
  {'name':"Coffee Maker",'itemID':7,'room':1,'row':2,'column':3},
  {'name':"Pantry",'itemID':35,'room':1,'row':2,'column':4},

  {'name':"Tony's Table",'itemID':23,'room':2,'row':0,'column':1},
  {'name':"Medical Locker",'itemID':3,'room':2,'row':0,'column':4},
  {'name':"Bed",'itemID':22,'room':2,'row':2,'column':1},
  {'name':"Bed",'itemID':21,'room':2,'row':2,'column':3},

  {'name':"Blaire and Ellen's Bunk Bed",'itemID':10,'room':3,'row':2,'column':0},
  {'name':"Doris and Tony's Bunk Bed",'itemID':5,'room':3,'row':3,'column':0},
  {'name':"John and Drake's Bunk Bed",'itemID':27,'room':3,'row':3,'column':2},
  {'name':"Shelf",'itemID':30,'room':3,'row':4,'column':2},

  {'name':"Water Circulator",'itemID':15,'room':5,'row':2,'column':2},

  {'name':"Equipment Locker",'itemID':0,'room':6,'row':0,'column':0},
  {'name':"Equipment Locker",'itemID':1,'room':6,'row':0,'column':1},

  {'name':"Freezer",'itemID':13,'room':7,'row':0,'column':0},
  {'name':"Supply Closet",'itemID':2,'room':7,'row':2,'column':0},
  {'name':"Table",'itemID':35,'room':7,'row':1,'column':1},
  {'name':"Table",'itemID':35,'room':7,'row':1,'column':2}
]

safes = [
    {'name':"Safe",'code':'0451','locked':True,'itemID':6,'room':2,'row':1,'column':4}
    ]

descTile = [
    {'name':'Docking Hatch #1','room':0,'row':0,'column':1},
    {'name':'Docking Hatch #2','room':0,'row':2,'column':1},

    {'name':'Toilet','room':2,'row':0,'column':0},
    
    {'name':'Water Processor','room':5,'row':1,'column':0},
    {'name':'Water Processor','room':5,'row':2,'column':0},
    {'name':'Toilet','room':5,'row':3,'column':0},
    {'name':'Air Filter','room':5,'row':1,'column':2},
    ]

#Item 35 is used for lockers that never contain an item, it is therefore set to true.
item_list = [
{'ID':0,'name':'Wetsuit','taken':False},
{'ID':1,'name':'Headset','taken':False},
{'ID':2,'name':'Alcohol','taken':False},
{'ID':3,'name':'Bandages','taken':False},
{'ID':4,'name':'Candy Bar','taken':False},
{'ID':5,'name':'Cotton Shirt','taken':False},
{'ID':6,'name':'Oxycodone','taken':False},
{'ID':7,'name':'Heating Element','taken':False},
{'ID':8,'name':'','taken':False},
{'ID':9,'name':'','taken':False},
{'ID':10,'name':'Blaire\'s PDA','taken':False},
{'ID':11,'name':'Ellen\'s PDA','taken':False},
{'ID':12,'name':'Doris\' PDA','taken':False},
{'ID':13,'name':'Tony\'s PDA','taken':False},
{'ID':14,'name':'John\'s PDA','taken':False},
{'ID':15,'name':'Drake\'s PDA','taken':False},
{'ID':16,'name':'','taken':False},
{'ID':17,'name':'','taken':False},
{'ID':18,'name':'','taken':False},
{'ID':19,'name':'','taken':False},
{'ID':20,'name':'Blaire\'s file','taken':False},
{'ID':21,'name':'Doris\' file','taken':False},
{'ID':22,'name':'Ellen\'s file','taken':False},
{'ID':23,'name':'Birthday card','taken':False},
{'ID':24,'name':'Base Eng. Guide','taken':False},
{'ID':25,'name':'N.E.S.S.I.E Handbook','taken':False},
{'ID':26,'name':'Deepwater Brochure','taken':False},
{'ID':27,'name':'E. Systems Guide','taken':False},
{'ID':28,'name':'','taken':False},
{'ID':29,'name':'','taken':False},
{'ID':30,'name':'Alien DVD','taken':False},
{'ID':31,'name':'Blair Witch Project','taken':False},
{'ID':32,'name':'Aliens','taken':False},
{'ID':33,'name':'Iron Man','taken':False},
{'ID':34,'name':'JW: Parabellum','taken':False},
{'ID':35,'name':'Nothing','taken':True},
{'ID':36,'name':'','taken':False},
{'ID':37,'name':'','taken':False},
{'ID':38,'name':'','taken':False},
{'ID':39,'name':'','taken':False}
]

strBlair1=[
    '*Alarms Blaring*',
    'You wake up on the floor',
    '*The alarms stop*',
    'Primary power is down.\nThe station is running on backup systems.',
    'You can barely see around you\nThe emergency lights are weak',
    '[What the hell happened?]',
    'You remember coming to the medbay...',
    'and the base moved off foundation...',
    'you got knocked to the ground\nand bumped your head on the way down.',
    '[I need to get to the CIC...\nI need to find the others]',
    '[I need to find answers...]',
    'The air is stating to feel stale...',
    'You don\'t have much time'
    ]

#Game Control Variables
player_Pos = {'row':2,'column':4}
currentRoom = 2
map_Current = map_Medbay
stay = False #For staying in the Room
continueGame = True
doorMasterCode = '5389'

#Functions and Classes
#Rendering
def Map_Display(map):
    '''Map_Display(map):
    map: Must be a 2-D np array of integers (Room map)
    This function is for displaying the map state of the current room.
    Current Issues:
    Map is distorted when Tile ID is more than 1 digit
    '''
    map_dimensions = map.shape
    #print(map_dimensions)
    s_map = ("_"*((map_dimensions[1]*2)+1))+"\n"
    for i in range(0,map_dimensions[0]):
        s_map = s_map+"|"
        for j in range(0,map_dimensions[1]):
            if((player_Pos['row']==i)and(player_Pos['column']==j)):
                s_map = s_map+'P|'
            else:
                s_map = s_map+str(' ')+"|"
        s_map = s_map+"\n"
        #s_map = s_map+('-'*((map_dimensions[1]*2)+1))+"\n"
    s_map = s_map+(chr(8254)*((map_dimensions[1]*2)+1))+"\n"
    print(s_map)

def Debug_Map_Display(map):
    '''Debug_Map_Display(map):
    map: Must be a 2-D np array of integers (Room map)
    This function is for displaying the map state of the current room.
    Current Issues:
    Map is distorted when Tile ID is more than 1 digit
    '''
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

# define our clear function
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
 
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')


#Player Input Handlers
def Input_Handler(char):
    '''Input_Handler(char)
    char: The input character to be handled
    This function is for handling player input.
    Current Controls mapping:
    w: Move up
    a: Move left
    s: Move down
    d: Move right
    e: Use
    i: Inventory
    '''
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
    #elif(char=='i'):
    #    Inventory()
    else:
        print('Unknown character')

def Movement_Controller(map, char):
    '''Movement_Controller(map, char)
    map: The map the player should be moving in
    char: The movement control the player has input to the game
    This function for controlling the player movement in the specified map
    '''
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
    '''Use_Handler(map)
    map: The map that needs to handled
    Function for calling the correct use handler for the right tile
    '''
    tile = map[player_Pos['row']][player_Pos['column']]
    if(tile==0):
        print("There is nothing here.")
    elif(tile==1):
        print("You used the door")
        doorHandler()
    elif(tile==2):
        print("You used a terminal")
        terminalHandler()
    elif(tile==3):
        print("You found something on the floor")
        itemFloorHandler()
    elif(tile==4):
        storageHandler()
    elif(tile==5):
        safeHandler()
    elif(tile==6):
        #print("There is something here")
        descHandler()
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
        print("You found an escape pod")
        Triton()
    hold = msvcrt.getwch() #Only for windows, uncomment if using clearConsole()

def Inventory():
    '''Inventory()
    '''

#Door Functions (Tile ID=1)
def doorHandler():
    '''doorHandler()
    This function is used to decide which door needs to be handled.
    It calls changeRoom() with the correct parameters of the door
    '''
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
    '''changeRoom(doorNo, invert)
    doorNo: The door to choose in the doors array
    invert: Invert bool is when you want to set the value to "from" values instead of "to"
    This function is resposible for changing the room the player is in
    '''
    global currentRoom, stay, player_Pos
    if(doors[doorNo]['locked']):
        print("This door is locked!");
        return;
    if (invert):
        currentRoom = doors[doorNo]['f_room'];
        player_Pos['row'] = doors[doorNo]['f_x'];
        player_Pos['column'] = doors[doorNo]['f_y'];
    else:
        currentRoom = doors[doorNo]['t_room'];
        player_Pos['row'] = doors[doorNo]['t_x'];
        player_Pos['column'] = doors[doorNo]['t_y'];
    stay = False

#Terminal Functions (Tile ID=2)
def terminalHandler():
    '''terminalHandler()
    This function is used to decide which terminal needs to be handled.
    It calls terminalInterface() with the correct parameters of the terminal.
    '''
    if(currentRoom==0):
        #Docking Hub 1
        #door[0] | Dock1-Prep1 (inv)
        terminalInterface(0)
    elif(currentRoom==1):
        #Prep Room 1
        if (player_Pos['column'] == 0):
          #doors[0] | Prep1-Dock1
          terminalInterface(0)
        elif (player_Pos['column'] == 3):
          #doors[1] | Prep1-Living
          terminalInterface(1)
        elif (player_Pos['column'] == 4):
          #doors[2] | Prep1-MedBay
          terminalInterface(2)
    elif(currentRoom==2):
        #Med Bay
        #doors[2] | MedBay-Prep1 (inv)
        terminalInterface(2)
    elif(currentRoom==3):
        #Living Quarters
        if (player_Pos['row'] == 5):
          #doors[1] | Living-Prep1 (inv)
          terminalInterface(1)
          return;
        else:
            #doors[3] | Living-CIC (inv)
            terminalInterface(3)
    elif(currentRoom==4):
        #CIC
        if (player_Pos['row'] == 2):
          #doors[3] | CIC-Living
          terminalInterface(3);
          return;
        #doors[4] | CIC-LifeSupport
        terminalInterface(4);
    elif(currentRoom==5):
        #Life Support
        if (player_Pos['row'] == 3):
          #doors[4] | LifeSupport-CIC (inv)
          terminalInterface(4);
          return;
        #doors[5] | LifeSuppport-Prep2
        terminalInterface(5);
    elif(currentRoom==6):
        #Prep Room 2
        if (player_Pos['column'] == 0):
          #doors[6] | Prep2-BioChem
          terminalInterface(6);
        elif (player_Pos['column'] == 3):
          #doors[5] | Prep2-LifeSupport
          terminalInterface(5)
        elif (player_Pos['column'] == 4):
          #To dev room/DockHub 2
          print("This door is sealed")
    elif(currentRoom==7):
        #BioChem
        #doors[6] | BioChem-Prep2 (inv)
        terminalInterface(6)

def terminalInterface(doorNo):
    '''terminalInterface(doorNo)
    doorNo: The door the terminal is associated with
    This function is responsible for the terminal of the interface.
    Player inputs will be locked to this function.
    It takes in 4 keys for passcode, or q to exit the terminal
    '''
    global doors, doorMasterCode
    #Add conditions to check before unlocking door here
    if(not(doors[doorNo]['locked'])):
        print("The door is already unlocked")
        return;
    userCode = ''
    data_count = 0
    loop = True
    locked = True
    print("Enter Password:")
    while (loop):
        key = msvcrt.getwch() #Only for windows
        if (key == 'q'):
            #To exit menu
            return;
        userCode = userCode+key
        print(key, end='')
        data_count=data_count+1
        if (data_count == 4):
            if (userCode==doorMasterCode):
                print("\nAccess Granted")
                loop = False
                locked = False
            else:
                print("\nIncorrect. Try Again.")
                userCode = ''
                data_count = 0
                print("Enter Password:")
    doors[doorNo]['locked']=locked

#Item Floor Functions (Tile ID=3)
def changeTile(map, tileID, row, column):
    map[row][column]=tileID

def itemFloorHandler():
    if(currentRoom==1):
        itemNo = 4
    elif(currentRoom==2):
        if(player_Pos['column']==2):
            itemNo = 2
        elif (player_Pos['column']==3):
            itemNo = 20
    elif(currentRoom==4):
      itemNo = 25
    elif(currentRoom==6):
      itemNo = 26
    item_list[itemNo]['taken'] = True
    print('Item Found: '+item_list[itemNo]['name'])
    changeTile(map_Current, 0, player_Pos['row'],player_Pos['column'])

#Storage Functions (Tile ID=4)
def storageHandler():
    '''storageHandler()

    '''
    if(currentRoom==1):
        if(player_Pos['column']==0):
            getStorageItem(0)
        elif(player_Pos['column']==1):
            getStorageItem(1)
        elif(player_Pos['column']==3):
            getStorageItem(2)
        else:
            getStorageItem(3)
    elif(currentRoom==2):
        if(player_Pos['row']==0):
            if(player_Pos['column']==1):
                getStorageItem(4)
            else:
                getStorageItem(5)
        elif(player_Pos['row']==2):
            if(player_Pos['column']==1):
                getStorageItem(6)
            else:
                getStorageItem(7)
    elif(currentRoom==3):
        if(player_Pos['row']==2):
            getStorageItem(8)
        elif(player_Pos['row']==3):
            if(player_Pos['column']==0):
                getStorageItem(9)
            else:
                getStorageItem(10)
        elif(player_Pos['row']==4):
            getStorageItem(11)
    elif(currentRoom==5):
        getStorageItem(12)
    elif(currentRoom==6):
        if(player_Pos['column']==0):
            getStorageItem(13)
        else:
            getStorageItem(14)
    elif(currentRoom==7):
        if(player_Pos['row']==0):
            getStorageItem(15)
        elif(player_Pos['row']==2):
            getStorageItem(16)
        else:
            if(player_Pos['column']==1):
                getStorageItem(17)
            else:
                getStorageItem(18)        

def getStorageItem(storageNo):
    '''getStorageItem()

    '''
    global item_list
    print('You found: '+storage[storageNo]['name'])
    if(item_list[storage[storageNo]['itemID']]['taken']):
        #If the item has been taken, then it shouldn't be there in the storage
        print('There is nothing else here.')
        return
    print('There is something else here.')
    print('Search?y/n')
    while True:
        take = msvcrt.getwch() #Only for windows
        if(take=='y'):
            item_list[storage[storageNo]['itemID']]['taken'] = True
            print('Item Found: '+item_list[storage[storageNo]['itemID']]['name'])
            break;
        elif(take=='n'):
            print('You left the item behind.')
            break;
        else:
            print('Unknown character!')

#Safe Functions (Tile ID=5)
def safeHandler():
    getSafeItem(0)

def getSafeItem(safeNo):
    '''getStorageItem()

    '''
    global safes, item_list
    print('You found '+safes[safeNo]['name'])
    if(item_list[safes[safeNo]['itemID']]['taken']):
        #If the item has been taken, then it shouldn't be there in the storage
        print('There is nothing else here.')
        return
    if(not(safes[safeNo]['locked'])):
        print("The door is already unlocked")
        return;
    userCode = ''
    data_count = 0
    loop = True
    locked = True
    print("Enter Password:")
    while (loop):
        key = msvcrt.getwch() #Only for windows
        if (key == 'q'):
            #To exit menu
            return;
        userCode = userCode+key
        print(key, end='')
        data_count=data_count+1
        if (data_count == 4):
            if (userCode==safes[safeNo]['code']):
                print("\nUnlocked")
                loop = False
                locked = False
            else:
                print("\nIncorrect. Try Again.")
                userCode = ''
                data_count = 0
                print("Enter Password:")
    safes[safeNo]['locked']=locked
    print('There is something else here.')
    print('Search?')
    while True:
        take = msvcrt.getwch() #Only for windows
        if(take=='y'):
            item_list[safes[safeNo]['itemID']]['taken'] = True
            print('Item Found: '+item_list[safes[safeNo]['itemID']]['name'])
            break;
        elif(take=='n'):
            print('You left the item behind.')
            break;
        else:
            print('Unknown character!')

#Tile w/Desc (Tile ID=6)
def descHandler():
    if(currentRoom==0):
        if(player_Pos['row']==0):
            tileNo=0
        else:
            tileNo=1
    elif(currentRoom==2):
        tileNo=2
    else:
        if(player_Pos['row']==1):
            if(player_Pos['column']==0):
                tileNo=3
            else:
                tileNo=6
        elif(player_Pos['row']==2):
            tileNo=4
        else:
            tileNo=5
    print('You Found: '+descTile[tileNo]['name'])

#Computer (Tile ID=7)

#NPCs
#(Tile ID=8)
def Doris():
    '''Function for the NPC Doris'''
    print(f"{'Test' : >150}")

#(Tile ID=9)    
def Ellen():
    '''Function for the NPC Ellen'''

#(Tile ID=10)
def Nessie():
    '''Function for the NPC N.E.S.S.I.E'''

def Blair():
    '''Function for the NPC Doris'''
    for dialogue in strBlair1:
        delay_print(dialogue)
        #print(f"{test3 : >120}")
        next = msvcrt.getwch() #Only for windows
        clearConsole()

#Triton
#(Tile ID=11)
def Triton():
    '''
    This function is used for running the logic to finish the game.
    '''
    global stay, continueGame
    print('You Won!')
    stay = False
    continueGame = False

#Menus
def Start_Screen():
    global continueGame
    while True:
        clearConsole()
        print(title)
        print('1: Start Game')
        print('2: Controls')
        print('3: Credits')
        print('4: Exit')
        char = msvcrt.getwch() #Only for windows
        if(char=='1'):
            #print('Starting Game')
            clearConsole()
            continueGame = True
            Blair()
            break
        elif(char=='2'):
            Controls()
        elif(char=='3'):
            Credits()
        elif(char=='4'):
            print('Exiting')
            continueGame = False
            break
        else:
            print('Unknown Character')

def Credits():
    clearConsole()
    print('CREDITS')
    print(title)
    print(credits)
    print('\nPress any key to continue...')
    hold = msvcrt.getwch() #Only for windows

def Controls():
    clearConsole()
    print('''
    |++++++++++++++++++++++++++++++++++++++++++++++++++++++++|
    |     ____  ____  ____  ____  ____  ____  ____  ____     |
    |    ||C ||||O ||||N ||||T ||||R ||||O ||||L ||||S ||    |
    |    ||__||||__||||__||||__||||__||||__||||__||||__||    |
    |    |/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|    |
    |                                                        |
    |++++++++++++++++++++++++++++++++++++++++++++++++++++++++|
    |                      W: Move up                        |
    |                      A: Move left                      |
    |                      S: Move down                      |
    |                      D: Move right                     |
    |                      E: Use\Interact                   |                 
    |++++++++++++++++++++++++++++++++++++++++++++++++++++++++|
    ''')
    print('\nPress any key to continue...')
    hold = msvcrt.getwch() #Only for windows


#Main Function/Testing functions
print('Game Start')
Start_Screen()
while continueGame:
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
    clearConsole()
    Debug_Map_Display(map_Current)
    stay = True
    while (stay):
        input_char = msvcrt.getwch() #Only for windows
        Input_Handler(input_char)
        clearConsole()
        Debug_Map_Display(map_Current)
#Credits()