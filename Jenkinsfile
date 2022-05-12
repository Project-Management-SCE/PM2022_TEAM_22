pipeline {
    agent {
                docker {
                    image 'python:3.10.1-slim'
                    args '-u root:root'
                }
    }
    stages {
        stage('Install Linux Libraries') {
            steps {
                sh '''#!/bin/bash
                 apt-get update

                 if [ $(dpkg-query -W -f="${Status}" libpq-dev 2>/dev/null | grep -c "ok installed") -eq 0 ];
                    then
                    apt-get install libpq-dev;
                    fi

                if [ $(dpkg-query -W -f="${Status}" python3-dev 2>/dev/null | grep -c "ok installed") -eq 0 ];
                    then
                    apt-get install python3-dev;
                    fi

                if [ $(dpkg-query -W -f="${Status}" build-essential 2>/dev/null | grep -c "ok installed") -eq 0 ];
                    then
                    apt-get install build-essential;
                    fi
         '''
            }
        }
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
