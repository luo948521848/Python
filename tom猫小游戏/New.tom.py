import pygame,sys
class TOM(object):
    #第一部分，main函数，窗口基本设置
    def main(self):
        # 1.1设置窗口标ti
        pygame.display.set_caption('tom猫')
        #1.2死循环
        while True:
            #1.4业务逻辑执行部分
            self.action()
            #1.5图形图片绘制
            self.paint()
            #1.3更新屏幕
            pygame.display.update()
    #2.action函数设置，业务逻辑处理
    def action(self):
        #2.1事件更新迭代
        for event in pygame.event.get():
            #2.2判断事件类型
            if event.type == pygame.QUIT:
                sys.exit()
            #2.3鼠标监听
            if event.type == pygame.MOUSEBUTTONDOWN:
                #2.4获取鼠标信息
                mouseX, mouseY = pygame.mouse.get_pos()
                # 2.5鼠标单击事件，
                # [0]左键单击 [1]左键双击[2]右击
                leftFlag = pygame.mouse.get_pressed()[0]
                #2.6判断吃鸟动作
                if leftFlag and 30 < mouseX < 30 + 60 and 300 < mouseY < 300 + 60:
                    # 2.7设置图片总数
                    self.count = 40
                    #2.8获取图片
                    self.getImage('eat')
                    #2.9设置图片集转换值
                    self.index = 0
                elif leftFlag and 230 < mouseX <290 and 300 < mouseY < 360:
                    self.count = 81
                    self.getImage('drink')
                elif leftFlag and 30 < mouseX < 30 + 60 and 350 < mouseY < 350 + 60:
                    # pie的动作
                    self.count = 24
                    self.getImage('pie')
                elif leftFlag and 230 < mouseX < 230 + 60 and 350 < mouseY < 350 + 60:
                    # fart的动作
                    self.count = 28
                    self.getImage('fart')
                elif leftFlag and 30 < mouseX < 30 + 60 and 400 < mouseY < 400 + 60:
                    # cymbal的动作
                    self.count = 13
                    self.getImage('cymbal')
                elif leftFlag and 230 < mouseX < 230 + 60 and 400 < mouseY < 400 + 60:
                    # scratch的动作
                    self.count = 56
                    self.getImage('scratch')
                elif leftFlag and 30 < mouseX < 30 + 210 and 100 < mouseY < 100 + 180:
                    # 点击头部
                    self.animation = 6
                elif leftFlag and 80 < mouseX < 80 + 180 and 300 < mouseY < 300 + 100:
                    # 点击肚子
                    self.count = 34
                    self.getImage('stomach')
                elif leftFlag and 160 < mouseX < 160 + 20 and 470 < mouseY < 470 + 50:
                    # 点击左脚
                    self.count = 30
                    self.getImage('footLeft')
                elif leftFlag and 120 < mouseX < 120 + 40 and 470 < mouseY < 470 + 50:
                    # 点击右脚
                    self.count = 30
                    self.getImage('footRight')
                elif leftFlag and 20 < mouseX < 20 + 40 and 50 < mouseY < 50 + 50:
                    # 点击爆炸
                    self.count = 81
                    self.getImage('knockout')


    def paint(self):
        # 3.1绘制背景图片
        self.screen.blit(pygame.transform.scale(self.background, (320, 512)), (0, 0))
        #3.2 绘制吃鸟动作
        self.screen.blit(self.eat,(30,300))
        #3.3
        if self.count * 10 >  self.index:
            self.index += 1
            ys = self.index/10%len(self.images)
            #赋值
            self.background = self.images[int(ys)]
        else:
            #结束清空所有值
            self.count = -1
            self.index = 0
            #列表清空
            self.images = []

        # 绘制吃鸟动作
        self.screen.blit(self.eat, (30, 300))
        # 绘制喝牛奶动作
        self.screen.blit(self.drink, (230, 300))
        # 绘制放屁动作
        self.screen.blit(self.pie, (30, 350))
        # 绘制fart动作
        self.screen.blit(self.fart, (230, 350))
        # 绘制cymbal动作
        self.screen.blit(self.cymbal, (30, 400))
        # 绘制scratch动作
        self.screen.blit(self.scratch, (230, 400))

    def __init__(self):
        self.screen = pygame.display.set_mode((320, 512), 0, 0)
        # 背景图片
        self.background = pygame.image.load('Animations/Eat/eat_00.jpg')
        # 图片列表存储
        self.eat = pygame.image.load('Buttons/eat.png')
        #4.4 图片存储列表
        self.images = []
        #4.5图片集转换值
        self. index = 0
        #4.6图片数量
        self.count = -1
        #4.7喝牛奶
        self.drink = pygame.image.load('Buttons/drink.png')
        # 4.8fart
        self.fart = pygame.image.load('Buttons/fart.png')
        # 4.9cymbal
        self.cymbal = pygame.image.load('Buttons/cymbal.png')
        # 4.10scratch
        self.scratch = pygame.image.load('Buttons/scratch.png')
        # 4.11pie
        self.pie = pygame.image.load('Buttons/pie.png')

    def getImage(self,name):
        #5.1 获取图片
        for i in range(0,self.count):
            #5.2判断路径地址
            if i < 10:
                imgPath = 'Animations/' + name + '/' + name + '_0'+ str(i) + '.jpg'
            else:
                imgPath = 'Animations/' + name + '/' + name + '_' + str(i) + '.jpg'
            self.images.append(pygame.image.load(imgPath))


if __name__ == '__main__':
    tm = TOM()
    tm.main()