# SIG Tracker
*In house application for tracking SIG progress and feedback.*

The name of the project is sig_tracker and the name of the app is main

## How to run?
###Setting up the Development Environment
1. For people using anaconda:<br>
   1. To install anaconda, [refer this](https://conda.io/docs/user-guide/install/index.html)<br>
   2. The base directory contains 'environment.yml' file. To replicate the same environment:
      ```bash
      conda env create -f environment.yml
      ```
2. For people using python3 virtual environment:
   1. To install virtualenv, refer [this](https://www.digitalocean.com/community/tutorials/common-python-tools-using-virtualenv-installing-with-pip-and-managing-packages#a-thorough-virtualenv-how-to)
      ```bash
      pip install virtualenv
      virtualenv --python=python3 sig_tracker
      ```
   2. The base directory contains 'requirements.txt' file. To install the required packages:
      ```bash
      pip install -r requirements.txt
      ```
###Running for the first time:<br>
   1. To migrate database:
      ```bash
      python manage.py makemigrations
      python manage.py migrate
      ```
   2. Start the development server:
      ```bash
      python manage.py runserver
      ```

Please file an issue if you face any problem while running the app.<br>
Improvements are always welcome. Feel free to fork the repository and send in pull requests with proper commit messages.
