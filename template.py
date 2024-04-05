import os
from pathlib import Path
import logging 

logging.basicConfig(
    level=logging.INFO, 
    format='[%(asctime)s]: %(message)s:'
)

project_name = 'crewAIProject'

list_of_files = [
    ".github/workflows/.gitkeep", 
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/travel.py",
    "requirements.txt",
    "setup.py",
    "experiment/trials.py",
    "test.py",
    ".gitignore",
    ".env"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    
    else: 
        logging.info(f"{filename} is already exists")

