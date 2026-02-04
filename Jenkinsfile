pipeline {
    agent any

    stages {

        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Virtual Env') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Build / Syntax Check') {
            steps {
                sh '''
                . venv/bin/activate
                python3 -m py_compile app.py
                '''
            }
        }

        stage('Testing Stage') {
            steps {
                sh '''
                mkdir -p test-reports
                . venv/bin/activate
                pytest test.py \
                --junitxml=test-reports/results.xml \
                --html=test-reports/report.html \
                --self-contained-html
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-reports/results.xml'
                    publishHTML(target: [
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'test-reports',
                        reportFiles: 'report.html',
                        reportName: 'Pytest HTML Report'
                    ])
                }
            }
        }
    }

    post {
        success {
            echo '✅ Python CI Pipeline completed successfully!'
        }
        failure {
            echo '❌ Python CI Pipeline failed'
        }
    }
}
