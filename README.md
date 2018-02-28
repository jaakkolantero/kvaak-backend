# KvaaK-backend

Backend for KvaaK  app created with Django.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.Instructions are made for Linux(Ubuntu 16.10).

### Prerequisites

To get started I presume you have ```python``` installed correctly(I'm using Python 3.6.4).
Other recomended packages include ```pip```, ```conda```

### Installing

Clone repository.

```
git clone https://github.com/terokoodaa/kvaak-backend.git
```

Before we can go any futher we have to create a virtual environment and activate it.
You can use any virtual environment you want but in this example I'm using [conda](https://conda.io).

```
conda create --name kvaak python=3.6
source activate kvaak
```

Next we need to install [Django](https://www.djangoproject.com/) and [Django Rest Framework](http://www.django-rest-framework.org/). You can install them either with pip or conda. I'm using pip this time.

```
pip install django djangorestframework
```

Install cors middleware.
```
pip install django-cors-headers
```

Before we can populate our database we have to migrate it.

```
cd kvaak-backend
cd kvaak
python manage.py migrate
```

Now we can populate our project with dummy data. Code for custom django-admin command can be found [here](https://github.com/terokoodaa/kvaak-backend/blob/master/kvaak/api/management/commands/populate_db.py). populate_db always creates 6 species and number of sigthings based on argument given(If no argument given populate_db creates 6 sightings).

```
python manage.py populate_db 100
```

Finally we can start our server and head out api endpoint to see some data.

```
python manage.py runserver
```

There is list and detail view for both species and sightings:
- [http://localhost:8000/species/](http://localhost:8000/species/)
- [http://localhost:8000/species/1](http://localhost:8000/species/1)
- [http://localhost:8000/sightings/](http://localhost:8000/sightings/)
- [http://localhost:8000/sightings/1](http://localhost:8000/sightings/1)

## Running the tests (NOT READY YET ='( )

Explain how to run the automated tests for this system

## Deployment

[deployment checklist](https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/)

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django Rest Framework](http://www.django-rest-framework.org/) - DRF

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/terokoodaa/kvaak-backend/tags). 

## Authors

* **Tero Jaakkola** - *Initial work* - [terokoodaa.io](https://terokoodaa.io/board/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
