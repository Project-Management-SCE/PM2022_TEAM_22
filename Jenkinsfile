pipeline {
    agent none
    stages {
        stage('build') {
            agent {
                docker {
                    image 'python:3.10.1-alpine'
                }
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh script:'''
                            #/bin/bash
                            echo "PATH is: $PATH"
                              
                              python --version
                              python -m pip install --upgrade pip --user
                              pip install --user wheel 
                              python setup.py bdist_wheel
                              ls
                              pip install --user -r requirements.txt
                              export PATH="$WORKSPACE/.local/bin:$PATH"
                                '''
                }
            }
        }
    }
}
