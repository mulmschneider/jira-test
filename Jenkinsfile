pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Hello World'
        sh 'echo "BLUB" >  build.tar'
      }
    }
    stage('Test') {
      steps {
        parallel(
          "Test": {
            echo 'Testing....'
            
          },
          "Parallel Test": {
            timeout(time: 10, unit: 'SECONDS') {
              sleep 3
              echo 'After Sleep'
              sh '''sleep 3
echo "asdf"'''
            }
            
            echo 'FIN'
            
          }
        )
      }
    }
    stage('Deploy') {
      steps {
        archiveArtifacts 'build.tar'
      }
    }
  }
}
