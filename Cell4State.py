
class Cell4State() :
        def __init__(self) :
            self.Empty = '-'
            self.Me = 'x'
            self.Enemy = 'o'
            self.MeNu = 0
            self.EnemyNu = 1
            self.WinUtility = 10000
            self.NormalizationConstant = 10000
            self.PowersOf10 = [1,10,100,1000,10000]
            self.States = {}
            self.ForwardAd = [ [ [-1,-1] for cell in range(4)] for state in range(81) ]
            self.BackwardAd = [ [ [-1,-1] for cell in range(4)] for state in range(81) ]
            self.UtilityChangeForward = [ [ [-1,-1] for cell in range(4)] for state in range(81) ]
            # self.NormalizedUCF = [ [ [-1,-1] for cell in range(4)] for state in range(81) ]
            # self.NormalizedUCB = [ [ [-1,-1] for cell in range(4)] for state in range(81) ]
            self.UtilityChangeBackward = [ [ [-1,-1] for cell in range(4)] for state in range(81) ]
            self.CurrentActiveStates = 0
            self.CurState = [self.Empty,self.Empty,self.Empty,self.Empty]
            self.StateUtility = [ 0 for state in range(81) ]
            self.AvailableMoves = [ [] for state in range(81) ]
            self.dfs(self.CurrentActiveStates)
            self.WinState = self.States[str([self.Me,self.Me,self.Me,self.Me])]
            self.LoseState = self.States[str([self.Enemy,self.Enemy,self.Enemy,self.Enemy])]

        def dfs(self,StateNo) :
            # Add the state to the list of known states
            self.States[str(self.CurState)] = StateNo
            self.StateUtility[StateNo] = self.FindCurStateUtility()
            self.CurrentActiveStates += 1

            NextStateNo = -1
            for cell in range(4) :
                # check for Empty cell
                if self.CurState[cell] == self.Empty :
                    # Add the cell to list of available moves from the current state
                    self.AvailableMoves[StateNo].append(cell)

                    # if payed by me
                    self.CurState[cell] = self.Me

                    if str(self.CurState) not in self.States :
                        NextStateNo =  self.CurrentActiveStates
                        self.dfs(NextStateNo)
                    else :
                        NextStateNo = self.States[str(self.CurState)]

                    # Add a forward Edge
                    self.ForwardAd[StateNo][cell][self.MeNu] = NextStateNo
                    # Add a Backward Edge
                    self.BackwardAd[NextStateNo][cell][self.MeNu] = StateNo

                    # ForwardUtility Change
                    self.UtilityChangeForward[StateNo][cell][self.MeNu] = self.StateUtility[NextStateNo] - self.StateUtility[StateNo]
                    # Normalized ForwardUtility
                    # self.NormalizedUCF[StateNo][cell][self.MeNu] = 10**(float(self.UtilityChangeForward[StateNo][cell][self.MeNu])/float(self.NormalizationConstant))
                    # BackwardUtility Change
                    self.UtilityChangeBackward[NextStateNo][cell][self.MeNu] = self.StateUtility[StateNo] - self.StateUtility[NextStateNo]
                    # Normalized BackwardUtility
                    # self.NormalizedUCB[NextStateNo][cell][self.MeNu] = 10**(float(self.UtilityChangeBackward[NextStateNo][cell][self.MeNu])/float(self.NormalizationConstant))


                    # if plpayed by Enemy
                    self.CurState[cell] = self.Enemy

                    if str(self.CurState) not in self.States :
                        NextStateNo =  self.CurrentActiveStates
                        self.dfs(NextStateNo)
                    else :
                        NextStateNo = self.States[str(self.CurState)]

                    # Add a forward Edge
                    self.ForwardAd[StateNo][cell][self.EnemyNu] = NextStateNo
                    # Add a Backward Edge
                    self.BackwardAd[NextStateNo][cell][self.EnemyNu] = StateNo

                    # ForwardUtility Change
                    self.UtilityChangeForward[StateNo][cell][self.EnemyNu] = self.StateUtility[NextStateNo] - self.StateUtility[StateNo]
                    # Normalized ForwardUtility
                    # self.NormalizedUCF[StateNo][cell][self.EnemyNu] = 10**(float(self.UtilityChangeForward[StateNo][cell][self.EnemyNu])/float(self.NormalizationConstant))
                    # BackwardUtility Change
                    self.UtilityChangeBackward[NextStateNo][cell][self.EnemyNu] = self.StateUtility[StateNo] - self.StateUtility[NextStateNo]
                    # Normalized BackwardUtility
                    # self.NormalizedUCB[NextStateNo][cell][self.EnemyNu] = 10**(float(self.UtilityChangeBackward[NextStateNo][cell][self.EnemyNu])/float(self.NormalizationConstant))

                    # Restore the cell
                    self.CurState[cell] = self.Empty

        def FindCurStateUtility(self) :
            MeCount =  self.CurState.count(self.Me)
            EnemyCount =  self.CurState.count(self.Enemy)
            if MeCount == 0 and EnemyCount == 0 :
                return 0
            if MeCount == 0 :
                return -self.PowersOf10[EnemyCount]
            if EnemyCount == 0 :
                return self.PowersOf10[MeCount]
            return 0

        # def BlockToRow(self,move) :
        #     return move[1]
        #
        # def BlockToCol(self,move) :
        #     return move[0]
        #
        # def BlocktoDiag(self,move) :
        #     return move[0]
        #
        # def UpdateStateForward(self,CurStateNo,Cell,Player) :
        #     # print self.ForwardAd[CurStateNo][Cell][Player], self.States[self.ForwardAd[CurStateNo][Cell][Player]]
        #     return self.ForwardAd[CurStateNo][Cell][Player]
        #
        # def UpdateStateBack(self,CurStateNo,Cell,Player) :
        #     # print self.BackwardAd[CurStateNo][Cell][Player], self.States[self.BackwardAd[CurStateNo][Cell][Player]]
        #     return self.BackwardAd[CurStateNo][Cell][Player]


a = Cell4State()
# print a.AvailableMoves[0]
# # print a.NormalizedUCF
# # print "aa",a.States[str(['-','o','o','o'])]
# # print "aa" , a.StateUtility[70]
b = [ "aak" for i in range(81)]
for state in a.States :
    b[a.States[state]] = state
#
# print b[a.WinState]
# print b[a.LoseState]
#
# for i in range(81) :
#     if abs(a.StateUtility[i]) == 1000 :
#         print i,b[i]
# print "*********************************" , a.NormalizedUCF[42][3][1]
# for i in range(81) :
#     get = False
#     for cell in range(4) :
#         for p in range(2) :
#             if abs(a.NormalizedUCF[i][cell][p]) > 7 :
#                 print b[i]
#
# for i in range(81) :
#     print i, b[i] , a.StateUtility[i]
# print a.States
