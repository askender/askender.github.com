help:
	@echo Usage: make [\TARGET\]
	@echo
	@echo TARGET:
	@echo "    clean    清理临时文件"
	@echo "    preview  start preview"
	@echo "    deploy   deploy askender"
	@echo


.PHONY: clean-pyc clean-build docs

clean: clean-build clean-pyc


clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info


clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

preview:
	@echo "starting askender"
	python -m SimpleHTTPServer 8004

deploy:
	@echo "starting deploy"
	fab deploy
