pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('Create venv') {
            sh 'pip install virtualenv --user'
            sh 'python -m venv env'
        }

        stage('build') {
            steps {
                 sh '''
                    source env/bin/activate
                    pip install -r requirements.txt --user
                    deactivate
                '''
            }
        }
    }
}