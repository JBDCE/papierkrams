import config
import re

def search_regex(content, regex_string, regex_index):
    return 'Your ad here!'

def parse_content(file_dict):
    output_fields = []

    for field in config.interesting_fields:
        outfield = {}
        outfield['fieldname'] = field.get('fieldname')

        # Prefer api field over regex string
        api_field_name = field.get('api_field')
        if api_field_name:
            outfield['result'] = file_dict[api_field_name]
            output_fields.append(outfield)
            continue

        outfield['result'] = search_regex(
            content=file_dict['content'],
            regex_string=field.get('regex_string'),
            regex_index=field.get('regex_index'),
        )

        output_fields.append(outfield)
    # to fill these fields we will use a very terrible hacky regex
    # This will run on a bunch of assumptions

    return output_fields


def main():
    from json import loads
    with open('samplefile.json') as sample:
        jsn = sample.read()
        print(jsn)
        samplefile = loads(jsn)
    print(parse_content(samplefile))
    return

if __name__ == '__main__':
    main()
