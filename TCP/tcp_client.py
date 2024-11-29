import socket
import time

bufferSize = 1024

host = "127.0.0.1"
port = 55552

# Saving location
fileName = 'tcp_output.txt'

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
  TCPClientSocket.connect((host, port))
  transferStartTime = time.time() 

  # Open the file in binary write mode to save the received data
  with open(fileName, 'wb') as file:
    print("TCP Client Transfer Initiated...")
    # Initialize counters for packets and bytes received
    receivedPackets = 0
    receivedBytes = 0  

    # Loop to continuously receive data from the server
    while True:
      try:
        # Receive data from the server in chunks of size bufferSize
        data = TCPClientSocket.recv(bufferSize)
      except:
        print("Error! Transfer failed")
      if not data:
        print("Transfer complete!")
        break           
      file.write(data)
      receivedPackets += 1
      receivedBytes += len(data)   

  # End the timer to calculate the transfer duration
  transferEndTime = time.time()
  transferDuration = transferEndTime - transferStartTime

print(f"Transfer time: {transferDuration:.5f} seconds")
print(f"Packets received: {receivedPackets}")
print(f"Bytes received: {receivedBytes}")