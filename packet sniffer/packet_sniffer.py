import platform
from scapy.all import sniff

PACKET_COUNT = 50  # Durmak için dinlenecek paket sayısı

def packet_callback(packet):
    packet.show()  # Paketin tamamını göster

def start_sniffing():
    print("Starting packet sniffer...")
    if platform.system() == "Windows":
        # Windows'ta, Npcap ile çalışmak için promisc parametresini True olarak ayarlayarak sniff fonksiyonunu kullanın
        sniff(prn=packet_callback, store=0, iface=None, promisc=True, count=PACKET_COUNT)
    elif platform.system() == "Darwin":
        # macOS için ek bir import gerekli değil
        pass
    elif platform.system() == "Linux":
        # Linux için ek bir import gerekli değil
        sniff(prn=packet_callback, store=0, iface=None, count=PACKET_COUNT)
    else:
        print("Unsupported operating system")
        return

if __name__ == "__main__":
    start_sniffing()
