# data_pipeline/collector.py
from scapy.all import sniff, Packet
from typing import Callable
import logging

logger = logging.getLogger(__name__)

def packet_sniffer(callback: Callable[[Packet], None], interface: str = None, count: int = 0):
    """
    Sniffs packets and passes each to a callback function.
    """
    logger.info(f"Starting packet sniffing on interface: {interface or 'default'}")
    sniff(prn=callback, iface=interface, store=False, count=count)
