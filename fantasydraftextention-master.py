#####init
import random
import pygame as p
import math
p.init()
screen=p.display.set_mode((1350,780))
p.display.set_caption('Oracle Algorithm GUI')
#####vars
placespos=["QB","RB","WR","TE","K","DEF"]
playrankshowing="QB"
screenplace=0
drafted=[]
myteam=[]
draftpos=4
numdrafting=10
draftspots=[]
ontheclock=1
loadbar=0
mode=0
avaplayerpage=1
draftrunning=True
running=True
#####var filler
for x in range(0,7):
    draftspots.append(draftpos+2*numdrafting*x)
    draftspots.append(draftpos+2*(numdrafting-draftpos)+1+2*numdrafting*x)
draftspots.append(draftpos+14*numdrafting)
#####colours and fonts
BLACK=(0,0,0)
GREEN=(0,255,0)
WHITE=(255,255,255)
GREY=(160,160,160)
RED=(255,0,0)
introtext = p.font.Font('Fonts\KOMIKAX_.ttf', 15)
playertext = p.font.Font('Fonts\Bebas-Regular.ttf', 43)
playvaltext=p.font.Font('Fonts\Bebas-Regular.ttf', 49)
#####images
draftedteam=p.image.load('Image Assets\draftedteam.jpg')
playrankside=p.image.load('Image Assets\playrankside.jpg')
playranktop=p.image.load('Image Assets\playranktop.jpg')
draftpickscreen=p.image.load('Image Assets\draftpickscreen.jpg')
draftinit=p.image.load('Image Assets\draftinit.jpg')
quitbutton=p.image.load('Image Assets\quitbutton.jpg')
draftorderimg=p.image.load('Image Assets\draftorder.jpg')
myteamimg=p.image.load('Image Assets\myteamimg.jpg')
Kimg=p.image.load('Image Assets\Klogo.jpg')
DEFimg=p.image.load('Image Assets\DEFlogo.jpg')
QBimg=p.image.load('Image Assets\QBlogo.jpg')
RBimg=p.image.load('Image Assets\RBlogo.jpg')
WRimg=p.image.load('Image Assets\WRlogo.jpg')
TEimg=p.image.load('Image Assets\TElogo.jpg')
myteimg=p.image.load('Image Assets\myteimg.jpg')
myqbimg=p.image.load('Image Assets\myqbimg.jpg')
myrbimg=p.image.load('Image Assets\myrbimg.jpg')
mywrimg=p.image.load('Image Assets\mywrimg.jpg')
mykimg=p.image.load('Image Assets\mykimg.jpg')
mydefimg=p.image.load('Image Assets\mydefimg.jpg')
credit=p.image.load('Image Assets\creditimage.jpg')
load=p.image.load('Image Assets\loadingscreen.jpg')
avplayers=p.image.load('Image Assets\playerlist.jpg')
#####init
screen.fill(BLACK)
screen.blit(load,(0,0))
screen.blit(credit,(1150,0))
p.draw.rect(screen,WHITE,(200,640,950,80))
p.draw.rect(screen,BLACK,(205,645,940,70))
screen.blit(introtext.render("Click your mouse to make dots appear if ",True,WHITE),(30,25))
screen.blit(introtext.render("you're bored while data is loading.",True,WHITE),(30,58))
p.display.update()
#####draftdayfuncs
def avaplayerlist(page,drafted):
    order=open("Draft Data\draftorder.txt","r")
    counter=0
    screen.blit(avplayers,(0,0))
    passedplayers=0
    desiredpassed=(page-1)*7
    shownplayers=[]
    plynames=[]
    plypos=[]
    plyval=[]
    for player in order:
        if len(shownplayers)<7:
            cont=0
            playerline=""
            position=""
            name=""
            val=""
            for i in player:
                if cont==0:
                    if i==",":
                        cont=1
                    else:
                        name+=i
                elif cont==1:
                    if i==";":
                        cont=2
                    else:
                        position+=i
                elif cont==2:
                    if i=="|":
                        cont=3
                    else:
                        val+=i
                if cont<3:
                    playerline+=i
            if playerline not in drafted:
                if passedplayers!=desiredpassed:
                    passedplayers+=1
                else:
                    shownplayers.append(playerline)
                    plynames.append(name)
                    plypos.append(position)
                    plyval.append(val)
    for x in range(0,len(shownplayers)):
        p.draw.rect(screen,GREY,(20,90+90*x,560,70))
        p.draw.rect(screen,(200,200,200),(400,90+90*x,110,70))
        screen.blit(playertext.render(str(plynames[x]),True,BLACK),(30,98+90*x))
        screen.blit(playvaltext.render(str(plyval[x]),True,((158-float(plyval[x])),float(plyval[x])*1.7,0)),(408,94+90*x))
        if plypos[x]=="RB":
            screen.blit(RBimg,(510,90+90*x))
        elif plypos[x]=="QB":
            screen.blit(QBimg,(510,90+90*x))
        elif plypos[x]=="WR":
            screen.blit(WRimg,(510,90+90*x))
        elif plypos[x]=="TE":
            screen.blit(TEimg,(510,90+90*x))
        elif plypos[x]=="K":
            screen.blit(Kimg,(510,90+90*x))
        elif plypos[x]=="DEF":
            screen.blit(DEFimg,(510,90+90*x))
        elif plypos[x]=="NONE":
            p.draw.rect(screen,GREY,(20,90+90*x,560,70))
    return shownplayers
