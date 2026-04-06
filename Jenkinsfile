pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/harshpandeyz/flask-api-docker-demo.git'
            }
        }

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
                bat 'curl http://localhost:5000/api/hello'
            }
        }
    }
}