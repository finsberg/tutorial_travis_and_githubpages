# Testing CI and github-pages

## Testing with Continous Itegration (CI)
We would like to run our tests every time we push in order to make sure that any update to the code does not break any core functionality.

Follow the [instructions](https://docs.travis-ci.com/user/tutorial/) on how to set up travis-ci.

For more information about how to test your python project check out the [documentation](https://docs.travis-ci.com/user/languages/python/)

Add a badge with the information about whether test passed or not. In my case this was

[![Build Status](https://travis-ci.com/finsberg/tutorial_travis_and_githubpages.svg?branch=master)](https://travis-ci.com/finsberg/tutorial_travis_and_githubpages)

## Sphinx
This is a simple tutorial showing how to use sphinx to document your code.
In this folder there is some very simple code, and we want to create some nice
looking documentation.