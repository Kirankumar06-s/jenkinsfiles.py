pipeline{
    agent any
    stages{
        stage('Checkout'){
            steps{
                git branch: 'main', url:'https://github.com/Kirankumar06-s/jenkinsfiles.py.git'
                
            }
        }
        stage('Install Dependencies'){
            steps{
                bat 'pip install -r requirement.txt'
            }
        }
        stage('Run Unit Tests'){
            steps{
                bat 'pytest test_app.py'
            }
        }
    }
}