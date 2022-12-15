pipeline {
    agent { node { label 'agent1' } }
    stages {
        stage('build') {
            steps {
                sh 'python test_function.py'
            }
        }
    }
}
