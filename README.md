<div style="color:red;">
<pre>
██████  ██    ██ ████████ ███████ ███████ ██    ██ ███    ██  ██████ 
██   ██  ██  ██     ██    ██      ██       ██  ██  ████   ██ ██      
██████    ████      ██    █████   ███████   ████   ██ ██  ██ ██      
██   ██    ██       ██    ██           ██    ██    ██  ██ ██ ██      
██████     ██       ██    ███████ ███████    ██    ██   ████  ██████ 
</pre>
</div>

ByteSync is a lightweight command-line tool similar to Netcat, designed to facilitate the seamless transfer of files between two users over a network connection. Whether you're sharing documents, images, or any other type of file, ByteSync offers a straightforward and efficient way to synchronize data between systems.

## Features

- **File Transfer:** Send and receive files of any type or size between two connected systems.
- **Cross-Platform:** ByteSync is designed to work on various operating systems, including Windows, macOS, and Linux.
- **Simple Interface:** Utilize a straightforward command-line interface for easy file sharing.
- **Fast and Efficient:** Transfer files quickly and efficiently over a network connection, ensuring minimal latency.

## Installation

To use ByteSync, follow these simple steps:

1. Clone the ByteSync repository to your local machine:

```
git clone https://github.com/harbingeroffire/bytesync.git
```

2. Navigate to the ByteSync directory:

```
cd bytesync
```

## Usage

ByteSync can be used to send or receive files between two systems. Here's how you can utilize it:

### Sending Files

To send a file using ByteSync, run the following command:

```
bytesync -t -f<file_path> -i<receiver_ip> -p<port>
```

Replace `<file_path>` with the path to the file you want to send, `<receiver_ip>` with the IP address of the receiving system, and `<port>` with the port number to establish the connection.

### Receiving Files

To receive a file using ByteSync, run the following command:

```
bytesync -l -p<port>
```

Replace `<port>` with the port number that the sender is using to establish the connection.

## Contributing

ByteSync is an open-source project, and contributions are welcome! If you'd like to contribute to the development of ByteSync, feel free to submit pull requests or open issues on our GitHub repository.

## License

ByteSync is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

ByteSync is developed and maintained by the ByteSync Team. For any inquiries or support, please contact us at bytesync@example.com. We hope you find ByteSync useful for your file synchronization needs!
