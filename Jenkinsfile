pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m pip install virtualenv'
                sh 'python -m virtualenv venv'
                sh 'source env/bin/activate && python -m pip install --user -r requirements.txt'
            }
        }
    }
}