import javaposse.jobdsl.dsl.DslFactory

DslFactory factory = this as DslFactory

factory.multibranchPipelineJob("repository_name") {
    displayName("Repository Name")
    description("repository description")
    branchSources {
        git {
            id("repository_name")
            remote("/tmp/samples/building-a-multibranch-pipeline-project")
            credentialsId('credential-id')
            includes('test release/*')
            // excludes('')
            // excludes('test/* test2/*')
        }
    }
    if (true) {
        configure {
            it / sources / 'data' / 'jenkins.branch.BranchSource' << {
                // default strategy when sourcing from a branch
                strategy(class: "jenkins.branch.DefaultBranchPropertyStrategy") {
                    properties(class: "java.util.Arrays\$ArrayList") {
                        a(class: "jenkins.branch.BranchProperty-array") {
                            // don't trigger builds
                            "jenkins.branch.NoTriggerBranchProperty"()
                        }
                    }
                }
            }
        }
    }
    it.factory {
        workflowBranchProjectFactory {
            scriptPath("Jenkinsfile")
        }
    }
    orphanedItemStrategy {
        discardOldItems {
            daysToKeep(7)
        }
    }
    triggers {
        periodic(1440*7)
    }
}
