import cx_Oracle
conn = cx_Oracle.connect('project/final//@localhost:1521/xe')
print(conn.version)