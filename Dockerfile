FROM python

WORKDIR D:\Project_O.A.B

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]