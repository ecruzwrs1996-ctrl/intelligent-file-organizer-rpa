# =========================================================
# By: EdderCR14
# Date: 02 June, 2026
# Goal: Create log on directory
# =========================================================

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