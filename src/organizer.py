from pathlib import Path
import shutil
from loguru import logger


def organize_files(input_folder="input", output_folder="output"):

    input_path = Path(input_folder)
    output_path = Path(output_folder)

    if not input_path.exists():
        logger.error(f"Input folder does not exist: {input_folder}")
        return

    for file in input_path.iterdir():

        if file.is_file():

            extension = file.suffix.lower().lstrip(".")

            category = extension if extension else "others"

            destination_folder = output_path / category

            destination_folder.mkdir(
                parents=True,
                exist_ok=True
            )

            destination_file = destination_folder / file.name

            try:

                shutil.move(file, destination_file)

                logger.info(
                    f"Moved: {file.name} -> {category}"
                )

            except Exception as error:

                logger.error(
                    f"Error moving {file.name}: {error}"
                )