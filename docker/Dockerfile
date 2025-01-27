
# docker build . -t aconvnet-pytorch
# Base container: docker pull pytorch/pytorch:1.9.0-cuda11.1-cudnn8-devel

FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-devel

ENV DEBIAN_FRONTEND=noninteractive

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV TZ=Asia/Singapore
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list

RUN apt-get -y update \
    && apt-get -y upgrade

RUN apt-get install --no-install-recommends -y --fix-missing \
    software-properties-common \
    build-essential \
    libgl1-mesa-glx \
    libgdal-dev locales \
    git ffmpeg vim nano

RUN pip install seaborn && \
    pip install numpy && \
    pip install scipy&& \
    pip install tqdm && \
    pip install jupyter && \
    pip install matplotlib && \
    pip install scikit-image && \
    pip install scikit-learn && \
    pip install opencv-python && \
    pip install absl-py && \
    pip install optuna

# Expose port 8888
EXPOSE 8888

# # By default, run the notebook
# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

RUN mkdir -p /workspace

ARG work_dir=/workspace

WORKDIR ${work_dir}
