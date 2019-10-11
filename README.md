# CS591L1 - Embedded Languages and Frameworks

Materials for a computer science course on embedded languages and frameworks.

Course website: [https://kinanbab.github.io/CS591L1/website](https://kinanbab.github.io/CS591L1/website)

## Lecture Notes

This repository contains all lecture notes from CS591L1. Most notes are notebooks that run interactive code in the browser.

You can view a static version of these notes through the schedule section in the [course website](https://kinanbab.github.io/CS591L1/website).

Lecture notes can also be run dynamically. This is recommended, since it allows you to interactively run and modify code snippets
and view their output. Lecture notes are mostly written in Jupyter notebook, or neptune notebook. Any lecture notes that does not
use one of these notebook enviornment has running instructions attached.

#### Lecture Notes in Python / Jupyter Notebook

To run these lecture notes, you need to have [python3](https://www.python.org/downloads/) and
[virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b) installed.

To install all the python library dependencies for the lecture notes, as well as jupyter notebook, follow these commands:
```bash
cd /path/to/repository
python3 -m venv venv  # creates a virtual environment
. venv/bin/activate  # activates the virtual environment
pip install -r requirements.txt # installs all dependencies including jupyter notebook
```

After installing Jupyter notebook, you can run the lecture notes using these commands:
```bash
cd <path/to/respository>
. venv/bin/activate  # activates the virtual environment
jupyter notebook  # will open a tab in your browser showing the lecture notes
```

Using Jupyter notebook is very intuitive, if you have not used one before, please look at this [tutorial](https://www.codecademy.com/articles/how-to-use-jupyter-notebooks).
