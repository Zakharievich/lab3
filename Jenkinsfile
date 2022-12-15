pipeline {
    agent { node { label 'agent1' } }
    stages {
        stage('build') {
            steps {
                bat 'python test_function.py'
            }
        }
    }
}
