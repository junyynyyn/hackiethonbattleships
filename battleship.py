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

def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit):
    # Bring in global variables
    global hits, targeted, state, hunt_state

    to_hit = [0, 0]

    # If Previous hit
    if (p1PrevHit):
        # Save previous hit
        hits.append(p1ShotSeq[-1])
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
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        to_hit = [x,y]
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
        x = 5
        y = 5
        to_hit = [x,y]
    
    return to_hit

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
    pass

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

if __name__ == "__main__":
    hunt_state = 3
    print(huntTargeting([1,1]))