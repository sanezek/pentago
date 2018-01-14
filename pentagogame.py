#pentago
#it is a board geme
#you can look rules on https://webdav.info.ucl.ac.be/webdav/ingi2261/ProblemSet3/PentagoRulesStrategy.pdf
#sololear can't run this code on server, but you can test it on your PC
#my github:github.com/sanezek/pentago
#pls print coments


pole=[						
['o','o','o','o','o','o'],				
['o','o','o','o','o','o'],				
['o','o','o','o','o','o'],				
['o','o','o','o','o','o'],				
['o','o','o','o','o','o'],				
['o','o','o','o','o','o']				
]							

pole2=[]

player=1

error=0

def format2():
	global pole 
	pole=[]
	for i in range(3):
		pole.append(pole2[0][i]+pole2[1][i])
	for i in range(3):
		pole.append(pole2[2][i]+pole2[3][i])


def format3():
	global pole2
	pole2=[]
	pole2.append([pole[0][0:3],pole[1][0:3],pole[2][0:3]])
	pole2.append([pole[0][3:],pole[1][3:],pole[2][3:]])
	pole2.append([pole[3][0:3],pole[4][0:3],pole[5][0:3]])
	pole2.append([pole[3][3:],pole[4][3:],pole[5][3:]])



def set_cvet(cor,cv):		#cordins=[x,y];cv= (1 or 2)
	
	global pole
	y=cor[1]
	x=cor[0]
	if cv==1:
		pole[x][y]='1'
	else:
		pole[x][y]='2'	
	format3()

def povp(kw):
	n=[]
	kw-=1
	f=pole2[kw]
	for i in range(3):
		n.append([f[2][i],f[1][i],f[0][i]])
	pole2[kw]=n
	format2()

def povl(kw):
	povp(kw)
	povp(kw)
	povp(kw)

def prow():
	format2()
	w1=0
	w2=0
	for i in range(6):
		if pole[i][0]==0:
			continue
		elif (pole[i][0]==1 and pole[i][1]==1 and pole[i][2]==1 and pole[i][3]==1 and pole[i][4]==1):
			w1=1
		elif (pole[i][0]==2 and pole[i][1]==2 and pole[i][2]==2 and pole[i][3]==2 and pole[i][4]==2):
			w2=1
	for i in  range(6):
		if pole[0][i]==0:
			continue
		elif (pole[0][i]==1 and pole[1][i]==1 and pole[2][i]==1 and pole[3][i]==1 and pole[4][i]==1):
			w1=1
		elif (pole[0][i]==2 and pole[1][i]==2 and pole[2][i]==2 and pole[3][i]==2 and pole[4][i]==2):
			w2=1
	for i in range(6):
		if pole[i][5]==0:
			continue
		elif (pole[i][5]==1 and pole[i][4]==1 and pole[i][3]==1 and pole[i][2]==1 and pole[i][1]==1):
			w1=1
		elif (pole[i][5]==2 and pole[i][4]==2 and pole[i][3]==2 and pole[i][2]==2 and pole[i][1]==2):
			w2=1
	for i in  range(6):
		if pole[5][i]==0:
			continue
		elif (pole[5][i]==1 and pole[4][i]==1 and pole[3][i]==1 and pole[2][i]==1 and pole[1][i]==1):
			w1=1
		elif (pole[5][i]==2 and pole[5][i]==2 and pole[3][i]==2 and pole[2][i]==2 and pole[1][i]==2):
			w2=1
	
	if(pole[0][0]==1 and pole[1][1]==1 and pole[2][2]==1 and pole[3][3]==1 and pole[4][4]==1):
		w1=1
	if(pole[0][0]==2 and pole[1][1]==2 and pole[2][2]==2 and pole[3][3]==2 and pole[4][4]==2):
		w2=1
	if(pole[0][5]==1 and pole[1][4]==1 and pole[2][3]==1 and pole[3][2]==1 and pole[4][1]==1):
		w1=1
	if(pole[0][5]==2 and pole[1][4]==2 and pole[2][3]==2 and pole[3][2]==2 and pole[4][1]==2):
		w2=1
	if(pole[5][5]==1 and pole[4][4]==1 and pole[3][3]==1 and pole[2][2]==1 and pole[1][1]==1):
		w1=1	
	if(pole[5][5]==2 and pole[4][4]==2 and pole[3][3]==2 and pole[2][2]==2 and pole[1][1]==2):
		w2=1
	if(pole[5][0]==1 and pole[4][1]==1 and pole[3][2]==1 and pole[2][3]==1 and pole[1][4]==1):
		w1=1	
	if(pole[5][0]==2 and pole[4][1]==2 and pole[3][2]==2 and pole[2][3]==2 and pole[1][4]==2):
		w2=1
	if(pole[1][0]==1 and pole[2][1]==1 and pole[3][2]==1 and pole[4][3]==1 and pole[5][4]==1):
		w1=1	
	if(pole[1][0]==2 and pole[2][1]==2 and pole[3][2]==2 and pole[4][3]==2 and pole[5][4]==2):
		w2=1
	if(pole[0][1]==1 and pole[1][2]==1 and pole[2][3]==1 and pole[3][4]==1 and pole[4][5]==1):
		w1=1	
	if(pole[0][1]==2 and pole[1][2]==2 and pole[2][3]==2 and pole[3][4]==2 and pole[4][5]==2):
		w2=1
	
	if(pole[0][4]==1 and pole[1][3]==1 and pole[2][2]==1 and pole[3][1]==1 and pole[4][0]==1):
		w1=1	
	if(pole[0][4]==2 and pole[1][3]==2 and pole[2][2]==2 and pole[3][1]==2 and pole[4][0]==2):
		w2=1
	if(pole[1][5]==1 and pole[2][4]==1 and pole[3][3]==1 and pole[4][2]==1 and pole[5][1]==1):
		w1=1	
	if(pole[1][5]==2 and pole[2][4]==2 and pole[3][3]==2 and pole[4][2]==2 and pole[1][5]==2):
		w2=1
	if w1==1 and w2==1:
		return(3)
	elif w1==0 and w2==0 :
		return(0)	
	elif w1==1:
		return(1)
	elif w2==1:
		return(2)
	

