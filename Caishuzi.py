import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个1到100之间的数字，你需要猜出它是多少。")

    while True:
        guess = int(input("请输入你的猜测："))
        attempts += 1

        if guess < number:
            print("猜错了，再大一点！")
        elif guess > number:
            print("猜错了，再小一点！")
        else:
            print(f"恭喜你，猜对了！你用了{attempts}次猜对了答案。")
            break

guess_number()
