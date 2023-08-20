import os
import json
import csv
from validations import validate_json, validate_csv


def format_data(data):
    formatted_data = []
    for key, value in data.items():
        formatted_data.append([key, value])
    return formatted_data


file_name = input("Enter the file name: ")

try:
    root_path = os.path.dirname(os.path.abspath(__file__))
    files_dir = os.path.join(root_path, "files")
    file_location = os.path.join(files_dir, file_name)
    
    with open(file_location, 'r') as file:
        file_type = file.name.split('.')[-1]
        data = file.read()

        if file_type == 'json':
            if validate_json(data):
                print("File uploaded successfully (JSON):")
                parsed_data = json.loads(data)
                print(format_data(parsed_data))
            else:
                print("Invalid content type for import")
        
        elif file_type == 'csv':
            if validate_csv(data):
                print("File uploaded successfully (CSV):")
                csv_rows = csv.reader(data.splitlines())
                header = "".join(next(csv_rows)).split(", ")
                data_rows = ["".join(row).split(", ") for row in csv_rows]
                # parsed_data = [dict(zip(header, row)) for row in data_rows]
                parsed_data = {}
                for row in data_rows:
                    for i in range(len(row)):
                        for j in range(len(header)):
                            if i == j:
                                parsed_data[header[j]] = row[i]
                                break
                
                print(format_data(parsed_data))
            else:
                print("Invalid content type for import")
        else:
            print("Unsupported file format")

except FileNotFoundError:
    print("File not found")
