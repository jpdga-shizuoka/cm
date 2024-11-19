FROM pandoc/latex:latest-ubuntu

RUN apt update && apt install -y \
        make ttf-mscorefonts-installer fontconfig python3 python3-venv && \
    rm -rf /var/lib/apt/lists/* \
    update-ms-fonts && \
    fc-cache -f && \
    tlmgr update --self --all && \
    tlmgr install collection-langjapanese enumitem
RUN python3 -m venv /home/venv && \
    /home/venv/bin/pip install panflute
