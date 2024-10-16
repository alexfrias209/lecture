import csv
import ipdb

csv_file_path = "random_data.csv"

with open(csv_file_path, mode="r") as file:
    reader = csv.reader(file)
    header = next(reader)
    
    for row in reader:
        ipdb.set_trace()
        age = 2
        try:
            if age > 3:
                print("Age is greater than 3.")
            else:
                print("Age is 3 or less.")
        except ValueError:
            print(f"Error: Age '{age}' is not a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            ipdb.set_trace()
