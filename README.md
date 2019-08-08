# Testing CI and github-pages

## Testing with Continous Itegration (CI)
We would like to run our tests every time we push in order to make sure that any update to the code does not break any core functionality.

Follow the [instructions](https://docs.travis-ci.com/user/tutorial/) on how to set up travis-ci.

For more information about how to test your python project check out the [documentation](https://docs.travis-ci.com/user/languages/python/)

Add a badge with the information about whether test passed or not. In my case this was

[![Build Status](https://travis-ci.com/finsberg/tutorial_travis_and_githubpages.svg?branch=master)](https://travis-ci.com/finsberg/tutorial_travis_and_githubpages)

## Creating documentation for your code.

We will use `sphinx` to generate documentation and we will publish the documentation using github pages. 


### Creating documenation with sphinx


### Building documenation that will be hosted on github pages

Create a new branch called `gh-pages`
```
git checkout -b gh-pages
```
