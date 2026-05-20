from src.logger_config import logger
from src.organizer import organize_files


def main():

    logger.info("Starting Intelligent File Organizer")

    organize_files()

    logger.info("Process completed")


if __name__ == "__main__":
    main()