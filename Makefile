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
	@echo '    html     generate local site'
	@echo "    watch    start watch"
	@echo "    publish  start publish"
	@echo "    preview  preview askender"
	@echo "    deploy   deploy askender"
	@echo "    all      all askender"
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

add:
	@echo "starting add"
	git add -A

co:
	@echo "starting commit"
	git commit -am 'new'

deploy:
	@echo "starting deploy"
	git push origin master
	# fab deploy

all: publish add co deploy
