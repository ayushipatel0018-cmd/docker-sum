pipeline {
    agent any

    environment {
        CONTAINER_ID = ''
        TEST_FILE_PATH = 'test_variables.txt'
    }

    stages {

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t sum-python-image .'
            }
        }

        stage('Run') {
            steps {
                script {
                    echo 'Running Docker container...'

                    def output = bat(
                        script: '@echo off & docker run -d sum-python-image tail -f /dev/null',
                        returnStdout: true
                    )

                    // ✅ Windows-safe + Jenkins-safe
                    def lines = output.trim().split(/\r?\n/)
                    env.CONTAINER_ID = lines[-1].trim()

                    echo "Container started with ID: ${env.CONTAINER_ID}"
                }
            }
        }

        stage('Run') {
    steps {
        script {
            echo 'Running Docker container...'

            def output = bat(
                script: '''
                @echo off
                docker run -d sum-python-image
                ''',
                returnStdout: true
            ).trim()

            // Windows-safe extraction
            def lines = output.split(/\r?\n/).findAll { it.trim() }
            env.CONTAINER_ID = lines[-1].trim()

            echo "Container started with ID: ${env.CONTAINER_ID}"
        }
    }
}
    }

    post {
        always {
            script {
                if (env.CONTAINER_ID?.trim()) {
                    echo "Cleaning up container ${env.CONTAINER_ID}"
                    bat "@echo off & docker rm -f ${env.CONTAINER_ID}"
                }
            }
        }
    }
}
