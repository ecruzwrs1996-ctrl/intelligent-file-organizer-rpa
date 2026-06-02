# =========================================================
# By: EdderCR14
# Date: 02 June, 2026
# Goal: CREATE CONFIG LOADER
# =========================================================

from pathlib import Path
import yaml


# =========================================================
# LOAD YAML CONFIGURATION
# =========================================================
def load_config(config_file="config/settings.yaml"):

    config_path = Path(config_file)

    if not config_path.exists():
        raise FileNotFoundError(
            f"Config file not found: {config_file}"
        )

    with open(config_path, "r") as file:

        config = yaml.safe_load(file)

    return config