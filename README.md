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

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
