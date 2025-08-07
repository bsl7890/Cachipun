import oracledb

usuario = "C##Cachipun"
contraseña = "Cachipun"
dsn = "localhost:1521/XE"

def obtener_conexion():
    try:
        return oracledb.connect(
            user = usuario,
            password = contraseña,
            dsn = dsn)
    except oracledb.Error as error:
        print("Error al conectar o ejecutar la consulta:",error)
        return None
    


