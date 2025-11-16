pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Akhil-jagadale/CLI-Expense-Tracker.git'
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt || true'
            }
        }
        stage('Test') {
            steps {
                sh 'python test_logic.py'
            }
        }
        stage('Deploy') {
            steps {
                sh 'aws s3 cp some_artifact.zip s3://yourbucket/'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished'
        }
        success {
            echo 'Deployment successful.'
        }
        failure {
            mail to: 'jagadaleakhilesh@gmail.com',
                subject: "Jenkins Build Failed",
                body: "See details: ${env.BUILD_URL}"
            }
        }
    }
