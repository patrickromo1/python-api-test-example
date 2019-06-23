# pytest-template

This repo is a template for running API and Load tests using `pytest` and `bzt`

---

## Local set-up instructions

1. Run `make install`
2. Run `make lint-all` to run all 3 linters (`flake8`, `yamllint`, `bzt` config validator)
3. Run `make test` to run the `pytest` api tests against the github api
4. Run `make test-load` to run the `bzt` load tests against the github api

---

## Running tests individually or by filename

To run a single test or a group of tests that match a pattern expression run `make test-single test_pattern=<TEST_NAME>`

**Example:**
`make test-single test_pattern=unique_username` will run all tests with unique_username in the test name
**Example without make:** `pipenv run pytest -k unique_username`

---
To run all of the tests in a specific file or directory run `make test-target target=<PATH>`

**Example:**
`make test-target target=tests/search_test.py` will run all tests in the search_test.py file
**Example without make:** `pipenv run pytest tests/search_test.py`

---

To run pytest with specific cli arguments run `make test-custom pytest_args="<PYTEST_CLI_ARGUMENTS>"`

**Example:**
`make test-custom pytest_args="-vv -k test_unique_username"` (Runs all tests with pattern test_unique_username)

This runs pytests with only the arguments you specify. Documentation for common pytest cli arguments can be found here https://docs.pytest.org/en/latest/usage.html

## Local clean-up instructions

1. Run `make clean` to remove log and report files.
2. Run `make uninstall` to remove all dependencies and destroy the current virtualenv

---

## Tools used in the Jenkins pipeline

### Dependency Management

* `pipenv` - Pipenv is used to manage dependencies in this project
https://pipenv.readthedocs.io/en/latest/
s

---

#### Linting

* `flake8` - Used for python file linting
http://flake8.pycqa.org/en/latest/
* `yamllint` - Used for yaml file linting
https://github.com/adrienverge/yamllint
* `bzt -lint` - Use for validating the `bzt` config file
https://gettaurus.org/docs/Linter/

---

#### API Testing

* `pytest` - Used for api tests against the github api
https://doc.pytest.org/

##### Pytest Plugins

* `flaky` - Used for retrying tests in `pytest`
https://docs.pytest.org/en/latest/flaky.html
https://github.com/box/flaky
* `pytest-randomly` - Used for randomizing the order of tests in `pytest`
https://github.com/pytest-dev/pytest-randomly
* `pytest-xdist` - Used for running tests in `pytest` in parallel processes
https://github.com/pytest-dev/pytest-xdist

---

#### Load Testing

* `bzt` - Used for load testing against the github api
https://gettaurus.org/
* `blazemeter` - Used for running `bzt` in the cloud
https://www.blazemeter.com/

---
#### Tips

* To run `pytest` commands without prepending `pipenv run` to each command run `pipenv shell` to start a subshell in the virtualenv.
