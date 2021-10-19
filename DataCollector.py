import json

class DataCollector:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_value(self):
        return json.dumps(self.items)

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

upload_data("some text")

collector = DataCollector()
collector.add_item(42)
collector.add_item(1000)
upload_data(collector)
