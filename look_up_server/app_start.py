import os
import csv
import argparse
import sys
import json

def main(args):
    location = args.location or 'newservers.csv'
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, location)
    list_of_dicts = []
    write_location = os.path.join(module_dir, 'look_up/data.json')
    try:
        with open(file_path) as phile:
            data = csv.DictReader(phile, delimiter=',')
            for row in data:
                list_of_dicts.append(row)
    except FileNotFoundError as error:
        print(f"File not present {error}")
        sys.exit(1)

    with open(write_location, 'w') as phile:
        phile.write(json.dumps(list_of_dicts))

    sys.exit(1)






if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get argument for getting the location of the CSV file")
    parser.add_argument('--location', help='file location of the csv')
    args = parser.parse_args()

    main(args)


list = [{
    'hostname': 'yo',
    'ip': '198.7.9'
},{
    'hostname': 'st',
    'ip': '198.6'
}
]

with open('../test-output', 'w') as phile:
    phile.write(str(list))

with open('../test-output') as phile:
    data = phile.read()
    print(f"data is {data}")