FROM mcr.microsoft.com/devcontainers/base:ubuntu

ARG ANO_CLAB_VERSION
ARG ANO_PRIV_KEY_NAME

ENV ANO_PRIV_KEY_NAME=${ANO_PRIV_KEY_NAME}
ENV ANO_CLAB_VERSION=${ANO_CLAB_VERSION}

# install some basic tools inside the container
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    make \
    curl \
    sshpass \
    iputils-ping \
    htop \
    python3 \
    python3-pip \
    sudo \
    wget \
    curl \
    tcpdump \
    telnet \
    openssh-client \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

# Ensure that the non-root user can run sudo without a password
RUN echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode && chmod 0440 /etc/sudoers.d/vscode

# copy postCreate script
COPY ./postCreate.sh /bin/postCreate.sh
RUN chmod +x /bin/postCreate.sh

# Switch to non-root user
USER vscode

# install the latest containerlab, yamllint, cook-and-cut and eos-downloader
RUN bash -c "$(curl -sL https://get.containerlab.dev)" -- -v ${ANO_CLAB_VERSION} \
    && pip3 install --user yamllint \
    && pip install --user "eos-downloader>=0.10.1" \
    && pip install --user passlib

# install FastAPI
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN pip install "fastapi[standard]"

# Generate an SSH key pair with no passphrase for EC2
# The -f option specifies the output file and -N "" sets an empty passphrase.
RUN ssh-keygen -t rsa -b 2048 -f ~/.ssh/${ANO_PRIV_KEY_NAME} -N ""