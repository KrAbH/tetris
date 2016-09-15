import random
import numpy as np
class blocks():
    arr_blocks= [[[' ',' ',' ',' '],['X','X','X','X']],[['X','X'],['X','X']],[['X',' '],['X',' '],['X','X']], [[' ', ' X',' '],['X','X','X']],[['X','X',' '],[' ','X','X']]]
    def selectblock(self):
        x= random.randint(0,2)
        return self.arr_blocks[x]
