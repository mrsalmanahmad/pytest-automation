import pytest
import requests

@pytest.mark.duckduckgo
@pytest.mark.restapi
def test_duckduckgo():

    #Arrange
   # url = 'https://api.duckduckgo.com/?q=python+programming&format=json'
    url = 'https://pocketfactory-qa.ssidecisions.com/'

    #Act
    response = requests.get(url)
    #body = response.json()

    #Assert
    assert response.status_code == 200
    #assert 'Python' in body['AbstractText']