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
    possible_layout3 = []

    smiley_layout = [[(4,2),(4,3),(4,4)],
                     [(3,8),(4,8),(5,8),(6,8),(7,8)],
                     [(2,6),(2,7)],
                     [(6,2),(6,3),(6,4)],
                     [(8,6),(8,7)]]
    
    tpose_layout = []

    choose = random.randint(10)
    if (choose <= 6):
        return possible_layout1
    else:
        return smiley_layout

    # due to a bug we have the indexing of ships are 0-9
    
    # shipPos = [[(3,1), (4,1),(5,1)], 
    #             [(2,1),(2,2),(2,3),(2,4),(2,5)], 
    #             [(7,7),(8,7)] , 
    #             [(0,9), (1,9), (2,9)], 
    #             [(5,9), (6,9)]]
    return smiley_layout