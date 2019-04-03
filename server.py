import socket
from drunk_htttp import randomHttp

f = randomHttp()

RESPIP = '127.0.0.1'
RESPPORT = 80
BUFFER_SIZE = 2048

resp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
resp_s.bind((RESPIP, RESPPORT))
resp_s.listen(1)
conn, addr = resp_s.accept()

# resp
while 1:
  who_cares_resp = conn.recv(BUFFER_SIZE)
  conn.send(f.response())
conn.close()
