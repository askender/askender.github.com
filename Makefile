PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/blog
LOCALCONF=$(BASEDIR)/conf/localconf.py
PUBLICCONF=$(BASEDIR)/conf/publishconf.py


help:
	@echo Usage: make [\TARGET\]
	@echo
	@echo TARGET:
	@echo "    clean    清理临时文件"
	@echo '    html     generate the web site          '
	@echo "    watch    start watch"
	@echo "    preview  preview askender"
	@echo "    deploy   deploy askender"
	@echo


clean:
	rm -fr blog/
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(LOCALCONF) $(PELICANOPTS)

watch:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(LOCALCONF) $(PELICANOPTS)

preview:
	@echo "preview askender at http://localhost:8004"
	python -m SimpleHTTPServer 8004

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLICCONF) $(PELICANOPTS)

commit:
	@echo "starting commit"
	fab commit

deploy:
	@echo "starting deploy"
	fab deploy


