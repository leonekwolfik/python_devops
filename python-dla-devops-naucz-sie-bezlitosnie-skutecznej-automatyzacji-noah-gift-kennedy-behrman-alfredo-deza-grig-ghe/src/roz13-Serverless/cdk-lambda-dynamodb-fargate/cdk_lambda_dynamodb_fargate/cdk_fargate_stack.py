from aws_cdk import core
from aws_cdk import aws_ecs, aws_ec2

class FargateStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = aws_ec2.Vpc(
            self, "MyVpc",
            cidr= "10.0.0.0/16",
            max_azs=3
        )
        # definicja klastra ECS hostowanego wewnątrz żądanego VPC
        cluster = aws_ecs.Cluster(self, 'cluster', vpc=vpc)

        # definicja zadania w pojedynczymm kontenerze
        # obraz jest zbudowany i opublikowany z lokalnego katalogu
        task_definition = aws_ecs.FargateTaskDefinition(self, 'LoadTestTask')
        task_definition.add_container('LocustLoadTest',
            image=aws_ecs.ContainerImage.from_asset("loadtest"),
            environment={'BASE_URL': "https://r212bfnymj.execute-api.us-east-2.amazonaws.com/prod/"})

        # definicja usługi fargate. TPS określa liczbę egzemplarzy, które oczekujemy 
        # od naszego zadania (każde zadanie tworzy pojedynczy TPS)
        aws_ecs.FargateService(self, 'service',
            cluster=cluster,
            task_definition=task_definition,
            desired_count=5)

