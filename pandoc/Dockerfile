FROM "pandoc/latex"
RUN apk --update --no-cache add make msttcorefonts-installer fontconfig sed && \
    update-ms-fonts && \
    fc-cache -f && \
    tlmgr update --self --all && \
    tlmgr install collection-langjapanese
    