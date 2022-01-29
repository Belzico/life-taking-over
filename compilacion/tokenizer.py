import compGlobals
import tokens




def readString(chain,currentPos,mytokens,line,column):
    currentToken=""
    currentPos+=1
    while currentPos<len(chain):
        if chain[currentPos]=="\"":
            break
        currentToken+=str(chain[currentPos])
    mytokens.append(tokens.Token(compGlobals.TokeTypes.tokString),line,column)
    return currentPos

def readAlphaNumeric(chain,currentPos,mytokens,line,column):
    currenToken=chain[currentPos]
    currentPos+=1
    while currentPos<len(chain):
        if chain[currentPos].isalpha() or chain[currentPos].isnumeric() or chain[currentPos]=="_":
            currenToken+=chain[currentPos]
        currentPos+=1
    if currentPos!=" ":
        #error
        return -1
    if currenToken in compGlobals.keywordsDic:
        tempType=compGlobals.keywordsDicc[currenToken]
        mytokens.append(tempType,line,column,currenToken)
    else:    
        mytokens.append(tokens.Token(compGlobals.TokeTypes.tokID),line,column)
    
    return currentPos

def readNumeric(chain, currentPos,mytokens,line,column):
    point=0
    currentToken=chain[currentPos]
    currentPos+=1
    while currentPos<len(chain):
        if chain[currentPos]==".":
            if point==1:
                #error
                return -1
            else:
                currentToken+=chain[currentPos]
        elif chain[currentPos].isnumeric():
            currentToken+=chain[currentPos]
        else: 
            break
        currentPos+=1
    
    if chain[currentPos]!=" ":
        #error 
        return-1
    
    if point==0:
        mytokens.append(tokens.Token(compGlobals.TokeTypes.tokInt),line,column,currentToken)
    else:
        mytokens.append(tokens.Token(compGlobals.TokeTypes.tokDouble),line,column,currentToken)
    return currentPos



def readComment(chain,currentPos):
    while currentPos<len(chain):
        currentPos+=1
        if chain[currentPos]=="\n":
            return currentPos
        currentPos+=1

def tokenizer(chain):
    line =1
    column=1
    currentPos=0
    initialPos=0
    currentToken=""
    mytokens=[]
    parenthesis=0
    squareBracket=0
    brackect=0
    
    
    while currentPos<len(chain):
        currentToken=chain[currentPos]
        if currentToken==" ":
            pass
        elif currentToken=="}":
            brackect-=1
            mytokens.append(tokens.Token(compGlobals.TokeTypes.tokClosedBracket),line,column)
        elif currentToken=="]":
            squareBracket-=1
            mytokens.append(tokens.Token(compGlobals.TokeTypes.tokClosedSquareBracket),line,column)
        elif currentToken==")":
            parenthesis-=1
            mytokens.append(tokens.Token(compGlobals.TokeTypes.tokClosedParen),line,column)
        elif currentToken=="{":
            brackect+=1
            mytokens.append(tokens.Token(compGlobals.TokeTypes.tokOpenBracket),line,column)
        elif currentToken=="[":
            squareBracket+=1
            mytokens.append(tokens.Token(compGlobals.TokeTypes.tokOpenBracket),line,column)
        elif currentToken=="(":
            parenthesis+=1
            mytokens.append(tokens.Token(compGlobals.TokeTypes.tokOpenParen),line,column)
        
        elif currentToken=="\n":
            line+=1
            column=0
        elif currentToken=="#":
            currentPos=readComment(chain,currentPos)-1
        elif currentToken.isnumeric():
            numericResult=readNumeric(chain,currentPos,mytokens,line,column)
            if numericResult==-1:
                #error wrong number
                pass
            else:
                currentPos=numericResult-1
        elif currentToken.isalpha():
            alphaResult=readAlphaNumeric(chain,currentPos,mytokens,line,column)-1
            if alphaResult==-1:
                #error wrong number
                pass
            else:
                currentPos=numericResult-1
        elif currentToken=="\"":
            stringResult=readString(chain,currentPos,mytokens,line,column)
        elif currentToken in compGlobals.operatorsDicc:
            tempType=compGlobals.operatorsDicc[currentToken]
            mytokens.append(tempType,line,column,currentToken)
        
        else:
            #error
            pass
                    
        currentPos+=1
        column+=currentPos-initialPos
        initialPos=currentPos
        balanceEverything(parenthesis,squareBracket,brackect)
        
        
def balanceEverything(parenthesis, squareBracket, brackect):
    if parenthesis!=0:
        #error
        pass
    if squareBracket!=0:
        #error
        pass
    if brackect!=0:
        #error
        pass