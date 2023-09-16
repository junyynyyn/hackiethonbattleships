import random
# Constants
relative = [[0,-1],[1,0],[0,1],[-1,0]]

# Global State Variables
hits = []
targeted = [0,0]
# State 0 = Neutral, 1 = Hit, 2 = Hunt, 3 = Hunt turn around
state = 0
# Hunt State 0 = Up, 1 = Right, 2 = Down, 3 = Left
hunt_state = 0

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
cM_2ndCenter = [(4,3),(6,3),(8,3),(8,5),(8,7),(3,8),(5,8),(7,8),(3,4),(3,6)]
cM_3rdCenter = [(3,2),(5,2),(7,2),(9,2),(2,9),(4,9),(6,9),(8,9),(2,3),(2,5),(2,7),(9,4),(9,6),(9,8)]
cM_FinalCenter = [(2,1),(4,1),(6,1),(8,1),(10,1),(1,2),(1,4),(1,6),(1,8),(1,10),(3,10),(5,10),(7,10),(9,10),(10,3),(10,5),(10,7),(10,9)]


def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit, p1storage):
    # Bring in global variables
    global hits, targeted, state, hunt_state
    to_hit = [0, 0]
    # If Previous hit
    if (p1PrevHit):
        # Save previous hit
        hits.append(p1ShotSeq[-1])
        eliminatecandidate(p1ShotSeq)
        # Change state to hit
        if (state == 0):
            state = 1
            targeted = p1ShotSeq[-1]
        # Change state to hunt and set hunt direction
        elif (state == 1):
            state = 2
            getHitDirection()
    else:
        # If miss
        if (state == 2):
            # If hunting
            # Turn around
            hunt_state = (hunt_state + 2) % 4
            state = 3
        elif (state == 3):
            # If finished hunting revert back to neutral state
            state = 0
    
    # Neutral State
    if (state == 0):
        to_hit =neutralState(cM_Center, cM_2ndCenter, cM_3rdCenter, cM_FinalCenter)


    # Hit State
    elif (state == 1):
        next_hit = hitTargeting(targeted, p1ShotSeq)
        if (next_hit != None):
            to_hit = next_hit

        else:
            state = 0
    # Hunt State
    elif (state >= 2):
        next_hit = huntTargeting(targeted, p1ShotSeq)
        if (next_hit != None):
            to_hit = next_hit
        else:
            state = 0

    if not isValidShot(to_hit, p1ShotSeq):
        to_hit = neutralState(cM_Center, cM_2ndCenter, cM_3rdCenter, cM_FinalCenter)
    return to_hit, p1storage

def isOutsideBoundaries(shot):
    for i in range(2):
        if (shot[i] < 1 or shot[i] > 10):
            return True

def isValidShot(shot, shotSeq):
    if (isOutsideBoundaries(shot)):
        return False
    if shot in shotSeq:
        return False
    return True

# Neutral target state
def neutralTargeting():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    return [x,y]

# return a coordinate by scanning targeted point clockwise
def hitTargeting(coords, shotSeq):
    check_coords = [[0,-1],[1,0],[0,1],[-1,0]]
    for check in check_coords:
        target_coords = coords.copy()
        target_coords[0] += check[0]
        target_coords[1] += check[1]
        
        if isValidShot(target_coords, shotSeq):
            return target_coords
    return None

def huntTargeting(coords, shotSeq):
    global state, hunt_state
    while (not isValidShot(coords, shotSeq)):
        coords = huntStep(coords)
        print(coords)
        if (isOutsideBoundaries(coords)):
            if (state == 2):
                hunt_state = (hunt_state + 2) % 4
                state = 3
            else:
                return None
    return coords
    
def huntStep(coords):
    global hunt_state
    target = coords.copy()
    target[0] += relative[hunt_state][0]
    target[1] += relative[hunt_state][1]
    return target

def getHitDirection():
    global hits, hunt_state
    direction = hits[-2].copy()
    direction[0] -= hits[-1][0]
    direction[1] -= hits[-1][1]

    hunt_state = relative.index(direction)




''' in neutral state, using algorithm to give a new shot efficiently here.
 as first step, start hitting from center, and once finish all center coodinate, 
 then broaden the scope we hit'''
def neutralState(cM_Center, cM_2ndCenter, cM_3rdCenter, cM_FinalCenter):
    #ramdomly choice
    x = random.randint(1, 10)
    y = random.randint(1, 10)

    while (x,y) not in candidateMap:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        return [x,y]

    #first step, choose from center
    if cM_Center != []:

        (x, y) = random.choice(cM_Center)
        return (x, y)

    elif cM_2ndCenter != []:
        (x, y) = random.choice(cM_2ndCenter)
        return (x,y)
    
    elif cM_3rdCenter != []:
        (x, y) = random.choice(cM_3rdCenter)
        return (x,y)
    
    else:
        (x, y) = random.choice(cM_FinalCenter)
        return (x,y)
    

    
#eliminate latest shot coordiate from candidateMap
def eliminatecandidate(shotSeq):
    global candidateMap, cM_Center, cM_2ndCenter, cM_3rdCenter, cM_FinalCenter
    latestShot = shotSeq[-1]
    if latestShot in candidateMap:
        candidateMap.remove(latestShot)

    if latestShot in cM_Center:
        cM_Center.remove(latestShot)

    if latestShot in cM_2ndCenter:
        cM_2ndCenter.remove(latestShot)

    if latestShot in cM_3rdCenter:
        cM_3rdCenter.remove(latestShot)

    if latestShot in cM_FinalCenter:
        cM_FinalCenter.remove(latestShot)
    return


if __name__ == "__main__":
    hunt_state = 3
    print(huntTargeting([1,1]))