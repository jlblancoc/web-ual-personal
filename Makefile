PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR?=$(HOME)/public_html/pelican
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

FTP_HOST=w3.ual.es
FTP_USER=jlblanco
FTP_TARGET_DIR=/WWW

PORT?=8000

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

help:
	@echo 'Makefile for the personal web site                                '
	@echo '                                                                  '
	@echo 'Usage:                                                            '
	@echo '   make html          (re)generate the site for local preview     '
	@echo '   make serve         preview at http://localhost:$(PORT), with   '
	@echo '                      automatic regeneration on changes           '
	@echo '   make publish       generate using production settings          '
	@echo '   make ftp_upload    publish and upload the site via FTP         '
	@echo '   make clean         remove the generated files                  '
	@echo '                                                                  '
	@echo 'Set DEBUG=1 to enable debugging, e.g. make DEBUG=1 html           '
	@echo 'Output directory: $(OUTPUTDIR)                                    '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

# Uses a plain static server (like the production one) instead of
# "pelican --listen", which prefers "foo.html" over "foo/index.html".
serve: html
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) --autoreload & \
	trap "kill $$!" EXIT INT TERM; \
	python3 -m http.server $(PORT) --bind 127.0.0.1 --directory $(OUTPUTDIR)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	chmod a+rX $(OUTPUTDIR) -R

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

ftp_upload: clean publish
	lftp ftp://$(FTP_USER)@$(FTP_HOST) -e "set ssl:verify-certificate false; mirror -v -p --recursion=always -R $(OUTPUTDIR)/ $(FTP_TARGET_DIR) ; quit"

.PHONY: html help serve publish clean ftp_upload