def printpole():
	print()
	for i in range(3):
		a=pole2[0][i][0]+' '+pole2[0][i][1]+' '+pole2[0][i][2]+' '+pole2[1][i][0]+' '+pole2[1][i][1]+' '+pole2[1][i][2]
		print(a)
	for i in range(3):
		a=pole2[2][i][0]+' '+pole2[2][i][1]+' '+pole2[2][i][2]+' '+pole2[3][i][0]+' '+pole2[3][i][1]+' '+pole2[3][i][2]
		print(a)
	print()

def game():
	printpole()
	global error
	error=0
	print('running {} player'.format(player))
	inp=input('>')
	if (len(inp)==4 and inp[0] in p[0] and inp[1] in p[1] and inp[2] in p[2] and inp[3] in p[3]): 
		hod(int(inp[0]),int(inp[1]))
		if error==0:
			if inp[3]=='l':
				povl2(int(inp[2]))
			else:
				povp2(int(inp[2]))		
		d=prow()
		if d==1:
			print('The first player winы')
			exit()
		elif d==2:
			print('The second player wins')
			exit()
		elif d==3:
			print('draw')
			exit()
	elif inp =='exit':
		exit()
	else:
		print(hell())


def hod(x,y):
	x=int(x)-1
	y=int(y)-1
	if pole[y][x]=='o':
		set_cvet([y,x],player)
	else:
		global error
		error=1
		print('Please put the chip into an empty cell')

def hell():
	print('Enter the data in the format xyns \nx - the number of the column in which to put the ball (1-6) \ny - the number of the line in which to put the ball (1-6) \nn - the number of the field you want to rotate (1-4) \ns is the side to rotate the selected field (l, r)')

def povl2(kw):
	kw=int(kw)
	povl(kw)
	global player
	if player==1:
		player=2
	else:
		player=1



def povp2(kw):
	global player
	kw=int(kw)
	povp(kw)
	if player==1:
		player=2
	else:
		player=1	

p=[
['1','2','3','4','5','6'],
['1','2','3','4','5','6'],
['1','2','3','4'],
['r','l']
]

print("sololearn can't  run my code, but u can test in on your PC")
print("rules here : https://webdav.info.ucl.ac.be/webdav/ingi2261/ProblemSet3/PentagoRulesStrategy.pdf")
format3()
while 1:
	game()
