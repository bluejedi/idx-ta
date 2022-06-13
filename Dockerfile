FROM python:3.6-alpine

WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install tradingview_ta

COPY . .

CMD [ "python", "./main.py" ]