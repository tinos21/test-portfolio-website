
pipeline {
    agent any

    environment {
        PYTHON = '/usr/local/bin/python3.12'  // Full path to your Python
        ALLURE_CLI = '/opt/homebrew/bin/allure'
        PROJECT_DIR = '/Users/tinopro14/Documents/TESTING_SCRIPTS/tino-dev-testing'
    }

    stages {
        stage('Use Local Repo') {
            steps {
                echo 'Running pipeline using local code repository.'
            }
        }

        stage('Set Up Python & Install Dependencies') {
            steps {
                dir("${env.PROJECT_DIR}") {
                    sh '''
                    ${PYTHON} -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests with Allure') {
            steps {
                dir("${env.PROJECT_DIR}") {
                    sh '''
                    source venv/bin/activate
                    pytest --alluredir=allure-results
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                dir("${env.PROJECT_DIR}") {
                    sh '''
                    ${ALLURE_CLI} generate allure-results --clean -o allure-report
                    '''
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/allure-report/**', fingerprint: true
        }
    }
}
