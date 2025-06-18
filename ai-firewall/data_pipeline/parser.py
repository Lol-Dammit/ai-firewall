from scapy.all import Packet

logger = logging.getLogger(__name__)

def parse_packet(packet: Packet) -> dict:
    """
    Extracts relevant features from a packet.
    """
    try:
        return {
            "src_ip": packet[0].src,
            "dst_ip": packet[0].dst,
            "protocol": packet[0].proto if hasattr(packet[0], 'proto') else 'N/A',
            "length": len(packet)
        }
    except Exception as e:
        logger.warning(f"Failed to parse packet: {e}")
        return {}

def extract_features(packet: Packet) -> dict:
    return {
        "src_ip": packet[0].src if packet else "",
        "dst_ip": packet[0].dst if packet else "",
        "length": len(packet),
    }
