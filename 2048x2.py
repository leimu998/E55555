"""
    2048 GAME
"""
import random
import copy

score = 0  # 分数
init_count = 2  # 初始值的个数
before_source = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]  # 操作前的矩阵
after_source = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]  # 操作后的矩阵（当前打印的矩阵）
random_tuple = (2, 4)  # 初始添加的值、移动时添加的值


# Controller层
def zero_to_end(list_data):
    """
    重排序函数（核心算法）
    非0元素移至最前（保持顺序），0元素移至最后，充当中间人处理列表的角色
    :param list_data: list 一维列表
    :return: None
    """
    for i in range(3, -1, -1):
        if not list_data[i]:
            del list_data[i]
            list_data.append(0)


def merge_single(list_data):
    """
    合并元素函数（核心算法）
    重排序后，左边两个相邻相同的非0元素相加，后方补0，并加分（可diy）
    如果两个相邻的元素不同或者为0，则不做其他操作
    :param list_data: list 一维列表
    :return: None
    """
    zero_to_end(list_data)
    for i in range(3):
        if list_data[i] == 0: break
        if list_data[i] == list_data[i + 1]:
            list_data[i] *= 2
            del list_data[i + 1]
            list_data.append(0)
            global score
            score += list_data[i]


def random_site():
    """
    随机填充0元素函数（非核心）
    随机挑选0元素的位置，进行随机填充random_list中的任意一个元素
    可通过增删改变random_list中的元素，从而影响到随机填充的数字
    :return: None
    """
    random_list_len = len(random_tuple)
    while True:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if after_source[x][y] == 0:
            after_source[x][y] = random_tuple[random.randint(0, random_list_len - 1)]
            break


def merge():
    """合并操作，详见merge_single()函数"""
    for i in range(4):
        merge_single(after_source[i])


def reverse():
    """逆转2048二维列表中的每一行一维列表"""
    for i in range(4):
        after_source[i].reverse()


def transposition():
    """二维列表转置（矩阵转置）"""
    for x in range(4):
        for y in range(x, 4):
            after_source[x][y], after_source[y][x] = after_source[y][x], after_source[x][y]


def compare_matrix():
    """
    二维数组比较
    操作前后的二维数组（矩阵）进行比较
    如果不相等，说明有元素可移动，当移动时调用random_site()函数
    """
    if not (before_source == after_source):
        random_site()


def left():
    """向左操作"""
    merge()


def right():
    """向右操作"""
    reverse()
    merge()
    reverse()


def up():
    """向上操作"""
    transposition()
    merge()
    transposition()


def down():
    """向下操作"""
    transposition()
    reverse()
    merge()
    reverse()
    transposition()


# View层
def init():
    """
    游戏初始化
    :return: None
    """
    print(f"""当前分数：{score}\n操作方式：q退出 n认输
       w(上)
a(左)  s(下)  d(右)""")
    for i in range(init_count):  # 随机生成init_count个初始值
        random_site()
    print_list()


def print_list():
    """打印游戏过程中必看的矩阵信息"""
    for single_list in after_source:
        print(single_list)


def forfeit():
    """认输"""
    print(f"玩家已认输，最终得分：{score}")
    raise KeyboardInterrupt


def main():
    """程序入口：初始化 + 输入 + 输出"""
    init()
    while True:
        try:
            global before_source
            before_source = copy.deepcopy(after_source)
            key = input("键入：")
            if key == "a": left()
            if key == "d": right()
            if key == "w": up()
            if key == "s": down()
            if key == "n": forfeit()
            if key == "q": break
            compare_matrix()
            print(f"当前分数：{score}")
            print_list()
        except KeyboardInterrupt:
            break


main()

