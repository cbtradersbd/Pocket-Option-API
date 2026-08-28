from src.services.database import CandleDatabase
from src.utils.logger import logger

def export_data():
    db = CandleDatabase()
    logger.info("Pocket Option Historical Database initialized for export.")

if __name__ == "__main__":
    export_data()
