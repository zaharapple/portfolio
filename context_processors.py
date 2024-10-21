from datetime import datetime


def helper(request):
    return {'helper': {
        'utc_time': datetime.utcnow().strftime("%d.%m.%Y %H:%M"),
        'ss': 'TEST'
        }
    }