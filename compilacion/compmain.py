import tokenizer
import fixGrammar
import parser  


def main():
    
    TerminalList = fixGrammar.terminales
    prodList = fixGrammar.productions
    
    Grammar = fixGrammar.Grammar("program", TerminalList , prodList)
    #Read(scripti).
    script=[]
    
    tokenList = tokenizer.tokenizer(script)
    
    typesList = []
    
    for token in tokenList:
        typesList.append(token.type)
        
    parser.GOTOACTION.build()


main()