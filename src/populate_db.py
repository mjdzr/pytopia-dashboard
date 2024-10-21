import os
import json
import importlib.util

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

    from db.models import BannedWord, Message, User

with open('input/good.json', 'r') as f:
    data = json.load(f)

    # Load the yes.py file from input folder
    spec = importlib.util.spec_from_file_location("yes", 'input/yes.py')
    yes = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(yes)

    # Print data
    for message in data['audio_features']:
        # intersect the message id with the ones in the yes.py file
        for track in yes.yes_ids['items']:
            if message['id'] == track['track']['id']:
                print(track['track']['name'])  # Print the name associated with the id



