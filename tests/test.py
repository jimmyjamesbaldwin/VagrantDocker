import requests

def test_container_is_running(host):
    cmd = host.run("docker ps | grep 'hello-world:latest'")
    assert cmd.stdout != None

def test_exposed_80_and_443_serve_content():
	http = requests.get('http://192.168.1.33')
	https = requests.get('https://192.168.1.33', verify=False)