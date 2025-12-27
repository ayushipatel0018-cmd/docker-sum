pipeline {
    agent any

    environment {
        CONTAINER_ID = ''
        TEST_FILE_PATH = 'test_variables.txt'
        DOCKER_HOST = 'tcp://127.0.0.1:2375'
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
                        script: '''
                        @echo off
                        docker run -d sum-python-image
                        ''',
                        returnStdout: true
                    ).trim()

                    def lines = output.split(/\r?\n/).findAll { it.trim() }
                    env.CONTAINER_ID = lines[-1].trim()

                    echo "Container started with ID: ${env.CONTAINER_ID}"
                }
            }
        }

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
                            script: "@echo off & docker exec ${env.CONTAINER_ID} python /app/sum.py ${arg1} ${arg2}",
                            returnStdout: true
                        )

                        def result = output.trim().split(/\r?\n/)[-1].toFloat()

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
                    bat "@echo off & docker rm -f ${env.CONTAINER_ID}"
                }
            }
        }
    }
}
