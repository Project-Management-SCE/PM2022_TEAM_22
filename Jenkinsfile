
String dockerFileName = 'Dockerfile.build'
String dockerFileArgs = '-u root:root'

pipeline {
    agent none
    stages {
        stage('Install Python Dependencies') {
                agent {
                dockerfile {
                    filename "$dockerFileName"
                    args "$dockerFileArgs"
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
    }

            post {
            always {
                deleteDir()
            }
        }
}

