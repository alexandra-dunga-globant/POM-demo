POM-Demo Tests
===============================

POM-Demo Tests is a suite of UI automated tests for testing the login part of a web application.

Running the Tests Locally
=========================

* System requirements:
  * python 3
  * pip

* Clone this repo

* Next, create and activate a virtual environment:

        virtualenv ve-pom -p python3
        source ve-pom/bin/activate

* Add the username / password into `USERNAME` / `PASSWORD` environment variable:

        USERNAME="ABCD"
        PASSWORD="XYZ"

* Install packages and project dependencies:

        pip install -r requirements.txt

* Run all tests or a certain UI test, on a given environment:

        pytest -v -s --html=./POM-demo3.html
        pytest Tests/test_LoginPage.py -v -nauto --html=./POM-demo3.html

* Run only 1 test: 
        
        pytest -v -s -k test_home_page_title

