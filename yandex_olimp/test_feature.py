class MyStr(str):
    def __init__(self, string=''):
        super().__init__()
        self.string = string

    def insert_into_pos(self, position=0, source=''):
        res = list(self.string)
        res.insert(position, source)
        return ''.join(res)


sss = MyStr('privetik')
ins_sss = sss.insert_into_pos(3, '89898')
upper_sss = sss.upper()
print(ins_sss)
print(upper_sss)
