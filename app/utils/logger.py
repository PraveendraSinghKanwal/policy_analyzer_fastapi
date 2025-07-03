import os
from loguru import logger
from config import settings

def setup_logging():
    log_dir = os.path.dirname(settings.LOG_FILE)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logger.remove()
    logger.add(
        settings.LOG_FILE,
        rotation="10 MB",
        retention=f"{settings.LOG_RETENTION_DAYS} days",
        level=settings.LOG_LEVEL,
        enqueue=True,
        backtrace=True,
        diagnose=True
    ) 