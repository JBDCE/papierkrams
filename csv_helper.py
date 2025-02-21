from csv import writer

def write_file(filepath, data):
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
    
    write_file('outfile.csv', sample_data)

