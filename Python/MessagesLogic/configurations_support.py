import os
import json


def find_environment_var(production: str = "Local") -> str:
    """
                        DESCRIPTION:
    Find the variable that describes in which environment
    work is being done.

                        PARAMETERS:
    > production (str) - indication in which environment we are
    operating. Defaults to "Local"

                           OUTPUT:
    > variable (str) - formatted properly definition of the description
    in what environment we are operating
    """
    default_variable = "Local"
    variable = os.environ.get(production)
    if variable is None or variable == "":
        return default_variable
    else:
        return variable


def read_json_file(file_path: str) -> dict:
    """
                        DESCRIPTION:
    Read a json file of our choice in a convenient manner.

                        PARAMETERS:
    > file_path (str) - Path to the json file in need of reading.

                           OUTPUT:
    > data (dict) - data present in the json structure
    """
    with open(file_path) as file:
        data = json.load(file)

    return data
