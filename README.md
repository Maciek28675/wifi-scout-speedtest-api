# WiFi Scout speedtest api

This is a REST API that will be used to meassure (approximately) network download/upload speed and ping in wifi scout app.

## How to run
### 1. Build container image
```shell
podman build -t speedtest_image .
```
### 2. Run container
```shell
podman run --name speedtest_container -p 8000:8000 speedtest_image 
```