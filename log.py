import datatime

def registrar_log(msg: str):
    agora = datatime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open ("log.txt", "a", encoding="utf=8") as f:
        f.write(f"[{agora}] {msg}\n")