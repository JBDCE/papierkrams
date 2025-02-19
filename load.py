import config
import secret
from requests import get
from json import loads

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
            },
            auth=(secret.username, secret.password)
        )

        result = loads(raw_res.text)

        print(result.get('next'))

        output.extend(result.get('results'))
        if not result.get('next'):
            break
        page_counter = page_counter + 1
    return output

def main():
    data = load_data()
    print(data[0].keys())
    return

if __name__ == '__main__':
    main()
