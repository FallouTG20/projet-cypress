pipeline {
  agent any

  stages {
    stage('Start Django server') {
      steps {
        dir('djangoprojet/bonappetit/bonappetit') {
          script {
            bat 'dir'
            bat '..\\..\\myenv\\Scripts\\python.exe manage.py runserver 127.0.0.1:8000'
          }
        }
      }
    }

    stage('Run Cypress Tests') {
      steps {
        dir('.') {
          bat 'npx cypress run'
        }
      }
    }
  }
}
