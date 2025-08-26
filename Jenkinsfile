pipeline{
    agent any
        stages {
            stage ("Create Selenum Grid container"){
                steps {
                    sh "docker compose -f docker-compose-selgrid.yaml up -d"
                }
            }
            stage ("Run Tests on container"){
                steps {
                    sh "docker build -t pytestsel ."
                    sh "docker run -v ./outputs:/home/Project/page_obj_proj/outputs pytestsel >> outputs/pytest.out.log"                    
                }
            }
            stage ("Stop Selenum Grid container"){
                steps {
                    sh "docker compose -f docker-compose-selgrid.yaml down"
                }
            }
        }
        post {
            always {
                archiveArtifacts artifacts: 'outputs/**', followSymlinks: false
                sh "docker system prune -af"
            }
        }
}
  