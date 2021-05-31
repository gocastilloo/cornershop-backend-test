# Cornershop backend test

Test: Order system with authentication made with Django.
## Getting Started

These instructions will cover usage information and for the docker container.

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

#### Instructions to run 
Once you've **cloned the git repo**, everything will happen in your terminal.
Make sure docker-compose file is here, you can list with command ```ls```

**Open your command line in the directory of this file**

Then:

    make up
Once the volume is build:

    
Then, we will apply the migrations to the file:

    python manage.py makemigrations utils
We will apply those migrations to the database:

    python manage.py migrate
And now, we will run Django

    python manage.py runserver 0.0.0.0:8000


#### Useful Links
The base URL will be:
`localhost:8000/signin`
##### Then you can use the following path:
If you want to login:
* `/login`

If you want to list the menu:
* `/menu` 

If you want to upload new food:
* `/admin`

Hope you enjoy it.
## Built With

* Django v3.0.8
* Postgres
* Celery
* Redis


## Authors

* **Hugo Castillo** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

