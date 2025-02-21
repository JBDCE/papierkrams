import config

from csv_helper import write_file
from load import load_data

def parse_file(file):
    row = {}
    for column in config.outfile_columns:
        # If the column desired is a default column from paperless use it directly
        if column['field_name'] != 'custom_fields':
            row[column['name']] = file[column['field_name']]
            continue

        # Add an error message in ccase the configuration is broken
        if not column['custom_field_id']:
            print("Invalid configuration for custom field: " + repr(column))
        # Otherwise its a custom column. Treat it as such
        # Iterate over the list of custom fields of the file
        # and the value from the custom field with the correct custom field id
        for field in file['custom_fields']:
            if field['field'] == column['custom_field_id']:
                row[column['name']] = field['value']

    return row

if __name__ == '__main__':
    # The important information is stored within custom fields
    data = load_data()

    rows = [parse_file(file) for file in data]

    print(rows)

    write_file('outfile.csv', rows)