"""Logging configuration."""
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Create logger instance
log = logging.getLogger("fastapi-calculator")
