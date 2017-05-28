
from ChessPiece import ChessPiece


class Pao(ChessPiece):

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RCS.gif"
            else:
                return "images/BCS.gif"
        else:
            if self.is_red:
                return "images/RC.gif"
            else:
                return "images/BC.gif"

    def can_move(self, board, dx, dy):
        if dx != 0 and dy != 0:
            # print 'no diag'
            return False
        nx, ny = self.x + dx, self.y + dy
        cnt = self.count_pieces(board, self.x, self.y, dx, dy)
        # print 'cnt',cnt
        if (nx, ny) not in board.pieces:
            if cnt!= 0:
                # print 'blocked'
                return False
        else:
            if cnt != 1:
                # print 'cannot kill'
                return False
        return True

    def __init__(self, x, y, is_red):
        ChessPiece.__init__(self, x, y, is_red)

    #below added by Fei Li
    def name(self):
        return 'Pao'
