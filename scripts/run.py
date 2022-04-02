import os

try:
    os.chdir("..")
    os.system("python manage.py runserver")
except KeyboardInterrupt:
    print("Server shutting down")
