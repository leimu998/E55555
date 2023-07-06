
import numpy as np
import matplotlib.pyplot as plt
import os

class Stat():
    def init(self, hp, basehp, crit1, crit2, inc, resist, ainc, qinc):
        self.hp = hp
        self.basehp = basehp
        self.crit1 = crit1
        self.crit2 = crit2
        self.crit = 1 + crit1 * crit2
        self.inc = 1 + inc
        resist = 0.1 - resist
        if(resist < 0):
            self.resist = (1 - resist / 2) * 0.5
        else:
            self.resist = (1 - resist) * 0.5
        self.ainc = ainc
        self.qinc = qinc
    
    def calc(self, sec, base):
        hp = self.hp
        if(sec >= 2.4):
            hp += self.basehp * 0.1
        if(sec >= 3.4):
            hp += self.basehp * 0.1
        inc = self.inc + min(50, 1 + 3.5 * np.floor(sec)) / 100
        damage = base * hp * self.crit * inc * self.resist
        #print(sec, base, hp, self.inc, inc, self.crit, self.resist, damage)
        return damage

    def A(self, sec):
        base = 0.325104
        self.inc += self.ainc
        res = self.calc(sec, base)
        self.inc -= self.ainc
        return res

    def E(self, sec):
        base = 0.481
        res = self.calc(sec, base)
        return res

    def Q(self, sec):
        base = 0.3151
        self.inc += self.qinc
        res = self.calc(sec, base)
        self.inc -= self.qinc
        return res
    
    def Q0(self, sec):
        base = 0.1553
        self.inc += self.qinc
        res = self.calc(sec, base)
        self.inc -= self.qinc
        return res

    def Q2(self, sec):
        base = 0.14
        self.inc += self.qinc
        res = self.calc(sec, base)
        self.inc -= self.qinc
        return res

A = [1.8, 2.8, 3.8, 4.1, 4.5]
E = [2.4, 3.4]
Q = [1.8, 2.4, 2.8, 3.4, 3.8, 4.8, 5.8, 6.8, 7.8, 8.9, 9.9, 10.9, 11.9, 12.9, 13.9, 14.9]
Q2 = [1.8, 3.7, 6.1, 8.1, 10.2, 12.2, 14.2]
Q0 = [1.2]

def calc(yelan, title):
    dam_dict = {}

    tot_a = 0
    tot_e = 0
    tot_q = 0
    for sec in A:
        tot_a += yelan.A(sec)
        if(sec not in dam_dict):
            dam_dict[sec] = 0
        dam_dict[sec] += yelan.A(sec)

    for sec in E:
        tot_e += yelan.E(sec)
        if(sec not in dam_dict):
            dam_dict[sec] = 0
        dam_dict[sec] += yelan.E(sec)

    for sec in Q:
        tot_q += yelan.Q(sec)
        if(sec not in dam_dict):
            dam_dict[sec] = 0
        dam_dict[sec] += yelan.Q(sec)

    for sec in Q2:
        tot_q += yelan.Q2(sec)
        if(sec not in dam_dict):
            dam_dict[sec] = 0
        dam_dict[sec] += yelan.Q2(sec)

    for sec in Q0:
        tot_q += yelan.Q0(sec)
        if(sec not in dam_dict):
            dam_dict[sec] = 0
        dam_dict[sec] += yelan.Q0(sec)

    print(title)
    print('生命值:', yelan.hp, '暴击率:', yelan.crit1 * 100, '% 暴击伤害:', yelan.crit2 * 100, '%')
    print('Total: ',tot_a + tot_e + tot_q)
    print('A: ', tot_a / (tot_a + tot_e + tot_q) * 100, '% ', tot_a)
    print('E: ', tot_e / (tot_a + tot_e + tot_q) * 100, '% ', tot_e)
    print('Q: ', tot_q / (tot_a + tot_e + tot_q) * 100, '% ', tot_q)

    dam_dict = dict(sorted(dam_dict.items(), key=lambda x : x[0], reverse = False))
    damage = 0
    tempx, tempy = [], []
    for (sec, dam) in dam_dict.items():
        damage += dam
        tempx.append(sec)
        tempy.append(damage)
    
    return tempx, tempy


