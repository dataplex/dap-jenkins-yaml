#!/usr/bin/env groovy

pipeline {
  agent any

  stages {

    stage('Generate Root Policy') {
      steps {
        sh '''
          mkdir -p output
          cp ./policy/root.yml ./output/root.yml
          if [ "$(ls -1 ./snow/*.yml | wc -l)" != "0" ];then
            for i in $(ls -1 ./snow/*.yml); do
              echo "Adding file $i"
              cat ./snow/$i >> ./output/root.yml
            done
          fi
        '''
      }
    }

    stage('Load Root Policy') {
      steps {
        withCredentials([usernameColonPassword(credentialsId: 'DAP_Admin', variable: 'DAP_ADMIN')]) {
          sh '''
            ./policyload.sh master.dpxlab.net dev "$DAP_ADMIN" root ./output/root.yml ./output/policy-load.out
          '''
        }
      }
    }

    stage('Onboard New Accounts') {
      steps {
        withCredentials([string(credentialsId: 'CCP_Info', variable: 'CCP_Info')]) {
          sh '''
            ./onboard_hosts_to_pas.sh master.dpxlab.net "$CCP_Info" "pvwa.dpxlab.net" ./output/policy-load.out
          '''
        }
      }
    }

  }

  post {
    always {
      archiveArtifacts artifacts: 'output/*', fingerprint: true
    }
  }
}
