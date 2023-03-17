class Checking:
    def __init__(self, matrix):
        self.matrix = matrix

    def boardCheck(self):
        winning = False
        mark = ''
        for i in range(0, 3):

            if self.matrix[i][i-i] == self.matrix[i][i+1-i] == self.matrix[i][i+2-i]:
                winning = True
                mark = self.matrix[i][i]
                break

            if self.matrix[i-i][i] == self.matrix[i+1-i][i] == self.matrix[i+2-i][i]:
                winning = True
                mark = self.matrix[i][i]
                break

        i = 0
        if self.matrix[i][i] == self.matrix[i+1][i+1] == self.matrix[i+2][i+2]:
            winning = True
            mark = self.matrix[i][i]

        if self.matrix[i][i+2] == self.matrix[i+1][i+1] == self.matrix[i+2][i]:
            winning = True
            mark = self.matrix[i][i+2]

        if not winning:
            return

        if winning:
            return mark
