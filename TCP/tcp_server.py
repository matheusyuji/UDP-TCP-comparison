import socket
import sys

bufferSize = 1024

# Check if a filename is provided 
if len(sys.argv) < 2:
  print("Usage: python3 tcp_server.py <filename>")
  sys.exit(1)

fileName = sys.argv[1]

serverIP = "127.0.0.1"
serverPort = 55552      

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket: 
  TCPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  TCPServerSocket.bind((serverIP, serverPort))
  TCPServerSocket.listen()  

  print('Waiting for connection...')
  clientSocket, address = TCPServerSocket.accept()
    
  print('Sending file...')

  # Send the file data to the client
  with clientSocket:         
    sentPackets = 0  
      
    with open(fileName, 'rb') as file:
      # Read the file in chunks
      data = file.read(bufferSize)
      while (data):       
        # Send each chunk of data to the client 
        clientSocket.send(data)
        sentPackets += 1
        data = file.read(bufferSize)
    print('File sent')

  print(f"Packets sent: {sentPackets}")