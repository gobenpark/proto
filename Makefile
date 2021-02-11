.PHONEY: upload

upload:
    python setup.py sdist bdist_whell
    python -m twine upload dist/*