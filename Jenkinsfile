pipeline {
    agent { 
      dockerfile true
    }
    stages {
      stage('Install') {
        steps {
          sh 'PIPENV_VENV_IN_PROJECT=1 make install-ci'
        }
      }

      stage('Linting') {
        steps {
          parallel(
            flake8: {
              sh 'PIPENV_VENV_IN_PROJECT=1 make lint'
            },
            'yaml-lint': {
              sh 'PIPENV_VENV_IN_PROJECT=1 make lint-yaml'
            },
            'bzt-lint': {
              sh 'PIPENV_VENV_IN_PROJECT=1 make lint-bzt'
            }
          )
        }
      }

      stage('API Tests') {
          steps {
            sh 'PIPENV_VENV_IN_PROJECT=1 make test'
          }
      }

      stage('Load Tests') {
        steps {
          sh 'PIPENV_VENV_IN_PROJECT=1 make test-load-ci'
        }
      }
    }
    post {
      always {
        junit "**/reports/*.xml"
        deleteDir()
      }
    }
}
