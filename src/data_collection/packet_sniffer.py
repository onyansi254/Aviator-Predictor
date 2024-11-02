from scapy.all import sniff
from utils.logger import get_logger

logger = get_logger(__name__)

def packet_callback(packet):
    logger.info(f"Packet captured: {packet.summary()}")  # Log packet summary

def start_sniffer(interface='lo'):
    try:
        logger.info("Starting packet sniffer...")
        sniff(iface=interface, prn=packet_callback, count=10)  # Adjust count as necessary
    except Exception as e:
        logger.error(f"Error in packet sniffer: {e}")

