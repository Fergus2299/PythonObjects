import logging

logging.basicConfig(filename='solitaire_log.log', filemode='w', level=logging.DEBUG)

class Peg:
    def __init__(self):
        pass
class Invalid:
    def __init__(self):
        pass
    
class Board:
    def __init__(self):
        self.data = [
        [Invalid, Invalid,Peg,Peg,Peg,Invalid,Invalid],
        [Invalid, Invalid,Peg,Peg,Peg,Invalid,Invalid],
        [Peg, Peg,Peg,Peg,Peg,Peg,Peg],
        [Peg, Peg,Peg,None,Peg,Peg,Peg],
        [Peg, Peg,Peg,Peg,Peg,Peg,Peg],
        [Invalid, Invalid,Peg,Peg,Peg,Invalid,Invalid],
        [Invalid, Invalid,Peg,Peg,Peg,Invalid,Invalid]
        ]

    def check_move(self, target,middle, origin):
        '''
        there needs to be a hole to jump into, the middle pos needs to be a peg, the origin needs to have a peg
    '''
        if target != None:
            return (0, f'error: not a free spot at target {target}')
        elif origin != Peg:
            return (0, 'error: origin not a peg')
        elif middle != Peg:
            return (0, 'error: not a free spot at target')
        else: return (1, 'move successful')


    def make_move(self, x,y,direction):
        '''
        takes coords of peg
        calls check of legality of move
        implements move
        '''
        origin = (x, y)
        if direction == 'n':
            target = (x, y-2)
            middle = (x, y-1)
        elif direction == 's':
            target = (x, y+2)
            middle = (x, y+1)
        elif direction == 'w':
            target = (x-2, y)
            middle = (x-1, y)
        elif direction == 'e':
            target = (x+2, y)
            middle = (x+1, y)
        else:
            print('not valid direction')
            return
        
        # check legality of the move
        # check whether move goes off the board
        for ind in range(2):
            if origin[ind] >= 7 or target[ind] >= 7:
                print('gone off the board')
                return 
        legal = self.check_move(self.data[target[1]][target[0]],self.data[middle[1]][middle[0]], self.data[origin[1]][origin[0]])
        if not legal[0]:
            print(legal)
            logging.DEBUG(f'Move failed to execute, origin: {origin}, target: {target}. Error info: {legal}')
            return
        # updating values
        self.data[target[1]][target[0]] = Peg
        self.data[middle[1]][middle[0]] = None
        self.data[origin[1]][origin[0]] = None
        logging.debug(f'Move executed, origin: {origin}, target: {target}')
        print('move executed')
        self.print()
    def print(self):
        for row in self.data:
            row_str = ''
            for col in row:
                if col == Peg:
                    row_str +=   '  peg  '
                elif col == Invalid:
                    row_str +=   'invalid'
                else: row_str += '       '
                row_str += ', '
            print(row_str)
        print('\n')
class Game:
    def __init__(self):
        self.play()
    def play(self):
        playing = True
        b = Board()
        b.print()
        while playing:
            x =input('enter x coord: ')
            y = input('enter y coord: ')
            dir = input('enter direction {"n", "s", "e" or "w"}: ')
            if (x.isdigit()) and (y.isdigit()):
                b.make_move(int(x),int(y), dir)
            else: print('enter valid number')





g = Game()
