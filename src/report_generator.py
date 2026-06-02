# =========================================================
# By: EdderCR14
# =========================================================

from pathlib import Path
from datetime import datetime
import pandas as pd
from loguru import logger


# =========================================================
# FUNCTION: Generate Metadata Report
# PURPOSE:
#   Extract file metadata and generate Excel audit report
# =========================================================
def generate_report(output_folder="output", report_folder="reports"):

    # -----------------------------------------------------
    # DEFINE MAIN PATHS
    # -----------------------------------------------------
    output_path = Path(output_folder)
    report_path = Path(report_folder)

    # Create reports directory if it does not exist
    report_path.mkdir(
        parents=True,
        exist_ok=True
    )

    # -----------------------------------------------------
    # STORE FILE METADATA
    # -----------------------------------------------------
    report_data = []

    # -----------------------------------------------------
    # ITERATE THROUGH ORGANIZED FILES
    # -----------------------------------------------------
    for file in output_path.rglob("*"):

        if file.is_file():

            # ---------------------------------------------
            # EXTRACT METADATA
            # ---------------------------------------------
            file_size_kb = round(
                file.stat().st_size / 1024,
                2
            )

            creation_date = datetime.fromtimestamp(
                file.stat().st_ctime
            )

            execution_timestamp = datetime.now()

            extension = file.suffix.lower().lstrip(".")

            category = file.parent.name

            # ---------------------------------------------
            # STORE METADATA RECORD
            # ---------------------------------------------
            report_data.append({

                "File Name": file.name,

                "Extension": extension,

                "Category": category,

                "Size KB": file_size_kb,

                "Creation Date": creation_date.strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                "Destination Path": str(file.resolve()),

                "Execution Timestamp": execution_timestamp.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            })

    # -----------------------------------------------------
    # CREATE PANDAS DATAFRAME
    # -----------------------------------------------------
    dataframe = pd.DataFrame(report_data)

    # -----------------------------------------------------
    # GENERATE REPORT NAME
    # -----------------------------------------------------
    report_name = f"files_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

    report_file = report_path / report_name

    # -----------------------------------------------------
    # EXPORT EXCEL REPORT
    # -----------------------------------------------------
    dataframe.to_excel(
        report_file,
        index=False
    )

    logger.info(
        f"Excel report generated: {report_file}"
    )