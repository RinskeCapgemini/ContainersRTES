FROM python:3.11-slim

WORKDIR /app

COPY E1/automated_cpu_test.py /app/
COPY CPU_calculation_scripts/long_calculation.py /app/
COPY CPU_calculation_scripts/medium_calculation.py /app/
COPY CPU_calculation_scripts/simple_calculation.py /app/

CMD ["sh", "-c", "python /app/automated_cpu_test.py && cat /app/automated_logs.txt"]
