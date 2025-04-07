FROM python:3.11-slim

WORKDIR /app

COPY E2/long_container/logger.sh /app/
COPY CPU_calculation_scripts/long_calculation.py /app/

RUN chmod +x logger.sh

ENTRYPOINT ["bash", "./logger.sh"]

