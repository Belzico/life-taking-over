import PySimpleGUI as sg
import os

from numpy import size
sg.theme('Green')





LinkedTrieCheckBox  = sg.Checkbox(enable_events = True,key =  "-LINKTRIE-",text = "Linked Trie", default  = False)
TrieCkeckbox = sg.Checkbox(enable_events = True,key =  "-TRIE-",text = "Trie", default = True )
AlphaCheckbox = sg.Checkbox(enable_events = True,key =  "-INTCHECK-",text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox = sg.Checkbox(enable_events = True,key =  "-SLACKCHECK-",text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
OmitCheckbox = sg.Checkbox(enable_events = True,key =  "-SKIP-",text = "Skip unnecesary words in the search(pronouns,articles,etc...)", default = False ,  disabled=False)
SlackCheckbox2 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox3 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox4 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox5 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox6 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox7 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox8 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox9 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox10 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox11 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox12 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox13 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox14 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox15 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)
SlackCheckbox16 = sg.Checkbox(enable_events = True,text = "Is valid", checkbox_color = 'red', default = False ,  disabled=False)

currentIntpb = 0
finalIntpb = 0
progressBarMaxValue = 20000

ProgressBar = sg.ProgressBar(max_value=progressBarMaxValue,size=(50, 20))
ProgressBarText = sg.Text(str(currentIntpb) + "/" +str(finalIntpb))

file_list_column = [
    [
            sg.Text("Globals Variables:",justification="right", )  ,
    ],
    [
    sg.HSeparator(),
    ],
    [
            sg.Text("CATASTROPHY OPTIONS:",justification="right", )  ,
    ],
    [
    sg.Text("Initial Posibility of Catasrophe:",justification="right", )  ,
    sg.In(enable_events=True, key="-INITIAL CATASTROPHY POSIBILITY INPUT-",size=10),
    SlackCheckbox,
    sg.Text(" (Default: 5 )",justification="right", )  ,
    ],
    [
    sg.Text("Incremental Posibility of Catasrophe:",justification="right", )  ,
    sg.In(enable_events=True, key="-ICREMENTAL CATASTROPHY POSIBILITY INPUT-",size=10),
    SlackCheckbox2,
    sg.Text(" (Default: 2 )",justification="right", )  ,
    ],
    [
    sg.Text("Maximum Number of Catasrophes:",justification="right", )  ,
    sg.In(enable_events=True, key="-MAXIMUM NUMBER OF CATASTROPHY INPUT-",size=10),
    SlackCheckbox3,
    sg.Text(" (Default: 15 )",justification="right", )  ,
    ],
    [
    sg.Text("Maximum Category of Catasrophes:",justification="right", )  ,
    sg.In(enable_events=True, key="-MAXIMUM CATEGORY OF CATASTROPHY INPUT-",size=10),
    SlackCheckbox4,
    sg.Text(" (Default: 5 )",justification="right", )  ,
    ],
    [
    sg.HSeparator(),
    ],
    [
            sg.Text("SPECIES OPTIONS:",justification="right", )  ,
    ],
    [
    sg.Text("Amount of Species:",justification="right", )  ,
    sg.In(enable_events=True, key="-AMOUNT OF SPECIES INPUT-",size=10),
    SlackCheckbox16,
    sg.Text(" (Default: 2 )",justification="right", )  ,
    ],
    [
    sg.Text("Amount of Creatures:",justification="right", )  ,
    sg.In(enable_events=True, key="-AMOUNT OF CREATURES INPUT-",size=10),
    SlackCheckbox15,
    sg.Text(" (Default: 5 )",justification="right", )  ,
    ],
    [
    sg.Text("Evolution Possibility:",justification="right", )  ,
    sg.In(enable_events=True, key="-EVOLUTION POSIBILITY INPUT-",size=10),
    SlackCheckbox5,
    sg.Text(" (Default: 1 )",justification="right", )  ,
    ],
    [
    sg.Text("Deaths Possibility:",justification="right", )  ,
    sg.In(enable_events=True, key="-DEATHS POSIBILITY INPUT-",size=10),
    SlackCheckbox6,
    sg.Text(" (Default: 2 )",justification="right", )  ,
    ],
    [
    sg.Text("Carnivorous Possibility:",justification="right", )  ,
    sg.In(enable_events=True, key="-CARNIVOROUS POSIBILITY INPUT-",size=10),
    SlackCheckbox7,
    sg.Text(" (Default: 1 )",justification="right", )  ,
    ],
    [
    sg.Text("Weakness of Prey:",justification="right", )  ,
    sg.In(enable_events=True, key="-WEAKNESS OF PREY INPUT-",size=10),
    SlackCheckbox8,
    sg.Text(" (Default: 5 )",justification="right", )  ,
    ],
    [
    sg.Text("Combat Min-Max Predictions:",justification="right", )  ,
    sg.In(enable_events=True, key="-COMBAT PREDICTIONS INPUT-",size=10),
    SlackCheckbox9,
    sg.Text(" (Default: 3 )",justification="right", )  ,
    ],
    [
    sg.Text("Evolution Timer:",justification="right", )  ,
    sg.In(enable_events=True, key="-EVOLUTION TIMER INPUT-",size=10),
    SlackCheckbox10,
    sg.Text(" (Default: 10 )",justification="right", )  ,
    ],
    [
    sg.HSeparator(),
    ],
    [
            sg.Text("WORLD OPTIONS:",justification="right", )  ,
    ],
    [
    sg.Text("World Size:",justification="right", )  ,
    sg.In(enable_events=True, key="-WORLD SIZE INPUT-",size=10),
    SlackCheckbox11,
    sg.Text(" (Default: 10 )",justification="right", )  ,
    ],
    [
    sg.Text("Amount of Zones:",justification="right", )  ,
    sg.In(enable_events=True, key="-ZONE COUNT INPUT-",size=10),
    SlackCheckbox14,
    sg.Text(" (Default: 3 )",justification="right", )  ,
    ],
    
    [
    sg.Text("Global Incremental Time:",justification="right", )  ,
    sg.In(enable_events=True, key="-WORLD INCREMENTAL TIME INPUT-",size=10),
    SlackCheckbox12,
    sg.Text(" (Default: 1 )",justification="right", )  ,
    ],
    [
    sg.Text("Amount of Cycles:",justification="right", )  ,
    sg.In(enable_events=True, key="-AMOUNT OF CYCLES INPUT-",size=10),
    SlackCheckbox13,
    sg.Text(" (Default: 500 )",justification="right", )  ,
    ],
    
    
    
    [
        sg.HSeparator()
    ],
    [
        sg.Button(button_text="START SIMULATION",enable_events=True, key= "-SUBMIT-", size=(20,5)),
        sg.Text("Time: ", key = "-TIME-")   
    ],
    
    
    [
        #Progress Bar
    ProgressBarText,
    ProgressBar,
    ],

    
]






view_column = [
    [
    sg.Text("Final Simulation Data :", key = "-DATA SHOW-"),
    ],
    [
    sg.Multiline(s=(60,30),enable_events=True, key="-SHOW-",default_text="Here it shows all the data saved after running the simulation.",disabled=True,autoscroll=True)
    ],
    [
    sg.HSeparator()
    ],
    [
    sg.Text("Log:")
    ],
    [
        sg.Multiline(s=(60,30),enable_events=True, key="-LOG-",default_text="Execution Log:",disabled=True,autoscroll=True)
    ],
]



# result_column = [
#     [sg.Text("Results:")],
#     [sg.Text(size = (40,1),key="-TOUT-")],
#     [sg.Listbox(
#             values= [],enable_events = True,size =(40,20),
#             key = "-RESULT LIST-"
#         )],
# ]
Map_column = [

    [sg.Text("Query:")],
    [
        sg.Multiline(s=(400,20),enable_events=True, key="-QUERY-"),
    ],
    [
    sg.HSeparator()
    ],
        [sg.Text("Results:")],
    [sg.Listbox(
            values= [],enable_events = True,s=(900,40),horizontal_scroll=True,
            key = "-RESULT LIST-"
        )],
]



layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(view_column),
        # sg.VSeparator(),
        # sg.Column(Map_column),
    ]
]

print(layout)