import random
chance = 5
res = random.choice(range(10)) + 1
print("恭喜您获得" + str(chance) + "次抽奖机会:")
# 判断是否中奖
while ( chance != 0 ):
    num = int(input("请输入数字(1-10): "))
    if  num == res:
        print("恭喜您中奖了！")
    else:
        print("好可惜，大奖与您擦肩而过，祝您下次好运！")
    chance -= 1
    print("您还有" + str(chance)+ "次抽奖机会!")
print("对不起，您的机会用完了!")

