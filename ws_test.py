import websocket
import traceback

url = "wss://proyecto-bmhp.onrender.com/_event"
print(f"Intentando conexión a: {url}")
try:
    ws = websocket.create_connection(url, timeout=15)
    print("Conectado correctamente")
    ws.close()
except Exception as e:
    print("Error al conectar:")
    traceback.print_exc()
