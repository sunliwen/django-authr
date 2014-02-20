django-authr [![Build Status](https://travis-ci.org/sunliwen/django-authr.png?branch=master)](https://travis-ci.org/sunliwen/django-authr) [![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/sunliwen/django-authr/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
============

Django Auth in RESTful way

### Installation

```console
git clone https://github.com/sunliwen/django-authr.git
mkvirtualenv django-authr
cd django-authr
make develop
```

### Run the tests

```console
make
```

### Fire up a temp server

```console
make migrate
make run
```

Run `open http://localhost:8000` to view the demo. The default username is `liwen` and password is `1234`.

### Authentication

#### Session-based
*TODO*
#### Token-based
*TODO*
#### OAuth
*TODO*

### Acknowledgements

Initially based on demo from @dustinfarris <https://github.com/dustinfarris/django-ember-authentication>

### License

(MIT)
