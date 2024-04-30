import platform
from scapy.all import sniff

PACKET_COUNT = 50  # Number of packets to sniff before stopping

def packet_callback(packet):
    packet.show()  # Show the entire packet

def start_sniffing():
    print("Starting packet sniffer...")
    if platform.system() == "Windows":
        # On Windows, use the sniff function with promisc set to True to work with Npcap
        sniff(prn=packet_callback, store=0, iface=None, promisc=True, count=PACKET_COUNT)
    elif platform.system() == "Darwin":
        # No additional imports required for macOS
        sniff(prn=packet_callback, store=0, iface=None, count=PACKET_COUNT)
        pass
    elif platform.system() == "Linux":
        # No additional imports required for Linux
        sniff(prn=packet_callback, store=0, iface=None, count=PACKET_COUNT)
    else:
        print("Unsupported operating system")
        return

if __name__ == "__main__":
    start_sniffing()
