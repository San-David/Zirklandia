# stuff to do:
#
# replace messagebox in end turn error with something that looks better
# make deliberation map functional
# add functionality for resizing
# integrate databases
# make stuff look pretty
# make countdown variable configurable

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font

class deliberationGui:
    def __init__(self, master):

        # Variables START ------------------------------------------------------
        
        # Sets countdown to 300
        # Add option to change this variable before game starts
        # Under countdownFrame
        self.countdownValue = 300

        # Change this to change height and width of map buttons
        # Default height = 5, width = 10
        # Under mapFrame
        self.heightSetting = 5
        self.widthSetting = 10

        # Sets the name displayed in each map button
        # Change this later
        # Buttons can fit 13 characters, but looks better with <= 12
        self.mapButtonStr1 = 'filler1'
        self.mapButtonStr2 = 'qwertyuiopas'
        self.mapButtonStr3 = 'filler3'
        self.mapButtonStr4 = 'filler4'
        self.mapButtonStr5 = 'qwertyuiopasd'
        self.mapButtonStr6 = 'filler6'
        self.mapButtonStr7 = 'filler7'
        self.mapButtonStr8 = 'qwertyuiopasdf'
        self.mapButtonStr9 = 'filler9'

        # Sets total and resources to some arbitrary number
        # Sets allocations to 0
        # Will move totalResources and futureResources somewhere else
        # Under diploFrame
        self.totalResources = 8
        self.totalLabelNumber = 0
        self.offenseAllocation = 0
        self.defenseAllocation = 0
        self.deterAllocation = 0
        self.futureResources = 8

        # Sets up a string variable for the diplomacy frame
        # Under diploFrame
        self.diplomacy = StringVar()

        # Variables END --------------------------------------------------------


        # Styling START --------------------------------------------------------

        # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

        # Styling END ----------------------------------------------------------


        # Frame Setup START ----------------------------------------------------

        self.master = master
        master.title("Zirklandia")
        master.resizable(FALSE, FALSE)
        
        # Creates a frame called content under master.
        # Gives gui a nice border
        self.content = ttk.Frame(master, padding=5)

        # Creates a main frame to hold all of our other frames. 
        self.mainFrame = ttk.Frame(self.content, borderwidth=5, relief="raised",
                                   padding=5)

        # Frame Setup END ------------------------------------------------------


        # Countdown Section START ----------------------------------------------
        
        # Creates a frame to hold the countdown button
        self.countdownFrame = ttk.Frame(self.mainFrame, borderwidth=5,
                                        relief="sunken")
        
        # Creates labels under mainframe, displays countdown timer.
        self.timeleftLabel = ttk.Label(self.countdownFrame, text='TIME REMAINING:')
        
        self.countdownLabel = ttk.Label(self.countdownFrame,
                                        text='%d' % self.countdownValue)

        # Countdown Section END ------------------------------------------------


        # Map Section START ----------------------------------------------------
        
        # Creates a frame to hold the map
        self.mapFrame = ttk.Frame(self.mainFrame, borderwidth=5,
                                  relief="sunken")
        
        # Creates a label for the map
        self.mapLabel = ttk.Label(self.mapFrame, text='MAP OF ZIRKLANDIA')

        # Creates a ton of buttons for the map        
        self.mapButton1 = Button(self.mapFrame,
                                 text=('%s' % self.mapButtonStr1),
                                 height=('%d' % self.heightSetting),
                                 width=('%d' % self.widthSetting))

        self.mapButton2 = Button(self.mapFrame,
                                 text=('%s' % self.mapButtonStr2),
                                 height=('%d' % self.heightSetting),
                                 width=('%d' % self.widthSetting))

        self.mapButton3 = Button(self.mapFrame,
                                 text=('%s' % self.mapButtonStr3),
                                 height=('%d' % self.heightSetting),
                                 width=('%d' % self.widthSetting))

        self.mapButton4 = Button(self.mapFrame,
                                 text=('%s' % self.mapButtonStr4),
                                 height=('%d' % self.heightSetting),
                                 width=('%d' % self.widthSetting))

        self.mapButton5 = Button(self.mapFrame,
                                 text=('%s' % self.mapButtonStr5),
                                 height=('%d' % self.heightSetting),
                                 width=('%d' % self.widthSetting))

        self.mapButton6 = Button(self.mapFrame,
                                 text=('%s' % self.mapButtonStr6),
                                 height=('%d' % self.heightSetting),
                                 width=('%d' % self.widthSetting))

        self.mapButton7 = Button(self.mapFrame,
                                 text=('%s' % self.mapButtonStr7),
                                 height=('%d' % self.heightSetting),
                                 width=('%d' % self.widthSetting))

        self.mapButton8 = Button(self.mapFrame,
                                 text=('%s' % self.mapButtonStr8),
                                 height=('%d' % self.heightSetting),
                                 width=('%d' % self.widthSetting))

        self.mapButton9 = Button(self.mapFrame,
                                 text=('%s' % self.mapButtonStr9),
                                 height=('%d' % self.heightSetting),
                                 width=('%d' % self.widthSetting))

        # Map Section END ------------------------------------------------------


        # Resource Section START -----------------------------------------------

        # Creates a frame to hold resource inputs
        self.resourceFrame = ttk.Frame(self.mainFrame, borderwidth=5,
                                       relief="sunken")

        # Creates a label to tell player their total resources
        self.totalLabel = ttk.Label(self.resourceFrame,
                                            text = 'Resources left = %d'
                                            % self.totalResources)        

        # Creates labels for offense, defense, and deterrance
        self.offenseLabel = ttk.Label(self.resourceFrame,
                                      text = 'Offense = %d'
                                      % self.offenseAllocation)

        self.defenseLabel = ttk.Label(self.resourceFrame,
                                      text = 'Defense = %d'
                                      % self.defenseAllocation)

        self.deterLabel = ttk.Label(self.resourceFrame,
                                    text = 'Deterrance = %d'
                                    % self.deterAllocation)

        # Creates a label to tell player their resources gained next turn
        self.futureLabel = ttk.Label(self.resourceFrame,
                                     text = 'Resources gained next turn = %d'
                                     % self.futureResources)

        # Creates scales for resource allocation
        self.offenseScale = ttk.Scale(self.resourceFrame, orient=HORIZONTAL,
                                      length=120, from_=0, to=self.totalResources,
                                      command=self.scaleChange)

        self.defenseScale = ttk.Scale(self.resourceFrame, orient=HORIZONTAL,
                                      length=120, from_=0, to=self.totalResources,
                                      command=self.scaleChange)

        self.deterScale = ttk.Scale(self.resourceFrame, orient=HORIZONTAL,
                                    length=120, from_=0, to=self.totalResources,
                                    command=self.scaleChange)

        # Resource Section END -------------------------------------------------


        # Diplomacy Section START ----------------------------------------------

        # Creates a frame to hold diplomacy options
        self.diploFrame = ttk.Frame(self.mainFrame, borderwidth=5,
                                    relief="sunken")

        # Creates a label for the diplomacy section.
        self.diploLabel = ttk.Label(self.diploFrame,
                                    text = 'You have selected __. Will you...')
        
        self.attackRadio = ttk.Radiobutton(self.diploFrame, variable=self.diplomacy,
                                      value='attack',
                                      text='...attack their people?')
        
        self.allianceRadio = ttk.Radiobutton(self.diploFrame, variable=self.diplomacy,
                                        value='alliance',
                                        text='...send them an alliance offer?')

        # Diplomacy Section END ------------------------------------------------

        
        # End Button START -----------------------------------------------------

        # Creates a frame to hold the 'end turn' button
        self.endFrame = ttk.Frame(self.mainFrame, borderwidth=5,
                                  relief="sunken")
        
        # Creates a button to end your turn
        self.endButton = ttk.Button(self.endFrame, text='End your turn?',
                                    command=self.endTurn)

        # End Button END -------------------------------------------------------

        
        # Widget Gridding START ------------------------------------------------

        self.content.grid(column=0, row=0, sticky=(N, S, E, W))
        self.mainFrame.grid(column=0, row=0, sticky=(N, S, E, W))

        self.countdownFrame.grid(column=0, row=0, columnspan=2, rowspan=2,
                              sticky=(N, S, E, W))
        self.timeleftLabel.grid(column=0, row=0, columnspan=2)
        self.countdownLabel.grid(column=0, row=1, columnspan=2)

        self.mapFrame.grid(column=0, row=2, rowspan=2, sticky=W)
        self.mapLabel.grid(column=0, row=0, columnspan=3, sticky=N)
        self.mapButton1.grid(column=0, row=1)
        self.mapButton2.grid(column=1, row=1)
        self.mapButton3.grid(column=2, row=1)
        self.mapButton4.grid(column=0, row=2)
        self.mapButton5.grid(column=1, row=2)
        self.mapButton6.grid(column=2, row=2)
        self.mapButton7.grid(column=0, row=3)
        self.mapButton8.grid(column=1, row=3)
        self.mapButton9.grid(column=2, row=3)

        self.resourceFrame.grid(column=1, row=2, sticky=N)
        self.totalLabel.grid(column=0, row=0, columnspan=2)
        self.offenseLabel.grid(column=0, row=1, sticky=W)
        self.defenseLabel.grid(column=0, row=2, sticky=W)
        self.deterLabel.grid(column=0, row=3, sticky=W)
        self.futureLabel.grid(column=0, row=4, columnspan=2)
        self.offenseScale.grid(column=1, row=1, sticky=E)
        self.defenseScale.grid(column=1, row=2, sticky=E)
        self.deterScale.grid(column=1, row=3, sticky=E)

        self.diploFrame.grid(column=1, row=3, sticky=N)
        self.diploLabel.grid(column=0, row=0, sticky=N)
        self.attackRadio.grid(column=0, row=1, sticky=W)
        self.allianceRadio.grid(column=0, row=2, sticky=W)

        self.endFrame.grid(column=1, row=4, sticky=E)
        self.endButton.grid(column=0, row=0, sticky=S)

        # Column and row configurations go here
        self.countdownFrame.columnconfigure(0, weight=2)

        # Widget Gridding END --------------------------------------------------


        # Start the countdown loop
        self.countdownLoop()


        # Deliberation Functions START -----------------------------------------

    # Subtracts 1 from countdown, changes label to new integer, waits, repeats
    # Disables countdownButton
    def countdownLoop(self, *args):
        self.countdownValue -= 0
        self.countdownLabel['text'] = '%d' % self.countdownValue

        # If countdownValue is 1, move on to the action phase
        if self.countdownValue < 1:
            messagebox.showinfo(title='ROUND ENDED!',
                                message='Start the action phase?')
            self.master.destroy()
        
        self.master.after(1000, self.countdownLoop)


    # Changes string values when the allocation sliders are changed    
    def scaleChange(self, *args):
        self.offenseAllocation = int(self.offenseScale.get())
        self.defenseAllocation = int(self.defenseScale.get())
        self.deterAllocation = int(self.deterScale.get())
        self.totalLabelNumber = (self.totalResources - (self.offenseAllocation +
                                                        self.defenseAllocation +
                                                        self.deterAllocation))

        self.totalLabel['text'] = 'Resources left = %d' % self.totalLabelNumber
        self.offenseLabel['text'] = 'Offense = %d' % self.offenseAllocation        
        self.defenseLabel['text'] = 'Defense = %d' % self.defenseAllocation
        self.deterLabel['text'] = 'Deterrance = %d' % self.deterAllocation
        self.futureLabel['text'] = 'Resources gained next turn = %d' % (
            self.deterAllocation + self.futureResources)


    # Closes the window
    # Will open the action phase window
    def endTurn(self, *args):
        # Will show players an ERROR if they end w/ negative resources
        if self.totalLabelNumber < 0:
            messagebox.showinfo(title='Zirklandia',
                                message="You're using more resources than you own!")
        else:
            # Check if all players have submitted scores.
            # Put a waiting screen or something here until all players have
            # submitted their scores.
            # When all players have submitted scores, destroy window and move
            # to action phase.
            
            self.master.destroy()

    # Deliberation Functions END -----------------------------------------------



