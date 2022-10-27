POM-demo Tests
===============================

POM-demo Tests is a suite of UI automated tests for testing the login part of a web application.

Running the Tests Locally
=========================

* System requirements:
  * python 3
  * pip

* Clone this repo

* Next, create and activate a virtual environment:

        virtualenv ve-pom -p python3
        source ve-pom/bin/activate

* Export the username / password into `USERNAME` / `PASSWORD` environment variable:

      export USERNAME="ABCD"
      export PASSWORD="XYZ"

* Install packages and project dependencies:
* 
        pip install -r requirements.txt

* Run all tests or a certain UI test, on a given environment:

        pytest Tests/test_HomePage.py -v --html=./POM-demo3.html
        pytest Tests/test_LoginPage.py -v -nauto --html=./POM-demo3.html

* Run 1 test pytest -k test_home_page_title

