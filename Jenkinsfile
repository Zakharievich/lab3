pipeline {
    agent { node { label 'agent1' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install pytest'
                sh 'pytest test_function.py'
                sh 'pytest --cov=./'
            }
        }
    }
}
