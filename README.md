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

##### * Task 1:

A Django model called `Artist` is provided to you as an example inside `artists/models.py`. For this task you'll have to implement a view inside `artists/views.py` that matches with `/artists` URL located in `django_practice_2/urls.py`.
This view will be in charged of fetching all `Artist`'s objects stored in the database (previously loaded with the given script) and render the `artists.html` template sending all `artists` as context.

You can test the response of the view in your browser, pointing to `http://localhost:8080/artists/`. This is the expected result:

<img src="https://user-images.githubusercontent.com/2788551/39497571-5071116c-4d7a-11e8-9659-3edcc9a4ee20.png" width="50%" height="50%">


##### * Task 2:

In this task you'll extend the previous view with some functionality. The idea is to filter the list of artists by name sending GET parameters in the URL (i.e: `/artists?first_name=stev`).
For this, check if a `first_name` GET parameter is sent inside `request.GET` dictionary. If so, filter the previous artists queryset that had ALL artists, in order to filter only the ones that contains the given pattern in their first_name.
The context while rendering the template will be the same as before, but now the artists queryset might have less artists than before, if a `first_name` parameter is given. The following image shows the expected result:

<img src="https://user-images.githubusercontent.com/2788551/39497588-65a6b6e0-4d7a-11e8-8f3b-4c5bbfb9cbfc.png" width="50%" height="50%">


##### * Task 3:

In a similar way as done before, check if a `popularity` GET parameter is given in the URL and if so, filter the artists queryset by artists that have a popularity greater or equal to the one given.
It should work like this:

<img src="https://user-images.githubusercontent.com/2788551/39497601-7892d2b6-4d7a-11e8-8dfd-b658262a7146.png" width="50%" height="50%">


##### * Task 4:

For this task you'll implement a brand new view under `/artist/<artist_id>` URL. This view will take the given `artist_id`, get the proper Artist object from the database and render the `artist.html` template sending the artist object as context.
If you want to check what id is associated with each artist, you can do it in the admin page at `/admin/` URL.

<img src="https://user-images.githubusercontent.com/2788551/39497626-9f1ee55a-4d7a-11e8-94fe-b0f81c0e6c14.png" width="50%" height="50%">
