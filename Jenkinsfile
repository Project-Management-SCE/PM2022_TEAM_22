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
                    sh "apt-get install libffi-dev"
                    sh script:'''
                            #/bin/bash
                            echo "PATH is: $PATH"
                              python --version
                              python -m pip install --upgrade pip --user
                              ls
                              pip install --user -r requirements.txt
                              export PATH="$WORKSPACE/.local/bin:$PATH"
                                '''
                }
            }
        }
    }
}
