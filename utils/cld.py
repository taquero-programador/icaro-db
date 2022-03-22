#!/usr/bin/env python3

"""
cld.py: 'clean, load and data', limpia y carga los datos.
"""

import sqlite3
import utils
import glob
import csv
import os
from utils.connection import conn, cur

cur.execute('DELETE from tiempos')
cur.execute('DELETE from abandono')

print('Tablas limpias!')

for file in sorted(glob.glob(r'files/RPT_DIALER_PERFORMANCE_*[0-9].csv')):
	rpt = file[39:]
	with open(file, 'r', encoding='utf-8-sig') as outer_file:
		lec = csv.reader(outer_file)
		fechas = list({n[0] for n in lec})


def load_data(args, query):
	"load data to db"

	for file in query:
		with open(r'files/' + file, 'r', encoding='utf-8-sig') as loader:
			lec = csv.reader(loader)

			for regs in lec:
				if file == 'tiempos.csv':
					cur.execute(utils.load_times, regs)
				else:
					cur.execute(utils.load_abnd, regs)

			conn.commit()


load_data(conn, ['tiempos.csv', 'abandon.csv'])