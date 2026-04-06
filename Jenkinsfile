pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-api-demo .'
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                docker rm -f flask-api-demo-container || exit 0
                docker run -d -p 5000:5000 --name flask-api-demo-container flask-api-demo
                '''
            }
        }

        stage('Test API') {
            steps {
                bat '''
                echo Waiting for app to start...
                timeout /t 5 > nul
                curl http://localhost:5000/api/hello
                '''
            }
        }
    }
} 