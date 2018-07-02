def lineToScore(lineString):
# This function takes a valid bowling line as an input string 
# and calculates the bowler's total score for the game
# Output: prints 'The Score for #lineString is #score'
    
    line = list(lineString)
    
    frame = 0              # This first segment determines the list index
    x = -1                 # of the 10th frame of the game. This is so
                           # we do not double-dip into the bonus frames for score
    while frame != 10:     # x is the index of the final roll of frame 10
        x += 1
        if line[x] == 'X':
            frame += 1
        else:
            frame += 0.5
    
    
    
    pinsHit = line.copy()                       # pinsHit is a list of the pins knocked down on each roll.
                                                # This is used to calculate X and / scores in the line. 
    for i in range(0, len(pinsHit)):
        
        if pinsHit[i] == 'X':
            pinsHit[i] = 10
        
        elif pinsHit[i] == '/':
            pinsHit[i] = 10 - int(pinsHit[i-1])
        
        elif pinsHit[i] == '-':
            pinsHit[i] = 0

    pinsHit = [ int(x) for x in pinsHit ]
    pinsHit.extend((0,0))
    
    
    for i in range(0, len(line)):                               # Converts each roll in the line to a score for that roll.
        if line[i] == 'X':  
            line[i] = pinsHit[i] + pinsHit[i+1] + pinsHit[i+2]
            
        elif line[i] == '/':
            line[i] = pinsHit[i] + pinsHit[i+1]
            
        elif line[i] == '-':
            line[i] = 0
            
    line = [int(x) for x in line]
    
    tenFrames = line[0:x+1]                   # tenFrames removes the bonus frame rolls from our line
    print ("The score for " + lineString + " is " + str(sum(tenFrames)))

lineToScore('XXXXXXXXXXXX')
lineToScore('9-9-9-9-9-9-9-9-9-9-')
lineToScore('5/5/5/5/5/5/5/5/5/5/5')
lineToScore('X7/9-X-88/-6XXX81')