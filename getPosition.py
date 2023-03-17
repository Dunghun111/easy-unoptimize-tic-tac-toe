class Position:
    def __init__(self, p_input):
        self.p_input = p_input

    def GetPosition(self):
        output = []

        if self.p_input % 3 == 0:
            Horizontal = int(self.p_input / 3)
            Vertical = self.p_input - ((Horizontal - 1) * 3)

        else:
            Horizontal = int(self.p_input / 3) + 1
            Vertical = self.p_input - ((Horizontal - 1) * 3)

        output.append(Horizontal - 1)
        output.append(Vertical - 1)

        return output
