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
                sh 'docker build -t flask-api-demo .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f flask-api-demo-container || true
                docker run -d -p 1234:1234 --name flask-api-demo-container flask-api-demo
                '''
            }
        }

        stage('Test API') {
            steps {
                sh 'curl http://localhost:1234/api/hello'
            }
        }
    }
}
