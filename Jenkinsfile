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
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Setup Node Env') {
            steps {
                bat '''
                    npm install
                    npx cypress install
                    npx cypress verify
                '''
            }
        }
        stage('Start Django server') {
            steps {
                bat '''
                    call myenv\\Scripts\\activate
                    start /B python djangoprojet\\bonappetit\\bonappetit\\manage.py runserver 127.0.0.1:8000
                '''
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
        stage('Stop Django server') {
            steps {
                bat '''
                    taskkill /IM python.exe /F || exit 0
                '''
            }
        }
    }
}
