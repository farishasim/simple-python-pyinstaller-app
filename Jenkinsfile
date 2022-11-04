node {
    docker.image('python:2-alpine').inside {
        stage('Build') {
            sh 'python -m py_compile sources/add2vals.py sources/calc.py'
        }
    }
    docker.image('qnib/pytest').inside {
        stage('Test') {
            sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
        }
    }
    docker.image('python:3-alpine').inside {
        stage('Deploy') {
            sh 'ls sources'
            sh 'python -m flask --app sources/app.py run'
            sleep 1m
        }
    }
}
