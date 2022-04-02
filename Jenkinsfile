pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'sudo pip install virtualenv'
                sh 'sudo python -m virtualenv venv'
                sh 'sudo source env/bin/activate && pip install --upgrade -r requirements.txt'
            }
        }
    }
}