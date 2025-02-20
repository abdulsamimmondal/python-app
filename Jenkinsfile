pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                git 'https://github.com/abdulsamimmondal/python-app.git'

            }

        }

        stage('Install Dependencies') {

            steps {

                sh 'pip install -r requirements.txt'

            }

        }

        stage('Run Tests') {

            steps {

                sh 'pytest tests/'

            }

        }

        stage('Build Artifact') {

            steps {

                sh 'python setup.py sdist'

            }

        }

        stage('Archive Artifact') {

            steps {

                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true

            }

        }

    }

}

