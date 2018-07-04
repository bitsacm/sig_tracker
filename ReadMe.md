# ACM SIG Tracker

To keep track about all info regarding SIGs

### Requirements

- Python 3.6
- Django 2.0:
  ```shell
  sudo -H pip3 install Django==2.0
  ```

### Usage

- Clone repository
- ```shell
  cd Downloads/sig_tracker/sig
  ```
- To sync database:
  ```shell
  python3 manage.py makemigrations
  ```
  And
  ```shell
  python3 manage.py migrate
  ```

- To start development server:
  ```shell
  python3 manage.py runserver
  ```
