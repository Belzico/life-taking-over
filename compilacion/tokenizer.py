from logging import error
import compGlobals
import tokens
import compErrors

def readOperator(chain,currentPos,mytokens,line,column):
    currentToken=chain[currentPos]
    currentPos+=1
    
    while currentPos<len(chain):
        tempOperator=currentToken+chain[currentPos]
        if tempOperator in compGlobals.operatorsDicc:
            currentPos+=1
            currentToken+=chain[currentPos]
    tempType=compGlobals.operatorsDicc[currentToken]
    mytokens.append(tokens.Token(tempType),line,column)
    
    return currentPos

def readString(chain,currentPos,mytokens,line,column):
    currentToken=chain[currentPos]
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
        compGlobals.errorsList.append(compErrors.CompError("Wrong alphanumeric token declared",line,column))
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
                compGlobals.errorsList.append(compErrors.CompError("Wrong number token declared",line,column))
                return -1
            else:
                currentToken+=chain[currentPos]
        elif chain[currentPos].isnumeric():
            currentToken+=chain[currentPos]
        else: 
            break
        currentPos+=1
    
    if chain[currentPos]!=" ":
        compGlobals.errorsList.append(compErrors.CompError("Wrong numer token declared",line,column)) 
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
            numericResult=readNumeric(chain,currentPos,mytokens,line,column)-1
            if numericResult<=-1:
                return None
            else:
                currentPos=numericResult-1
        elif currentToken.isalpha():
            alphaResult=readAlphaNumeric(chain,currentPos,mytokens,line,column)-1
            if alphaResult==-1:
                return None
            else:
                currentPos=alphaResult-1
        elif currentToken=="\"":
            stringResult=readString(chain,currentPos,mytokens,line,column)
        elif currentToken in compGlobals.operatorsDicc :
            currentPos=readOperator(chain,currentPos,mytokens,line,column)-1
        else:
            compGlobals.errorsList.append(compErrors.CompError("Unexpected token",line,column)) 
            return None
                    
        currentPos+=1
        column+=currentPos-initialPos
        initialPos=currentPos
        if balanceEverything(parenthesis,squareBracket,brackect):
            return mytokens
        return None
        
        
        
def balanceEverything(parenthesis, squareBracket, brackect):
    if parenthesis!=0:
        compGlobals.errorsList.append(compErrors.CompError("Unbalance parenthesis",-1,-1)) 
        return -1
    if squareBracket!=0:
        compGlobals.errorsList.append(compErrors.CompError("Unbalance squareBracket",-1,-1)) 
        return -1
    if brackect!=0:
        compGlobals.errorsList.append(compErrors.CompError("Unbalance brackect",-1,-1)) 
        return -1