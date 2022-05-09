pipeline {
    agent {
                docker {
                    image 'python:3.10.1-slim'
                    args '-u root:root'
                }
    }
    stages {
        stage('Build') {
            steps {
                sh '''#!/bin/bash
                 apt-get update
                 apt-get install libpq-dev python3-dev build-essential -y
                 python -m venv env
                 source env/bin/activate
                 python -m pip install --upgrade pip
                 pip install -r requirements.txt
         '''
            }
        }
        stage('Tests') {
            steps {
                sh '''#!/bin/bash
                 source env/bin/activate
                 coverage run --source='base' manage.py test

         '''
            }
        }
        stage('Coverage Report') {
            steps {
                sh '''#!/bin/bash
                 source env/bin/activate
                 coverage report
         '''
            }
        }
    }
}

