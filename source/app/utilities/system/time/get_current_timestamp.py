import re

from datetime import datetime

def get_current_timestamp ( ):

    result = {
        'year':  None,
        'month': None,
        'day':   None,
        'hour':  None,
        'min':   None,
        'sec':   None,
        'mil':   None
    }

    regex   = r'(\d{4})-(\d{2})-(\d{2})\s*(\d{2})\:(\d{2}):(\d{2})\.(\d{3})'

    matches = re.match ( regex, str ( datetime.now ( ) ) )


    for i, entry in enumerate ( result ):

        result [ entry ] = matches.group ( i + 1 )


    return result
