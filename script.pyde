#Define number of nurons in each layer

nodesHiddenidden = 12
nodesOutput =4
nodesInput = 5
sizeY = 600
sizeX = 1200


#sets up sizing and incraments

Osize = min([((((sizeY-(sizeY/10))/nodesHiddenidden)/10)*9), ((((sizeY-(sizeY/10))/nodesInput)/10)*9),((((sizeY-(sizeY/10))/nodesOutput)/10)*9)])
xIincrament = (sizeX- Osize) / 2

hiddenIincrament = ((sizeY - (sizeY / 10)) / nodesHiddenidden)
inputIincrament = ((sizeY - (sizeY / 10)) / nodesInput)
outputIincrament = ((sizeY - (sizeY / 10)) / nodesOutput)



def setup():
    size(sizeX,sizeY)
    noLoop()
    
def draw():
    xPlace = Osize/2
    ellipseMode(CENTER)
    background(255)
    hiddenIincramentHold = hiddenIincrament/2
    inputIincramentHold = inputIincrament /2
    
    
    for x in range(nodesInput):    
        ellipse(xPlace,(inputIincramentHold),Osize,Osize)

        hiddenIincramentHold = hiddenIincrament/2
        for xx in range(nodesHiddenidden):
            line(xPlace + (Osize/2),(inputIincramentHold), (xPlace +xIincrament) - (Osize/2),hiddenIincramentHold)
            hiddenIincramentHold = hiddenIincramentHold + hiddenIincrament
        inputIincramentHold= inputIincramentHold + inputIincrament
        
    xPlace = xPlace + xIincrament
    hiddenIincramentHold = hiddenIincrament/2
    
    for x in range(nodesHiddenidden):
        ellipse(xPlace,hiddenIincramentHold,Osize,Osize)
        Hold = outputIincrament /2 
        for xx in range(nodesOutput):
            line(xPlace + (Osize/2),(hiddenIincramentHold), (xPlace +xIincrament) - (Osize/2),Hold)
            Hold = Hold + outputIincrament
        hiddenIincramentHold = hiddenIincramentHold + hiddenIincrament
        
    xPlace = xPlace + xIincrament
    Hold = outputIincrament /2 
    
    for x in range(nodesOutput):
        ellipse(xPlace,(Hold),Osize,Osize)
        Hold = Hold + outputIincrament
