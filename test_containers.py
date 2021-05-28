import requests, docker, time, pytest
time.sleep(20)

def test_es_running():
    count = 0
    while count < 10:
        try:
            response = requests.get('https://localhost:9200', verify=False)
            response.status_code
            count = 11
            assert response.status_code == 401
            break
        except:
            time.sleep(5)
            count += 1
            
def test_runningcontainers():
    client = docker.from_env()
    if client.containers.list(all=True):
        assert len(client.containers.list(all=True)) == 6
    else:
        assert False
