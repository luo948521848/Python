import pygame,sys
'''
1.搭建窗口信息

'''
class TOM(object):
    #第一部分，main函数，窗口基本设置
    def main(self):
        pygame.display.set_caption('tom猫')
        #1.2设置窗口标ti
        while True:
            #1.4业务逻辑执行部分
            self.action()
            #图形图片绘制
            self.paint()
            #1.3更新屏幕
            pygame.display.update()
    #2.action函数设置，业务逻辑处理
    def action(self):
        #2.1事件更行迭代
        for event in pygame.event.get():
            #2.2判断事件类型
            if event.type == pygame.QUIT:
                sys.exit()
            mouseX,mouseY = pygame.mouse.get_pos()
            #2.3鼠标单击事件，[0]左键单击 [1]左键双击[2]右击
            leftFlag = pygame.mouse.get_pressed()[0]
            #2.4判断
            if  leftFlag and 30 < mouseX < 30 + 60 and 300 < mouseY < 300 + 60:
                #吃鸟的动作
                self.animation = 0
            elif leftFlag and 230 < mouseX < 230 + 60 and 300 < mouseY < 300 + 60:
                # 喝水的动作
                self.animation = 1
            elif  leftFlag and 30 < mouseX < 30 + 60 and 350 < mouseY < 350 + 60:
                #pie的动作
                self.animation = 2
            elif leftFlag and 230 < mouseX < 230 + 60 and 350 < mouseY < 350 + 60:
                # fart的动作
                self.animation = 3
            elif leftFlag and 30 < mouseX < 30 + 60 and 400 < mouseY < 400 + 60:
                # cymbal的动作
                self.animation = 4
            elif leftFlag and 230 < mouseX < 230 + 60 and 400 < mouseY < 400 + 60:
                # scratch的动作
                self.animation = 5
            elif leftFlag and  30 < mouseX < 30 + 210 and 100 < mouseY < 100 + 180:
                #点击头部
                self.animation = 6
            elif leftFlag and  80 < mouseX < 80 + 180 and 300 < mouseY < 300 + 100:
                #点击肚子
                self.animation = 7
            elif leftFlag and  160 < mouseX < 160 + 20 and 470 < mouseY < 470 + 50:
                #点击左脚
                self.animation = 8
            elif leftFlag and  120 < mouseX < 120 + 40 and 470 < mouseY < 470 + 50:
                #点击右脚
                self.animation = 9
            elif leftFlag and  20 < mouseX < 20 + 40 and 50 < mouseY < 50 + 50:
                #点击爆炸
                self.animation = 10
    #3.paint函数，绘制图形
    def paint(self):
        #判断是否执行动画效果
        #吃鸟
        if self.animation == 0:
            #3.2图片转换值增加
            self.index += 1
            #设置图片转换频率
            ys = self.index / 30 % len(self.eats)
            #重新赋值图片 注意ys ===》float
            self.background = self.eats[int(ys)]
            #判断是否最后一张
            if ys == 39:
                self.animation = -1
                self.index = 0
        #喝水
        elif self.animation == 1:
            #3.2图片转换值增加
            self.index += 1
            #设置图片转换频率
            ys = self.index / 30 % len(self.drinks)
            #重新赋值图片 注意ys ===》float
            self.background = self.drinks[int(ys)]
            #判断是否最后一张
            if ys == 80:
                self.animation = -1
                self.index = 0
        #pie
        elif self.animation == 2:
            #3.2图片转换值增加
            self.index += 1
            #设置图片转换频率
            ys = self.index / 30 % len(self.pies)
            #重新赋值图片 注意ys ===》float
            self.background = self.pies[int(ys)]
            #判断是否最后一张
            if ys == 23:
                self.animation = -1
                self.index = 0
        #fart
        elif self.animation == 3:
            #3.2图片转换值增加
            self.index += 1
            #设置图片转换频率
            ys = self.index / 30 % len(self.farts)
            #重新赋值图片 注意ys ===》float
            self.background = self.farts[int(ys)]
            #判断是否最后一张
            if ys== 27:
                self.animation = -1
                self.index = 0
        #cymbal
        elif self.animation == 4:
            #3.2图片转换值增加
            self.index += 1
            #设置图片转换频率
            ys = self.index / 30 % len(self.cymbals)
            #重新赋值图片 注意ys ===》float
            self.background = self.cymbals[int(ys)]
            #判断是否最后一张
            if ys == 12:
                self.animation = -1
                self.index = 0
        #scratch
        elif self.animation == 5:
            #3.2图片转换值增加
            self.index += 1
            #设置图片转换频率
            ys = self.index / 30 % len(self.scratchs)
            #重新赋值图片 注意ys ===》float
            self.background = self.scratchs[int(ys)]
            #判断是否最后一张
            if ys == 55:
                self.animation = -1
                self.index = 0
        #点击头部
        elif self.animation == 6:
            # 3.2图片转换值增加
            self.index += 1
            # 设置图片转换频率
            ys = self.index / 30 % len(self.angrys)
            # 重新赋值图片 注意ys ===》float
            self.background = self.angrys[int(ys)]
            # 判断是否最后一张
            if ys == 25:
                self.animation = -1
                self.index = 0
        #点击肚子
        elif self.animation == 7:
            # 3.2图片转换值增加
            self.index += 1
            # 设置图片转换频率
            ys = self.index / 30 % len(self.stomachs)
            # 重新赋值图片 注意ys ===》float
            self.background = self.stomachs[int(ys)]
            # 判断是否最后一张
            if ys == 33:
                self.animation = -1
                self.index = 0
        # 点击左脚
        elif self.animation == 8:
            # 3.2图片转换值增加
            self.index += 1
            # 设置图片转换频率
            ys = self.index / 30 % len(self.FootLefts)
            # 重新赋值图片 注意ys ===》float
            self.background = self.FootLefts[int(ys)]
            # 判断是否最后一张
            if ys == 29:
                self.animation = -1
                self.index = 0
        # 点击右脚
        elif self.animation == 9:
            # 3.2图片转换值增加
            self.index += 1
            # 设置图片转换频率
            ys = self.index / 30 % len(self.FootRights)
            # 重新赋值图片 注意ys ===》float
            self.background = self.FootRights[int(ys)]
            # 判断是否最后一张
            if ys == 29:
                self.animation = -1
                self.index = 0
        # 点击爆炸
        elif self.animation == 10:
            # 3.2图片转换值增加
            self.index += 1
            # 设置图片转换频率
            ys = self.index / 30 % len(self.Knockouts)
            # 重新赋值图片 注意ys ===》float
            self.background = self.Knockouts[int(ys)]
            # 判断是否最后一张
            if ys == 80:
                self.animation = -1
                self.index = 0
        #3.1绘制背景图片
        self.screen.blit(pygame.transform.scale(self.background,(320,512)),(0,0))
        #绘制吃鸟动作
        self.screen.blit(self.eat, (30, 300))
        #绘制喝水动作
        self.screen.blit(self.drink, (230, 300))
        #绘制放屁动作
        self.screen.blit(self.pie, (30, 350))
        #绘制fart动作
        self.screen.blit(self.fart, (230, 350))
        #绘制cymbal动作
        self.screen.blit(self.cymbal, (30, 400))
        #绘制scratch动作
        self.screen.blit(self.scratch, (230, 400))
    #4.init函数，属性初始化
    def __init__(self):
        self.screen = pygame.display.set_mode((320, 512), 0, 0)
        #背景图片
        self.background = pygame.image.load('Animations/Eat/eat_00.jpg')
        #图片列表存储
        self.eats = self.getImageEat()
        self.drinks = self.getImageDrink()
        self.pies = self.getImagePie()
        self.cymbals = self.getImageCymbal()
        self.farts = self.getImageFart()
        self.scratchs = self.getImageScratch()
        self.angrys = self.getImageAngry()
        self.stomachs = self.getImageStomach()
        self.FootLefts = self.getImageFootLeft()
        self.FootRights = self.getImageFootRight()
        self.Knockouts = self.getImageKnockout()
        #图片集转换值
        self.index = 0
        #吃鸟
        self.eat = pygame.image.load('Buttons/eat.png')
        self.animation = -1
        # 喝水
        self.drink = pygame.image.load('Buttons/drink.png')
        #fart
        self.fart = pygame.image.load('Buttons/fart.png')
        #cymbal
        self.cymbal = pygame.image.load('Buttons/cymbal.png')
        #scratch
        self.scratch = pygame.image.load('Buttons/scratch.png')
        #pie
        self.pie = pygame.image.load('Buttons/pie.png')
