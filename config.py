paperless_url = '192.168.176.28'
paperless_port = '8000'

interesting_fields = [
    # The Issuer is assumed to be contained in a single row.
    # The first result of the file should yield the target most of the time
    {
        'fieldname': 'issuer',
        'api_field': None,
        'regex_string': r'^.*\d{5,}.*$',
        'regex_index': 0,
    },
    # Use the field paperless provides for this
    {
        'fieldname': 'issuedate',
        'api_field': 'created_date',
        'regex_string': None,
        'regex_index': None,
    },
    # Good luck
    # Maybe the last index that contains words like "summe" or "gesamt"
    {
        'fieldname': 'payment_total',
        'api_field': None,
        'regex_string': None,
        'regex_index': None,
    }
]
