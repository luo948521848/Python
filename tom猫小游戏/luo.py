


import pygame,sys,math
class Word(object):
    def action(self):


        #窗口按钮
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def __init__(self):
        #屏幕
        self.screen = pygame.display.set_mode((1000, 800), 0, 0)

        self.screen.fill((233, 233, 233))
        # 赋值






      #绘制函数
    def paint(self):
        pygame.draw.circle(self.screen, (255, 255, 0), (500, 400), 350, 5)
        pygame.draw.circle(self.screen, (255, 255, 0), (500, 400), 250, 0)

        pygame.draw.circle(self.screen, (0, 0, 0), (500, 400), 250, 5)
        #外圈
        pygame.draw.circle(self.screen, (0, 0, 0), (375, 275), 50, 0)
        pygame.draw.circle(self.screen, (0, 0, 0), (625, 275), 50, 0)
        #眼睛
        pygame.draw.circle(self.screen, (0, 0, 0), (500, 350), 20, 0)
        #鼻子
        pygame.draw.line(self.screen, (0, 0, 0), (250, 400), (750, 400), 6)
        pygame.draw.line(self.screen, (0, 0, 0), (500, 650), (500, 400), 6)
        pygame.draw.line(self.screen, (0, 0, 0), (375, 400), (375, 610), 6)
        pygame.draw.line(self.screen, (0, 0, 0), (625, 400), (625, 610), 6)
        #嘴
        pygame.draw.line(self.screen, (0, 0, 0), (500, 650), (500, 750),6)
        pygame.draw.line(self.screen, (0, 0, 0), (500, 50), (500, 150),6)
        #外圈的六根线
        pygame.draw.line(self.screen, (0, 0, 0), (324, 576),(253,653), 6)
        pygame.draw.line(self.screen, (0, 0, 0), (676, 576),(747,653), 6)
        pygame.draw.line(self.screen, (0, 0, 0), (324, 224), (253, 153), 6)
        pygame.draw.line(self.screen, (0, 0, 0), (676, 224), (747, 153), 6)



        pygame.draw.arc(self.screen, (0, 0, 0),((350, 40), (450,80)) ,1,3.14,5)
    def main(self):
        self.__init__()
        pygame.display.set_caption('心脏')



        while True:


            self.action()
            self.paint()
            pygame.display.update()

if __name__ == '__main__':
    wd = Word()
    wd.main()