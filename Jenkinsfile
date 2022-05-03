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
                sh '''#!/bin/bash
                 python -m venv env
                 source env/bin/activate
                 python -m pip install --upgrade pip
                 pip install -r requirements.txt
         '''
            }
        }
        stage('Test') {
            steps {
                sh '''#!/bin/bash
                 source env/bin/activate
                 python manage.py test
         '''
            }
        }
    }
}

