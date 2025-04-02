FROM python:3.11-slim

WORKDIR /app

COPY logger.sh /app/
COPY CPU_calculation_scripts/medium_calculation.py /app/


RUN chmod +x logger.sh

ENTRYPOINT [./logger.sh]

