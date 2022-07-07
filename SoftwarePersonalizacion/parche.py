import conexiondb as db

def cargarperfiles(usu):
    perfiles = []
    usus = db.obtenerUsuarios()
    for user in usus:
        if(usu == user[1]):
            usuario = user[0]
    perfiles_ints = db.obtenerPerfiles(str(usuario))
    for perfil in perfiles_ints:
        perfiles.append(str(perfil[2]))
    print(perfiles)

cargarperfiles('Javi')
cargarperfiles('Patri')