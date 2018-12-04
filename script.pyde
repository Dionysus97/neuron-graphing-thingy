#Define number of nurons in each network

nodesHiddenidden = 12
nodesOutput =4
nodesInput = 5
sizeY = 600
sizeX = 1200


#sets up sizing and incraments

Osize = min([((((sizeY-(sizeY/10))/nodesHiddenidden)/10)*9), ((((sizeY-(sizeY/10))/nodesInput)/10)*9),((((sizeY-(sizeY/10))/nodesOutput)/10)*9)])
xIincrament = (sizeX- Osize) / 2

HiddenIincrament = ((sizeY - (sizeY / 10)) / nodesHiddenidden)
inputIincrament = ((sizeY - (sizeY / 10)) / nodesInput)
outputIincrament = ((sizeY - (sizeY / 10)) / nodesOutput)



def setup():
    size(sizeX,sizeY)
    noLoop()
    
def draw():
    xPlace = Osize/2
    ellipseMode(CENTER)
    background(255)
    hiddenIincramentHold = HiddenIincrament/2
    inputIincramentHold = inputIincrament /2
    
    
    for x in range(nodesInput):    
        ellipse(xPlace,(inputIincramentHold),Osize,Osize)

        hiddenIincramentHold = HiddenIincrament/2
        for xx in range(nodesHiddenidden):
            line(xPlace + (Osize/2),(inputIincramentHold), (xPlace +xIincrament) - (Osize/2),hiddenIincramentHold)
            hiddenIincramentHold = hiddenIincramentHold + HiddenIincrament
        inputIincramentHold= inputIincramentHold + inputIincrament
        
    xPlace = xPlace + xIincrament
    hiddenIincramentHold = HiddenIincrament/2
    
    for x in range(nodesHiddenidden):
        ellipse(xPlace,hiddenIincramentHold,Osize,Osize)
        outputIincramentHold = outputIincrament /2 
        for xx in range(nodesOutput):
            line(xPlace + (Osize/2),(hiddenIincramentHold), (xPlace +xIincrament) - (Osize/2),outputIincramentHold)
            outputIincramentHold = outputIincramentHold + outputIincrament
        hiddenIincramentHold = hiddenIincramentHold + HiddenIincrament

    xPlace = xPlace + xIincrament
    outputIincramentHold = outputIincrament /2 
    for x in range(nodesOutput):
        ellipse(xPlace,(outputIincramentHold),Osize,Osize)
        outputIincramentHold = outputIincramentHold + outputIincrament
