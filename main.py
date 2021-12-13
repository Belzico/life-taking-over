import especies
import globals


def main():
    globals.allSpecies["Alfie"]=especies.Alfie()
    current=globals.allSpecies["Alfie"]
    current.individuos["Alfie1"].breed()
    print(len(current.individuos))
    
    
main()