# SIG Tracker
*In house application for tracking SIG progress and feedback.*

The Project Name is 'sig_tracker'. 'sig' is the app name.

## How to run?
###Setting up the Development Environment
1. For people using anaconda:<br>
   1. To install anaconda, [refer this](https://conda.io/docs/user-guide/install/index.html)<br>
   2. The base directory contains 'environment.yml' file. To replicate the same environment:
      ```bash
      conda env create -f environment.yml
      ```
2. For people using python3 virtual environment:
   1. To install python3-venv, [refer this](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04#step-2-%E2%80%94-setting-up-a-virtual-environment)
   2. Create a folder 'environments'.
      ```bash
      mkdir environments
      cd environments   
      ```
   3. The base directory contains 'requirements.txt' file. To replicate the same environment:
      ```bash
      virtualenv sig_tracker
      source sig_tracker/bin/activate
      pip install -r requirements.txt
      ```
###Running for the first time:<br>
   1. To migrate databases:
      ```bash
      python manage.py makemigrations
      python manage.py migrate
      ```
   2. Start the development server:
      ```bash
      python manage.py runserver
      ```

*Raise issues if you face any problems with respect to firing up the app.*
Suggestions are welcome, changes for improvements are welcome.