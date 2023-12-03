pipeline {
    agent any
 
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the repository
                script {
                    checkout scm
                }
            }
        }
        
        stage('Run Python Code') {
            steps {
                // Run Python code
                script {
                    sh 'pytest'
                }
            }
        }
    }
    
    post {
        success {
            echo 'Python code execution successful!'
        }
        failure {
            echo 'Failed to run Python code!'
        }
    }
}
