import random
# Constants


# Global State Variables
hits = []
targeted = [0,0]
# State 0 = Neutral, 1 = Hit, 2 = Hunt
state = 0

#create 10 by 10 map

candidateMap = [[(2,1),(4,1),(6,1),(8,1),(10,1)], 
                [(1,2),(3,2),(5,2),(7,2),(9,2)], 
                [(2,3),(4,3),(6,3),(8,3),(10,3)],
                [(1,4),(3,4),(5,4),(7,4),(9,4)],
                [(2,5),(4,5),(6,5),(8,5),(10,5)],
                [(1,6),(3,6),(5,6),(7,6),(9,6)],
                [(2,7),(4,7),(6,7),(8,7),(10,7)],
                [(1,8),(3,8),(5,8),(7,8),(9,8)],
                [(2,9),(4,9),(6,9),(8,9),(10,9)],
                [(1,10),(3,10),(5,10),(7,10),(9,10)]]

cM_Center = [(5,4),(7,4),(4,5),(6,5),(5,6),(7,6),(4,7),(6,7)]




def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit):
    # Bring in global variables
    global hits, targeted, state

    # If Previous hit
    if (p1PrevHit):
        # Save previous hit
        hits.append(p1ShotSeq[-1])
        # Change state to cross check
        if (state == 0):
            state = 1
            targeted = p1ShotSeq[-1]
        
    
    
    # Neutral State
    if (state == 0): #ここでランダム関数返すからここでやる
        [x, y] = neutralState(candidateMap)

    # Hit State
    elif (state == 1):
        next_hit = crossCheck(targeted, p1ShotSeq)
        if (next_hit):
            return next_hit
        else:
            # Return to neutral fire
            pass
    # Hunt State
    elif (state == 2):
        pass

    return [x, y]

# return a coordinate by scanning targeted point clockwise
def crossCheck(coords, shotSeq):
    global hits
    check_coords = [[0,-1],[1,0],[0,1],[-1,0]]
    for check in check_coords:
        target_coords = coords
        target_coords[0] += check[0]
        target_coords[1] += check[1]
        if target_coords not in shotSeq:
            return target_coords
    return None

# def getValidShot(shot, shotSeq):


def getNextShotInLine(shotSeq):
    check_coords = [[0,-1],[1,0],[0,1],[-1,0]]
    for check in check_coords:
        if (isLine(shotSeq)):
            shot = shotSeq[-1]
            shot[0] += check[0]
            shot[1] += check[1]
            return shot

# Returns true if a shot sequence is a uninterrupted line
def isLine(shotSeq):
    currentShot = shotSeq[-1]
    # Up Right Down Left
    check_coords = [[0,-1],[1,0],[0,1],[-1,0]]
    line = False
    for check in check_coords:
        currentShot = shotSeq[-1]
        line = True
        for shot in range(len(shotSeq)-1):
            check_x = shotSeq[shot][0] + check[0]
            check_y = shotSeq[shot][1] + check[1]
            shot_check = [check_x, check_y]
            if shotSeq[shot+1] != shot_check:
                line = False
                break

        if line == True:
            break
    
    return line


# in neutral state, using algorithm to give a new shot efficiently here.
def neutralState(cM_Center):
    #ramdomly choice
    '''while (x, y) not in candidateMap:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        return [x, y]'''

    #choose from center
    if cM_Center != []:
        (x, y) = random.choice(cM_Center)
        return (x, y)
    
    
#eliminate latest shot coordiate from candidateMap
def eliminatecandidate(shotSeq):
    global candidateMap, cM_Center
    latestShot = shotSeq[-1]
    if latestShot in candidateMap:
        candidateMap.remove(latestShot)

    if latestShot in cM_Center:
        candidateMap.remove(latestShot)
    return
    







if __name__ == "__main__":
    print("Hello World")

    