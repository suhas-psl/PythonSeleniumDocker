# PythonSeleniumDocker
Automated Pytest Selenium Code

This is a demo automation project for testing a flight reservation system.
The framework used for testing is Pytest.
This consists of automated tests using the tool Selenium. 
The tests are present in Git at this repository.
Here I have created selenium grid setup with docker containers.
With the help of docker compose file the selenium grid containers are created.
A separate container is created in which python test cases are executed.
The python selenium container contains the dependencies and test cases to be executed on the selenium grid.
The Jenkins file contains Pipeline code for creating the selenium grid containers and then executing the tests in python container.
The results are published as artifacts using report.html.

Pre-requisite for this framework is a linux machine or vm on which Jenkins is installed.
On this Jenkins we have to create pipeline job which will get the Jenkins file from Github repository.

Please refer pictorial block diagram for more understanding.
