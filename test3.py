#!/user/bin/python
#-*-coding:utf-8-*-
import pygame, sys
import os     #文件操作的库，用于判断图片是否正确
from pygame.locals import * #引入一些常量名
pathpw = r'D:\python\雏燕计划前端界面\看图识词20题'  #题图的路径
pathwp = r'D:\python\雏燕计划前端界面\识词辨图'
path1 = r'D:\python\雏燕计划前端界面\arrow'        #箭头的路径
path3 = r'D:\python\雏燕计划前端界面\元素'         #正确，错误图案的路径

class question(pygame.sprite.Sprite):             #加载图片的类
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = screen
        self.image = None
        self.rect = None
    def load(self,filename,left,top,width=None):
        self.image = pygame.image.load(filename).convert_alpha()
        rect = self.image.get_rect()              # 获取图片信息
        if(width!=None):
            imageheight = int(rect.height * width / rect.width)  # 转化不允许浮点数，需要转化为int型
            self.image = pygame.transform.smoothscale(self.image, (width, imageheight), )  # 转化大小为100左右
        else:
            width = rect.width
            imageheight = rect.height
        self.rect = left,top,width,imageheight
class showquestion(question, pygame.sprite.Group):  #显示一道题的类
    def __init__(self,screen):               #number是第几道题，screen是主屏幕
        self.screen = screen
    def Load(self,path,number):
        Path = path + '\\' + str(number)
        #以下是载入图片
        self.word = question(self.screen)
        self.word.load(os.path.join(Path,os.listdir(Path)[0]), 335, 245,110)#参数分别为路径，左坐标、上坐标、宽度
        self.up = question(self.screen)
        self.up.load(os.path.join(Path,os.listdir(Path)[1]), 330, 50,100)
        self.uparrow = question(self.screen)
        self.uparrow.load(os.path.join(path1,os.listdir(path1)[0],),350,150,60)
        self.down = question(self.screen)
        self.down.load(os.path.join(Path,os.listdir(Path)[2]), 330, 450,100)
        self.downarrow = question(self.screen)
        self.downarrow.load(os.path.join(path1,os.listdir(path1)[1]),350,355,60)
        self.left = question(self.screen)
        self.left.load(os.path.join(Path,os.listdir(Path)[3]), 140, 250,100)
        self.leftarrow = question(self.screen)
        self.leftarrow.load(os.path.join(path1,os.listdir(path1)[2]),250,260,80)
        self.right = question(self.screen)
        self.right.load(os.path.join(Path,os.listdir(Path)[4]), 540, 250,100)
        self.rightarrow = question(self.screen)
        self.rightarrow.load(os.path.join(path1,os.listdir(path1)[3]),450,260,80)
        #将所有精灵加入一个精灵组一起操作
        self.group = pygame.sprite.Group()
        self.group.add(self.word, self.left, self.leftarrow, self.right, self.rightarrow, self.up, self.uparrow, self.down, self.downarrow)
    def Add(self):                               #这个重新加载5张图片
        self.group.add(self.word,self.left,self.leftarrow,self.right,self.rightarrow,self.up,self.uparrow,self.down,self.downarrow)
        # print(self.group)
        # self.group.empty()
        self.group.draw(self.screen)
    def Empty(self):                             #让图片消失
        self.group.empty()
        # self.word.kill()
        # self.group.draw(self.screen)
        # print(self.group)
pygame.init()                                    #初始化
#
font1 = pygame.font.Font("C:/Windows/Fonts/simhei.ttf",25)  #提示语字体
font2 = pygame.font.Font("C://Windows//Fonts//STHUPO.TTF",36)#计分字体
BLACK = (0,0,0)
wordcolor = (0,255,255)                          #蓝青色
tipscolor = (0,110,250)                          #左下角提示语颜色
#文字绘制
def print_text(font,x,y,text,color=(255,255,255),shadow=True):#显示文字函数，用于显示分数,shadow表示阴影,不给颜色默认为白色
    if shadow:
        imgText = font.render(text,True,(BLACK))
        screen.blit(imgText,(x-2,y-2))
    imgText = font.render(text,True,color)
    screen.blit(imgText,(x,y))
screen = pygame.display.set_mode((800,600),0,32) #主屏幕
pygame.display.set_caption("Happy Learning")     #左上角名字
def showfirstpage():
    rpath = r'D:\python\雏燕计划前端界面\元素'#首页上各图片的路径
    p1 = question(screen)
    p1.load(rpath+'\个人信息.png',330,100)   #参数为filename，left，top
    p2 = question(screen)
    p2.load(rpath+'\看图识词.png',125,250)
    p3 = question(screen)
    p3.load(rpath +'\识词辨图.png',525,250)
    p4 = question(screen)
    p4.load(rpath+'\听词辨图.png',330,400) #注：英文命名的文件开头要加反斜线（转义字符），中文不用
    p5 = question(screen)
    p5.load(rpath+'\\righttop.png',600,0)  #首页右上图
    p6 = question(screen)
    p6.load(rpath + '\\leftdown.png',0,420)#首页左下图
    group = pygame.sprite.Group()
    group.add(p1,p2,p3,p4,p5,p6)
    return group
questioncount = 1                                #第几题
fmenu = 0                                        #功能控制变量
score = 0                                        #得分
showscore = False                                #显示分数
# q1 = showquestion(questioncount,screen)        #显示第一道题
# q1.Empty()                                     #先不显示q1
firstpagegroup  = showfirstpage()                #首页
correct = question(screen)
correct.load(path3+'\\correct.png',200,100)      #导入正确图案
wrong = question(screen)
wrong.load(path3+'\\wrong.png',200,100)          #错误图案
framerate = pygame.time.Clock()                  #建立一个时钟对象来帮助追踪时间