def draftorder(ontheclock,draftspots):
    screen.blit(draftorderimg,(600,500))
    for x in range(0,7):
        if x+ontheclock in draftspots:
            colour=RED
        else:
            colour=WHITE
        if ontheclock+x<numdrafting*15+1:
            if x==0:
                if 100>x+ontheclock>9:
                    drafttext = p.font.Font(None, 178)
                    screen.blit(drafttext.render(str(ontheclock+x),True,colour),(616,566))
                elif x+ontheclock>=100:
                    drafttext = p.font.Font(None, 118)
                    screen.blit(drafttext.render(str(ontheclock+x),True,colour),(616,589))
                else:
                    drafttext = p.font.Font(None, 270)
                    screen.blit(drafttext.render(str(ontheclock+x),True,colour),(637,550))
            elif x==1:
                if 100>x+ontheclock>9:
                    drafttext = p.font.Font(None, 92)
                    screen.blit(drafttext.render(str(ontheclock+x),True,colour),(784,654))
                elif x+ontheclock>=100:
                    drafttext = p.font.Font(None, 74)
                    screen.blit(drafttext.render(str(ontheclock+x),True,colour),(775,649))
                else:
                    drafttext = p.font.Font(None, 160)
                    screen.blit(drafttext.render(str(ontheclock+x),True,colour),(790,632))
            elif x==2:
                if 100>x+ontheclock>9:
                    drafttext = p.font.Font(None, 64)
                    screen.blit(drafttext.render(str(ontheclock+x),True,colour),(877,695))
                elif x+ontheclock>=100:
                    drafttext = p.font.Font(None, 44)
                    screen.blit(drafttext.render(str(ontheclock+x),True,colour),(877,695))
                else:
                    drafttext = p.font.Font(None, 105)
                    screen.blit(drafttext.render(str(ontheclock+x),True,colour),(884,681))
            else:
                if 100>x+ontheclock>9:
                    drafttext = p.font.Font(None, 44)
                    screen.blit(drafttext.render(str(ontheclock+x),True,colour),(992+49*(x-4),714))
                elif x+ontheclock>=100:
                    drafttext = p.font.Font(None, 29)
                    screen.blit(drafttext.render(str(ontheclock+x),True,colour),(992+49*(x-4),714))
                else:
                    drafttext = p.font.Font(None, 64)
                    screen.blit(drafttext.render(str(ontheclock+x),True,colour),(998+49*(x-4),706))
