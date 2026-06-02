# =========================================================
# By: EdderCR14
# Initial project structure
# Add file categorization
# Implement logging system
# Add duplicate file validation
# Refactor organizer using pathlib
# Add recursive folder scanning
# =========================================================
from loguru import logger
from src.organizer import organize_files
from src.report_generator import generate_report

# =========================================================
# MAIN EXECUTION
# =========================================================
if __name__ == "__main__":

    logger.info(
        "Starting Intelligent File Organizer..."
    )

    # -----------------------------------------------------
    # ORGANIZE FILES
    # -----------------------------------------------------
    organize_files()

    # -----------------------------------------------------
    # GENERATE EXCEL REPORT
    # -----------------------------------------------------
    generate_report()

    logger.info(
        "Process completed successfully."
    )