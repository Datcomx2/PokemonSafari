import tkinter as tk
import random
#All the extra credit is there.

#FIRST: Implement and test your Pokemon class below
class Pokemon:
    def __init__(self,name,dex,catch_rate,speed):
        self.name = name
        self.dex = int(dex)
        self.catch_rate = int(catch_rate)
        self.speed = int(speed)
        
    def __str__(self):
        return str(self.name)

#NEXT: Complete the class definition provided below
class SafariSimulator(tk.Frame):
    def __init__(self, master=None):
        print("In SafariSimulator init")
        fp = open('pokedex.csv')
        read = fp.readlines()
        self.countball = 30
        self.caught_pokemon = []
        self.pokelist = []
        self.throw_rock = 0
        self.throw_bait = 0
        self.angry_ch = 0
        self.eat = 0
        for line in read[1:]:
            i = line.split(",")
            name = i[1]
            dex = i[0]
            catch_rate = i[2]
            speed = i[3]
            p = Pokemon(name, dex, catch_rate, speed)
            self.pokelist.append(p)
        self.cp = random.choice(self.pokelist)
        self.tb = min(int(self.cp.catch_rate) +1, 151) / 449.5

    
        

            
        #Read in the data file from pokedex.csv at some point here
        #It's up to you how you store and handle the data 
        #(e.g., list, dictionary, etc.),
        #but you must use your Pokemon class in some capacity

        #Initialize any instance variables you want to keep track of

        #DO NOT MODIFY: These lines set window parameters and create widgets
        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=200)
        master.maxsize(width=275, height=500)
        master.title("Safari Zone Simulator")
        self.pack()
        self.createWidgets()

        #Call nextPokemon() method here to initialize your first random pokemon
        self.nextPokemon()

    def createWidgets(self):
        print("In createWidgets")
        #See the image in the instructions for the general layout required
        #"Run Away" button has been completed for you as an example:
        self.ThrowButton = tk.Button(self)
        self.ThrowButton["text"] = "Throw Safari Ball ("  + str(self.countball) + " left)"
        self.ThrowButton["command"] = self.throwBall
        self.ThrowButton.grid(row=0, column=0)

        self.baitButton = tk.Button(self)
        self.baitButton["text"] = "Throw Bait"
        self.baitButton["command"] = self.throwBait
        self.baitButton.grid(row=0, column=1)

        
        self.runButton = tk.Button(self)
        self.runButton["text"] = "Run Away"
        self.runButton["command"] = self.nextPokemon
        self.runButton.grid(row=1, column=1)

        self.rockButton = tk.Button(self)
        self.rockButton["text"] = "Throw Rock"
        self.rockButton["command"] = self.throwRock
        self.rockButton.grid(row=1, column=0)
        
        #You need to create an additional "throwButton"
        #A label for status messages has been completed for you as an example:
        self.messageLabel = tk.Label(bg="grey")
        self.messageLabel.pack(fill="x", padx=5, pady=5)

        #You need to create two additional labels:
        self.photolabel = tk.Label(bg="white")
        self.photolabel.pack(fill="x", padx=5, pady=5)
        
        
        self.chanceLabel = tk.Label(bg="grey")
        self.chanceLabel.pack(fill="x", padx=5, pady=5)

        self.runLabel = tk.Label(bg="grey")
        self.runLabel.pack(fill="x", padx=5, pady=5)

        #Complete and pack the pokemonImageLabel here.

        #Complete and pack the catchProbLabel here.

    def nextPokemon(self):
        print("In nextPokemon")
        self.cp = random.choice(self.pokelist)
        self.tb = (((min(self.cp.catch_rate +1, 151)) / 449.5))
        print(self.tb)
        r =  2*(int(self.cp.speed))/256
        self.throw_rock = 0
        self.throw_bait = 0
        self.angry_ch = 0
        self.runLabel["text"] = "The chance of running away is " + str(int(r*100)) + "%"
        self.chanceLabel["text"] = "Your chance of catching it is " + str(round(self.tb*100)) + "%"
        self.messageLabel['text'] = "You encounter a wild " + str(self.cp.name)
        self.sprite = tk.PhotoImage(file = "sprites/" + str(self.cp.dex) + ".gif")
        self.photolabel["image"] = self.sprite
        
        #This method must:
            #Choose a random pokemon
            #Get the info for the appropriate pokemon
            #Ensure text in messageLabel and catchProbLabel matches the pokemon
            #Change the pokemonImageLabel to show the right pokemon

        #Hint: to see how to create an image, look at the documentation 
        #for the PhotoImage/Label classes in tkinter.
        
        #Once you generate a PhotoImage object, it can be displayed 
        #by setting self.pokemonImageLabel["image"] to it
        
        #Note: the PhotoImage object MUST be stored as an instance
        #variable for some object (you can just set it to self.photo).
        #Not doing this will, for weird memory reasons, cause the image 
        #to not be displayed.
        
    def throwBall(self):
       print("In throwBall")
       attempt = random.uniform(0,1)
       print(attempt)
       if attempt < self.tb:
           self.countball -= 1
           self.ThrowButton["text"] = "Throw Safari Ball ("  + str(self.countball) + " left)"
           self.caught_pokemon.append(self.cp.name)
           if self.countball == 0:
               self.endAdventure()
           else:
               self.nextPokemon()
               
       elif attempt > self.tb:
           self.countball -= 1
           rand = random.uniform(0,1)
           self.poke_run = 2*(int(self.cp.speed))/256
           self.ThrowButton["text"] = "Throw Safari Ball ("  + str(self.countball) + " left)"
           self.messageLabel['text'] = "Aargh! It escaped!"
           if self.countball == 0:
               self.endAdventure()
           elif rand > self.poke_run:
               print ("hello")
               self.nextPokemon()
               self.runLabel["text"] = "Aargh! It ran away!"

    def throwRock(self):
        print("rock")
        self.angry_ch = random.randint(1,5)
        self.angry_ch += self.angry_ch
        if self.angry_ch > 0:   
            rand = random.uniform(0,1)
            self.poke_run = min(255, 4*(self.cp.speed)/256)
            self.throw_rock += 1
            self.tb = int(2**self.throw_rock)*self.tb
            print(self.tb)
            self.runLabel["text"] = "The chance of running away is " + str(int(self.poke_run*100)) + "%"
            self.chanceLabel["text"] = "Your chance of catching it is " + str(round(self.tb*100)) + "%"
            if self.tb*100 > round((151/449.5)*100):
                self.tb = round((151/449.5)*100)
                self.chanceLabel["text"] = "Your chance of catching it is " + str(self.tb) + "%"
            if rand < self.poke_run:
                self.nextPokemon()
                self.runLabel["text"] = "Aargh! It ran away!"
        else:
            self.tb = min(int(self.cp.catch_rate) +1, 151) / 449.5
            self.poke_run = 2*(int(self.cp.speed))/256

    def throwBait(self):
        print("Bait")
        self.eat = random.randint(1,5)
        self.eat += self.eat
        if self.eat > 0:
            self.throw_bait += 1
            rand = random.uniform(0,1)
            self.tb = (.5**self.throw_bait)*(min(int(self.cp.catch_rate) +1, 151) / 449.5)
            self.poke_run = (int(self.cp.speed)/2)/256
            self.chanceLabel["text"] = "Your chance of catching it is " + str(round(self.tb*100)) + "%"
            self.runLabel["text"] = "The chance of running away is " + str(int(self.poke_run*100)) + "%"
            if rand < self.poke_run:
                self.nextPokemon()
                self.runLabel["text"] = "Aargh! It ran away!"
        else:
            self.tb = min(int(self.cp.catch_rate) +1, 151) / 449.5
            self.poke_run = 2*(int(self.cp.speed))/256
                
            
        
        
        
        

        
           
            #This method must:

            #Decrement the number of balls remaining
            #Try to catch the pokemon
            #Check to see if endAdventure() should be called

        #To determine whether or not a pokemon is caught, generate a random
        #number between 0 and 1, using random.random().  If this number is
        #less than min((catchRate+1), 151) / 449.5, then it is caught. 
        #catchRate is the integer in the Catch Rate column in pokedex.csv, 
        #for whatever pokemon is being targetted.
        
        #Don't forget to update the throwButton's text to reflect one 
        #less Safari Ball (even if the pokemon is not caught, it still 
        #wastes a ball).
        
        #If the pokemon is not caught, you must change the messageLabel
        #text to "Aargh! It escaped!"
        
        #Don't forget to call nextPokemon to generate a new pokemon 
        #if this one is caught.
        
    def endAdventure(self):
        print("In endAdventure")
        self.runButton.pack_forget()
        self.ThrowButton.pack_forget()
        self.photolabel.pack_forget()
        self.rockButton.pack_forget()
        self.runLabel.pack_forget()
        
        self.messageLabel['text'] = "You're all out of balls, hope you had fun!"
        self.chanceLabel['text'] = "You caught " + str(len(self.caught_pokemon)) + " Pokemon: \n"
        for i in self.caught_pokemon:
            self.chanceLabel['text'] += i + "\n"
        
        #This method must: 

            #Display adventure completion message
            #List captured pokemon

        #Hint: to remove a widget from the layout, you can call the 
        #pack_forget() method.
        
        #For example, self.pokemonImageLabel.pack_forget() removes 
        #the pokemon image.




#DO NOT MODIFY: These lines start your app
app = SafariSimulator(tk.Tk())
app.mainloop()
