FROM xalwart/{{ cc }}:{{ compiler_version }}-alpine-{{ os_version }}

# Upgrade distro.
RUN apk update && apk upgrade

# Install libraries.
RUN apk add --update --no-cache \
      {{ libraries_to_install }}

# Install framework.
COPY ./framework /usr/local
RUN ldconfig /etc/ld.so.conf.d

CMD ["bash"]
