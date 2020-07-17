#1/user/bin/python3.8
#Filename: MonsterBattleDome.py
'''
Author: Nicholas A Zehm
Filename: MonsterBattleDome.py
7-11-20
The Monster Dueling Game
Introducing a simple gui
Version Unstable Alpha 0002
Notes:
Slowly working towards migrating to the Tk interface. I could look into using html as an alternative.

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
        gameMenu.add_command(label="Check out the monsters in the pen", command=lambda : self.showPen())
        gameMenu.add_command(label="Add a new monster to Pen", command=lambda : self.makeMonster())
        gameMenu.add_command(label="Bring monsters to the Battle Dome!", command=lambda : self.selectMonster())
        gameMenu.add_command(label="Kill monster in pen", command=lambda : self.killMonster())
        gameMenu.add_command(label="Save the pen to file", command=lambda : self.savePen())
        gameMenu.add_command(label="Load a pen from a save file", command=lambda : self.loadPen())
        gameMenu.add_command(label="Exit", command=lambda : self.client_exit)

        # Add the main menu
        menu.add_cascade(label="Main menu", menu=gameMenu)

        text = Text(root)

    def client_exit(self):
        exit()

    def showPen(self):
        if len(pen) < 1:
            output = "There are no monsters in the pen \nPerhaps you should add a few"
        else:
            for name in pen:
                obj = pen[name]
                health = obj.getHealth()
                exp = obj.getExp()
                output = output + "Name: {0} \t Health: {1} \t Experience: {2} \n".format(name, health, exp)
        text = Label(self, text = output)
        text.pack()
        
    def makeMonster(self):
        
        output = '\nLets make a monster! \n'
        name = 'bob {0}'.format(len(pen))
        health = random.randint(1,20) # make monster health
        exp = 0
        output = output + '{0} has {1} health and {2} experience'.format(name,health,exp)
        obj = Monster(health,exp) # make the monster
        pen[name] = obj # store in pen
        del obj
        print(output)
        text = Label(self, text = output)
        text.pack()

    def killMon():


        '''kills a monster in the pen'''


        if ab == 0:


            output = 'There is no-one in the pen!'
            output = output + 'Leaving the slaughterhouse...'
            text = Label(self, text = output)
            text.pack()
        showPen()


        name = input('\nWhich monster do you want to kill? : ')
 #Change this to use the window frame, maybe create a textbox here?
        if name in ab:


            kmonst = input('Are you sure you want to kill {0}, who has {1} health? '.format(name, ab[name]))


            if kmonst == 'yes':


                del ab[name]


                print('\n{0} has been killed... Its bloody corpse was eaten by the others.\n'.format(name))


                showPen()


        else:


            print('\n{0} is not in the pen!\n'.format(name))


        print('Leaving the slaughterhouse...\n')


        return main()

    def selectMonster():


        '''chooses a monster for the battle pit'''


        showPen()


        name1 = input('Choose a monster to fight in the battle dome!\n')


        if name1 in ab:


            monst1 = name1


        else:


            print('\n{0} is not in the pen!\n'.format(name1))


            return main()





        name2 = input('Choose the monster to fight {0}!\n'.format(name1))


        if name2 in ab:


            monst2 = name1


        else:


            print('\n{0} is not in the pen!\n'.format(name2))


            return main()


        print('\nEntering the battle pit!')


        return Battle(name1, name2)

    def savePen():


        '''Write pen to file'''


        f = open(penabFile, 'wb')


        pickle.dump(ab, f) # dump the object to a file


        f.close()


        text = Label(self, text = output)
        text.pack()

    def loadpen():
        '''Load pen to file'''
        f = open(penabFile, 'rb')
        ab = pickle.load(f) # load object from file


        output = '*** Pen loaded ***'
        showPen()


root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)


#mainloop 
root.mainloop()  
