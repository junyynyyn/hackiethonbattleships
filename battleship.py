import random
# Constants


# Global State Variables
hits = []
targeted = [0,0]
# State 0 = Neutral, 1 = Hit, 2 = Hunt
state = 0

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
    if (state == 0):
        pass
    # Hit State
    elif (state == 1):
        crossCheck(targeted)
    # Hunt State
    elif (state == 2):
        pass

    x = random.randint(1, 10)
    y = random.randint(1, 10)
    return [x,y]

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

if __name__ == "__main__":
    print("Hello World")