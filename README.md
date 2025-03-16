Packet Sniffer
==============

This is a simple packet sniffer written in Python using the Scapy library. The script captures network packets and displays their details in real-time.

Requirements
------------

-   Python 3.x
-   `scapy` library
-   Administrator/root privileges to run the script
-   Npcap (Windows only, required for packet capturing)

Installation
------------

1.  Install Python if not already installed.
2.  Install Scapy using pip:

    ```
    pip install scapy

    ```

3.  (Windows Only) Install [Npcap](https://npcap.com/) if not already installed.

Usage
-----

Run the script with administrator/root privileges:

```
python packet_sniffer.py

```

How It Works
------------

-   The script detects the operating system and configures Scapy accordingly.
-   It listens for network packets and displays their details.
-   The script captures a fixed number of packets (`PACKET_COUNT = 50` by default) before stopping.
-   It works on Windows, macOS, and Linux.

Notes
-----

-   On Windows, the script uses promiscuous mode (`promisc=True`) to capture packets using Npcap.
-   On macOS and Linux, no additional configuration is required.
-   If running on Linux/macOS, ensure you execute the script as `sudo` to access network interfaces.

License
-------

This project is open-source and free to use for educational and personal purposes.
