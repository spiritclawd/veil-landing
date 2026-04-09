
import http.server, socketserver, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 8080
handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({'.svg': 'image/svg+xml'})
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Veil landing on :{PORT}")
    httpd.serve_forever()
