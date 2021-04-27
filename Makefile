#! make
# export PYTHONPATH=
# export PYTHONSTARTUP=

.PHONY: backup test egg dist

egg:
	py -3.5 setup.py bdist_egg --dist-dir dist

dist:
	py -3.5 setup.py sdist --dist-dir dist

cleanup:
	## cleaning up all
	rm -rfv build dist *.egg-info
