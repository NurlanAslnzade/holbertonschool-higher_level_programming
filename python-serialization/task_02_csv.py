#!/usr/bin/python3
import csv
import json as j

def convert_csv_to_json(filename):
    try:
        with open(filename, "r") as f:
            data = list(csv.DictReader(f))

        with open(filename, "w") as f:
            data.json = j.dump(data, f)
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
