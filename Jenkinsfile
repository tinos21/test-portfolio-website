

pipeline {
    agent any

    environment {
        PYTHON = '/usr/local/bin/python3.12'  // Update to match the Jenkins agent's Python
        ALLURE_CLI = '/opt/homebrew/bin/allure'
     }

    stages {
        stage('Checkout from GitHub') {
            steps {
                echo 'Cloning from GitHub repository...'
                checkout scm
            }
        }

        stage('Set Up Python & Install Dependencies') {
            steps {
                sh '''
                ${PYTHON} -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests with Allure') {
            steps {
                sh '''
                source venv/bin/activate
                pytest --alluredir=allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                ${ALLURE_CLI} generate allure-results --clean -o allure-report
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/allure-report/**', fingerprint: true
        }
    }
}
