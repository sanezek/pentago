

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


def hod(x,y):
	x=int(x)-1
	y=int(y)-1
	if pole[y][x]=='o':
		set_cvet([y,x],player)
	else:
		global error
		error=1

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
format3()
