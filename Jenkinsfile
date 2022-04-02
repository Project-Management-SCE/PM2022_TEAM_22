pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('Create venv') {
            sh 'pip install virtualenv --user'
        }

        stage('build') {
            steps {
                 sh '''
                    source bin/activate
                    pip install -r <relative path to requirements file>
                    deactivate
                '''
            }
        }
    }
}