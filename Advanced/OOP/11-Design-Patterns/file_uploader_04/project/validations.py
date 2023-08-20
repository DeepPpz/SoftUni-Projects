import json
import csv


def validate_json(json_data):
    try:
        json.loads(json_data)
        return True
    except json.JSONDecodeError:
        return False


def validate_csv(csv_data):
    try:
        csv_reader = csv.reader(csv_data.splitlines())
        header = next(csv_reader)
        if not header:
            return False

        rows = list(csv_reader)
        if len(rows) < 1:
            return False
        return True

    except:
        return False
