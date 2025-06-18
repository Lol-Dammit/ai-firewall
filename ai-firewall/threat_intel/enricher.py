# threat_intel/enricher.py

from .feeds import ThreatFeedManager
from loguru import logger

class ThreatIntelEnricher:
    def __init__(self, feed_manager: ThreatFeedManager):
        self.feed_manager = feed_manager

    def enrich_ip(self, ip: str):
        enrichment = {
            "ip": ip,
            "shodan": {},
            "threat_level": "unknown"
        }

        shodan_data = self.feed_manager.query_shodan(ip)
        enrichment["shodan"] = shodan_data

        ports = shodan_data.get("ports", [])
        if ports and any(p in [22, 23, 3389] for p in ports):
            enrichment["threat_level"] = "high"
        elif ports:
            enrichment["threat_level"] = "medium"
        else:
            enrichment["threat_level"] = "low"

        logger.debug(f"Enriched IP {ip} with threat level: {enrichment['threat_level']}")
        return enrichment
