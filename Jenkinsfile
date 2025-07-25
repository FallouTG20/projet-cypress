pipeline {
  agent any

  environment {
    RESULTS_DIR = "${WORKSPACE}\\results"
  }

  stages {
    stage('Build Docker Image') {
      steps {
        script {
          echo "🛠️ Construction de l'image Docker"
          docker.build('cypress-tests')
        }
      }
    }

    stage('Run Cypress Tests') {
      steps {
        script {
          echo "🚀 Lancement des tests Cypress avec rapport JUnit"

          // S'assurer que le dossier results existe côté hôte
          bat "mkdir ${RESULTS_DIR}"

          // Exécuter le conteneur avec montage du dossier results
          bat """
            docker run --rm ^
              -v "${RESULTS_DIR}:/e2e/results" ^
              cypress-tests npx cypress run --reporter junit --reporter-options mochaFile=results/results-[hash].xml,toConsole=true
          """
        }
      }
    }
  }

  post {
    always {
      echo "📄 Récupération des rapports JUnit"
      junit 'results/*.xml'
    }
  }
}
