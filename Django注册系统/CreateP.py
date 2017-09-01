'''
由于Django中命令行创建工程
2017-8-4 by：羽凡
'''
import os
import time
#创建工程的名字
project_name = input('Project:')
#创建应用的名字
app_name = input('App:')
#构造命令
Porder = 'django-admin startproject '+str(project_name)
Aorder = 'python manage.py startapp '+str(app_name)

# 如果当前目录没有该工程
if project_name not in os.listdir(os.getcwd()):
	#试着执行创建工程的命令
	try:
		os.popen(Porder)
		#新建后可能存在延迟，导致os.getcwd()得不到准确信息，所以加延迟1秒
		time.sleep(1)
		#如果命令执行后新建工程存在则成功
		if project_name in os.listdir(os.getcwd()):
			print('OK：工程创建成功')
			#如果工程中没有该应用
			if app_name not in os.listdir(os.getcwd()+'/'+project_name):
				try:
					os.chdir(os.getcwd()+'/'+project_name)
					os.popen(Aorder)
					time.sleep(1)
					if app_name in os.listdir(os.getcwd()):
						print('OK:创建应用成功')
					else:
						print('Error1:创建应用失败')
				except:
					print('Error2:创建应用失败')
		else:
			print('Error1:创建工程失败')
	except:
		print('Error2:创建工程失败')
		pass
else:
	print('Error：工程已存在')
	if app_name not in os.listdir(os.getcwd()+'/'+project_name):
		try:
			os.chdir(os.getcwd()+'/'+project_name)
			os.popen(Aorder)
			time.sleep(1)
			if app_name in os.listdir(os.getcwd()):
				print('OK:创建应用成功')
			else:
				print('Error1:创建应用失败')
		except:
			print('Error2:创建应用失败')


