import os

try:
    os.system("python manage.py runserver")
except KeyboardInterrupt:
    print("Server shutting down")