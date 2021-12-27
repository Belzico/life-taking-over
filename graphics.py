from tkinter import *
from tkinter import ttk
import globals
import zones
import map

#El color de la zona
ZoneRGB = {'Prairie': "green" ,  'Mountain': "brown", 'Ocean': "blue"}

class GraphicController:
    def __init__(self):
        self.root = Tk()
        self.root.title('Life Taking Over')
        # self.root.geometry("800x600")
        self.root.resizable(0,0)
 
        
        
        
        
        
        
        
        
        
        
        
        
        
    #Este fue un intento de crear un Mapa con un array de Canvas    
    #     # wrapper1= LabelFrame(self.root)
    #     # wrapper2= LabelFrame(self.root)
        
    #     # myCanvas = Canvas(wrapper1)
    #     # myCanvas.pack(side = LEFT)
    #     # yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical",command= myCanvas.yview)
    #     # yscrollbar.pack(side=RIGHT, fill='y')
        
    #     main_frame = LabelFrame(self.root, padx=50 , pady= 50, height=600,width=600)
    #     main_frame.grid(row=0,column=0 ,padx=20,pady=10)
    #     main_frame.configure(height= main_frame["height"],width= main_frame["width"])
    #     main_frame.grid_propagate(0)
    #     main_frame.pack_propagate(0)
        
        
    #     main_frame.
        
    #     main_Canvas = Canvas(main_frame)
    #     main_Canvas.pack(side=BOTTOM,fill = BOTH)
        

        
    #     # self.OutsideFrame = LabelFrame(main_Canvas, text = "Mapa",padx= 0,  pady=0,height=600,width=600)
    #     # self.OutsideFrame.pack(padx=10 , pady= 10)
    #     # self.OutsideFrame.configure(height= self.OutsideFrame["height"],width= self.OutsideFrame["width"])
    #     # self.OutsideFrame.grid_propagate(0)
    #     # self.OutsideFrame.pack_propagate(0)
    #     horizontalScrollbar = ttk.Scrollbar(main_frame, orient= "horizontal",command=main_Canvas.xview)
    #     horizontalScrollbar.pack(side=TOP,fill=X)
    
    
        
        
    #     self.MapFrame = LabelFrame(main_Canvas ,padx= 20,text="Mapa",  pady=20,height=300,width=300)
    #     # self.MapFrame.configure(height=  self.MapFrame["height"],width=  self.MapFrame["width"])
    #     # self.MapFrame.grid_propagate(0)
    #     # self.MapFrame.pack_propagate(0)
    #     self.MapFrame.pack()   
        
    #     # wrapper1.pack(fill="both",expand="yes",padx= 10, pady=10)
    #     # wrapper2.pack(fill="both",expand="yes",padx= 10, pady=10)
   

      
                


        
    #     self.ContrllerFrame = LabelFrame(self.root, text = "Controlador",padx= 10, pady=10,height=600,width=800)
    #     self.ContrllerFrame.grid(row= 0, column= 1, padx=50 , pady= 50)
    #     self.ContrllerFrame.configure(height=  self.ContrllerFrame["height"],width=  self.ContrllerFrame["width"])
    #     self.ContrllerFrame.grid_propagate(0)
      
    
        
        
    #     self.ButtonFrame = LabelFrame( self.ContrllerFrame,text = "Botones",height=450,width=200)
    #     self.ButtonFrame.grid(row= 0, column= 0, padx=50 , pady= 50)
    #     self.ButtonFrame.configure(height=  self.ButtonFrame["height"],width=  self.ButtonFrame["width"])
    #     self.ButtonFrame.grid_propagate(0)
    #     self.ButtonFrame.propagate(0)
    #     self.ButtonNext = Button(self.ButtonFrame, anchor= "center", text="Siguiente Ciclo")
    #     self.ButtonNext.pack()
        
    #     self.LogFrame = LabelFrame(self.ContrllerFrame, text = "Log",padx= 10, pady=10,height=450,width=400)
    #     self.LogFrame.configure(height=  self.LogFrame["height"],width=  self.LogFrame["width"])
    #     self.LogFrame.grid_propagate(0)
    #     self.LogFrame.grid(row= 0, column= 1, padx=50 , pady= 50)
    #     self.LogFrame.propagate(0)
        
    #     self.populateMap()
        
    #     self.root.mainloop()
        
        
    # def populateMap(self):
    #     self.CanvasList = []
        
    #     for i in globals.worldMap.Tiles:
    #         for j in i:
    #             temp = Canvas(self.MapFrame,width=80,height=80,bg= ZoneRGB[j.Zone.ZoneType])
    #             temp.grid(row = j.Coordinates[0],column = j.Coordinates[1],padx=5,pady=5)
    #             self.CanvasList.append(temp)
            
            
       
        




class MapGraphics:
    def __init__(self, map):
        return
      
        
    def updateMap(slef):
        return



class TileGraphics:
    def __init__(self, Tile):
        self.Canvas = Canvas
        
        
        
        

class IndividuoGrahpics:
    def __init__(self):
        return
    
class SpeciesGraphics:
    def __init__(self):
        return
    
    