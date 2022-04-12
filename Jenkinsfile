pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python:3.10.1-alpine'
                    args '-u root:root'
                }
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev"

                    sh script:'''
                            #/bin/bash
                            echo "PATH is: $PATH"
                              python --version
                              python -m pip install --upgrade pip --user
                              ls
                              pip install --user -r requirements.txt
                              python manage.py test
                              export PATH="$WORKSPACE/.local/bin:$PATH"
                                '''
                }
            }
        }
    }
}

