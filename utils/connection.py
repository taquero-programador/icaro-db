#!/usr/bin/env python3

import sqlite3
import os
from sqlite3 import Error
import utils


def conn_db():
	"genera conexion a la db"

	try:
		conn = sqlite3.connect(r'utils/sqlite.db')
		print('DB connected!')
		return conn
	except Error:
		print(Error)


conn = conn_db()
cur = conn.cursor()


def create_tables(args_conn, query):
	"creacion de las tablas para la db"

	cur.execute(query)
	conn.commit()

print('Tablas listas!')


create_tables(conn, utils.table_times)
create_tables(conn, utils.table_abandon)
create_tables(conn, utils.table_services)
create_tables(conn, utils.table_resulados)