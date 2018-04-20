FROM resin/rpi-raspbian

WORKDIR /root

RUN \
  apt-get update && \
  apt-get install -y python python-pip

COPY requirements.txt ./

RUN \
  pip install --user --upgrade pip && \
  pip install --user --upgrade setuptools && \
  pip install --user -r requirements.txt

ARG INTERVAL

ENV INTERVAL=$INTERVAL
ENV FIREBASE_CERTIFICATE=firebase/certificate.json
ENV FIREBASE_CONFIG=firebase/config.json

COPY firebase/certificate.json $FIREBASE_CERTIFICATE
COPY firebase/config.json $FIREBASE_CONFIG
COPY run-poller.py ./

ENTRYPOINT [ "tini", "-s", "--" ]

CMD while true; do python run-poller.py; sleep $INTERVAL; done
