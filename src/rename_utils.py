# =========================================================
# By: EdderCR14
# Date: 02 June, 2026
# Name: GENERATE UNIQUE FILE NAME
# Goal: Prevent overwrite collisions
# =========================================================

from pathlib import Path

def generate_unique_name(destination_file):

    counter = 1

    new_file = destination_file

    while new_file.exists():

        stem = destination_file.stem
        suffix = destination_file.suffix
        parent = destination_file.parent

        new_name = f"{stem}_{counter}{suffix}"

        new_file = parent / new_name

        counter += 1

    return new_file