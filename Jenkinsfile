pipeline {
    agent {
                docker {
                    image 'python:3.10.1'
                    args '-u root:root'
                }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv tutorial-env'
                sh 'source tutorial-env/bin/activate'
                sh  'python -m pip install --upgrade pip --user'
                sh  'pip install --user -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh  'python manage.py test'
            }
        }
    }
}