def playerranks(playrankshowing,screenplace):
    rnktext = p.font.Font('Fonts\KOMIKAX_.ttf', 25)
    p.draw.rect(screen,(20,20,20),(600,0,550,500))
    counter=0
    if playrankshowing=="QB":
        order=open('Draft Data\oQBdraftorder.txt',"r")
    elif playrankshowing=="WR":
        order=open('Draft Data\oWRdraftorder.txt',"r")
    elif playrankshowing=="RB":
        order=open('Draft Data\oRBdraftorder.txt',"r")
    elif playrankshowing=="TE":
        order=open('Draft Data\oTEdraftorder.txt',"r")
    elif playrankshowing=="K":
        order=open('Draft Data\oKdraftorder.txt',"r")
    else:
        order=open('Draft Data\oDEFdraftorder.txt',"r")
    for player in order:
        screen.blit(rnktext.render(player,True,WHITE),(620,160+40*counter+screenplace))
        counter+=1
    screen.blit(playranktop,(600,0))
    screen.blit(playrankside,(950,0))
    
def my_team(myteam):
    screen.blit(myteamimg,(1150,100))
    screen.blit(credit,(1150,0))
    totalval=0
    qbhad=0
    rbhad=0
    khad=0
    tehad=0
    wrhad=0
    defhad=0
    bnchhad=0
    flxhad=0
    counter=0
    for player in myteam:
        cont=0
        playerline=""
        position=""
        name=""
        val=""
        for i in player:
            if cont==0:
                if i==",":
                    cont=1
                else:
                    name+=i
            elif cont==1:
                if i==";":
                    cont=2
                else:
                    position+=i
            elif cont==2:
                val+=i
            playerline+=i
        if len(name)>15:
            myteamtext = p.font.Font('Fonts\KOMIKAX_.ttf',10)
        else:
            myteamtext = p.font.Font('Fonts\KOMIKAX_.ttf',26-math.floor(len(name)*0.9))
        if position=="QB":
            if qbhad==1:
                screen.blit(myqbimg,(1160,522+37*bnchhad))
                screen.blit(myteamtext.render(str(name),True,WHITE),(1205,524+37*bnchhad))
                bnchhad+=1
            else:
                screen.blit(myqbimg,(1160,164))
                screen.blit(myteamtext.render(str(name),True,WHITE),(1205,166))
                qbhad+=1
        elif position=="RB":
            if rbhad==2:
                if flxhad==1:
                    screen.blit(myrbimg,(1160,522+37*bnchhad))
                    screen.blit(myteamtext.render(str(name),True,WHITE),(1205,524+37*bnchhad))
                    bnchhad+=1
                else:
                    screen.blit(myrbimg,(1160,392))
                    screen.blit(myteamtext.render(str(name),True,WHITE),(1205,394))
                    flxhad+=1
            else:
                screen.blit(myrbimg,(1160,201+38*rbhad))
                screen.blit(myteamtext.render(str(name),True,WHITE),(1205,203+38*rbhad))
                rbhad+=1
        elif position=="WR":
            if wrhad==2:
                if flxhad==1:
                    screen.blit(mywrimg,(1160,522+37*bnchhad))
                    screen.blit(myteamtext.render(str(name),True,WHITE),(1205,524+37*bnchhad))
                    bnchhad+=1
                else:
                    screen.blit(mywrimg,(1160,392))
                    screen.blit(myteamtext.render(str(name),True,WHITE),(1205,394))
                    flxhad+=1
            else:
                screen.blit(mywrimg,(1160,277+38*wrhad))
                screen.blit(myteamtext.render(str(name),True,WHITE),(1205,279+38*wrhad))
                wrhad+=1
        elif position=="TE":
            if tehad==1:
                screen.blit(myteimg,(1160,522+37*bnchhad))
                screen.blit(myteamtext.render(str(name),True,WHITE),(1205,524+37*bnchhad))
                bnchhad+=1
            else:
                screen.blit(myteimg,(1160,353))
                screen.blit(myteamtext.render(str(name),True,WHITE),(1205,355))
                tehad+=1
        elif position=="K":
            if khad==1:
                screen.blit(mykimg,(1160,522+37*bnchhad))
                screen.blit(myteamtext.render(str(name),True,WHITE),(1205,524+37*bnchhad))
                bnchhad+=1
            else:
                screen.blit(mykimg,(1160,431))
                screen.blit(myteamtext.render(str(name),True,WHITE),(1205,433))
                khad+=1
        elif position=="DEF":
            if defhad==1:
                screen.blit(mydefimg,(1160,522+37*bnchhad))
                screen.blit(myteamtext.render(str(name),True,WHITE),(1205,524+37*bnchhad))
                bnchhad+=1
            else:
                screen.blit(mydefimg,(1160,469))
                screen.blit(myteamtext.render(str(name),True,WHITE),(1205,471))
                defhad+=1
        counter+=1
        totalval+=float(val)
    myteamtext = p.font.Font('Fonts\KOMIKAX_.ttf',16)
    screen.blit(myteamtext.render(str(int(totalval*100)/100),True,WHITE),(1266,742))
    
