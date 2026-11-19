
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Fetching source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Python application...'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'
                sh 'python3 -m unittest test_app.py'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                sh 'minikube image build -t calculator-app:latest .'
            }
        }

        stage('Kubernetes Deployment') {
            steps {
                echo 'Deploying application to Kubernetes...'
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl rollout status deployment/calculator-deployment'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed!'
        }
    }
}
