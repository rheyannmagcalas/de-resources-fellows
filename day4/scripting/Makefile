env:
        pip3 install pipenv
        pipenv shell --python3.9
clean:
        find . -iname "*.pyc" | xargs rm -Rf
        find . -iname "*.pyo" | xargs rm -Rf
        find . -iname "*.pyd" | xargs rm -Rf
        find . -iname "__pycache__" | xargs rm -Rf
install:
        pipenv install
run:
        make clean
        make install
        pipenv run python3 rand.py