PART 1: SETUP AND INTRODUCTION for linux
1- Install Vscode

2- Overview of Django Models-Views-Templates

3- Test python3 --version

4- Create Virtual Environment where you install python packages to isolate from other packages in your system py -3 -m venv env

create a requirements.txt file

create a git ignore file

5- Activate Environment
python3 -m venv env
source env/bin/activate

6- Install Django
pip install django

Test Django
python -m django --version

pip install -r requirements.txt

7- Start a new project in the directory
django-admin startproject nameofproject . 
it is important that you add that . after the name of the project.


9- Create an app.
python manage.py startapp nameofapp

10- Add app to settings

11- do the migration 
python manage.py makemigrations
python manage.py migrate

Check project python manage.py runserver

PART 2: MODELS AND ADMIN INTERFACE

12- Create Models, and apply migrations 
python manage.py makemigrations
 python manage.py migrate

12b. Register Models in Admin Interface (optional but recommended for managing data)

13- Create superuser 
python manage.py createsuperuser

confirm by adding /admin/login to the url aftrewards try running the server with 'python manage.py runserver'

14- Add string methods

def __str__(self):
        return str(self.id)
15- Configure static files path and urls

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/')

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
16- Tell Django where to find the static files while on the browser

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
PART 3: VIEWS AND TEMPLATES

17- Write basic view, add index.html in app template folder and configure app url

def index(request):
    return render(request, 'index.html')
18- Add assets folder to static_root folder

Frontend https://github.com/bedimcode/responsive-portfolio-website-JhonDoe
19- Load static files in html file

20- Write Views

21- Add Data in Admin interface

22- Load content from views to Templates

{% static 'assets/css/styles.css' %}

{{ model.field }}
Check DEPLOYMENT

GIT RESET

rm -rf .git*