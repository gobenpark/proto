.PHONEY: upload

upload:
	python -m pip freeze > requirements.txt
	python setup.py sdist bdist_whell
	python -m twine upload dist/*