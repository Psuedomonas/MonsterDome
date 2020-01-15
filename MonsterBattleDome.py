#1/user/bin/python3.8
#Filename: MonsterBattleDome.py
'''
Author: Nicholas A Zehm
Filename: MonsterBattleDome.py
1-4-20
The Monster Dueling Game
Introducing a simple gui
Version 0001
'''

from tkinter import * #GUI
import pickle # for data save
import random # random numbers
import time # for delay ...

# The Monster Pen
pen = {}

# The Monster Object
class Monster:
    '''Initialize the monster'''
    def __init__(self, health, exp):
        self.health = health
        self.exp = exp
        self.totalhealth = health
	
    # Accesors
    def getHealth(self):
        return self.health
    
    def getExp(self):
        return self.exp
		
    def getTotalHealth(self):
        return self.totalhealth
		
    # Mutators
    def setHealth(self, health):
        self.health = health
	
    def setExp(self, exp):
        self.exp = exp

''' The GUI => using Tk '''
class Window(Frame):

    def __init__(self, master=None):
        # parameters to send to the frame class
        Frame.__init__(self, master=None)
        
        # reference to the master widget, the tk window
        self.master = master

        # run init_window
        self.init_window()


    def init_window(self):
        # changing the title of our master widget
        self.master.title("Monster Battle Dome")
		
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # create a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object
        gameMenu = Menu(menu)

        # Menu Options
        gameMenu.add_command(label="Check out the monsters in the pen", command=self.showPen)
        #gameMenu.add_command(label="Add a new monster to Pen", command=self.makeMonster)
        #gameMenu.add_command(label="Bring monsters to the Battle Dome!", command=self.selectMonster)
        #gameMenu.add_command(label="Kill monster in pen", command=self.killMonster)
        #gameMenu.add_command(label="Save the pen to file", command=self.savePen)
        #game.add_command(label="Load a pen from a save file", command=self.loadPen)
        gameMenu.add_command(label="Exit", command=self.client_exit)

        # Add the main menu
        menu.add_cascade(label="Main menu", menu=gameMenu)

        text = Text(root)

    def client_exit(self):
        exit()

def showPen(self):
    output = "" # initialize the string var
    if len(pen) < 1:
        output = "There are no monsters in the pen \nPerhaps you should add a few"
    else:
        for name in pen:
            obj = pen[name]
            health = obj.getHealth()
            exp = obj.getExp()
            output = output + "Name: {0} \t Health: {1} \t Experience: {2} \n".format(name, health, exp)
    text(INSERT, output)

def makeMonster(self):
    output = '\nLets make a monster! \n'
    name = 'bob {0}'.format(len(pen))
    health = random.randint(1,20) # make monster health
    exp = 0
    output = output + '{0} has {1} health and {2} experience'.format(name,health,exp)
    obj = Monster(health,exp) # make the monster
    pen[name] = obj # store in pen
    del obj
    text = Label(self, text = output)
    text.pack()

root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()  
    
