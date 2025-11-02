FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

RUN apt-get update &&     apt-get install -y --no-install-recommends     python3 python3-pip git wget curl vim &&     rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip &&     pip install openllm[serve] torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121

COPY . /app

RUN openllm download mistralai/mistral-7b-instruct-v0.2

EXPOSE 3000

ENV MODEL_ID=mistralai/mistral-7b-instruct-v0.2
ENV OPENLLM_MODEL_NAME=$MODEL_ID
ENV OPENLLM_BACKEND=pt

CMD ["openllm", "start", "--model", "mistralai/mistral-7b-instruct-v0.2", "--port", "3000", "--workers", "2", "--timeout", "300"]
