pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m virtualenv venv'
                sh 'source env/bin/activate && pip install --upgrade -r requirements.txt'
            }
        }
    }
}