class chatGui:
    def __init__(self, master):

        # Variables START ------------------------------------------------------



        # Variables END --------------------------------------------------------


        # Styling START --------------------------------------------------------



        # Styling END ----------------------------------------------------------


        # Frame Setup START ----------------------------------------------------
        
        self.master = master
        master.title("Zirklandia")
        master.resizable(FALSE, FALSE)

        # Creates a frame called content under master
        # Gives a nice border
        self.content = ttk.Frame(master, padding="5")

        # Creates a main frame to hold all of our other frames. 
        self.mainFrame = ttk.Frame(self.content, borderwidth=5, relief="raised",
                                   padding=5)

        # Frame Setup END ------------------------------------------------------


        # Chat Display START ---------------------------------------------------

        # Creates a frame to hold the chat window
        self.chatFrame = ttk.Frame(self.mainFrame, borderwidth=5,
                                   relief="sunken")



        # Chat Display END -----------------------------------------------------


        # Player List START ----------------------------------------------------

        # Creates a frame to hold the player list
        self.playerFrame = ttk.Frame(self.mainFrame, borderwidth=5,
                                     relief="sunken")



        # Player List END ------------------------------------------------------


        # Message Entry START --------------------------------------------------

        # Creates a frame to hold the message entry and button
        self.messageFrame = ttk.Frame(self.mainFrame, borderwidth=5,
                                      relief="sunken")

        # Creates an entry for players to type messages in
        self.message = StringVar()
        self.messageEntry = ttk.Entry(self.messageFrame)

        # Creates a button that sends messageEntry when clicked
        self.messageButton = ttk.Button(self.messageFrame, text="Send")

        # Message Entry END ----------------------------------------------------
        
        
        # Widget Gridding START ------------------------------------------------
        
        self.content.grid(column=0, row=0, sticky=(N, S, E, W))
        self.mainFrame.grid(column=0, row=0, sticky=(N, S, E, W))

        self.chatFrame.grid(column=0, row=0)
        
        self.playerFrame.grid(column=1, row=0)
        
        self.messageFrame.grid(column=0, row=1, columnspan=2)
        self.messageEntry.grid(column=0, row=0)
        self.messageButton.grid(column=1, row=0)

        # Widget Gridding END --------------------------------------------------


        # Chat Functions START -------------------------------------------------



        # Chat Functions END ---------------------------------------------------
        


gameRoot = Tk()
deliberationGui = deliberationGui(gameRoot)

chatRoot = Tk()
chatGui = chatGui(chatRoot)

gameRoot.mainloop()
chatRoot.mainloop()
