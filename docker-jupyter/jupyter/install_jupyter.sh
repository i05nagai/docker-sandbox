#/bin/bash

# TODO: Attach Header
# TODO: Extract Method

# path to s3 base

applications="Name=Hadoop Name=Spark Name=Ganglia"
ec2_attributions=$(cat << EOS
{
  "KeyName": "key_name",
  "InstanceProfile": "EMR_EC2_DefaultRole",
  "SubnetId": "subnet-",
  "EmrManagedSlaveSecurityGroup": "sg-",
  "EmrManagedMasterSecurityGroup": "sg-"
}
EOS
)
release_label="emr-5.7.0"
log_url="s3n://aws-logs-......-ap-northeast-1/elasticmapreduce/"
instance_groups=$(cat << EOS
[
  {
    "InstanceCount": 2,
    "EbsConfiguration": {
      "EbsBlockDeviceConfigs": [
        {
          "VolumeSpecification": {
            "SizeInGB": 32,
            "VolumeType": "gp2"
          },
          "VolumesPerInstance": 1
        }
      ],
      "EbsOptimized": true
    },
    "InstanceGroupType": "CORE",
    "InstanceType": "c4.2xlarge",
    "Name": "Core"
  },
  {
    "InstanceCount": 1,
    "InstanceGroupType": "MASTER",
    "InstanceType": "m3.xlarge",
    "Name": "Master"
  }
]
EOS
)
configurations=$(cat << EOS
[
  {
    "Classification": "spark-env",
    "Properties": {},
    "Configurations": [
      {
        "Classification": "export",
        "Properties": {
          "PYSPARK_PYTHON": "python34"
        },
        "Configurations": []
      }
    ]
  }
]
EOS
)
bootstrap_actions=$(cat << EOS
[
  {
    "Name": "Install jupyter notebook",
    "Path": "s3://aws-bigdata-blog/artifacts/aws-blog-emr-jupyter/install-jupyter-emr5.sh",
    "Args": [
      "--toree",
      "--torch",
      "--ds-packages",
      "--ml-packages",
      "--python-packages",
      "'ggplot nilearn'",
      "--port",
      "8880",
      "--password",
      "jupyter",
      "--jupyterhub",
      "--jupyterhub-port",
      "8001",
      "--cached-install",
      "--notebook-dir",
      "s3://path/to/jupyter/",
      "--copy-samples"
      ]
  }
]
EOS
)
auto_scaling_role="EMR_AutoScaling_DefaultRole"
service_role="EMR_DefaultRole"
name="cluster_name"
scale_down_behavior="TERMINATE_AT_TASK_COMPLETION"
region="ap-northeast-1"

create_cluster=`aws emr create-cluster \
  --applications ${applications} \
  --ec2-attributes "${ec2_attributions}" \
  --release-label "${release_label}" \
  --log-uri "${log_url}" \
  --instance-groups "${instance_groups}" \
  --configurations "${configurations}" \
  --auto-scaling-role "${auto_scaling_role}" \
  --bootstrap-actions "${bootstrap_actions}" \
  --service-role "${service_role}" \
  --enable-debugging \
  --name "${name}" \
  --scale-down-behavior "${scale_down_behavior}" \
  --region "${region}"`

cluster_id=`echo $create_cluster | jq -r '.ClusterId'`
aws emr add-tags \
  --resource-id ${cluster_id} \
  --tags Name="${name}"
echo $cluster_id

