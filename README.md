

# Requirements

In local dev we use `requirements.dev.txt`. 

```
Django
dj-static
dj-database-url
djangorestframework
django-cors-headers
python-decouple
```

In production we add those from dev plus heroku required ones.

```
-r requirements.dev.txt
psycopg2
gunicorn
```

# Heroku

## Procfile

Execute gunicorn server, require path to `wsqi.py` file.

```yaml
web: gunicorn project.wsgi --log-file -
```

## runtime.txt 

Its pointing to used python executable. 
Simply write 

```
python-3.8.2
```

### Python Support 

https://devcenter.heroku.com/articles/python-support

#### 04.2020

Supported runtimes

- python-3.8.2 on all supported runtime stacks
- python-3.7.6 on all supported runtime stacks
- python-3.6.10 on all supported runtime stacks
- python-2.7.17 on all supported runtime stacks