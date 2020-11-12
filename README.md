# pytest-automation
This is a sample project for automation using pytest

Toturial link : https://testautomationu.applitools.com/pytest-tutorial/
https://docs.pytest.org/

How to run tests
Command
python -m pytest

Pacakages 

pip install requests
pip install pytest
pip install pytest-html
pip install pytest-cov
pip install pytest-xdist // for paralle threads
pip install pytest-bdd

https://tavern.readthedocs.io/en/latest/

Command to generate HTML report
 python -m pytest --html=report.html

Command to generate code coverage report
python -m pytest --cov=stuff

Command to run tests in parralel threads
python -m pytest -n 3 // it will run tests in 3 parallel threads