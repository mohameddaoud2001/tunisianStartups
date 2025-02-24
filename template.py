import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "tunisianStartups"  # Updated project name

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_cleaner.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_loader.py", # Redundant, but keeping in list as per structure
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/email_automation.py",
    f"src/{project_name}/components/lead_analyzer.py",
    f"src/{project_name}/components/scheduler.py", # Optional scheduler component
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/constants.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/frontend/__init__.py", # Added frontend folder
    f"src/{project_name}/frontend/dashboard.py", # Dashboard file
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/logging/logger.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/automation_pipeline.py",
    f"src/{project_name}/pipelines/data_pipeline.py",
    f"src/{project_name}/pipelines/scheduler.py", # Optional scheduler pipeline
    f"src/{project_name}/templates/__init__.py", # Added templates folder
    f"src/{project_name}/templates/business_opportunity.html", # Email template
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    "config/config.yaml",
    "config/params.yaml",
    "data/raw/.gitkeep", # Added .gitkeep for data/raw
    "data/processed/.gitkeep", # Added .gitkeep for data/processed
    "notebooks/.gitkeep", # Added .gitkeep for notebooks
    "research/.gitkeep", # Added .gitkeep for research
    "Dockerfile", # Optional Dockerfile
    "requirements.txt",
    "setup.py", # Optional setup.py
    "README.md"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass # Create empty file
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")


print("Project structure template created successfully!")
print("Run 'python template.py' from the project root to generate the structure.")