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
            timeout(time: 11) {
              sleep 12
            }
            
            
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