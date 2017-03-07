from Cell4State import *
LineState = Cell4State()
class Block() :
    def __init__(self) :
        # Initially all are in State 0
        self.Rows = [ 0 for row in range(4)]
        self.Cols = [ 0 for col in range(4)]
        self.Diags = [ 0 for diag in range(2)]
        self.History = [ [0  for col in range(4)] for row in range(4) ]
        # No of Empty Cells
        self.EmptyCells = 16

        # Current Utility of the Block
        self.BlockUtility = 10*LineState.StateUtility[0]

        self.Status = "War"

  # [ Current State][ Cell No ][ Player No]
    def UpdateForward(self,Move,Player) :
        # Update Row State
        self.BlockUtility += LineState.UtilityChangeForward[ self.Rows[Move[0]] ][ Move[1] ][ Player ]
        self.Rows[Move[0]] = LineState.ForwardAd[ self.Rows[Move[0]] ][ Move[1] ][ Player ]

        # Update Col State
        self.BlockUtility += LineState.UtilityChangeForward[ self.Cols[Move[1]] ][ Move[0] ][ Player ]
        self.Cols[Move[1]] = LineState.ForwardAd[ self.Cols[Move[1]] ][ Move[0] ][ Player ]

        # check for Block Status
        if self.Rows[Move[0]] == LineState.WinState or self.Cols[Move[1]] == LineState.WinState :
            self.Status = "Won"
        elif self.Rows[Move[0]] == LineState.LoseState or self.Cols[Move[1]] == LineState.LoseState :
            self.Status = "Lost"

        # if this lies on diagonal 0
        if Move[0] == Move[1] :
            self.BlockUtility += LineState.UtilityChangeForward[ self.Diags[0] ][ Move[0] ][ Player ]
            self.Diags[0] = LineState.ForwardAd[ self.Diags[0] ][ Move[0] ][ Player ]
            if self.Diags[0] == LineState.WinState :
                self.Status = "Won"
            elif self.Diags[0] == LineState.LoseState:
                self.Status = "Lost"

        # if this lies on diagonal 1
        if Move[0] + Move[1] == 3 :
            self.BlockUtility += LineState.UtilityChangeForward[ self.Diags[1] ][ Move[0] ][ Player ]
            self.Diags[1] = LineState.ForwardAd[ self.Diags[1] ][ Move[0] ][ Player ]
            if self.Diags[1] == LineState.WinState :
                self.Status = "Won"
            elif self.Diags[1] == LineState.LoseState:
                self.Status = "Lost"

        # Decrement the number of Empty cells
        self.EmptyCells -= 1

    def UpdateBackward(self,Move,Player) :
        # Update Block Stats if relevent
        if self.Rows[Move[0]] == LineState.WinState or self.Cols[Move[1]] == LineState.WinState :
            self.Status = "War"
        elif self.Rows[Move[0]] == LineState.LoseState or self.Cols[Move[1]] == LineState.LoseState :
            self.Status = "War"

        # Update Row State
        self.BlockUtility += LineState.UtilityChangeBackward[ self.Rows[Move[0]] ][ Move[1] ][ Player ]
        self.Rows[Move[0]] = LineState.BackwardAd[ self.Rows[Move[0]] ][ Move[1] ][ Player ]

        # Update Col State
        self.BlockUtility += LineState.UtilityChangeBackward[ self.Cols[Move[1]] ][ Move[0] ][ Player ]
        self.Cols[Move[1]] = LineState.BackwardAd[ self.Cols[Move[1]] ][ Move[0] ][ Player ]

        # if this lies on diagonal 0
        if Move[0] == Move[1] :
            if self.Diags[0] == LineState.WinState :
                self.Status = "War"
            elif self.Diags[0] == LineState.LoseState:
                self.Status = "War"

            self.BlockUtility += LineState.UtilityChangeBackward[ self.Diags[0] ][ Move[0] ][ Player ]
            self.Diags[0] = LineState.BackwardAd[ self.Diags[0] ][ Move[0] ][ Player ]

        # if this lies on diagonal 1
        if Move[0] + Move[1] == 3 :
            if self.Diags[1] == LineState.WinState :
                self.Status = "War"
            elif self.Diags[1] == LineState.LoseState:
                self.Status = "War"

            self.BlockUtility += LineState.UtilityChangeBackward[ self.Diags[1] ][ Move[0] ][ Player ]
            self.Diags[1] = LineState.BackwardAd[ self.Diags[1] ][ Move[0] ][ Player ]

        # Decrement the number of Empty cells
        self.EmptyCells += 1
