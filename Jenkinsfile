pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git url:'https://github.com/KPkm25/python_pipeline.git', branch:'main'
            }
        }
        stage('Set up Virtual Environment') {
            steps {
                script {
                    // Create a virtual environment using python3
                    sh 'python3 -m venv venv'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Use bash to activate the virtual environment and install dependencies
                    sh '''
                        bash -c "source venv/bin/activate"
                        venv/bin/pip install -r requirements.txt
			venv/bin/pip install setuptools
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Use bash to activate the virtual environment and run tests with PYTHONPATH set
                    sh '''
                        bash -c "source venv/bin/activate"
                        export PYTHONPATH=$(pwd)  # Set PYTHONPATH to the current directory
                        venv/bin/pytest tests/
                    '''
                }
            }
        }
        stage('Build Artifact') {
            steps {
                script {
                    // Use bash to activate the virtual environment and build the artifact
                    sh '''
                        bash -c "source venv/bin/activate"
                        venv/bin/python setup.py sdist
                    '''
                }
            }
        }
        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }
    }
}
