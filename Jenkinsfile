pipeline {
    agent any

    environment {
        CONTAINER_ID = ""
        SUM_PY_PATH = "${WORKSPACE}/sum.py"
        DIR_PATH = "${WORKSPACE}"
        TEST_FILE_PATH = "${WORKSPACE}/test_variables.txt"
        IMAGE_NAME = "sum-python-image"
    }

    stages {
        stage('Build') {
            steps {
                echo "Building Docker image..."
                bat "docker build -t %IMAGE_NAME% %DIR_PATH%"
            }
        }

        stage('Run') {
            steps {
                echo "Running Docker container..."
                script {
                    // Run container in detached mode and capture output
                    def output = bat(
                        script: "docker run -d %IMAGE_NAME% tail -f /dev/null",
                        returnStdout: true
                    )
                    def lines = output.split('\n')
                    // Last line should contain container ID
                    CONTAINER_ID = lines[-1].trim()
                    echo "Container started with ID: ${CONTAINER_ID}"
                }
            }
        }
    }
}
