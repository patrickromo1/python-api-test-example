green="\033[92m"
white="\033[0m"

.PHONY: install
install:
	@echo ${green}Installing the latest version of Python...${white}
	brew update && brew list python3 &>/dev/null || brew install python3
	@echo ${green}Installing pipenv...${white}
	pip3 install pipenv
	@echo ${green}Installing python dependencies...${white}
	pipenv install --dev

.PHONY: install-ci
install-ci:
	@echo ${green}Installing python dependencies...${white}
	pipenv sync --dev

.PHONY: lint
lint:
	@echo ${green}Running Flake8 linting...${white}
	pipenv run flake8 --config .flake8

.PHONY: lint-yaml
lint-yaml:
	@echo ${green}Running linting on yaml files...${white}
	pipenv run yamllint taurus.yaml

.PHONY: lint-bzt
lint-bzt:
	@echo ${green}Running linting on bzt config files...${white}
	pipenv run bzt -lint taurus.yaml

.PHONY: lint-all
lint-all:
	make lint
	make lint-yaml
	make lint-bzt

.PHONY: test
test:
	make clean
	@echo ${green}Running pytests...${white}
	pipenv run pytest -n 4

.PHONY: test-debug
test-debug:
	make clean
	@echo ${green}Running pytests...${white}
	pipenv run pytest -vv -n 4

.PHONY: test-target
test-target:
	@echo ${green}Running pytests... ${white}
	pipenv run pytest ${target} -vv

.PHONY: test-single
test-single:
	@echo ${green}Running pytests that match pattern ${test_pattern}... ${white}
	pipenv run pytest -vv -k ${test_pattern}

.PHONY: test-custom
test-custom:
	@echo ${green}Running pytests with custom cli args...${white}
	pipenv run pytest ${pytest_args}

.PHONY: test-load
test-load:
	@echo ${green}Running bzt load tests...${white}
	pipenv run bzt taurus.yaml -report

.PHONY: test-load-ci
test-load-ci:
	@echo ${green}Running bzt load tests in the cloud...${white}
	pipenv run bzt taurus.yaml -cloud -report

.PHONY: clean
clean:
	@echo ${green}Cleaning up reports and logs...${white}
	rm -rf ${PWD}/reports
	rm -rf ${PWD}/logs
	rm -rf ${PWD}/.pytest_cache
	rm -f jmeter.log

.PHONY: uninstall
uninstall:
	@echo ${green}Uninstalling python dependencies...${white}
	pipenv uninstall --all
	@echo ${green}Removing the virtualenv...${white}
	pipenv --rm
