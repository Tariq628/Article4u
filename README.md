# ***Article4u***
***Article4u*** is my big project which i have made by my own, after a months of coding ***Article4u*** blog has been reached on completion. Most of the Django concepts that i have learnt in life, All the concepts have been used in this beautiful blog..
# More About ***Article4u***
***Article4u*** is a mixture of all famous blogs like: [medium](https://medium.com/), [HubSpot](https://blog.hubspot.com/), [Unspalsh](https://unsplash.com/blog/) I tried to cover all the features of popular blogs in ***Article4u***, Blog contains beautiful code editor ***Summernote***, it maintains user's ***HTML*** perfectly
## Contribute
You can feel free to contribute in ***Article4u***, Make pull request i will definitely merge it.

# Getting Started with Django project
This blog was made with [Django Project](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)
## Available scripts
### Clone repo
Clone the repository in your specific directory by terminal ```git clone https://github.com/Tariq628/Article4u```

### Virtual Environment
Open editor where manage.py exist, make virtual env by terminal.

```virtualenv myprojectenv```
#### Activate your virtual environment
```.\myprojectenv\Scripts\activate```
### Install packages
```pip install -r requirements.txt```

## Move SQLITE3 to MYSQL
Download MYSQL [here](https://dev.mysql.com/downloads/installer/) create database with any name
### Replace SQLITE3 setting with MYSQL in settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'root',
        'PASSWORD': 'database_password',
        'HOST':'localhost',
        'PORT': '3306'
    }
}
```
### Don't forget to apply migrations
```python manage.py makemigrations```

```python manage.py migrate```
