# infrastructure/network.py

from scapy.all import sniff, Packet
from loguru import logger
from typing import Callable, Optional

class NetworkSniffer:
    def __init__(self, interface: Optional[str] = None):
        self.interface = interface
        logger.info(f"NetworkSniffer initialized on interface: {interface or 'default'}")

    def start_sniffing(self, callback: Callable[[Packet], None], packet_count: int = 0):
        logger.info(f"Starting packet sniffing (count={packet_count})")
        sniff(prn=callback, iface=self.interface, count=packet_count, store=False)

