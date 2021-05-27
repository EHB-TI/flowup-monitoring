import pytest, requests, time, docker
time.wait(20)
def test_elastic_search():
    URL = "https://localhost:9200/_status"
    status = 0
    while status < 10:
        try:
            response = requests.get(url = URL, verify=False)
            print(response.status_code)
            assert response.status_code == 401
        except:
            print("ES still not up, trying again in 3 sec...")
            time.sleep(5)
            status += 1

def test_containers_running():
    client = docker.from_env()
    if client.containers.list(all=True):
        assert client.containers.list(all=True).count() == 6
    else:
        assert False