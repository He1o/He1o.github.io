def level(honor):
    if honor <= 2:
        return 1
    if 3 <= honor <= 7:
        return 2
    if 8 <= honor <= 14:
        return 3
    if 15 <= honor <= 23:
        return 4
    if 24 <= honor <= 34:
        return 5
    if 35 <= honor <= 47:
        return 6
    if 48 <= honor <= 62:
        return 7
    if 63 <= honor <= 79:
        return 2
    if 80 <= honor <= 98:
        return 2
    if 99 <= honor <= 119:
        return 2


class player():

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.honor = 0
        self.reputation = 0

    def honor_cal(self, num):
        self.honor += num
        tmp_level = level(self.honor)
        if tmp_level != self.level:
            if tmp_level % 2 == 0:
                 print('指挥升级')
            if tmp_level % 2 == 0:
                 print('指挥升级') 