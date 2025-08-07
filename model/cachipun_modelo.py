from db.conexion_oracle import obtener_conexion

def guardar_partida(nombre, jugador, consola, resultado):
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO Cachipun (id_Cachipun, nombre, elec_jugador, elec_consola, resultado)
                VALUES (seq_cachipun_id.NEXTVAL, :1, :2, :3, :4)
            """, (nombre, jugador, consola, resultado))
            conexion.commit()
        except Exception as e:
            print("Error al guardar partida:", e)
        finally:
            conexion.close()

def obtener_partidas():
    conexion = obtener_conexion()
    partidas = []
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre, elec_jugador, elec_consola, resultado FROM Cachipun")
            partidas = cursor.fetchall()
        except Exception as e:
            print("Error al obtener partidas:", e)
        finally:
            conexion.close()
    return partidas

def limpiar_tabla_cachipun():
    conexion = obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM Cachipun")
            conexion.commit()
            print("Tabla Cachipun limpiada correctamente.")
        except Exception as e:
            print("Error al limpiar la tabla:", e)
        finally:
            conexion.close()