# VagrantDocker
A Hello World application served by Nginx inside a Docker container on Alpine linux, running inside a VM built by Vagrant, configured by Ansible, tested using testinfra.

## Building
#### Clone repo
```
https://github.com/jimmyjamesbaldwin/VagrantDocker
cd repo
```

#### Generate certs
(original instructions from: https://gist.github.com/iwazaru/579b547cc04f205b929d32e4f243d4f9)
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout app/certs/nginx-selfsigned.key -out app/certs/nginx-selfsigned.crt
sudo openssl dhparam -out app/certs/dhparam.pem 2048
```

#### Spin up VM
```
vagrant up
```

## Accessing the site
The VM IP is currently set in `Vagrantfile`; head to `http://192.168.1.33` and see the glory for yourself. To prevent people stealing your bananas, you can also use `https://192.168.1.33`, although you'll get warnings as the certificate is self-signed.

![Alt Text](https://media.giphy.com/media/2kUszZfHe3xvYX5TWR/giphy.gif)


## Testing
There are limited automated tests, which can be run with the following:
```
pip install tests/requirements.txt
chmod +x test.sh
./test.sh
```