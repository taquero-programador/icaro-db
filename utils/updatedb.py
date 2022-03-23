#!/usr/bin/env python3

"""
updatedb.py: actualiza la tabla resultados en caso de existir
una base adicional (elimina y carga).
"""

import os
import csv 
import sqlite3
from utils import cur, conn

# pruebas, no es parte del desarrollo.
for e in cur.execute('select * from tiempos'):
	print(e)

r = 'select * from abandono'
cur.execute(r)
result = cur.fetchall()

for w in result:
	print(w)