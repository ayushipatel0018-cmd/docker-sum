pipeline {
    agent any

    environment {
        CONTAINER_ID = ''
        SUM_PY_PATH = 'sum.py'
        DIR_PATH = '.'
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
                        script: 'docker run -d sum-python-image tail -f /dev/null',
                        returnStdout: true
                    )
                    CONTAINER_ID = output.trim()
                    echo "Container started with ID: ${CONTAINER_ID}"
                }
            }
        }

        // 👇 ADD TEST STAGE HERE
        stage('Test') {
            steps {
                script {
                    echo "Starting tests..."

                    def testLines = readFile(TEST_FILE_PATH).trim().split('\n')

                    for (line in testLines) {
                        def vars = line.trim().split(' ')
                        def arg1 = vars[0]
                        def arg2 = vars[1]
                        def expectedSum = vars[2].toFloat()

                        def output = bat(
                            script: "docker exec ${CONTAINER_ID} python /app/sum.py ${arg1} ${arg2}",
                            returnStdout: true
                        )

                        def result = output.trim().split('\n')[-1].toFloat()

                        if (result == expectedSum) {
                            echo "✅ PASS: ${arg1} + ${arg2} = ${result}"
                        } else {
                            error "❌ FAIL: ${arg1} + ${arg2} expected ${expectedSum} but got ${result}"
                        }
                    }
                }
            }
        }
    }
}
