import http.server
import socketserver
import socket
import pyautogui
import qrcode

PORT = 8000

# Página HTML com visual moderno e responsivo
html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Controle de Slides Avançado</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(160deg, #a18cd1, #fbc2eb);
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    color: #fff;
}
h1 {
    font-size: 2em;
    margin-bottom: 40px;
    text-shadow: 1px 1px 5px rgba(0,0,0,0.3);
}
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
}
button {
    font-size: 24px;
    padding: 20px 60px;
    margin: 15px;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    color: white;
    font-weight: bold;
    box-shadow: 0 6px 15px rgba(0,0,0,0.2);
    transition: all 0.2s ease;
}
button:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 20px rgba(0,0,0,0.3);
}
#start { background-color: #28a745; }
#prev { background-color: #6c757d; }
#next { background-color: #6A0DAD; }
#exit { background-color: #dc3545; }
</style>
</head>
<body>
<h1>Controle de Slides</h1>
<div class="container">
    <button id="start" onclick="fetch('/start')">▶️ Iniciar</button>
    <button id="prev" onclick="fetch('/prev')">⬅️ Anterior</button>
    <button id="next" onclick="fetch('/next')">➡️ Próximo</button>
    <button id="exit" onclick="fetch('/exit')">⏹️ Sair</button>
</div>
</body>
</html>
"""

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        elif self.path == "/next":
            pyautogui.press("right")
            self.send_response(200)
            self.end_headers()
        elif self.path == "/prev":
            pyautogui.press("left")
            self.send_response(200)
            self.end_headers()
        elif self.path == "/start":
            pyautogui.press("f5")
            self.send_response(200)
            self.end_headers()
        elif self.path == "/exit":
            pyautogui.press("esc")
            self.send_response(200)
            self.end_headers()
        else:
            self.send_error(404, "Not Found")

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

if __name__ == "__main__":
    ip = get_ip()
    url = f"http://{ip}:{PORT}"
    print(f"\nServidor rodando em: {url}\n")

    # QR Code no terminal
    qr = qrcode.QRCode(border=2)
    qr.add_data(url)
    qr.make(fit=True)
    qr.print_ascii(invert=True)

    print("\nEscaneie o QR Code com o celular para acessar o controle.\n")

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        httpd.serve_forever()
