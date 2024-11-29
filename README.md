# UDP-TCP-comparison

The objective of this repository is to perform a performance comparison between the TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) communication protocols using the Python programming language. Both protocols are widely used in computer networks, but they differ significantly in the way they transmit data.

TCP is a connection-oriented protocol, meaning it guarantees the delivery of data in the correct order and without errors, providing reliability in communication. On the other hand, UDP is a connectionless protocol, which does not guarantee packet delivery or the order of reception, but is faster and more efficient in terms of overhead.

In this repository, a practical analysis of both protocols will be conducted, focusing on two main areas: file transfer and packet loss detection in the case of UDP. The impact of packet loss on performance will be evaluated, along with a comparison of the performance of both protocols in terms of speed and efficiency in data transfer.

When testing the TCP and UDP protocols on a normal loopback, without introducing packet loss, no significant difference in performance is noticed because communication occurs efficiently and error-free, as all packets are delivered correctly. Both TCP and UDP behave as expected, with TCP ensuring the reliable and ordered delivery of packets, and UDP transmitting data quickly without additional checks.

## Loopback Network Simulation with Packet Loss

To simulate packet loss in a loopback network, you can use the following command. This command configures the local network interface to introduce a 10% packet loss, which is useful for testing the behavior of TCP and UDP protocols under conditions of packet loss:

```bash
sudo tc qdisc add dev lo root netem loss 10%
```

To undo the packet loss simulation and restore the network interface to its original state, you can use the following command:

```bash
sudo tc qdisc del dev lo root
```

This packet loss simulation is crucial for understanding the impact of network conditions on the performance of both protocols and helps to highlight the advantages and disadvantages of each in scenarios with variable network quality.

## Running the Server and Client

To run the server, use the following commands depending on the desired protocol:

- For the UDP server:
  
```bash
python3 udp_server <filename>
```

- For the TCP server:
  
```bash
python3 tcp_server <filename>
```

- For the UDP client:
  
```bash
python3 udp_client 
```

- For the TCP client:
  
```bash
python3 tcp_client 
```