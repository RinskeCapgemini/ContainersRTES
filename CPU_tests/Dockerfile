FROM python:3.11-slim

WORKDIR /app

COPY automated_cpu_test.py .
COPY long_calculation.py .
COPY medium_calculation.py . 
COPY simple_calculation.py .

CMD ["sh", "-c", "python automated_cpu_test.py && cat output.txt"]
