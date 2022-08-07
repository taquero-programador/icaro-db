#!/usr/bin/env python3

"""
gdata.py: se encarga de extraer la información de la DB y lo
guarda en un archivo.
"""

import os
import csv
import time
import sqlite3
import utils
from utils import cur, conn

inicio = time.time()

def consulta(args):
    for i, e in enumerate(cur.execute(utils.consulta), 1):
        print(f"{i}: {e}")

consulta(conn)

def extract(args):
    sq = 'SELECT * from resultado_icaro'
    with open(r"RESULTADOS.csv", "w", newline="") as sl:
        esc = csv.writer(sl)
        for regs in cur.execute(sq):
            esc.writerow(regs)

extract(conn)
conn.close()

print(time.time() - inicio)
time.sleep(3)
