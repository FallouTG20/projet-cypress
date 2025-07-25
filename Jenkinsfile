pipeline {
  agent any

  stages {
    stage('Build Docker Image') {
      steps {
        script {
          docker.build('cypress-tests')
        }
      }
    }

    stage('Run Cypress Tests') {
      steps {
        script {
          // ⚠️ Sur Windows, évite `inside {}` ➜ utilise `run()` directement
          docker.image('cypress-tests').run()
        }
      }
    }
  }
}