def Work(title, hp, basehp, crit1, crit2, inc, resist, ainc, qinc, Crit1, Crit2, HP):
    yelan = Stat()
    fig, ax = plt.subplots()
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']

    print(title)
    yelan.init(hp = HP, basehp = basehp, crit1 = Crit1, crit2 = Crit2, inc = inc, resist = resist, ainc = 0, qinc = qinc)
    tx, ty = calc(yelan, '四绝缘')
    ax.plot(tx, ty, c = 'purple', label = '四绝缘')
    mintime = -1

    yelan.init(hp = hp + basehp * 0.2, basehp = basehp, crit1 = crit1, crit2 = crit2, inc = inc + 0.15, resist = resist, ainc = 0, qinc = 0)
    tempx, tempy = calc(yelan, '二水二千岩')
    for i in range(5, len(tx)):
        if(ty[i] > tempy[i]):
            mintime = max(mintime, tx[i])
            break
        if(i == len(tx) - 1):
            mintime = 16
    ax.plot(tempx, tempy, c = 'green', label = '二水二千岩')

    yelan.init(hp = hp, basehp = basehp, crit1 = crit1, crit2 = crit2, inc = inc + 0.15, resist = resist, ainc = 0, qinc = 0.2)
    tempx, tempy = calc(yelan, '二水二宗室')
    for i in range(5, len(tx)):
        if(ty[i] >= tempy[i]):
            mintime = max(mintime, tx[i])
            break
        if(i == len(tx) - 1):
            mintime = 16
    ax.plot(tempx, tempy, c = 'pink', label = '二水二宗室')

    yelan.init(hp = hp, basehp = basehp, crit1 = crit1, crit2 = crit2, inc = inc + 0.15, resist = resist, ainc = 0.3, qinc = 0)
    tempx, tempy = calc(yelan, '四水')
    for i in range(5, len(tx)):
        if(ty[i] >= tempy[i]):
            mintime = max(mintime, tx[i])
            break
        if(i == len(tx) - 1):
            mintime = 16
    ax.plot(tempx, tempy, c = 'blue', label = '四水')

    if(mintime > 0 and mintime <= 15):
        print('绝缘4套装将在', mintime, 's赶超其他圣遗物套装')

    '''
    ax.tick_params(bottom = 'off', top = 'off', left = 'off', right = 'off')
    for key, spine in ax.spines.items():
        spine.set_visible(False)
    '''
    ax.legend(loc = 'upper right')
    ax.set_title(title)
    plt.xlabel('时间')
    plt.ylabel('伤害期望')
    fig.savefig(title + '.png', dpi = 600, format = 'png')




Work('100充能下夜兰单人时间-伤害曲线', hp = 35645.2, basehp = 14450, crit1 = 1, crit2 = 2.242, inc = 0.666, resist = 0, ainc = 0, qinc = 0.3, Crit1 = 1, Crit2 = 2.242, HP = 35645.2)
Work('120充能下夜兰单人时间-伤害曲线', hp = 33044.2, basehp = 14450, crit1 = 1, crit2 = 2.242, inc = 0.666, resist = 0, ainc = 0, qinc = 0.3, Crit1 = 1, Crit2 = 2.242, HP = 35645.2)
Work('140充能下夜兰单人时间-伤害曲线', hp = 30385.4, basehp = 14450, crit1 = 1, crit2 = 2.242, inc = 0.666, resist = 0, ainc = 0, qinc = 0.35, Crit1 = 1, Crit2 = 2.242, HP = 33044.2)
Work('160充能下夜兰单人时间-伤害曲线', hp = 29142.7, basehp = 14450, crit1 = 0.972, crit2 = 2.176, inc = 0.666, resist = 0, ainc = 0, qinc = 0.4, Crit1 = 1, Crit2 = 2.242, HP = 30385.4)
Work('180充能下夜兰单人时间-伤害曲线', hp = 29142.7, basehp = 14450, crit1 = 0.913, crit2 = 2.057, inc = 0.666, resist = 0, ainc = 0, qinc = 0.45, Crit1 = 0.972, Crit2 = 2.176, HP = 29142.7)


Work('100充能下夜兰组队时间-伤害曲线', hp = 35645.2 + 5346.5, basehp = 14450, crit1 = 1, crit2 = 2.242, inc = 0.666 + 0.75, resist = 0.75, ainc = 0, qinc = 0.3, Crit1 = 1, Crit2 = 2.242, HP = 35645.2 + 5346.5)
Work('120充能下夜兰组队时间-伤害曲线', hp = 33044.2 + 5346.5, basehp = 14450, crit1 = 1, crit2 = 2.242, inc = 0.666 + 0.75, resist = 0.75, ainc = 0, qinc = 0.3, Crit1 = 1, Crit2 = 2.242, HP = 35645.2 + 5346.5)
Work('140充能下夜兰组队时间-伤害曲线', hp = 30385.4 + 5346.5, basehp = 14450, crit1 = 1, crit2 = 2.242, inc = 0.666 + 0.75, resist = 0.75, ainc = 0, qinc = 0.35, Crit1 = 1, Crit2 = 2.242, HP = 33044.2 + 5346.5)
Work('160充能下夜兰组队时间-伤害曲线', hp = 29142.7 + 5346.5, basehp = 14450, crit1 = 0.972, crit2 = 2.176, inc = 0.666 + 0.75, resist = 0.75, ainc = 0, qinc = 0.4, Crit1 = 1, Crit2 = 2.242, HP = 30385.4 + 5346.5)
Work('180充能下夜兰组队时间-伤害曲线', hp = 29142.7 + 5346.5, basehp = 14450, crit1 = 0.913, crit2 = 2.057, inc = 0.666 + 0.75, resist = 0.75, ainc = 0, qinc = 0.45, Crit1 = 0.972, Crit2 = 2.176, HP = 29142.7 + 5346.5)
