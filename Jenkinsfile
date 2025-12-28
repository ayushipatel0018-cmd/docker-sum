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

                    // Run container in detached mode and capture its ID
                    def output = bat(
                        script: 'cmd /c docker run -d sum-python-image',
                        returnStdout: true
                    ).trim()

                    env.CONTAINER_ID = output
                    echo "Container started with ID: ${env.CONTAINER_ID}"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Starting tests...'

                    def testLines = readFile(TEST_FILE_PATH).trim().split('\\r?\\n')

                    for (line in testLines) {
                        def vars = line.trim().split(' ')
                        def arg1 = vars[0]
                        def arg2 = vars[1]
                        def expectedSum = vars[2].toFloat()

                        // Execute sum.py inside the running container
                        def output = bat(
                            script: "cmd /c docker exec ${env.CONTAINER_ID} python /app/sum.py ${arg1} ${arg2}",
                            returnStdout: true
                        ).trim()

                        def result = output.split('\\r?\\n')[-1].toFloat()

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

    post {
        always {
            script {
                if (env.CONTAINER_ID?.trim()) {
                    echo "Cleaning up container ${env.CONTAINER_ID}"
                    bat "cmd /c docker rm -f ${env.CONTAINER_ID}"
                }
            }
        }
    }
}
