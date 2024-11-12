FROM pandoc/latex:latest-ubuntu

RUN apt-get update && apt-get install -y \
        make ttf-mscorefonts-installer fontconfig sed gawk && \
    rm -rf /var/lib/apt/lists/* \
    update-ms-fonts && \
    fc-cache -f && \
    tlmgr update --self --all && \
    tlmgr install collection-langjapanese enumitem
    