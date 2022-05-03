pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python:3.10.1'
                    args '-u root:root'
                }
            }
            steps {
                sh  'python -m pip install --upgrade pip --user'
                sh  'pip install --user -r requirements.txt'
                sh  'python manage.py test'
            }
        }
    }
}

