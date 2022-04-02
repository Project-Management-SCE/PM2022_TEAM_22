def installed = fileExists 'bin/activate'

if (!installed) {
    stage("Install Python Virtual Enviroment") {
        sh 'virtualenv --no-site-packages .'
    }
}   

pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                 sh '''
                    source bin/activate
                    pip install -r <relative path to requirements file>
                    deactivate
                '''
            }
        }
    }
}