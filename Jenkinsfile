pipeline {
    agent {
                dockerfile {
                    filename 'Dockerfile'
                    args '-u root:root'
                }
    }
    stages {
        stage('Install Python Dependencies') {
            steps {
                sh '''#!/bin/bash
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

