# Testing CI and github-pages

## Testing with Continous Itegration (CI)
We would like to run our tests every time we push in order to make sure that any update to the code does not break any core functionality.

Follow the [instructions](https://docs.travis-ci.com/user/tutorial/) on how to set up travis-ci.

For more information about how to test your python project check out the [documentation](https://docs.travis-ci.com/user/languages/python/)

Add a badge with the information about whether test passed or not. In my case this was

[![Build Status](https://travis-ci.com/finsberg/tutorial_travis_and_githubpages.svg?branch=master)](https://travis-ci.com/finsberg/tutorial_travis_and_githubpages)

## Creating documentation for your code.

We will use `sphinx` to generate documentation and we will publish the documentation using github pages. 
Create a the directory where we will put the documentation

mkdir docs
cd docs
Now we run the `sphinx-quickstart` which is the first step in generating documentation. This will ask you some questions, and I will reply as follows

```
$ sphinx-quickstart
Welcome to the Sphinx 1.8.3 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]:

Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]:
[Interrupted.]

henriknf at Henrik-Finsbergs-MacBook-Pro in ~/local/src/IN1910/tutorial_travis_and_githubpages/docs on master [!]
$ sphinx-quickstart
Welcome to the Sphinx 1.8.3 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y

Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]:

The project name will occur in several places in the built documentation.
> Project name: Mypackage
> Author name(s): Henrik Finsberg
> Project release []: 1.0

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.
> Project language [en]:

The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.
> Source file suffix [.rst]:

One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.
> Name of your master document (without suffix) [index]:
Indicate which of the following Sphinx extensions should be enabled:
> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> doctest: automatically test code snippets in doctest blocks (y/n) [n]:
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:
> coverage: checks for documentation coverage (y/n) [n]:
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
> ifconfig: conditional inclusion of content based on config values (y/n) [n]:
> viewcode: include links to the source code of documented Python objects (y/n) [n]: y
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: y

A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html' instead of invoking sphinx-build
directly.
> Create Makefile? (y/n) [y]:
> Create Windows command file? (y/n) [y]:

Creating file ./source/conf.py.
Creating file ./source/index.rst.
Creating file ./Makefile.
Creating file ./make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file ./source/index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

You can look at your documentation by running
```
make html
python -m http.server
```
Then open a web-browser and go to http://localhost:8000, and navigate to build/html.

### Creating API documentation

Now we will make the documentation for our python package

```
sphinx-apidoc -o source/ ../code
```

If you run make html now you will get a warning saying the it is unable to import `mymodule`. To fix this open `source/conf.py` and add the following lines at the top
```Python
import os
import sys

sys.path.insert(0, os.path.abspath("../../code"))
```

Unexpected section title, and this is because I have documented the code using the numpy style, which is not default. Open source/conf.py and add `sphinx.ext.napoleon` to the list called extensions. Let us also change the html theme. Scroll down and set `html_theme = 'sphinx_rtd_theme'`, and run pip install sphinx-rtd-theme.

### Building documenation that will be hosted on github pages

Create a new branch called `gh-pages`
```
git checkout -b gh-pages
```
Now delete everything in the repo and commit it
```
rm -rf *
git add -u
git commit -m "Remove all files"
```
Now go back to the `master` brach and build the documentation.
```
git checkout master
cd docs
make html
```
This will build the html documentation. Now checkout the `gh-pages` branch again, move the html files to the root folder and add them.
```
git checkout gh-pages
mv docs/build/html/* .
rm -r docs
git add .
commit -m "Adding documentation"
```

All stemps can be summarized in the following bash script
```shell
git checkout master
cd docs
make html
cd ..
git checkout gh-pages
cp -r docs/build/html/* .
rm -r docs code
git add .
commit -m "Adding documentation"
```