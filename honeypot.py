import paramiko
import socket
import threading

from datetime import datetime
filename = f"honeypot_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
log_file = open(filename, "w")

class HoneypotServer(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        log_file.write(f"[ATTEMPT] IP: {client_ip} | Username: {username} | Password: {password}\n")
        log_file.flush()  # writes immediately instead of buffering
        return paramiko.AUTH_FAILED

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", 2222))
server_socket.listen(100)

try:
    def handle_client(client, client_ip):
        try:
            host_key = paramiko.RSAKey.generate(2048)
            transport = paramiko.Transport(client)
            transport.add_server_key(host_key)
            server = HoneypotServer()
            transport.start_server(server=server)
            transport.accept(20)
        except Exception:
            pass

    while True:
        print("Honeypot listening on port 2222...")
        client, addr = server_socket.accept()
        client_ip = addr[0]
        thread = threading.Thread(target=handle_client, args=(client, client_ip))
        thread.start()

except KeyboardInterrupt:
    print("\n[*] Shutting down honeypot...")
    log_file.close()
    server_socket.close()