# Instructions for Sprint A

## Objectives

- Demonstrate a minimal Flask project structure.
- Define view functions and routes for GET requests.
- Serve JSON encoded responses.

## Initialize Repository

1. Clone the master branch of this repository to a convenient location and change directories into the cloned repository.

    ```bash
    git clone git@github.com:KenzieAcademy/backend-epithet-generator.git
    cd backend-epithet-generator
    ```

2. Create a sprint-a branch for work in progress and add the recommended Python [local .gitignore](https://github.com/github/gitignore) starter file from GitHub.

    ```bash
    git checkout -b sprint-a
    curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore
    ```

    curl displays contents of URLs to stdout, a.k.a the terminal, and the > operator redirects stdout to the specified file. If the file does not exist, the redirect operator creates the file. If the provided file does exist, it will be overwritten with the contents of the URL. For additional examples of curl, [this tutorial](https://gist.github.com/caspyin/2288960) explores the GitHub API using curl.
   - Review the contents of the recommended .gitignore file to see commonly ignored Python artifacts.
    - Notice GitHub recommends not committing virtualenvs to version control. It is unnecessary and has considerable storage costs. Instead, use pipenv to centrally manage environments outside of project repositories.
    If curl is not installed, it can be installed with most package managers, like Homebrew, or APT. See your instructor if you need assistance with this.

        ```bash
        #MacOS
        brew install curl
        ```

3. Delete all sections of the downloaded .gitignore file except sections listed below. Unless a statement in the downloaded .gitignore collides with a name of a project resource, it is not necessary to remove any of the entries, but we will for the sake of being explicit. It is probable that files from each of these sections could end up in a Flask project. The others are less probable and can be ignored later if introduced. Alternatively, you can add the removed sections to your [$HOME/.gitignore_global](https://help.github.com/articles/ignoring-files/) file to protect all git repositories on your computer from these files without adding the ignore statements to each
project.
   - Byte-compiled / optimized / DLL files
   - C extensions
   - Installer logs
   - Unit test / coverage reports
   - Flask stuff
   - pyenv
   - Environments

4. Stage the .gitignore file and create an initial commit of the sprint-a branch.

## Configuring Development Environments

In order to create a virtual environment, we'll use Pipenv to help create it for us. Running the commands below will create a `Pipfile` and a `Pipfile.lock`. The `Pipfile` is where all of your dependencies and versions are stored, and the `Pipfile.lock` file contains the dependencies of _those_ dependencies... and so on and so forth. If you're interested in reading more about this concept, check out this article on [deterministic builds](https://en.wikipedia.org/wiki/Reproducible_builds).

```bash
pipenv install flask

# install support for .env files
pipenv install python-dotenv

# install pytest with additional helper packages for the flask microframework
pipenv install pytest-flask --dev

# start a new shell with the environment activated
pipenv shell
```

## Structuring Projects

There are many ways to structure Flask applications, but not all project structures are equal. We will start the Epithet
Generator project as a single Python package with four files and evolve the project structure according to Flask best-practices when needed.

1. Although a single file is sufficient for minimal Flask applications, we define a minimal application as a
 Python package consisting of four files: `app.py`, `helpers.py`, `test_helpers.py`, and the package's `__init__.py` file. (Note: there are two underscores on either side of `init`.) We will focus on these four files first before showing how to refactor the project structure for
 [large projects](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications) in a later sprint. Use the bash command `touch` to create empty files that we can then fill.

```bash
touch __init__.py
touch app.py
touch helpers.py
touch test_helpers.py
touch .env
```

|File|Description
|---|---|
\_\_init\_\_.py | An empty (for now) file that Python uses to identify whether or not it can use a directory.
app.py | Organize defined routes. You may see this file called `app.py` or `<project-name>.py` in other projects. Flask defaults to loading `app.py`, so we will default to using `app.py` here, but the name is arbitrary and can be configured with the `FLASK_APP` environment variable.
helpers.py | Organize application logic keeping it decoupled from routes defined in `app.py`. By decoupling application and routing, application logic can be easily reused in other areas of an application or in other projects.
test_helpers.py | Organize unit and integration tests for the Flask application. In larger applications, helpers in `helpers.py` would be distributed across multiple packages, each with a `test_<package-name>.py` file of tests.
.env| Store application configuration management as environment variables. This file is not considered in the four files of a Flask application as `.env` files are used across programming languages and frameworks.

## Instantiating Flask

When starting out, we first have to explain to Flask what it's going to be running. We can do that by invoking one of the 'magic variables' in python called `__name__`. This variable lets us know which file is currently being run; if it's the file that was started from the command line, the name will be "\_\_main\_\_". If it's imported by the file that was started from the command line, then the name will be the name of the file.

### In the .env File

Add to following to the .env file.

```ini
FLASK_APP=app
FLASK_ENV=development
```

- The FLASK_APP environment variable tells Flask which file & variable to use when loading applications. If FLASK_APP is not defined, Flask will default to app but we'll define it here to be explicit.
- The FLASK_ENV environment variable tells Flask which environment settings to use. If FLASK_ENV is not set, Flask will default to production environment settings which disables Flask's debug mode for security purposes. Setting FLASK_ENV to development enables debugging.

### In the app.py File

We start at the top by importing flask, as expected:

`from flask import Flask`

The `Flask` object is the core of the system, and we can instantiate our own app off of that object.

`app = Flask(__name__)`

When we start building out different functions of the server, binding them all to the `app` object will let us keep track of the scope of our app and help alleviate any "gotcha's" during the build process.

## Defining Routes

1. In app.py, use the app.route decorator to:
    - bind a view function called generate_epithets to '/'. This route will eventually serve a randomly generated epithet.
    - bind a view function called vocabulary to '/vocabulary'. This route will eventually serve the vocabulary used to generate epithets.
2. Right now, have these functions return the following JSON representations respectively: `{"epithets": []}` and `{"vocabulary": {}}`.

## Starting Flask's Development Server

At this point, we have defined a working Flask application and can verify our progress by starting Flask's development server and navigating to the routes we defined.

1. Launch the pipenv shell within the project's root directory.

2. Once the shell is open, start the Flask application by calling `flask run` in your environment.

3. Navigate to http://127.0.0.1:5000 and verify both routes are serving their respective payloads configured in the previous section.

4. If both routes are serving their payloads, this sprint of the assignment is complete.
