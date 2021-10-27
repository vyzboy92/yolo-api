FROM ubuntu:16.04

RUN apt-get update -y && apt-get install software-properties-common -y

RUN apt-get install -y build-essential python3 python3-dev python3-pip

RUN python3 -m pip install --upgrade pip==20.3.4
	
RUN apt-get install -y ffmpeg libsm6 libxext6 libxrender-dev

RUN pip install -U numpy\
	opencv-python\
	imutils\
	flask
	
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf ~/.cache/pip

RUN mkdir obj-demo

COPY app.py /obj-demo

WORKDIR "obj-demo"

RUN chmod +x app.py

ENTRYPOINT ["python3", "app.py"]