FROM python:3.8

WORKDIR /usr/src/app

COPY main.py .

RUN pip install fastapi "uvicorn[standard]"

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
