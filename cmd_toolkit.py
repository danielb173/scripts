import tkinter as tk
import pyperclip 

class Window:
    def __init__(self, master):
        # Create a custom font with size 16
        custom_font = ("Major Mono Display", 14)

        # Create a frame with specified width and height
        mainframe = tk.Frame(master, width=125, height=0)
        mainframe.pack()

        # Configure the custom font for all widgets
        master.option_add("*Font", custom_font)

        # Create a menu bar for the main frame
        mainmenu = tk.Menu(mainframe)
        # Configure the master window to use the created menu bar
        master.config(menu=mainmenu)
        # Store a reference to the master window as an attribute in the class instance
        self.master = master
        # Create a menu for the "Commands" cascade in the menu bar
        commandmenu = tk.Menu(mainframe, tearoff=0)

        # Commands go here
        diagmenu = tk.Menu(mainframe, tearoff=0)
        diagmenu.add_command(label="Command One", command=self.CommandOne)
        diagmenu.add_command(label="Command Two", command=self.CommandTwo)
        diagmenu.add_command(label="Command Three", command=self.CommandThree)

        breakfixmenu = tk.Menu(mainframe, tearoff=0)
        breakfixmenu.add_command(label="Command Four", command=self.CommandFour)
        breakfixmenu.add_command(label="Command Five", command=self.CommandFive)
        breakfixmenu.add_command(label="Command Six", command=self.CommandSix)

        networkingmenu = tk.Menu(mainframe, tearoff=0)
        networkingmenu.add_command(label="Command Seven", command=self.CommandSeven)
        networkingmenu.add_command(label="Command Eight", command=self.CommandEight)
        networkingmenu.add_command(label="Command Nine", command=self.CommandNine)

        consolesmenu = tk.Menu(mainframe, tearoff=0)
        consolesmenu.add_command(label="Command Ten", command=self.CommandTen)
        consolesmenu.add_command(label="Command Eleven", command=self.CommandEleven)
        consolesmenu.add_command(label="Command Twelve", command=self.CommandTwelve)

        # To add more menu options you need to add another commandmenu.add_cascade(label="New Name", menu=NewNamemenu and then above, add the menu in the same way as the others but change the command labels.
        mainmenu.add_cascade(label="Commands", menu=commandmenu)
        commandmenu.add_cascade(label="Diagnostics", menu=diagmenu)
        commandmenu.add_cascade(label="Breakfix", menu=breakfixmenu)
        commandmenu.add_cascade(label="Networking", menu=networkingmenu)
        commandmenu.add_cascade(label="Consoles", menu=consolesmenu)

        # Get the current position of the cursor
        cursor_x, cursor_y = master.winfo_pointerxy()

        # Set the initial position of the window
        root.geometry(f"+{cursor_x}+{cursor_y}")

    # This is where the commands will go, added as functions, in this demo we have commands labelled One to Twelve. So we will need to define all Twelve commands as functions below.
    def CommandOne(self):
        text_to_copy = "THIS IS COMMAND ONE"
        pyperclip.copy(text_to_copy)
        print(f'Text "{text_to_copy}" copied to clipboard')
        self.master.destroy() # Once the command is saved to clipboard the app will close

    def CommandTwo(self):
        text_to_copy = "THIS IS COMMAND TWO"
        pyperclip.copy(text_to_copy)
        print(f'Text "{text_to_copy}" copied to clipboard')
        self.master.destroy() # Once the command is saved to clipboard the app will close

    def CommandThree(self):
        text_to_copy = "THIS IS COMMAND THREE"
        pyperclip.copy(text_to_copy)
        print(f'Text "{text_to_copy}" copied to clipboard')
        self.master.destroy() # Once the command is saved to clipboard the app will close

    def CommandFour(self):
        text_to_copy = "THIS IS COMMAND FOUR"
        pyperclip.copy(text_to_copy)
        print(f'Text "{text_to_copy}" copied to clipboard')
        self.master.destroy() # Once the command is saved to clipboard the app will close
    
    def CommandFive(self):
        text_to_copy = "THIS IS COMMAND FIVE"
        pyperclip.copy(text_to_copy)
        print(f'Text "{text_to_copy}" copied to clipboard')
        self.master.destroy() # Once the command is saved to clipboard the app will close

    def CommandSix(self):
        text_to_copy = "THIS IS COMMAND SIX"
        pyperclip.copy(text_to_copy)
        print(f'Text "{text_to_copy}" copied to clipboard')
        self.master.destroy() # Once the command is saved to clipboard the app will close
    
    def CommandSeven(self):
        text_to_copy = "THIS IS COMMAND SEVEN"
        pyperclip.copy(text_to_copy)
        print(f'Text "{text_to_copy}" copied to clipboard')
        self.master.destroy() # Once the command is saved to clipboard the app will close

    def CommandEight(self):
        text_to_copy = "THIS IS COMMAND EIGHT"
        pyperclip.copy(text_to_copy)
        print(f'Text "{text_to_copy}" copied to clipboard')
        self.master.destroy() # Once the command is saved to clipboard the app will close

    def CommandNine(self):
        text_to_copy = "THIS IS COMMAND NINE"
        pyperclip.copy(text_to_copy)
        print(f'Text "{text_to_copy}" copied to clipboard')
        self.master.destroy() # Once the command is saved to clipboard the app will close

    def CommandTen(self):
        text_to_copy = "THIS IS COMMAND TEN"
        pyperclip.copy(text_to_copy)
        print(f'Text "{text_to_copy}" copied to clipboard')
        self.master.destroy() # Once the command is saved to clipboard the app will close

    def CommandEleven(self):
        text_to_copy = "THIS IS COMMAND ELEVEN"
        pyperclip.copy(text_to_copy)
        print(f'Text "{text_to_copy}" copied to clipboard')
        self.master.destroy() # Once the command is saved to clipboard the app will close

    def CommandTwelve(self):
        text_to_copy = "THIS IS COMMAND TWELVE"
        pyperclip.copy(text_to_copy)
        print(f'Text "{text_to_copy}" copied to clipboard')
        self.master.destroy() # Once the command is saved to clipboard the app will close

root = tk.Tk()
root.title("")  # Remove the title text
window = Window(root)
root.mainloop()



