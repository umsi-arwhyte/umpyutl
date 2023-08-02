import sys
from pathlib import Path

PROJECT_PATH = Path.cwd().parent
# if PROJECT_PATH not in sys.path:
#     sys.path.insert(0, str(PROJECT_PATH))

SOURCE_PATH = PROJECT_PATH.joinpath("src")
if SOURCE_PATH not in sys.path:
    sys.path.append(str(SOURCE_PATH))
