#!/usr/bin/env python3

"""
cld.py: 'clean, load and data', limpia y carga los datos.
"""

import sqlite3
import utils
import glob
import csv
from utils.connection import conn, cur

cur.execute('DELETE from tiempos')
cur.execute('DELETE from abandono')

print('Tablas limpias!')

for file in sorted(glob.glob(r'files/RPT_DIALER_PERFORMANCE_*[0-9].csv')):
	rpt = file[39:]
	with open(file, 'r', encoding='utf-8-sig') as outer_file:
		lec = csv.reader(outer_file)
		fechas = list({n[0] for n in lec})

with open(r'files/tiempos.csv', 'r', encoding='utf-8-sig') as f:
	lec = csv.reader(f)

	for n in lec:
		cur.execute(utils.load_times, n)

with open(r'files/abandon.csv', 'r', encoding='utf-8-sig') as af:
	lec = csv.reader(af)

	for i in lec:
		cur.execute(utils.load_abnd, i)

conn.commit()
