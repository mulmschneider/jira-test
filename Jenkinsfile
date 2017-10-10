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
            timeout(time: 6) {
              sleep 12
              echo 'After Sleep'
              sh '''sleep 20
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