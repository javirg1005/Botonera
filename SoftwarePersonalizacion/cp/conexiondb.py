import sqlite3

def obtenerPerfiles(usu):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Perfiles WHERE id_usu = " + usu)
    reply = cur.fetchall()
    con.commit()
    con.close()
    return reply

def obtenerUsuarios():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    print("Se ejecuta la sentencia")
    cur.execute("SELECT * FROM Usuarios")
    reply = cur.fetchall()
    print(reply)
    con.commit()
    con.close()

def borrarUsuario(id):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    print("Se ejecuta la sentencia")
    cur.execute("DELETE FROM Usuarios WHERE id_usu = "+id+";")
    reply = cur.fetchall()
    print(reply)
    con.commit()
    con.close()

def obtenerBotones(usu,perfil):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute()
    reply = cur.fetchall()
    con.commit()
    con.close()
    return reply

def guardarBotones():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("Sentencia para guardar las configuraciones")
    reply = cur.fetchall()
    
    con.commit()
    con.close()
    return reply

def crearUsuario(usu):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Usuarios (name) VALUES ("+usu+")")
    reply = cur.fetchall()
    con.commit()
    con.close()
    return reply

def crearPerfil(name,id_usu):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Perfiles ( name , id_usu) VALUES ('"+name+"', "+id_usu+")")
    reply = cur.fetchall()
    con.commit()
    con.close()
    return reply

def borrarPerfil(id):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    print("Se ejecuta la sentencia")
    cur.execute("DELETE FROM Perfiles WHERE id_profile = "+id+";")
    reply = cur.fetchall()
    print(reply)
    con.commit()
    con.close()

def eliminarconfiguracion(id_perf):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Perfiles WHERE id_profile ="+id_perf)
    reply = cur.fetchall()
    con.commit()
    con.close()
    return reply
