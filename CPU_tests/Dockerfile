FROM python:3.11-slim

WORKDIR /app

COPY automated_cpu_test.py /app/
COPY long_calculation.py /app/
COPY medium_calculation.py /app/
COPY simple_calculation.py /app/

CMD ["sh", "-c", "python /app/automated_cpu_test.py && cat /app/automated_logs.txt"]
