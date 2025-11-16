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
                sh './build.sh'   // Adjust for your environment
            }
        }
        stage('Test') {
            steps {
                sh './test.sh'
            }
        }
        stage('Deploy') {
            steps {
                sh './deploy.sh'  // Deployment script
                // OR AWS CLI commands instead
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
