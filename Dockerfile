FROM balenalib/raspberry-pi:latest

# Install necessary packages
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
    unzip \
    nano
RUN apt-get clean

# make things work...maybe.
RUN ln -s /usr/bin/python3 /usr/bin/python && \
    touch /var/log/cron.log && \
    /etc/init.d/rsyslog start && \
    /etc/init.d/cron start
# install cron and things
COPY crontab.txt /etc/cron.d/crontab.txt
COPY cron.sh /opt/cron.sh
RUN chown root /opt/cron.sh && chmod +x /opt/cron.sh
RUN crontab -u root /etc/cron.d/crontab.txt && mkdir /root/stemnet
WORKDIR /root/stemnet
COPY ./STEMNET-Daily-Files /root/stemnet/STEMNET-Daily-Files

ENTRYPOINT ["/opt/cron.sh"]
