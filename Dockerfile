FROM python:3.12

RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    libx11-6 \
    x11-xserver-utils \
    && rm -rf /var/lib/apt/lists/*

RUN pip install pygame

ENV XDG_RUNTIME_DIR=/tmp/runtime-root
ENV DISPLAY=host.docker.internal:0
ENV QT_X11_NO_MITSHM=1

WORKDIR /app
COPY . /app

RUN echo "For macOS users, please install and run XQuartz. Ensure it is running before starting the Docker container." > /app/README.txt

CMD ["python", "app/main.py"]
