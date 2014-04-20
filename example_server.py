import socket
from req_resp_maker import randomHttp

f = randomHttp()

RESPIP = '127.69.69.69'
RESPPORT = 80
BUFFER_SIZE = 2048

# resp
resp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
resp_s.bind((RESPIP, RESPPORT))
resp_s.listen(1)
conn, addr = resp_s.accept()
while 1:
    who_cares_resp = conn.recv(BUFFER_SIZE)
    if not who_cares_resp: break
    conn.send(f.response())
conn.close()
