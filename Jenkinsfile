pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git url:'https://github.com/abdulsamimmondal/python-app.git',branch:'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Create and activate virtual environment, then install dependencies
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest in the virtual environment
                sh '. venv/bin/activate && pytest tests/'
            }
        }

        stage('Build Artifact') {
            steps {
                // Build the artifact in the virtual environment
                sh '. venv/bin/activate && python setup.py sdist'
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }

    }
}
