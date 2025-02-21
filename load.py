import config
import secret
from requests import get
from json import loads

def load_correspondent_lookup():
    correspondants = []
    page_counter = 1
    url = 'http://{url}:{port}/api/correspondents/'.format(
        url=config.paperless_url,
        port=config.paperless_port,
    )
    # Request data from paperless until we know
    # we arrived at the last page
    while True:
        raw_res = get(
            url=url,
            params={
                'page': page_counter,
                'format': 'json',
            },
            auth=(secret.username, secret.password)
        )
        result = loads(raw_res.text)
        correspondants.extend(result.get('results'))
        if not result.get('next'):
            break
        page_counter = page_counter + 1

    return {cr['id']: cr['name'] for cr in correspondants}

def resolve_correspondents(data):
    # Load the list of correspondants and create a lookup dictionary
    correspondent_lookup = load_correspondent_lookup()
    print(correspondent_lookup)

    # Go over each row of the data and replace the id with the name
    for row in data:
        row['correspondent'] = correspondent_lookup.get(row['correspondent'])

    return data

def load_data():
    # Load the next dataset until the next url is null
    # TODO This might be a nice usecase for python iterators maybe?
    output = []
    page_counter = 1
    url = 'http://{url}:{port}/api/documents/'.format(
        url=config.paperless_url,
        port=config.paperless_port,
    )

    # Request data from paperless until we know
    # we arrived at the last page
    while True:
        raw_res = get(
            url=url,
            params={
                'page': page_counter,
                'format': 'json',
                'ordering': 'created',
            },
            auth=(secret.username, secret.password)
        )
        result = loads(raw_res.text)
        output.extend(result.get('results'))
        if not result.get('next'):
            break
        page_counter = page_counter + 1

    # Resolve correspondant field in loaded data updating the results
    output = resolve_correspondents(output)

    return output

def main():
    data = load_data()
    print(data[0].items())
    return

if __name__ == '__main__':
    main()
