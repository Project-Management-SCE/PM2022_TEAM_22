pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python:3.10.1'
                }
            }
            steps {
                sh  'sudo python -m pip install --upgrade pip --user'
                sh  'sudo pip install --user -r requirements.txt'
                sh  'python manage.py test'
            }
        }
    }
}