#####loading-loop
loaded=0
while mode<3:
    if loaded==0:
        if loadbar<941:
            if random.randint(0,25)<2:
                p.time.delay(random.randint(1,5)*random.randint(10,20))
            p.draw.rect(screen,GREEN,(205,645,loadbar,70))
            loadbar+=1
            p.display.update()
        else:
            mode=1
            loaded=1
            screen.blit(draftinit,(0,0))
            p.display.update()
    for event in p.event.get():
        if event.type==p.MOUSEBUTTONDOWN:
            if mode==0:
                for x in range(0,random.randint(5,11)):
                    p.draw.circle(screen,(random.randint(100,255),random.randint(0,200),random.randint(0,200)),(random.randint(0,1350),random.randint(0,780)),random.randint(4,12))
            elif mode==1:
                position=event.pos
                if 83<position[0]<1248 and 241<position[1]<589:
                    mode=2
                    screen.blit(draftpickscreen,(0,0))
                    p.display.update()
                elif 427<position[0]<910 and 628<position[1]<733:
                    draftrunning=False
                    mode=3
            elif mode==2:
                playerranks(playrankshowing,screenplace)
                avaplayerlist(avaplayerpage,drafted)
                draftorder(ontheclock,draftspots)
                my_team(myteam)
                mode=3
                p.display.update()
#####master-draftloop
while draftrunning:
    if ontheclock>(numdrafting*15):
        draftrunning=False
    for event in p.event.get():
        if event.type == p.QUIT:
            draftrunning=False
        elif event.type == p.MOUSEBUTTONDOWN:
            position=event.pos
            if 20<position[0]<580:
                if 90<position[1]<160 or 180<position[1]<250 or 270<position[1]<340 or 360<position[1]<430 or 450<position[1]<520 or 540<position[1]<610 or 630<position[1]<700:
                    shownplayers=avaplayerlist(avaplayerpage,drafted)
                    index=math.floor((position[1]-90)/90)
                    if ontheclock in draftspots:
                        myteam.append(shownplayers[index])
                    drafted.append(shownplayers[index])
                    ontheclock+=1
            if 228<position[0]<267 and 730<position[1]<750:
                if avaplayerpage>1:
                    avaplayerpage-=1
            elif 331<position[0]<367 and 730<position[1]<750:
                order=open("draftorder.txt","r")
                counting=0
                for x in order:
                    counting+=1
                counting-=len(drafted)
                counting=math.floor(counting/7)
                order.close()
                if avaplayerpage<counting:
                    avaplayerpage+=1
            elif 973<position[0]<1125 and 191<position[1]<435:
                playrankshowing=placespos[math.floor((position[1]-191)/41)]
            elif 602<position[0]<944 and 152<position[1]<496:
                print("not available yet")
            playerranks(playrankshowing,screenplace)
            avaplayerlist(avaplayerpage,drafted)
            my_team(myteam)
            draftorder(ontheclock,draftspots)
            p.display.update()
#####master-loop
screen.blit(draftedteam,(0,0))
my_team(myteam)
p.display.update()

