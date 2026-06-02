# =========================================================
# By: EdderCR14
# Date: 02 June, 2026
# Goal: Detect duplicate files and verify integrity
# =========================================================

import hashlib

def generate_file_hash(file_path):

    md5_hash = hashlib.md5()

    with open(file_path, "rb") as file:

        for chunk in iter(
            lambda: file.read(4096),
            b""
        ):

            md5_hash.update(chunk)

    return md5_hash.hexdigest()