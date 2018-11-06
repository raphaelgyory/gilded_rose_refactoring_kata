============================
Gilded Rose Refactoring Kata
============================

This an implementation of the Gilded Rose refactoring kata (https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/master/GildedRoseRequirements.txt)

My approach consists in allowing a dynamic update of the sell_in and quality values.
The python code was responsible for two things: updating items and defining the conditions of the update.
The new code allows to dynamically define these conditions, which are called Rules. The objective is to move them to a DB in the future. You can see an example in tests/fixtures.py
The Gilded Rose class is now only responsible to iterate through the items and call the rules that apply to them.

The main python classes are defined in gilded_rose_refactoring_kata/gilded_rose.py

The tests and fixtures are in the tests folder.


Installation
------------

Clone the repository

    git clone https://github.com/raphaelgyory/gilded_rose_refactoring_kata

    cd gilded_rose_refactoring_kata

Create a virtual environment and install python requirements.

    virtualenv -p python3 gilded_rose_venv

    source gilded_rose_venv/bin/activate

    pip3 install -r requirements_dev.txt


Run tests

    make test


* Free software: MIT license


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
