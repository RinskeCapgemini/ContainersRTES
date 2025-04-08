

sudo docker build -f E1/Dockerfile -t e1:1.0 .

sudo docker run --cpuset-cpus=3 -v /home/rinske/Github/ContainersRTES/CPU_tests/E1/log_files:/app/logs e1:1.0