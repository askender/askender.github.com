PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/blog
CONFFILE=$(BASEDIR)/conf/pelicanconf.py


help:
	@echo Usage: make [\TARGET\]
	@echo
	@echo TARGET:
	@echo "    clean    清理临时文件"
	@echo '    html     generate the web site          '
	@echo "    watch    start watch"
	@echo "    deploy   deploy askender"
	@echo


clean:
	rm -fr blog/
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

watch:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
	@echo "start watching askender"
	python -m SimpleHTTPServer 8004

deploy:
	@echo "starting deploy"
	fab deploy
