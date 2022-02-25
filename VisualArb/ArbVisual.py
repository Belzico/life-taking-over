import tkinter as tk


def VisualArb():
    visual = VisualApk("Arbol Evolutivo")
    
    frameDraw = tk.Frame()
    
    RunVisual(visual)

def RunVisual(visual):
    visual.mainloop()    

def VisualApk(title = "", resiable = (False,False), ico = None, geometry = (650,350)):
    #-------- Iniciando visual ----------- #
    visual = tk.Tk()
    
    #-------- Configuracion--------------- #
    visual.title(title)
    visual.resizable(resiable[0],resiable[1])
    
    if ico != None:
        visual.iconbitmap(ico)
        
    geometrytext = geometry[0]+"x"+geometry[1]
    
    visual.geometry(geometrytext)
    
    return visual

VisualArb()