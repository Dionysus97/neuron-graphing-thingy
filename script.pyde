#Define number of nurons in each network
nodes= [6,3,3,4,5,7,4,2,1,5]

sizeY = 600
sizeX = 1200


#sets up sizing and incraments

Osize = ((((sizeY-(sizeY/10))/max(nodes))/10)*9)

xIincrament = (sizeX- Osize) / (len(nodes)-1)

def setup():
    size(sizeX,sizeY)
    noLoop()
    
def draw():
    xPlace = Osize/2
    ellipseMode(CENTER)
    background(255)
    nodes.append(1)
    
    for i in range(len(nodes)-1):
        Iincrament0 = ((sizeY - (sizeY / 10)) / nodes[i])
        Iincrament1 = ((sizeY - (sizeY / 10)) / nodes[i+1])
        IincramentHold0 = Iincrament0 /2
    
        for x in range(nodes[i]):    
            IincramentHold1 = Iincrament1 /2
            ellipse(xPlace,(IincramentHold0),Osize,Osize)

            for xx in range(nodes[i+1]):
                if i is not (len(nodes)-2):
                    line(xPlace + (Osize/2),(IincramentHold0), (xPlace +xIincrament) - (Osize/2),IincramentHold1)
                IincramentHold1 = IincramentHold1 + Iincrament1
            IincramentHold0= IincramentHold0 + Iincrament0
            
        IincramentHold0= IincramentHold0 + Iincrament0
        xPlace = xPlace + xIincrament
    
    
