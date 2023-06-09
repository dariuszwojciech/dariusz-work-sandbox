import os

from dotenv import load_dotenv
import json
import yaml

from const.adf import (
    PIPELINE,
    LINKED_SERVICE,
    FACTORY,
    DATASET,
    INTEGRATION_RUNTIME,
    TRIGGER,
    DATAFLOW,
    NOTEBOOK,
    SQL_SCRIPT,
)
from incubator.common_utils import create_folder
from test.utils import fetch_files

load_dotenv()


def generate_yamls(collection, system_under_test):
    export_folder = f"../_out_/{system_under_test}/"
    files = fetch_files(system_under_test, collection)
    for f in files:
        filename = os.getenv(system_under_test) + "\\" + collection + "\\" + f
        if filename.endswith(".json"):
            with open(filename, "r") as current_file:
                data = current_file.read()
                python_dict = json.loads(data)
                create_folder(export_folder + collection)
                saved_filename = (
                    export_folder + collection + "\\" + f.replace(".json", ".yaml")
                )
                file = open(saved_filename, "w")
                yaml.dump(python_dict, file)
                file.close()
                print(f"YAML file saved {saved_filename}")


asset_folders = [
    LINKED_SERVICE,
    DATASET,
    INTEGRATION_RUNTIME,
    PIPELINE,
    FACTORY,
    # MAPPED_VIRTUAL_NETWORK,
    TRIGGER,
    DATAFLOW,
    NOTEBOOK,
    SQL_SCRIPT,
]

systems_to_inspect = ["SUT_P_DIR", "SUT_T_DIR", "SUT_B_DIR"]

for s in systems_to_inspect:
    for folder in asset_folders:
        generate_yamls(folder, s)
