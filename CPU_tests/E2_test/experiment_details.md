

Created the container using the Dockerfile and the following commands:

From CPU test directory:
sudo docker build -t e2:mid_script -f E2/medium_container/Dockerfile . 


From container directory:
bash spinning_x.sh

-v = bind mount volume list
-d = detatch -> container runs in background?

(sudo docker run --rm -v /home/pirinske/GitHub/ContainersRTES/CPU_tests/E2/medium_container/log_files:/host_log_files e2:mid_script)

Container name 

| Script name | Container name | Image ID |
|---|---|---|
| simple_calculation.py  | e2:simple_script  | 9b5ce4013001 |
| medium_calculation.py  | e2:mid_script  | 4ded1d82c496 |
| long_calculation.py  |  e2:long_script | 52a78b7aa545 | 



