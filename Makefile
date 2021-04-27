#! make
# export PYTHONPATH=
# export PYTHONSTARTUP=

.PHONY: backup test egg

egg:
	# egg
	py -3.5 setup.py bdist_egg --dist-dir dist
	# ...laid

cleanup:
	## cleaning up all
	rm -rfv build dist *.egg-info
