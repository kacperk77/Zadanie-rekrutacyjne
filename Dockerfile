FROM python:3.8.8

ADD main.py .
ADD test.py .
ADD dane_wejsciowe.txt .
ADD wynik.txt .


CMD [ "python", "./main.py" ]
CMD [ "python", "./test.py" ]