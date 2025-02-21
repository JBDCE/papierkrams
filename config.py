paperless_url = '192.168.176.71'
paperless_port = '8000'


outfile_columns = [
    {
        'name': 'Zahlungsempfänger',
        'field_name': 'correspondent',
    },
    {
        'name': 'Ausstellungsdatum',
        'field_name': 'created_date',
    },
    {
        'name': 'Gesammtsumme',
        'field_name': 'custom_fields',
        'custom_field_id': 3,
    },
    {
        'name': 'Anliegerwohnungsanteil in %',
        'field_name': 'custom_fields',
        'custom_field_id': 2,
    }
]
