import socket
import time

bufferSize = 1024 

host = "127.0.0.1"  
port = 12000        

# Saving Location
fileName = 'udp_output.txt'

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDPClientSocket:
  # Send an initial 'START' message to the server to begin the transfer
  UDPClientSocket.sendto(b'START', (host, port)) 
  
  transferStartTime = time.time() 

  # Open the file in binary write mode to save the received data
  with open(fileName, 'wb') as file:
    print("UDP Client Transfer Initiated...")
    receivedPackets = 0  
    receivedBytes = 0  
    while True:
      # Receive data from the server
      data, address = UDPClientSocket.recvfrom(bufferSize)
    
      if data == b'END':
        break  
      
      # Write the received data to the file
      file.write(data)
      receivedPackets+= 1
      receivedBytes += len(data)           

  # Record the end time of the transfer 
  transferEndTime = time.time()
  transferDuration = transferEndTime - transferStartTime

print(f"Transfer time: {transferDuration:.5f} seconds")
print(f"Packets received: {receivedPackets}")
print(f"Bytes received: {receivedBytes}")