#5.get image函数，获取图片列表
    def getImageEat(self):
        #5.4定义列表
        imageEatList = []
        #5.1循环迭代赋值图片
        for i in range(0,40):
            #5.2获取图片路径
            if i < 10:
                imgPath = 'Animations/Eat/eat_0' + str(i)+ '.jpg'
            else:
                imgPath = 'Animations/Eat/eat_' + str(i) + '.jpg'
        #返回列表==》地址
            imageEatList.append(pygame.image.load(imgPath))
        return imageEatList
    def getImageDrink(self):
        #5.4定义列表
        imageDrinkList = []
        #5.1循环迭代赋值图片
        for i in range(0,81):
            #5.2获取图片路径
            if i < 10:
                imgPath = 'Animations/Drink/drink_0' + str(i)+ '.jpg'
            else:
                imgPath = 'Animations/Drink/drink_' + str(i) + '.jpg'

        #返回列表==》地址
            imageDrinkList.append(pygame.image.load(imgPath))
        return imageDrinkList
    def getImagePie(self):
        #5.4定义列表
        imagePieList = []
        #5.1循环迭代赋值图片
        for i in range(0,24):
            #5.2获取图片路径
            if i < 10:
                imgPath = 'Animations/Pie/pie_0' + str(i)+ '.jpg'
            else:
                imgPath = 'Animations/Pie/pie_' + str(i) + '.jpg'
        #返回列表==》地址
            imagePieList.append(pygame.image.load(imgPath))
        return imagePieList
    def getImageFart(self):
        #5.4定义列表
        imageFartList = []
        #5.1循环迭代赋值图片
        for i in range(0,28):
            #5.2获取图片路径
            if i < 10:
                imgPath = 'Animations/Fart/fart_0' + str(i)+ '.jpg'
            else:
                imgPath = 'Animations/Fart/fart_' + str(i) + '.jpg'
        #返回列表==》地址
            imageFartList.append(pygame.image.load(imgPath))
        return imageFartList
    def getImageCymbal(self):
        #5.4定义列表
        imageCymbalList = []
        #5.1循环迭代赋值图片
        for i in range(0,13):
            #5.2获取图片路径
            if i < 10:
                imgPath = 'Animations/Cymbal/cymbal_0' + str(i)+ '.jpg'
            else:
                imgPath = 'Animations/Cymbal/cymbal_' + str(i) + '.jpg'
        #返回列表==》地址
            imageCymbalList.append(pygame.image.load(imgPath))
        return imageCymbalList
    def getImageScratch(self):
        #5.4定义列表
        imageScratchList = []
        #5.1循环迭代赋值图片
        for i in range(0,56):
            #5.2获取图片路径
            if i < 10:
                imgPath = 'Animations/Scratch/scratch_0' + str(i)+ '.jpg'
            else:
                imgPath = 'Animations/Scratch/scratch_' + str(i) + '.jpg'
        #返回列表==》地址
            imageScratchList.append(pygame.image.load(imgPath))
        return imageScratchList
    def getImageAngry(self):
        #5.4定义列表
        imageAngryList = []
        #5.1循环迭代赋值图片
        for i in range(0,26):
            #5.2获取图片路径
            if i < 10:
                imgPath = 'Animations/Angry/angry_0' + str(i)+ '.jpg'
            else:
                imgPath = 'Animations/Angry/angry_' + str(i) + '.jpg'
        #返回列表==》地址
            imageAngryList.append(pygame.image.load(imgPath))
        return imageAngryList
    def getImageStomach(self):
        #5.4定义列表
        imageStomachList = []
        #5.1循环迭代赋值图片
        for i in range(0,34):
            #5.2获取图片路径
            if i < 10:
                imgPath = 'Animations/Stomach/stomach_0' + str(i)+ '.jpg'
            else:
                imgPath = 'Animations/Stomach/stomach_' + str(i) + '.jpg'
        #返回列表==》地址
            imageStomachList.append(pygame.image.load(imgPath))
        return imageStomachList
    def getImageFootLeft(self):
        #5.4定义列表
        imageFootLeftList = []
        #5.1循环迭代赋值图片
        for i in range(0,30):
            #5.2获取图片路径
            if i < 10:
                imgPath = 'Animations/FootLeft/footLeft_0' + str(i)+ '.jpg'
            else:
                imgPath = 'Animations/FootLeft/footLeft_' + str(i) + '.jpg'
        #返回列表==》地址
            imageFootLeftList.append(pygame.image.load(imgPath))
        return imageFootLeftList
    def getImageFootRight(self):
        #5.4定义列表
        imageFootRightList = []
        #5.1循环迭代赋值图片
        for i in range(0,30):
            #5.2获取图片路径
            if i < 10:
                imgPath = 'Animations/FootRight/footRight_0' + str(i)+ '.jpg'
            else:
                imgPath = 'Animations/FootRight/footRight_' + str(i) + '.jpg'
        #返回列表==》地址
            imageFootRightList.append(pygame.image.load(imgPath))
        return imageFootRightList
    def getImageKnockout(self):
        #5.4定义列表
        imageKnockoutList = []
        #5.1循环迭代赋值图片
        for i in range(0,81):
            #5.2获取图片路径
            if i < 10:
                imgPath = 'Animations/Knockout/knockout_0' + str(i)+ '.jpg'
            else:
                imgPath = 'Animations/Knockout/knockout_' + str(i) + '.jpg'
        #返回列表==》地址
            imageKnockoutList.append(pygame.image.load(imgPath))
        return imageKnockoutList
if __name__ == '__main__':
    #获取类
    tm = TOM()
    #调用类方法
    tm.main()



