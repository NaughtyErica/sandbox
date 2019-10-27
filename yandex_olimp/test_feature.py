class MyStr(str):
    def __init__(self, string=''):
        self.string = string
        super().__init__()

    def insert_into_pos(self, position=0, source=''):
        res = list(self.string)
        # ins = list(source)
        res.insert(position, source)
        return res



sss = MyStr('okpopoi')
print(sss.upper())
print(sss.insert_into_pos(3, '89898'))

