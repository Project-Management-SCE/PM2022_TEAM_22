
String dockerFileName = 'Dockerfile.build'
String dockerFileArgs = '-u root:root'

pipeline {
    agent none
    stages {
        stage('Install Python Dependencies') {
                agent {
                dockerfile {
                    filename dockerFileName
                    args dockerFileArgs
                }
            }
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
            agent {
                dockerfile {
                    filename "$dockerFileName"
                    args "$dockerFileArgs"
                }
            }
            steps {
                sh '''#!/bin/bash
                 source env/bin/activate
                 coverage run --source='base' manage.py test
         '''
            }
        }
        stage('Coverage Report') {
            agent {
                dockerfile {
                    filename "$dockerFileName"
                    args "$dockerFileArgs"
                }
            }
            steps {
                sh '''#!/bin/bash
                 source env/bin/activate
                 coverage report
         '''
            }
        }
        stage('Deploy') {
            agent {
                docker {
                    image 'cimg/base:stable'
                    args '-u root'
                }
            }
            steps {
                sh '''#!/bin/bash
                 curl https://cli-assets.heroku.com/install.sh | sh
                 heroku container:login
                 heroku container:push web -a gentle-temple-64246
                 heroku container:release web -a gentle-temple-64246
         '''
            }
        }
    }
}

