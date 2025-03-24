FROM python:3.11-slim

WORKDIR /app

COPY container_testscript.py

# COPY automated_cpu_test.py .
# COPY long_calculation.py .
# COPY medium_calculation.py . 
# COPY simple_calculation.py .

CMD ["sh", "-c", "container_testscript.py"]
