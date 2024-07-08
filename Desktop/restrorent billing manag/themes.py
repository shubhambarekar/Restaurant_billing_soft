import mysql.connector as MYSQL
import sqlite3 as sqlite


CONN = None
C = None



def init_server():
    global CONN
    global C

    try:
        CONN = sqlite.connect("alpha.vtdb", check_same_thread=False)
        C = CONN.cursor()
        print('connected')
        return True
    except Exception as e:
        print(e)
        return False


def retrieve():
    global CONN
    global C
    print('retrieve')
    q = C.execute('select * from theme_color')
    v = None
    for i in q:
        v = i
##    print(v[0])
    v1 = v[0]
    v2 = v[1]
    return v1,v2

def save(v1,v2):
    global CONN
    global C

    q = C.execute('DELETE FROM theme_color')
    q1 = C.execute('INSERT INTO theme_color(str1,str2) VALUES (?,?)',(v1,v2))
    CONN.commit()
    print('Theme save.')
    
    
##init_server()
##print(retrieve())
