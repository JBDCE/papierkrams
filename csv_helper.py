from csv import writer, QUOTE_ALL

def write_file(filepath, data):
    with open(filepath, 'w') as outfile:
        wr = writer(outfile, quoting=QUOTE_ALL, lineterminator=';\n')

        # Add a header with the column names just for convenience
        wr.writerow(data[0].keys())
        for row in data:
            wr.writerow(row.values())
    return

if __name__ == '__main__':
    sample_data = [
        {
            'num': 1,
            'name': 'Foo',
            'sum': 12.3,
        },
        {
            'num': 2,
            'name': 'Bar',
            'sum': 23.4,
        },
        {
            'num': 3,
            'name': 'Fizz',
            'sum': 34.5,
        }
    ]

    write_file(
        filepath='outfile.csv',
        data=sample_data
    )
