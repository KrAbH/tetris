from block import blocks
from player import Player
import time
import sys
import os
import select
import numpy as np

rows , columns =32,32

class Board():
    def collisioncheck(self, var, index,line,selected_piece,board):
        flag=False
        if var=='a':
            if index < len(selected_piece[0]):
                flag=True
            else:
                for i in range(line, line+len(selected_piece)-1):
                    for j in range(1, len(selected_piece)):
                        if board[line][index-j]=='X' and selected_piece[line][index]=='X':
                            flag=True
                            break
                    if flag==True:
                        break

        elif var=='d':
            if index+len(selected_piece[0]) > 30:
                flag=True
            else:
                for i in range(line, line+len(selected_piece)-1):
                    for j in range(1, len(selected_piece)):
                        if board[line][index+j]=='X' and selected_piece[line][index]=='X':
                            flag=True
                            break
                    if flag==True:
                        break
        return flag

    def moveleft(self,index):
        return index-1

    def moveright(self,index):
        return index+1

    def drop(self, index,line,selected_piece,board):
        temp = 0
        for i in range(line+1, 30):
            for j in range(index, index+len(selected_piece[0])-1):
                if selected_piece[len(selected_piece)-1][j-index]=='X' and board[i][j]=='X':
                    temp =1
                    break
            if temp==1:
                break
        return i-1-len(selected_piece)

class Gameplay(Player, blocks,Board):
    
    columns = 32
    rows = 32
    board = [[0 for i in range(columns)]for j in range(rows)]
    temp_board = [[0 for i in range(columns)]for j in range(rows)]
    def makeboard(self,row, column):
        for i in range(row):
            for j in range(column):
                if (i==0 or i==row-1)and j%2==1 :
                    self.board[i][j]='-'
                elif j==0 or j==column-1:
                    self.board[i][j]='|'
                else:
                    self.board[i][j]=' '
        self.board[0][0]= '+'
        self.board[31][31]= '+'
        self.board[0][31]= '+'
        self.board[31][0]= '+'
        for i in range(row):
            for j in range(column):
                print self.board[i][j],
            print '\n',

    def updateboard(self,x):
        for i in range(x, 1,-1):
            for j in range(1, self.columns-1,1):
                self.board[i][j]= self.board[i-1][j]

    def checkRowFull(self):
        flag=0
        temp=0
        for i in range(30,1,-1):
            for j in range(1, 30):
                if self.board[i][j] ==' ':
                    flag=1
                    break        
            if(flag==0):
                self.updateboard(i)
                self.score_row()
                print'Row cleared : 100 points'
            else:
                break

    def printboard(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print self.board[i][j],
            print '\n',
    def selectpiece(self):
        temp = self.selectblock()
        selected_block=temp 
        return selected_block


    def from_temp_board(self):
      #  print 'vvjdsvnj'
        for i in range(self.rows):
            for j in range(self.columns):
                self.board[i][j]=self.temp_board[i][j]
        self.checkRowFull()
        self.moveblock()


    block_on_board = False
    def moveblock(self):
        if self.block_on_board ==False:
            selected_piece= self.selectpiece()
            index = 16
            line =1
            temp_line=line
            temp_index=index
            for i in range(len(selected_piece[0])):
                if self.board[line][index+i]=='X' :
                    print ('Game Over')
                    self.printscore()
                    quit() 
            self.score_ten()

            while line != self.rows-len(selected_piece):
                flag=0

                for i in range(self.rows):
                    for j in range(self.columns):
                        self.temp_board[i][j]=self.board[i][j]
                
                for j in range(len(selected_piece)):
                    for k in range(len(selected_piece[0])):
                        self.temp_board[temp_line][temp_index]=selected_piece[j][k]
                        temp_index+=1
                    temp_line+=1
                    temp_index =index

                for i in range(self.rows):
                    for j in range(self.columns):
                        print self.temp_board[i][j],
                    print '\n',

                self.printscore()
                print 'Press a for left '
                print 'Press d for right'
                print 's for free fall'
                print 'w to rotate the block'
                print "Next Move please:(Press enter after every move) "
                h,o,e= select.select([sys.stdin],[],[],0.4)
                if h:
                    var=sys.stdin.readline().strip()
                    if var=='a' and self.collisioncheck(var, index, line,selected_piece,self.board)==False:
                        index= self.moveleft(index)
                    elif var=='d' and self.collisioncheck(var, index,line,selected_piece,self.board)==False:
                        index=self.moveright(index)
                    elif var=='s' :
                        line=self.drop(index, line, selected_piece,self.board)
                    elif var=='w':
                        selected_piece=zip(*selected_piece)
                temp_index= index
 #               time.sleep(0.5)
                os.system('clear')
                line += 1
                temp_line=line
                
                block_line = len(selected_piece)
                for i in range(len(selected_piece[0])):
                    if line+block_line <=30:
                        if self.temp_board[line+block_line-1][index+i]=='X' and self.board[line+block_line][index+i]=='X':
                            self.from_temp_board()
                            flag= 1
                            break

                if flag==1:
                    self.moveblock()

            for i in range(self.rows):
                for j in range(self.columns):
                    self.board[i][j]=self.temp_board[i][j]
            self.moveblock()

     

play= Gameplay()
os.system('clear')
play.makeboard(rows,columns)
time.sleep(1)
os.system('clear')
play.moveblock()
