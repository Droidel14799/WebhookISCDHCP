FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY /home/$USER/Webhook/__main__.py /usr/src/app

CMD [ "python", "./__main__.py" ]