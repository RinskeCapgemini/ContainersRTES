

Created the container using the Dockerfile and the following commands:
sudo docker build -t e2:simple_script -f E2/Dockerfile . 


sudo docker run -rm -v "/E2/log_files" e2:container_name


Container name 

| Script name | Container name | Image ID |
|---|---|---|
| simple_calculation.py  | e2:simple_script  | 9b5ce4013001 |
| medium_calculation.py  | e2:mid_script  | 4ded1d82c496 |
| long_calculation.py  |  e2:long_script | 52a78b7aa545 | 



