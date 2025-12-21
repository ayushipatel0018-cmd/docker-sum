pipeline {
    agent any  // Use any available Jenkins agent

    environment {
        CONTAINER_ID = ""
        SUM_PY_PATH = "${WORKSPACE}/sum.py"
        DIR_PATH = "${WORKSPACE}"
        TEST_FILE_PATH = "${WORKSPACE}/test_variables.txt"
    }

    stages {
        stage('Example') {
            steps {
                echo "Agent and environment variables defined."
            }
        }
    }
}
