class API:
    """A dummy API."""
    def send(item):
        print(f'Uploaded {item!r}!')

def upload_data(item):
    """Uploads the provided value to our database."""
    if hasattr(item, 'get_value'):
        data = item.get_value()
        API.send(data)
    else:
        API.send(item)
