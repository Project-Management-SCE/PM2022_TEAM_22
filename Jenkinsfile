pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install package_name --user'
                sh 'python -m virtualenv venv'
                sh 'source env/bin/activate'
                sh 'pip install -r requirements.txt --user'
            }
        }
    }
}