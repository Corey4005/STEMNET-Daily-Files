FROM debian:latest
RUN apt-get update && apt-get install -y \ 
    git \
    wget \
    cron \
    python3 \
    curl \
    lsof \
    python3-pip \
    procps \
    systemctl \
    vim \
    rsyslog\
    build-essential \
    base-files \
    sudo \
    nano 
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN touch /var/log/cron.log
RUN systemctl enable rsyslog 
RUN systemctl start rsyslog
RUN mkdir /root/stemnet
WORKDIR /root/stemnet
ADD crontab.txt crontab.txt
RUN crontab -u root crontab.txt
RUN git clone https://github.com/Corey4005/STEMNET-Daily-Files.git 
CMD ["cron", "-f"]
