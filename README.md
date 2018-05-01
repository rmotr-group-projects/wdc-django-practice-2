### Django practice nº 2

##### Setup Instruction

```bash
$ mkvirtualenv -p $(which python3) django_practice_2
$ pip install -r requirements.txt
$ make migrate
```

You can now run the development server and point the browser to the correct URL:

```bash
$ make runserver
```


### Your Tasks

The structure of the whole Django project is built for you. Your job will be divided into three parts and multiple tasks for each part. You have to focus on implementing models inside `models.py`, a couple of views inside `views.py`, some URLs inside `urls.py` and templates in the `templates` folder.

If you run the development server with `$ make runserver`, you'll be able to test your views in the browser pointing to `http://localhost:8080/<some-path>`.


#### Part 1

Once you have your virtualenv setup with all the requirements installed and the Django migrations migrated, there is one more step that you need to do. A script called `load_initial_data_1.py` is provided to you in order to have some initial data stored in the database. You can run it by doing:

```bash
$ python load_initial_data_1.py
```

You'll now have a superuser created with username `admin` and password `admin`, so you can access the admin site vía `http://localhost:8080/admin/`

##### Task 1:

A Django model called `Artist` is provided to you as an example inside `artists/models.py`. For this task you'll have to implement a view inside `artists/views.py` that matches with `/artists` URL located in `django_practice_2/urls.py`.
This view will be in charged of fetching all `Artist`'s objects stored in the database (previously loaded with the given script) and render the `artists.html` template sending all `artists` as context.

You can test the response of the view in your browser, pointing to `http://localhost:8080/artists/`. This is the expected result:

<img src="https://user-images.githubusercontent.com/2788551/39494132-9c24ca2c-4d6b-11e8-89b8-b68e38a2d821.png" width="50%" height="50%">
