#!/usr/bin/env python3

"""
updatedb.py: actualiza la tabla resultados en caso de existir
una base adicional (elimina y carga).
"""

import os
import csv 
import sqlite3
import utils
from utils import cur, conn

# 8317

file_append = "RPT_DIALER_PERFORMANCE.csv"

def update_append():
	"update tabla resultado, new .csv"

	if os.path.exists(file_append):
		print("se detecto nueva base")
		quest = input("Desea actualizar [Y/N]: ").lower()
		if quest == 'y':
			cur.execute("DELETE from resultado_icaro")
			print("- Base limpia!")
			with open(file_append, "r", encoding="utf-8-sig") as update_load:
				lec = csv.reader(update_load)

				for regs in lec:
					cur.execute(utils.update_load, regs)
				conn.commit()
		elif quest == "n":
			print("- Sin cambios.")
		else:
			print("Comando invalido!!!")
			return update_append()
	else:
		print('- Ok DB.')

update_append()