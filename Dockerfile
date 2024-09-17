FROM ubuntu:22.04

WORKDIR /YandexSpeechKit

COPY ./requirements.txt ./

RUN apt-get update && apt-get install -y ffmpeg && apt-get -y install python3-pip
RUN python3 -m pip install --upgrade pip && pip install --no-cache-dir -r ./requirements.txt

COPY ./ ./

RUN mkdir data && mkdir data/audio && mkdir data/text

