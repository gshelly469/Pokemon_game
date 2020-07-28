from a1_support import *



def display_game(game,grid_size):
    '''this function is used to
    display the game'''

    line=('-'*(grid_size*4+4))
    print(' ',end=' ')
    for i in range(grid_size):
        
        if i<9:
            print('|',i+1,end=" ")
        else:
            print('|',i+1,end='')

    print("|")
    print(line)

    for j in range(grid_size):
        print(ALPHA[j],end=" ")

        for k in range(grid_size):
            print('|',game[j*grid_size+k],end=" ")

        print("|")
        print(line)




def parse_position(action,grid_size):
    '''This function parses the position and 
    return a tuple containing the position of action'''

    if (len(action)==2 or len(action)==3):

        if (action[1].isnumeric()):

            if ( len(action)==2 and ord('A')<=ord(action[0]) and ord(action[0])<=ord(ALPHA[grid_size-1]) and int(action[1])<=grid_size ):
                a=ALPHA.index(action[0])
                b=(a,int(action[1])-1)
                return b

            elif ( len(action)==3 and ord('A')<=ord(action[0]) and ord(action[0])<=ord(ALPHA[grid_size-1]) and int(action[1]+action[2])<=grid_size ):
                a=ALPHA.index(action[0])
                b=(a,int(action[1]+action[2])-1)
                return b

            else:
                print(INVALID)
                return None

        else:
            print(INVALID)
            return None


    elif ( len(action)==4 or len(action)==5 ):

        if ( action[0]=='f' and action[1]==' ' and action[3].isnumeric() ):

            if ( len(action)==4 and int(action[3])<=grid_size and (ord('A')<=ord(action[2]) and ord(action[2])<=ord(ALPHA[grid_size-1])) ):
                c=ALPHA.index(action[2])
                d=(c,int(action[3])-1)
                return d

            elif ( len(action)==5 and int(action[3]+action[4])<=grid_size and (ord('A')<=ord(action[2]) and ord(action[2])<=ord(ALPHA[grid_size-1])) ):
                c=ALPHA.index(action[2])
                d=(c,int(action[3]+action[4])-1)
                return d

            else:
                print(INVALID)
                return None

        else:
            print(INVALID)
            return None


    else:
        return None





def position_to_index(position,grid_size):
    '''This function should convert the row, column coordinate in the grid to the game strings index. The function
    returns an integer representing the index of the cell in the game string.'''

    return (position[0]*grid_size+position[1])





def replace_character_at_index(game,index,character):
    '''This function returns an updated game string with the specified character placed at the specified index.'''

    if character==POKEMON:
        game=game[:index]+character+game[index+1:]
        return game
    else:
        if game[index]=='~':
            g=game[:index]+character+game[index+1:]
            return g
        else:
            return None




def flag_cell(game,index):
    '''This function returns an updated game string after "toggling" the flag 
    at the specified index in the game string.'''

    if (game[index] != FLAG and game[index]=='~'):
        h=game[:index]+FLAG+game[index+1:]
    elif game[index] == FLAG:
        h=game[:index]+'~'+game[index+1:]
    return h




def index_in_direction(index,grid_size,direction):
    '''This function takes in the index to a cell in the game string and returns a new index corresponding to an
    adjacent cell in the specified direction.'''

    if ((direction=='right' or direction=='up-right' or direction=='down-right') and ((index+1)%grid_size)==0):
        return None
    if ((direction=='left' or direction=='up-left' or direction=='down-left') and ((index)%grid_size)==0):
        return None

    if (direction=='up'):
        index-=grid_size
    elif (direction=='down'):
        index+=grid_size
    elif (direction=='left'):
        index-=1
    elif (direction=='right'):
        index+=1
    elif (direction=='up-right'):
        index=index-grid_size+1
    elif (direction=='up-left'):
        index=index-grid_size-1
    elif (direction=='down-right'):
        index=index+grid_size+1
    elif (direction=='down-left'):
        index=index+grid_size-1

    if (index>=0 and index<grid_size*grid_size):
        return index
    else:
        return None





def check_win(game, pokemon_locations):
    '''This function returns True if the player has won the game, and returns False otherwise.'''

    var1=0
    for i in game:
        if (i==FLAG):
            if game.index(i) in pokemon_locations:
                var1+=1
        elif (i==UNEXPOSED):
            return False
        else:
            pass
    if var1==len(pokemon_locations):
        return True
    else:
        return False





def number_at_cell(game,pokemon_locations,grid_size,index):
    '''This function returns the number of Pokemon in neighbouring cells.'''

    u=0
    p=neighbour_directions(index,grid_size)
    for i in p:
        if i in pokemon_locations:
            u+=1
    return u
    

    

