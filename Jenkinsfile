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
          // Sur Windows, utilise bat au lieu de sh
          bat 'docker run --rm -v "%cd%/results:C:/e2e/results" cypress-tests npx cypress run --reporter junit --reporter-options mochaFile=results/results-[hash].xml,toConsole=true'
        }
      }
      post {
        always {
          // Jenkins lit les rapports JUnit générés dans results/
          junit 'results/*.xml'
          archiveArtifacts 'results/*.xml'
        }
      }
    }
  }
}
