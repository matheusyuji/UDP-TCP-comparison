import socket
import sys

bufferSize = 1024  

# Check if a filename is provided 
if len(sys.argv) < 2:
  print("Usage: python3 udp_server.py <filename>")
  sys.exit(1)

fileName = sys.argv[1]

serverIP = "127.0.0.1"  
serverPort = 12000       

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDPServerSocket:
  # Bind the server socket to the specified IP and port
  UDPServerSocket.bind((serverIP, serverPort))
  print('Waiting for connection...')

  # Continuously listen for incoming requests
  while True:   
    # Receive a message from a client
    msg, address = UDPServerSocket.recvfrom(bufferSize)
    if msg == b'START':  
      print(f"Received 'START' request from")
      sentPackets = 0  

      # Open the file in binary read mode
      with open(fileName, 'rb') as file:
        # Read the file in chunks and send it to the client
        data = file.read(bufferSize)
        while (data):
          # Send each chunk to the client
          UDPServerSocket.sendto(data, address)
          sentPackets += 1 
          data = file.read(bufferSize)

      # Send an 'END' message to indicate the end of the file transfer   
      UDPServerSocket.sendto(b'END', address)

      print(f"Packets sent: {sentPackets}")
      break

print("Server shutting down.")