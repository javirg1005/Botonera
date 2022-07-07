import sqlite3
import json

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
    return reply

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
    reply = cur.fetchall("SELECT * FROM Botones WHERE id_profile == "+perfil)
    con.commit()
    con.close()
    return reply

def guardarBotones(id_profile):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    with open('./salida_btn.json') as file:
        derulos = json.load(file)
    cur.execute("DELETE FROM Botones WHERE id_profile == "+id_profile)
    for derulo in derulos:
        stn = "INSERT INTO Botones (id_profile, name, shortcut, position, mantener) VALUES ({}, \"{}\", \"{}\", \"{}\", {});".format(id_profile, derulo['name'], derulo['shortcut'], derulo['position'], derulo['mantener'])
        print(stn)
        cur.execute(stn)
    reply = cur.fetchall()
    
    con.commit()
    con.close()
    return reply


def crearUsuario(usu):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    print(usu)
    cur.execute("INSERT INTO Usuarios (name) VALUES ('"+usu+"')")
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
    cur.execute("DELETE FROM Botones WHERE id_profile == "+id)
    reply = cur.fetchall()
    print(reply)
    con.commit()
    con.close()


