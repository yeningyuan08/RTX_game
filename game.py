import myconfig,platform,os,sys,helps
map_list={}
if platform.system()=='Darwin':
	print('对不起，此游戏暂时不支持Mac系统，请使用windows或linux（全发行版）系统游玩。:-('）
	sys.exit(1)
try:
	helps.read_map_list
print('欢迎您打开此游戏')
while true:
	print('''\n\n
———————————————————————菜单———————————————————————
|		  			1.单人游戏					 |
|				2.多人局域网游戏					 |
|				3.多人服务器游戏                  |
|            4.创建一个局域网游戏	     		 |
|			   5.地图编辑器（暂不可用） 			  |
|					 6.退出						 |
——————————————————————————————————————————————————
	''')
	t=input("请输入选项序号："）
	if t==6:
		sys.exit(0)
	if t==1:
		if platform.system()=='Windows':
			os.system("cls")
		else:
			os.system("reset")
    

