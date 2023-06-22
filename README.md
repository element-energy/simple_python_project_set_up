# Template repository for new Python software tools

This is a template Git repository for ERM Sustainable Energy Solutions (SES) (Element Energy/E4Tech) Python software projects.

Please use this template for **all** coding repositories for Python software tools.  We have prepared this repository to include
all the basic requirements to get started on a Python project, as well as a clear structure to help you build in good coding standards and practices from the get-go!

## Creating your new repository using this one as a template

The easiest way to create a repository "in the image" of this one is to **create a fork**.  See [here](https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html) for how to do this on GitLab.

At the top-right of the repository's page on GitLab, click 'Fork'.  Ensure to fill in the project name and if on GitLab ensure that you select the `element-energy` namespace (not your own private one), or if creating it within an existing project group, use that namespace instead (e.g. `element-energy/sfs`). Amend the project description for your project (this is important, as it tells the rest of the organisation what your code is for!) and click 'Fork Project'.  These instructions will need to be adjusted appropriately for GitHub.

## Template repository features

### Template folder structure

This repo contains these folders, which we recommend you use:

Folders:
- `constants` - create modules in this folder to store constants that will be used throughout your project. An example is provided.
- `model` - this contains all the model source code, which itself should be split into modules and packages (folders).  This is where your core modelling logic will live.
- `tests` - tests that ensure that all of your source code in `model` works as expected.  **For all re-usable software tools, every function/class should have tests**.  Ensure that you write tests alongside your model code: tests of individual modules/classes should be in `unit`, whereas tests combining multiple modules or end-to-end functionality should be in `integration`.
- `.gitlab` - contains templates for GitLab issues and merge requests 

Root folder files:
- `requirements.txt` - this should contain lists of all the Python packages required for your project.  Add/edit as required.
- `main.py` - this is an example of a main entrypoint for your model, and should be the only place the model is called from.
- `.gitlab-ci.yml` - this specifies default settings for running your pipeline (tests, formatting checks) on GitLab

### Setting up your repository in PyCharm

- Clone repository to a folder **not** tracked by SharePoint, setting up any SSH keys as required.
- Create a blank virtual environment for the project using the desired Python version and install only the dependencies in `requirements.txt` (settings -> project interpreter)
- Set up `pytest` as the default test runner
- Ensure that you can run the example tests in Python and that they all pass

### Procedure: issue and merge request templates, branches

Please use GitLab's issues to organise coding tasks required for your project.  No matter the size of the project, it is always useful
to split work into manageable chunks, and issues allow you to specify this.  This repository provides a number of pre-prepared issue templates which you can use straight away to organise your work:

- `feature_request` - small, <5 day pieces of work introducing a new/changed feature to the code
- `task` - requests to run the model without making any code changes
- `meta-issue` - collects together multiple modelling tasks (`feature_request` or `task`) under a common theme (e.g., a work stream) to visualise and track all tasks needed to implement the work stream fully.

Use the `develop` branch as the default branch on your project.  When you add a feature, do not commit straight to `develop` but make feature branch, with the number of the ticket referenced in the branch name.

Once your feature is ready for merging, make a merge request and use the `merge_request` template for the merge request description.  In that, **be sure to fill out which ticket the merge request relates to**.  It is _very important_ to 
**link your merge request to the issue which it relates to**.  Assign a reviewer.  **Please follow the link between merge requests and tickets at all times to make it easy for a reviewer to know what is being implemented**.

### Template Gitlab CI/CD pipeline settings

Your pipeline consists of all the tests you write in the `tests` folder which verify that the model is functioning as expected.
By default, the `.gitlab-ci.yml` file in this repository will run all of these tests, both `unit` and `integration`.

This `.gitlab-ci.yml` file also includes basic Python formatting checks as standard, to ensure that your code conforms
to good style standards and conventions (PEP8).  These include: black formatting, PyLint, isort and MyPy.

### Default logger set-up

This repository contains a default set up of the `logging` module.  **Please avoid using `print` statements in your Python code and use `logging.info/debug/warning/error` instead, as these are much easier to track, redirect and test.

(Balint to complete)

### Setting up PyLinting for your project

(Balint to complete)