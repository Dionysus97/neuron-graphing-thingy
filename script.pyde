nodesH = 12
nodesE =4
nodesI = 5
sizey = 600
sizex = 1200
CS = min([((((sizey-(sizey/10))/nodesH)/10)*9), ((((sizey-(sizey/10))/nodesI)/10)*9),((((sizey-(sizey/10))/nodesE)/10)*9)])
crep = (sizex- CS) / 2

Hinc = ((sizey - (sizey / 10)) / nodesH)
Iinc = ((sizey - (sizey / 10)) / nodesI)
Einc = ((sizey - (sizey / 10)) / nodesE)

def setup():
    size(sizex,sizey)
    noLoop()
    
def draw():
    sC = CS/2
    ellipseMode(CENTER)
    background(255)
    Hi = Hinc/2
    Ii = Iinc /2
    for x in range(nodesI):    
        ellipse(sC,(Ii),CS,CS)

        Hi = Hinc/2
        for xx in range(nodesH):
            line(sC + (CS/2),(Ii), (sC +crep) - (CS/2),Hi)
            Hi = Hi + Hinc
        Ii= Ii + Iinc
    sC = sC + crep
    Hi = Hinc/2
    for x in range(nodesH):
        ellipse(sC,Hi,CS,CS)
        eI = Einc /2 
        for xx in range(nodesE):
            line(sC + (CS/2),(Hi), (sC +crep) - (CS/2),eI)
            eI = eI + Einc
        Hi = Hi + Hinc
    sC = sC + crep
    eI = Einc /2 
    for x in range(nodesE):
        ellipse(sC,(eI),CS,CS)
        eI = eI + Einc
