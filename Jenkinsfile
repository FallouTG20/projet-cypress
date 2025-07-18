pipeline {
  agent any

  stages {
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t cypress-tests .'
      }
    }

    stage('Run Cypress Tests') {
      steps {
        sh 'docker run --rm cypress-tests'
      }
    }
  }
}
