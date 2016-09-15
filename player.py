class Player():
    __score=0
    def printscore(self):
        print "Present Score :%d" % self.__score
        #return self.score
    def returnscore(self):
        return self.__score
    def score_ten(self):
        self.__score +=10

    def score_row(self):
        self.__score+=100

