import random
X = []

def ShipLogic(round, yourMap, yourHp, enemyHp, p1ShotSeq, p1PrevHit):
    global X 
    if (p1PrevHit):
        X.append(p1ShotSeq[-1])
    print(X)

    FollowThrough(p1PrevHit,p1ShotSeq,enemyHp)

    x = random.randint(1, 10)
    y = random.randint(1, 10)
    return [x,y]

# Will target areas in a straight line or around a point
def FollowThrough(prevHit, shotSeq, enemyHp):
    # Targeting: Up Right Down Left

    # Get previous shot sequences up to 4
    if (enemyHp >= 5):
        prevShots = shotSeq[-5:]
    else:
        prevShots = shotSeq[-enemyHp:]

    lineLength = 0
    isLineCheck = False
    if len(prevShots) >= 2:
        for i in range(len(prevShots)):
            if (isLine(prevShots[-i:])):
                lineLength = i
                isLineCheck = True
                break
    # If Hit:
    if (prevHit):
        # If previous shot sequences are in a line
        
        if (isLineCheck):
            # Fire at end of line (next slot)
            pass
        # Else fire upwards
        else:

            target_shot = prevShots[-1]
            target_shot[1] -= 1;
            return target_shot

    # If Miss
    # If previous shot sequences are in a line fire on opposite side

    # Else
        # Find next sequence in a cross to fire at

    pass

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