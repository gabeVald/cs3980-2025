import logging

logging.basicConfig(
    format="%(asctime)s: %(name)s: %(levelname).4s - %(message)s", level=logging.INFO
)

logger = logging.getLogger("__name__")
logger.warning("This line will be logged with the level of warning")
logger.info("info message")
logger.error("error message")
logger.fatal("fatal message")

logging.debug("debug message")
