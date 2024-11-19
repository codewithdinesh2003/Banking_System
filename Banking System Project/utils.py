# utils.py
import json

def load_data(filename="data.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data, filename="data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
