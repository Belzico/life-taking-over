from tkinter import *
import globals
import zones
import map

class MapGraphics:
    def __init__(self, map):
      
        # Create an instance of tkinter frame or window
        win=Tk()

        # Set the size of the tkinter window
        win.geometry("700x350")

        # Create a canvas widget
        canvas=Canvas(win, width=500, height=300)
        canvas.pack()

        # Add a line in canvas widget
        for i in range(map.SizeX):
            for j in range(map.SizeY):
                pass
                
       
        return
      
        
    def updateMap(slef):
        return



class TileGraphics:
    def __init__(self):
        return


class IndividuoGrahpics:
    def __init__(self):
        return
    
class SpeciesGraphics:
    def __init__(self):
        return
    
    