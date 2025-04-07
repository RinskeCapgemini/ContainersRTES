FROM python:3.11-slim

WORKDIR /app

COPY E2/medium_container/logger.sh /app/
COPY CPU_calculation_scripts/medium_calculation.py /app/

RUN chmod +x logger.sh

ENTRYPOINT ["bash", "./logger.sh"]

