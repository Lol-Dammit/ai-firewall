# infrastructure/logger.py

from loguru import logger
import sys

def setup_logger():
    logger.remove()
    logger.add(sys.stdout, level="INFO", format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>")
    logger.add("logs/firewall.log", rotation="5 MB", retention="10 days", level="DEBUG")
    logger.info("Logger configured successfully.")
