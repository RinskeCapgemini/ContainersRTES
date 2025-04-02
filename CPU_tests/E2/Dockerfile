FROM python:3.11-slim

WORKDIR /app

COPY CPU_calculation_scripts/medium_calculation.py /app/

RUN cat /etc/hostname


CMD ["python", "medium_calculation.py"]
