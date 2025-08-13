pipeline {
  agent any
  options { timestamps() }
  environment {
    IMAGE = 'sirvin703/product-service'
    VERSION = "0.1.${env.BUILD_NUMBER}"
    DOCKER_BUILDKIT = '1'
  }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Docker Login') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub',
                                          usernameVariable: 'DOCKERHUB_USER',
                                          passwordVariable: 'DOCKERHUB_PASS')]) {
          sh 'echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin'
        }
      }
    }
    stage('Build') { steps { sh 'docker build -t $IMAGE:$VERSION -t $IMAGE:latest .' } }
    stage('Push')  { steps { sh 'docker push $IMAGE:$VERSION && docker push $IMAGE:latest' } }

    // ----- Placeholder environment stages for the screenshot deliverable -----
    stage('Dev')     { steps { sh 'echo "Deploy to Dev (placeholder)"' } }
    stage('Staging') { steps { sh 'echo "Deploy to Staging (placeholder)"' } }
    stage('Prod')    { steps { sh 'echo "Deploy to Prod (placeholder)"' } }
  }
  post { always { sh 'docker logout || true' } }
}
