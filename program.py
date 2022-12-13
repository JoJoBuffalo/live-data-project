def get_data(https://api.nasa.gov/DONKI/CME?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=iZfqQhESERl9LDQep7Wh3Lgubr3USaX9MqXhjCi3):
    """
    Get data from NASA
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def get_image_url(data):
    """
    Get the image url from the data
    """
    if data is not None:
        return data['url']
    return None


def get_image_title(data):
    """
    Get the image title from the data
    """
    if data is not None:
        return data['title']
    return None


def get_image_explanation(data):
    """
    Get the image explanation from the data
    """
    if data is not None:
        return data['explanation']
    return None


def get_image_date(data):
    """
    Get the image date from the data
    """
    if data is not None:
        return data['date']
    return None


def get_image_copyright(data):
    """
    Get the image