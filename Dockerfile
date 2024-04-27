FROM python:3.11.5


WORKDIR /main


COPY ./requirements.txt /main/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /main/requirements.txt

COPY ./initialize.py /main/initialize.py
RUN python3 /main/initialize.py

COPY . .

CMD ["uvicorn", "mlapi:app", "--host", "0.0.0.0", "--port", "80"]
