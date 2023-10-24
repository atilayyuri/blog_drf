# blog_drf

Example Python **Django** application to create post cards using **django-rest-framework**. This application demonstrates create-update operations using class based views in Django.

Created by Atilay Tamkan <tamkan.atilay@gmail.com>

## Setup

Ensure that you have [Python](https://www.python.org/downloads/) Version >= 3.9.

- Clone this repository to your local machine using ```git clone https://github.com/atilayyuri/blog_drf.git```

- Setup the environment by executing below in order (to activate venv on Windows use ```.\venv\Scripts\Activate.ps1``` for PowerShell or ```.\venv\Scripts\activate.bat``` for cmd. Use Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force if you got authorization errors)
```
cd blod_drf
python -m venv venv
source .venv/bin/activate
python -m pip install -r ./blog_drf/requirements.txt
``` 

## Execution
```
python manage.py runserver 127.0.0.1:8000
```
Visit the web browser with 'https://127.0.0.1:8000' 

To create a new post you need to create a user using ````python manage.py createsuperuser```. After entering credentials and logging, you can create your post cards.

    


