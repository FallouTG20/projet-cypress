pipeline {
  agent any

  environment {
    DOCKER_NETWORK = "projet-cypress_default"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Start Django') {
      steps {
        bat 'docker-compose up -d django'
      }
    }

    stage('Wait for Django to be ready') {
      steps {
        bat 'timeout /t 10 /nobreak'
      }
    }

    stage('Build Docker Image') {
      steps {
        bat 'docker build -t cypress-tests .'
      }
    }

    stage('Run Cypress Tests') {
      steps {
        bat 'docker run --rm --network %DOCKER_NETWORK% cypress-tests'
      }
    }
  }

  post {
    always {
      bat 'docker-compose down'
    }
  }
}
