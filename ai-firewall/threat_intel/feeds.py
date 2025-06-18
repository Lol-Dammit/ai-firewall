# threat_intel/feeds.py

from taxii2client.v20 import Server
from stix2 import TAXIICollectionSource, Filter
import requests
import os
from loguru import logger

class ThreatFeedManager:
    def __init__(self, taxii_url: str = None, shodan_key: str = None):
        self.taxii_url = taxii_url
        self.shodan_key = shodan_key
        self.shodan_url = "https://api.shodan.io/shodan/host/"

    def fetch_taxii_iocs(self):
        try:
            server = Server(self.taxii_url)
            api_root = server.api_roots[0]
            collection = api_root.collections[0]
            source = TAXIICollectionSource(collection)

            filters = [Filter("type", "=", "indicator")]
            indicators = source.query(filters)

            logger.info(f"Fetched {len(indicators)} STIX indicators from TAXII.")
            return indicators
        except Exception as e:
            logger.error(f"Error fetching TAXII indicators: {e}")
            return []

    def query_shodan(self, ip: str):
        try:
            response = requests.get(f"{self.shodan_url}{ip}?key={self.shodan_key}")
            if response.status_code == 200:
                return response.json()
            else:
                logger.warning(f"Shodan query failed for {ip}: {response.status_code}")
                return {}
        except Exception as e:
            logger.error(f"Shodan query error: {e}")
            return {}
