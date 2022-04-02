pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'virtualenv env && source env/bin/activate && pip install --upgrade -r requirements.txt'
            }
        }
    }
}