# data_pipeline/pipeline.py
from data_pipeline.collector import packet_sniffer
from data_pipeline.parser import parse_packet
from data_pipeline.preprocessor import preprocess
from ai_engine.detector import detect_threat

parsed_packets = []

def handle_packet(packet):
    parsed = parse_packet(packet)
    if parsed:
        parsed_packets.append(parsed)

def start_pipeline():
    packet_sniffer(callback=handle_packet)

    if parsed_packets:
        data = preprocess(parsed_packets)
        predictions = detect_threat(data)
        return predictions
    return []