showright = False                  #在一个if语句里只能等if结束之后才能draw到屏幕上，所以这里使用一个控制变量，在两个if中完成答案正确动画效果
showwrong = False
choose = True                                 #使得显示对错期间按键失效
q1 = showquestion(screen)
while True:
    framerate.tick(30)                           #更新时钟
    ticks = pygame.time.get_ticks()              #得到以毫秒为间隔的时间
    screen.fill((255,255,255))                   #背景填充为白色
    if showright:
        pygame.time.delay(1000)                  #延时1s
        firstpagegroup.empty()                   #正确图案消失
        pygame.event.clear()                     #清空事件队列，防止显示对错期间按键冲突
        questioncount = questioncount + 1
        # q1.Load(Ps,questioncount) #显示下一个题目
        showright = False
        choose = True
    elif showwrong:
        pygame.time.delay(1000)
        firstpagegroup.empty()
        pygame.event.clear()
        questioncount = questioncount + 1
        # q1.Load(Ps,questioncount)#显示下一个题目
        showwrong = False
        choose = True
    elif showscore:
        print_text(font2,20,20,"得分："+str(score),wordcolor)
        print_text(font1,20,550,"按下方向键选择正确答案",tipscolor,False)
        back = question(screen)
        back.load("D:\python\雏燕计划前端界面\元素\返回.png",640,455,100)   #返回按钮
        backgroup = pygame.sprite.Group()
        backgroup.add(back)
        backgroup.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if (fmenu == 0):
                    fmenu = 1
                elif (fmenu >= 1):
                    choose = False
                    if (len(os.listdir(P)[1].split("#")) == 2):
                        print("恭喜您回答正确")
                        q1.Empty()
                        firstpagegroup.add(correct)
                        showright = True
                        score = score + 1
                    else:
                        print("很抱歉，您的答案是错的")
                        q1.Empty()
                        firstpagegroup.add(wrong)
                        showwrong = True
            elif event.key == pygame.K_DOWN:
                if (fmenu == 0):
                    fmenu = 2
                    firstpagegroup.empty()
                    showscore = True
                elif (fmenu >= 1):
                    choose = False
                    if (len(os.listdir(P)[2].split("#")) == 2):
                        print("恭喜您回答正确")
                        q1.Empty()
                        firstpagegroup.add(correct)
                        showright = True
                        score = score + 1
                    else:
                        print("很抱歉，您的答案是错的")
                        q1.Empty()
                        firstpagegroup.add(wrong)
                        showwrong = True
            elif event.key == pygame.K_LEFT:
                if (fmenu == 0):
                    fmenu = 3
                    firstpagegroup.empty()
                    showscore = True
                elif (fmenu >= 1):
                    choose = False
                    if (len(os.listdir(P)[3].split("#")) == 2):
                        print("恭喜您回答正确")
                        q1.Empty()
                        firstpagegroup.add(correct)
                        showright = True
                        score = score + 1
                    else:
                        print("很抱歉，您的答案是错的")
                        q1.Empty()
                        firstpagegroup.add(wrong)
                        showwrong = True
            elif event.key == pygame.K_RIGHT:
                if (fmenu == 0):
                    fmenu = 4
                    firstpagegroup.empty()
                    showscore = True
                elif (fmenu >= 1):
                    choose = False
                    if (len(os.listdir(P)[4].split("#")) == 2):
                        print("恭喜您回答正确")
                        q1.Empty()
                        firstpagegroup.add(correct)
                        showright = True
                        score = score + 1
                    else:
                        print("很抱歉，您的答案是错的")
                        q1.Empty()
                        firstpagegroup.add(wrong)
                        showwrong = True
            elif event.key == pygame.K_RETURN:
                if (fmenu >= 1):
                    choose = False
                    firstpagegroup.empty()
                    questioncount += 1
                    if (questioncount <= 20):
                        q1.Load(Ps, questioncount)  # 显示下一道题
                    else:
                        print("您已经做完啦！！！")
        elif event.type == MOUSEBUTTONDOWN:  #鼠标点击事件
            presseed =  pygame.mouse.get_pressed()
            if presseed[0] == 1 and showscore:
                pos = pygame.mouse.get_pos()
                print(pos)
                if pos[0]>=640 and pos[0]<=737:    #判断按钮位置
                    if pos[1]>=455 and pos[1]<=528:
                        #按了返回键后
                        print("按钮触发")
                        q1.Empty()
                        firstpagegroup = showfirstpage()  # 首页
                        questioncount = 1
                        fmenu = 0
                        showscore = False
                        score = 0


    if fmenu == 3 and choose:  #选择答案时要显示对错，所以加一个条件choose
        P = pathpw + "//"+str(questioncount)
        Ps = pathpw
        q1.Load(Ps,questioncount)
    elif fmenu == 4 and choose:
        P = pathwp + "//" + str(questioncount)
        Ps = pathwp
        q1.Load(Ps,questioncount)
    if not fmenu==0:
        q1.group.update(ticks)   #精灵组更新，不要也没影响
        q1.group.draw(screen)    #绘制精灵组的所有image
    firstpagegroup.update(ticks)
    firstpagegroup.draw(screen)

    pygame.display.update()  # 程序刷新

