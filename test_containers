import requests, docker, time, pytest

def test_runningcontainers():
    client = docker.from_env()
    if client.containers.list(all=True):
        assert client.containers.list(all=True).count() == 6
    else:
        assert False

def test_es_running():
    count = 0
    while count < 10:
        try:
            response = requests.get('https://localhost:9200', verify=False)
            response.status_code
            count = 11
            assert response.status_code == 401
        except:
            time.sleep(5)
            count += 1
