from tkinter import Misc
import especies
import globals
import map
import misc
import fenomeno
import PySimpleGUI as sg
from visuals.components import *
import time
import random

def worldController():
    
    
    window = sg.Window("LIFE TAKING OVER", layout,size = (1100,800),resizable = True)

    #App Loop
    while True:
        event, values = window.read()

        #EXITING
        if event=="Exit" or event == sg.WIN_CLOSED:
            window.close()
            break
        

        if event == "-INITIAL CATASTROPHY POSIBILITY INPUT-" :
            try:
                temp = float(values["-INITIAL CATASTROPHY POSIBILITY INPUT-"])
                if 0<temp<=100:
                    SlackCheckbox.Update(True)
                    SlackCheckbox.Update(checkbox_color='green')
                    globals.CatastrophyPosibility = temp
                    window["-LOG-"].write("\n"+"Initial catastrophe posibility value successfully change.")
                else:
                    SlackCheckbox.Update(False)
                    SlackCheckbox.Update(checkbox_color='red')
                    globals.CatastrophyPosibility = 5
                    pass
            except:
                SlackCheckbox.Update(False)
                SlackCheckbox.Update(checkbox_color='red')
                globals.CatastrophyPosibility = 5
                pass
        
        if event == "-ICREMENTAL CATASTROPHY POSIBILITY INPUT-" :
            try:
                temp = float(values["-ICREMENTAL CATASTROPHY POSIBILITY INPUT-"])
                if 0<temp<=100:
                    SlackCheckbox2.Update(True)
                    SlackCheckbox2.Update(checkbox_color='green')
                    globals.TurnsToCatastrophy = temp
                    window["-LOG-"].write("\n"+"Icremental catastrophe posibility value successfully change.")
                else:
                    SlackCheckbox2.Update(False)
                    SlackCheckbox2.Update(checkbox_color='red')
                    globals.TurnsToCatastrophy = 2
                    pass
            except:
                SlackCheckbox2.Update(False)
                SlackCheckbox2.Update(checkbox_color='red')
                globals.TurnsToCatastrophy = 2
                pass    
        
        if event == "-MAXIMUM NUMBER OF CATASTROPHY INPUT-" :
            try:
                temp = float(values["-MAXIMUM NUMBER OF CATASTROPHY INPUT-"])
                if 0<temp<=100:
                    SlackCheckbox3.Update(True)
                    SlackCheckbox3.Update(checkbox_color='green')
                    globals.MaxCatastrophy = temp
                    window["-LOG-"].write("\n"+"Maximum number of catastrophes posibility value successfully change.")
                else:
                    SlackCheckbox3.Update(False)
                    SlackCheckbox3.Update(checkbox_color='red')
                    globals.MaxCatastrophy = 15
                    pass
            except:
                SlackCheckbox3.Update(False)
                SlackCheckbox3.Update(checkbox_color='red')
                globals.MaxCatastrophy = 15
                pass   
                
        if event == "-MAXIMUM CATEGORY OF CATASTROPHY INPUT-" :
            try:
                temp = float(values["-MAXIMUM CATEGORY OF CATASTROPHY INPUT-"])
                if 0<temp<=100:
                    SlackCheckbox4.Update(True)
                    SlackCheckbox4.Update(checkbox_color='green')
                    globals.MaxCategory = temp
                    window["-LOG-"].write("\n"+"Maximum category of catastrophes posibility value successfully change.")
                else:
                    SlackCheckbox4.Update(False)
                    SlackCheckbox4.Update(checkbox_color='red')
                    globals.MaxCategory = 5
                    pass
            except:
                SlackCheckbox4.Update(False)
                SlackCheckbox4.Update(checkbox_color='red')
                globals.MaxCategory = 5
                pass  
        
        if event == "-EVOLUTION POSIBILITY INPUT-" :
            try:
                temp = float(values["-EVOLUTION POSIBILITY INPUT-"])
                if 0<temp<=100:
                    SlackCheckbox5.Update(True)
                    SlackCheckbox5.Update(checkbox_color='green')
                    globals.EvolutionFrequency = temp
                    window["-LOG-"].write("\n"+"Evolution possibility value of species successfully change.")
                else:
                    SlackCheckbox5.Update(False)
                    SlackCheckbox5.Update(checkbox_color='red')
                    globals.EvolutionFrequency = 1
                    pass
            except:
                SlackCheckbox5.Update(False)
                SlackCheckbox5.Update(checkbox_color='red')
                globals.EvolutionFrequency = 1
                pass  
        
        if event == "-CARNIVOROUS POSIBILITY INPUT-" :
            try:
                temp = float(values["-CARNIVOROUS POSIBILITY INPUT-"])
                if 0<temp<=100000:
                    SlackCheckbox7.Update(True)
                    SlackCheckbox7.Update(checkbox_color='green')
                    globals.Hunting = temp
                    window["-LOG-"].write("\n"+"Carnivorous possibility value of species successfully change.")
                else:
                    SlackCheckbox7.Update(False)
                    SlackCheckbox7.Update(checkbox_color='red')
                    globals.Hunting = 1
                    pass
            except:
                SlackCheckbox7.Update(False)
                SlackCheckbox7.Update(checkbox_color='red')
                globals.Hunting = 1
                pass  
        
        if event == "-WEAKNESS OF PREY INPUT-" :
            try:
                temp = float(values["-WEAKNESS OF PREY INPUT-"])
                if 0<temp<=100000:
                    SlackCheckbox8.Update(True)
                    SlackCheckbox8.Update(checkbox_color='green')
                    globals.Weakness = temp
                    window["-LOG-"].write("\n"+"Weakness of preys successfully change.")
                else:
                    SlackCheckbox8.Update(False)
                    SlackCheckbox8.Update(checkbox_color='red')
                    globals.Weakness = 10
                    pass
            except:
                SlackCheckbox8.Update(False)
                SlackCheckbox8.Update(checkbox_color='red')
                globals.Weakness = 10
                pass  
        
        if event == "-DEATHS POSIBILITY INPUT-" :
            try:
                temp = float(values["-DEATHS POSIBILITY INPUT-"])
                if 0<temp<=100000:
                    SlackCheckbox6.Update(True)
                    SlackCheckbox6.Update(checkbox_color='green')
                    globals.killerModifier = temp
                    window["-LOG-"].write("\n"+"Death possibility value successfully change.")
                else:
                    SlackCheckbox6.Update(False)
                    SlackCheckbox6.Update(checkbox_color='red')
                    globals.killerModifier = 2
                    pass
            except:
                SlackCheckbox6.Update(False)
                SlackCheckbox6.Update(checkbox_color='red')
                globals.killerModifier = 2
                pass 
        
        if event == "-COMBAT PREDICTIONS INPUT-" :
            try:
                temp = float(values["-COMBAT PREDICTIONS INPUT-"])
                if 0<temp<=100:
                    SlackCheckbox9.Update(True)
                    SlackCheckbox9.Update(checkbox_color='green')
                    globals.tempPredictions = temp
                    window["-LOG-"].write("\n"+"Amount of predictions in combat successfully change.")
                else:
                    SlackCheckbox9.Update(False)
                    SlackCheckbox9.Update(checkbox_color='red')
                    globals.tempPredictions = 3
                    pass
            except:
                SlackCheckbox9.Update(False)
                SlackCheckbox9.Update(checkbox_color='red')
                globals.tempPredictions = 3
                pass 
            
            
        if event == "-EVOLUTION TIMER INPUT-" :
            try:
                temp = float(values["-EVOLUTION TIMER INPUT-"])
                if 0<temp<=1000000:
                    SlackCheckbox10.Update(True)
                    SlackCheckbox10.Update(checkbox_color='green')
                    globals.evolutionTimeCheck = temp
                    window["-LOG-"].write("\n"+"Evolution timer successfully change.")
                else:
                    SlackCheckbox10.Update(False)
                    SlackCheckbox10.Update(checkbox_color='red')
                    globals.evolutionTimeCheck = 10
                    pass
            except:
                SlackCheckbox10.Update(False)
                SlackCheckbox10.Update(checkbox_color='red')
                globals.evolutionTimeCheck = 10
                pass 
        
                    
        if event == "-WORLD SIZE INPUT-" :
            try:
                temp = int(values["-WORLD SIZE INPUT-"])
                if 3<temp<=10000:
                    SlackCheckbox11.Update(True)
                    SlackCheckbox11.Update(checkbox_color='green')
                    globals.WorldSize = temp
                    window["-LOG-"].write("\n"+"World size successfully change.")
                else:
                    SlackCheckbox11.Update(False)
                    SlackCheckbox11.Update(checkbox_color='red')
                    globals.WorldSize = 10
                    pass
            except:
                SlackCheckbox11.Update(False)
                SlackCheckbox11.Update(checkbox_color='red')
                globals.WorldSize = 10
                pass 
        
        
        if event == "-WORLD INCREMENTAL TIME INPUT-" :
            try:
                temp = int(values["-WORLD INCREMENTAL TIME INPUT-"])
                if 1<=temp<=10000:
                    SlackCheckbox12.Update(True)
                    SlackCheckbox12.Update(checkbox_color='green')
                    globals.globalTime = temp
                    window["-LOG-"].write("\n"+"World time increments successfully change.")
                else:
                    SlackCheckbox12.Update(False)
                    SlackCheckbox12.Update(checkbox_color='red')
                    globals.globalTime = 1
                    pass
            except:
                SlackCheckbox12.Update(False)
                SlackCheckbox12.Update(checkbox_color='red')
                globals.globalTime = 1
                pass 
        
        
        if event == "-AMOUNT OF CYCLES INPUT-" :
            try:
                temp = int(values["-AMOUNT OF CYCLES INPUT-"])
                if 3<temp<=10000:
                    SlackCheckbox13.Update(True)
                    SlackCheckbox13.Update(checkbox_color='green')
                    globals.iterationCicles = temp
                    window["-LOG-"].write("\n"+"Amount of cycles successfully change.")
                else:
                    SlackCheckbox13.Update(False)
                    SlackCheckbox13.Update(checkbox_color='red')
                    globals.iterationCicles = 1000
                    pass
            except:
                SlackCheckbox13.Update(False)
                SlackCheckbox13.Update(checkbox_color='red')
                globals.iterationCicles = 1000
                pass 
        
                
        if event == "-ZONE COUNT INPUT-" :
            try:
                temp = int(values["-ZONE COUNT INPUT-"])
                if 1<temp<=globals.WorldSize:
                    SlackCheckbox14.Update(True)
                    SlackCheckbox14.Update(checkbox_color='green')
                    globals.ZoneCount = temp
                    window["-LOG-"].write("\n"+"Amount of zones successfully change.")
                else:
                    SlackCheckbox14.Update(False)
                    SlackCheckbox14.Update(checkbox_color='red')
                    globals.ZoneCount = 3
                    pass
            except:
                SlackCheckbox14.Update(False)
                SlackCheckbox14.Update(checkbox_color='red')
                globals.ZoneCount = 3
                pass 
        
        if event == "-AMOUNT OF SPECIES INPUT-" :
            try:
                temp = int(values["-AMOUNT OF SPECIES INPUT-"])
                if 1<temp<=100:
                    SlackCheckbox16.Update(True)
                    SlackCheckbox16.Update(checkbox_color='green')
                    globals.SpeciesAmount = temp
                    window["-LOG-"].write("\n"+"Amount of species successfully change.")
                else:
                    SlackCheckbox16.Update(False)
                    SlackCheckbox16.Update(checkbox_color='red')
                    globals.SpeciesAmount = 2
                    pass
            except:
                SlackCheckbox16.Update(False)
                SlackCheckbox16.Update(checkbox_color='red')
                globals.SpeciesAmount = 2
                pass 
    
        if event == "-AMOUNT OF CREATURES INPUT-" :
            try:
                temp = int(values["-AMOUNT OF CREATURES INPUT-"])
                if 1<temp<=100:
                    SlackCheckbox15.Update(True)
                    SlackCheckbox15.Update(checkbox_color='green')
                    globals.CreaturesAmount = temp
                    window["-LOG-"].write("\n"+"Amount of creatures successfully change.")
                else:
                    SlackCheckbox15.Update(False)
                    SlackCheckbox15.Update(checkbox_color='red')
                    globals.CreaturesAmount = 5
                    pass
            except:
                SlackCheckbox15.Update(False)
                SlackCheckbox15.Update(checkbox_color='red')
                globals.CreaturesAmount = 5
                pass 
        
        



        if event == "-SUBMIT-":
            
            start =time.time()
            
            globals.worldMap=map.Map(globals.WorldSize,globals.WorldSize,globals.ZoneCount)
            
            for i in range(globals.SpeciesAmount):
                especies.Especies(globals.CreaturesAmount,random.randint(0,globals.WorldSize-1),random.randint(0,globals.WorldSize-1))
            
            
            #globals.allSpecies["1"].ModifyCaracteristic("Vida",100) #ej de modify
            especies.Especies.initSpecies()
            
            window["-SHOW-"].update("Here it shows all the data saved after running the simulation.")
            window["-LOG-"].write("\n"+"Begin Simulation!!!!!---------------------------------")
            
            
            
            
            while (globals.iterationCicles>=globals.globalTime):

                ProgressBarText.Update(value = (str(globals.globalTime) + "/" +str(globals.iterationCicles)))
                
                increments = progressBarMaxValue/globals.iterationCicles
                ProgressBar.Update(current_count=globals.globalTime*increments)
                value=''
                for val in globals.worldIndividuals:
                    value=globals.worldIndividuals[val]
                    tempMap=globals.worldMap.movementMatrix(value) 
                    value.resolveIteration(tempMap)


                misc.dieList()
                misc.bornList()

                if globals.globalTime%globals.evolutionTimeCheck == 0:
                    for h in  globals.worldMap.Zones:
                        for j in globals.allSpecies.keys():
                            h.startEvolving(globals.allSpecies[j])

                fenomeno.Euristics(globals.worldMap)
                for n in globals.CatastrophyList:
                    n.Executing()

                for item in globals.waitSpeciesList:
                    globals.allSpecies[item[0]]=item[1]

                globals.waitSpeciesList=[]

                
                window["-LOG-"].write("\n"+"---------------------------------CYCLE "+str(globals.globalTime)+"-------------------------------------------------")
                globals.globalTime+=1
                print('---------------------------------NEW CYCLE-------------------------------------------------')
                #####################################    
                #####################################
            window["-LOG-"].write("\n"+"Simulation finished!!!!!")
            
            end =time.time()
            
            window["-TIME-"].update("Time: " + str(misc.round_half_up(end-start,5)) +" sec.")
            
            printData(window)
            
            misc.reset()
            print("Simulation finished!!!!!")        



def printData(window):
    for speciesKey in globals.allSpecies.keys():
        window["-SHOW-"].write("\n")
        window["-SHOW-"].write("\n")
        window["-SHOW-"].write("\n")
        window["-SHOW-"].write("\n Writing data of species:"+str(globals.allSpecies[speciesKey])+"---------------------------------")
        for datakey in globals.allSpecies[speciesKey].dataDicc.keys():
            window["-SHOW-"].write("\n"+str(datakey)+ " : " + str(globals.allSpecies[speciesKey].dataDicc[datakey]))
    
    
    pass



def main():
    # globals.worldMap=map.Map(10,10,5)
    # especies.Especies(5,0,0)
    # especies.Especies(5,0,0)

    
    print("star world")
    worldController()
    
main()
    
