import requests, docker, pytest
from parseXML import *

def test_parse():
    xmltest = """
        <heartbeat> 
            <header> 
                <code>2000</code> 
                <origin>FrontEnd</origin> 
                <timestamp>2021-05-25T12:00:00+01:00</timestamp> 
            </header> 
            <body> 
                <nameService>Website</nameService> 
                <CPUload>5.63</CPUload> 
                <RAMload>86.13</RAMload> 
            </body> 
        </heartbeat> """

    result = parse(xmltest)
    assert result == "FrontEnd:Website - 2021-05-25T12:00:00+01:00 - 86.13 - 5.63 - 2000" 

def test_runningcontainers():
    client = docker.from_env()
    if client.containers.list(all=True):
        assert len(client.containers.list(all=True)) >= 6
    else:
        assert False

def test_es_running():
    count = 0
    while count < 10:
        try:
            response = requests.get('https://localhost:9200', verify=False)
            response.status_code
            assert response.status_code == 401
            break          
        except:
            time.sleep(5)
            count += 1

