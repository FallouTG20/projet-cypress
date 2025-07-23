pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python Env') {
            steps {
                bat '''
                    python -m venv myenv
                    call myenv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Setup Node Env') {
            steps {
                bat '''
                    npm install
                    npx cypress install
                '''
            }
        }
        stage('Start Django server') {
            steps {
                bat '''
                    call myenv\\Scripts\\activate
                    start /B python manage.py runserver 127.0.0.1:8000
                '''
                // Note : je suppose que Jenkins est dans le dossier racine où se trouve manage.py
            }
            dir('djangoprojet\\bonappetit\\bonappetit') {
                // Si nécessaire, déplace ce stage dans ce dir pour que manage.py soit trouvé
            }
        }
        stage('Run Cypress Tests') {
            steps {
                bat '''
                    call myenv\\Scripts\\activate
                    npx cypress run
                '''
            }
        }
    }
    post {
        always {
            // Arrête le serveur Django (kill python.exe)
            bat 'taskkill /IM python.exe /F || exit 0'
        }
    }
}