def neighbour_directions(index,grid_size):
    '''This function returns a list of indexes that have a neighbouring cell. (Note that the cells at the edges of the
    grid do not have all possible directions).'''

    list1=[]
    for i in DIRECTIONS:
        x=index_in_direction(index,grid_size,i)
        if x is None:
            continue
        else:
            list1.append(x)
    return list1




def main():
    '''This function handles player interaction. At the start of the game the player should be prompted for the Input'''

    print("Please input the size of the grid:",end=' ')
    grid_size=int(input())

    print("Please input the number of pokemons:",end=' ')
    number_of_pokemons=int(input())
    game=(UNEXPOSED*grid_size*grid_size)
    display_game(game,grid_size)
    print('')
    pokemon_locations=generate_pokemons(grid_size,number_of_pokemons)
    game_copy=game

    while(True):
        print('Please input action: ',end='')
        action=input()
        if (action=='q'):
            print('You sure about that buddy? (y/n):',end=' ')
            confirm_action=input()
            if confirm_action=='n':
                print("Let's keep going.")
                display_game(game,grid_size)
                print('')
            elif confirm_action=='y':
                print('Catch you on the flip side.')
                break
            else:
                print(INVALID)
                display_game(game,grid_size)
                print('')

        elif (action=='h'):
            print(HELP_TEXT)
            display_game(game,grid_size)
            print('')


        elif (action==':)'):
            print("It's rewind time.")
            game=game_copy
            pokemon_locations=generate_pokemons(grid_size,number_of_pokemons)
            display_game(game,grid_size)
            print('')


        else:
            if (len(action)==2 or len(action)==3):
                position=parse_position(action,grid_size)
                if position is None:
                    display_game(game,grid_size)
                    print('')
                    continue
                else:
                    index=position_to_index(position,grid_size)
                    if index in pokemon_locations and game[index] == '~':
                        for pokemon_index in pokemon_locations:
                            game=replace_character_at_index(game, pokemon_index, POKEMON)
                        display_game(game,grid_size)
                        print('You have scared away all the pokemons.')
                        break

                    exposed_cell_index=big_fun_search(game,grid_size,pokemon_locations,index)
                    exposed_cell_index.append(index)

                    for cells in exposed_cell_index:
                        m=number_at_cell(game, pokemon_locations, grid_size, cells)
                        temp=replace_character_at_index(game,cells,str(m))
                        if temp is None:
                            continue
                        else:
                            game=temp
            elif (len(action)==4 or len(action)==5):
                position=parse_position(action,grid_size)
                if position is None:
                    display_game(game,grid_size)
                    print('')
                    continue
                else:
                    index=position_to_index(position,grid_size)
                    game=flag_cell(game,index)

            else:
                print(INVALID)
                display_game(game,grid_size)
                print('')
                continue

            display_game(game,grid_size)

        
            bool1=check_win(game,pokemon_locations)
            if bool1:
                print('You win.')
                break

            print('')




"""Searching adjacent cells to see if there are any Pokemon"s present.

 	Using some sick algorithms.

 	Find all cells which should be revealed when a cell is selected.

 	For cells which have a zero value (i.e. no neighbouring pokemons) all the cell"s
 	neighbours are revealed. If one of the neighbouring cells is also zero then
 	all of that cell"s neighbours are also revealed. This repeats until no
 	zero value neighbours exist.

 	For cells which have a non-zero value (i.e. cells with neightbour pokemons), only
 	the cell itself is revealed.

 	Parameters:
 		game (str): Game string.
 		grid_size (int): Size of game.
 		pokemon_locations (tuple<int, ...>): Tuple of all Pokemon's locations.
 		index (int): Index of the currently selected cell

 	Returns:
 		(list<int>): List of cells to turn visible.
"""


def big_fun_search(game, grid_size, pokemon_locations, index):
        '''The big fun search function is required to uncover a section of cells.'''
        queue = [index]
        discovered = [index]
        visible = []
        

        
        if game[index] == FLAG:
            return queue
        
        number = number_at_cell(game, pokemon_locations, grid_size, index)
        if number != 0:
            return queue
        
        while queue:
            node = queue.pop()
            
            for neighbour in neighbour_directions(node, grid_size):
                if neighbour in discovered or neighbour is None:
                    continue
                
                discovered.append(neighbour)
                if game[neighbour] != FLAG:
                    number = number_at_cell(game, pokemon_locations, grid_size, neighbour)
                    if number == 0:
                        queue.append(neighbour)
                visible.append(neighbour)
        return visible

if __name__ == "__main__":
    main()
