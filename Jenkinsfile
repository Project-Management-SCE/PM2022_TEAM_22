pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'pwd'
                sh 'pip install --user -r requirements.txt'
            }
        }
    }
}