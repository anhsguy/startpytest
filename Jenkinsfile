pipeline {
    agent any

    environment {
        VIRTUAL_ENV = "${WORKSPACE}/venv"
        PATH = "${VIRTUAL_ENV}/bin:${PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the repository
                script {
                    checkout scm
                }
            }
        }

        stage('Set Up Python Virtual Environment') {
            steps {
                script {
                    // Set up a Python virtual environment
                    sh 'python3 --version'
                    sh 'apt install python3.11-venv'
                    sh 'python3 -m venv ${VIRTUAL_ENV}'
                    sh 'source ${VIRTUAL_ENV}/bin/activate'
                }
            }
        }

        stage('Install Python Packages') {
            steps {
                script {
                    // Install required Python packages
                    sh 'pip install pytest behave robotframework pandas appium-python-client selenium numpy scipy Django matplotlib'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run your tests here
                    sh 'pytest'
                    // Add Robot Framework, Appium, Selenium, and other test commands as needed
                }
            }
        }
    }

    post {
        always {
            // Clean up virtual environment
            script {
                sh 'deactivate || true'
                sh 'rm -rf ${VIRTUAL_ENV}'
            }
        }
    }
}
