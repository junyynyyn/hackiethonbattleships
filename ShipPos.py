import random
def getShipPos():
    '''
    THIS IS THE LIST OF SHIPS
    [5,3,3,2,2] 
    That is: 
    1x 5 long
    2x 3 long
    2x 2 long

    Your ships must satisfy this 
    '''

    possible_layout1 = [[(0,6),(1,6),(2,6)],
                        [(0,2),(1,2),(2,2),(3,2),(4,2)],
                        [(2,8),(2,9)],
                        [(7,5),(8,5),(9,5)],
                        [(7,0),(7,1)]]
    possible_layout2 = [[(1,5),(1,6),(1,7)],
                        [(5,1),(6,1),(7,1),(8,1),(9,1)],
                        [(0,1),(1,1)],
                        [(6,4),(6,5),(6,6)],
                        [(7,9),(8,9)]]
    possible_layout3 = [[(1,6),(1,7),(1,8)],
                        [(9,2),(9,3),(9,4),(9,5),(9,6)],
                        [(0,0),(0,1)],
                        [(3,5),(3,6),(3,7)],
                        [(5,6),(5,7)]]
    possible_layout3 = [[[(1,6),(1,7),(1,8)],
                        [(9,2),(9,3),(9,4),(9,5),(9,6)],
                        [(0,0),(0,1)],
                        [(3,5),(3,6),(3,7)],
                        [(5,6),(5,7)]]]

    smiley_layout = [[(4,2),(4,3),(4,4)],
                     [(3,8),(4,8),(5,8),(6,8),(7,8)],
                     [(2,6),(2,7)],
                     [(6,2),(6,3),(6,4)],
                     [(8,6),(8,7)]] 
    
    tpose_layout = [[(1,7),(2,7),(3,7)],
                    [(4,2),(4,3),(4,4),(4,5),(4,6)],
                    [(2,3),(3,3)],
                    [(5,7),(6,7),(7,7)],
                    [(5,3),(6,3)]]

    choose = random.randint(0, 100)
    print(choose)
    # 80% Chance proper layout
    if (choose <= 80):
        return possible_layout1
    #20% Chance smiley face
    elif (choose > 80 and choose < 100):
        return smiley_layout
    # 1% Chance meme layout
    else:
        return tpose_layout

    # due to a bug we have the indexing of ships are 0-9
    
    # shipPos = [[(3,1), (4,1),(5,1)], 
    #             [(2,1),(2,2),(2,3),(2,4),(2,5)], 
    #             [(7,7),(8,7)] , 
    #             [(0,9), (1,9), (2,9)], 
    #             [(5,9), (6,9)]]
    return smiley_layout

if __name__ == "__main__":
    print(getShipPos())