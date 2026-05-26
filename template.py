import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "AI_Trip_Planner"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/tools/__init__.py",
    f"src/{project_name}/tools/arithmetic_op_tool.py",
    f"src/{project_name}/tools/currency_conversion_tool.py",
    f"src/{project_name}/tools/expense_calculator_tool.py",
    f"src/{project_name}/tools/place_search_tool.py",
    f"src/{project_name}/tools/weather_info_tool.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/config_loader.py",
    f"src/{project_name}/utils/expense_calculator.py",
    f"src/{project_name}/utils/currency_convertor.py",
    f"src/{project_name}/utils/model_loader.py",
    f"src/{project_name}/utils/place_info_search.py",
    f"src/{project_name}/utils/save_to_document.py",
    f"src/{project_name}/utils/weather_info.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/config.yaml",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/logger/logging.py",
    f"src/{project_name}/prompt_library/__init__.py",
    f"src/{project_name}/prompt_library/prompt.py",
    f"src/{project_name}/agent/__init__.py",
    f"src/{project_name}/agent/agentic_workflow.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/exception/exceptionhandling.py",
    "streamlit_app.py",
    "app.py",
    "Dockerfile",
    "research/trials.ipynb",
    "main.py",
    "setup.py",
    "requirements.txt"

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")