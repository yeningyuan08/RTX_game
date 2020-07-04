import pickle
class basedx:              #地形
    basexg={}              #基础效果
    tsxg={}                #特殊效果（如：核辐射）
    in_units=[]            #驻守单位
    in_bulldings=[]        #内部建筑
    max_bullding=10        #最大建筑数
class hill(basedx):        #山
    def __init__(self):
        self.basexg['soldiers_range']=2
        self.basexg['soldiers_defend']=1.5
        self.basexg['armored_car_health']=0.75
        self.basexg['Non_armoured_vehicle_defend']=1.5
        self.basexg['rocket_range']=2.5
        self.basexg['plane_attack']=0.5
        self.basexg['plane_to_death']=1
class contry(basedx):
    def __init__(self):
        self.basexg['soldiers_defend']=2.5
        
class game_save:
	def __init__(mapfilename,self):
	    t=read_map(mapfilename)
	    if (type(t[0]['plys'])!=int or type(t[0]['max_x'])!=int) or type(t[0]['max_y'])!=int:
	        raise TypeError("读取地图时发生致命错误")
		self.players=t[0]['plys']
		self.max_x=t[0]['max_x']
		self.max_y=t[0]['max_y']
		self.base_map=t[0]['map']
		self.real_time_map=[]
		for i in range(1,max_x+1)
		
def read_map(mapfilename):
	f=open(mapfilename,'r')
	t=pickle.load(f)
	f.close()
	back={'map_x':t[0]['max_x'], 'map_y':t[0]['max_y'], 'players':t[0]['plys'], 'map':t[0]['map'] }
	return back
def read_map_list():
	f=open("map_list.dat",'r')
	t=pickle.load(f)
	f.close()
	return t
