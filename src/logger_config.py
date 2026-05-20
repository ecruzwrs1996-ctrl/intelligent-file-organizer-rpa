from loguru import logger
from pathlib import Path

LOG_PATH = Path("logs")

LOG_PATH.mkdir(exist_ok=True)

logger.add(
    LOG_PATH / "automation.log",
    rotation="1 MB",
    retention="10 days",
    level="INFO",
    format="{time} | {level} | {message}"
)