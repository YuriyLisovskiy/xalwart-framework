FROM xalwart/{{ cc }}:{{ compiler_version }}-ubuntu-{{ os_version }}

ENV DEBIAN_FRONTEND=noninteractive

# Upgrade distro.
RUN apt-get update && apt-get -y upgrade

# Install libraries.
RUN apt-get install -y \
      {{ libraries_to_install }}

# Install framework.
COPY ./framework /usr/local
RUN ldconfig /etc/ld.so.conf.d

CMD ["bash"]
