#pentago

pole=[						# kw=1   kw=2
[0,0,0,0,0,0],				# 0 0 0| 0 0 0
[0,0,0,0,0,0],				# 0 0 0| 0 0 0
[0,0,0,0,0,0],				# 0 0 0| 0 0 0
[0,0,0,0,0,0],				#_____________
[0,0,0,0,0,0],				# kw=3   kw=4
[0,0,0,0,0,0]				# 0 0 0| 0 0 0
]							# 0 0 0| 0 0 0
							# 0 0 0| 0 0 0


pole2=[]

player=1

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
	pole[x][y]=cv
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
		a=str(pole2[0][i][0])+' '+str(pole2[0][i][1])+' '+str(pole2[0][i][2])+'   '+str(pole2[1][i][0])+' '+str(pole2[1][i][1])+' '+str(pole2[1][i][2])
		print(a)
	print()
	for i in range(3):
		a=str(pole2[2][i][0])+' '+str(pole2[2][i][1])+' '+str(pole2[2][i][2])+'   '+str(pole2[3][i][0])+' '+str(pole2[3][i][1])+' '+str(pole2[3][i][2])
		print(a)
	print()

def game():
	printpole()
	print('ход {} игрока'.format(player))
	if coms['hod'][1]==1:
		print('поставьте фишку')
	if coms['hod'][1]==0:
		print('поверние любое из полей')
	inp=input('>').split()
	if len(inp)!=0:
		com=inp[0]
		if (com in coms)  :
			if coms[com][1]==1:
				comm=coms[com][0]
			if len(inp)==2:
				try:
					comm(inp[1])
				except TypeError:
					print("недостаточно данных, попробуйте снова")
			elif len(inp)==3:
				comm(inp[1],inp[2])
			elif len(inp)==1:
				try:
					comm()
				except TypeError:
					print("недостаточно данных, попробуйте снова")
		else:
			print('\nUnknown command\n'+help2())
		d=prow()
		if d==1:
			print('Первый игрок победил, поздравляю')
			exit()
		elif d==2:
			print('Второй игрок победил, поздравляю')
			exit()
		elif d==3:
			print('Поздравляю победила дружба, но КАК ВЫ ЭТО СДЕЕЛАЛИ???')
			exit()
	else:
		print(help())


def hod(x,y):
	try:
		x=int(x)-1
		y=int(y)-1
		if pole[y][x]==0:
			set_cvet([y,x],player)
			coms['hod'][1]=0
			coms['povp'][1]=1
			coms['povl'][1]=1
		else:
			print('Пожалуйста,поместите фишку в свободную ячейку')
	except ValueError:
		print('Данные не в нужном формате, попробуйте снова')

def help2():
	return'Вот список доступных команд:\nhelp - помощь\nhod x y - ход игрока у которго право хода по координатам x y \npovp kw - поворот вправо квадрато под номер kw\npovд kw - поворот влево квадрато под номер kw\nexit - выход'


def help():
	print('Вот список доступных команд:\nhelp - помощь\nhod x y - ход игрока у которго право хода по координатам x y \npovp kw - поворот вправо квадрато под номер kw\npovд kw - поворот влево квадрато под номер kw\nexit - выход')

def povl2(kw):
	try:
		kw=int(kw)
		povl(kw)
		global player
		if player==1:
			player=2
		else:
			player=1
		coms['hod'][1]=1
		coms['povp'][1]=0
		coms['povl'][1]=0
	except ValueError:
		print('Данные не в нужном формате, попробуйте снова')


def povp2(kw):
	try:
		global player
		kw=int(kw)
		povp(kw)
		if player==1:
			player=2
		else:
			player=1	
		coms['hod'][1]=1
		coms['povp'][1]=0
		coms['povl'][1]=0
	except ValueError:
		print('Данные не в нужном формате, попробуйте снова')

coms={
	'help':[help,1],				#haha
	'hod':[hod,1],
	'povl':[povl2,0],
	'povp':[povp2,0],
	'exit':[exit,1]
}

format3()
while 1:
	game()