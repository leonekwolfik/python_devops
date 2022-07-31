from aws_cdk import core
from aws_cdk.core import App, Construct, Duration
from aws_cdk import aws_dynamodb, aws_lambda, aws_apigateway

class CdkLambdaDynamodbStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # definicja tabeli do przechowywania elementów Todo
        table = aws_dynamodb.Table(self, "Table",
            partition_key=aws_dynamodb.Attribute(
                name="id",
                type=aws_dynamodb.AttributeType.STRING),
            billing_mode = aws_dynamodb.BillingMode.PAY_PER_REQUEST)
#            read_capacity=10,
#            write_capacity=5)

        # definicja funkcji Lambda
        list_handler = aws_lambda.Function(self, "TodoListFunction",
            code=aws_lambda.Code.asset("./lambda"),
            handler="list.list",
            timeout=Duration.minutes(5),
            runtime=aws_lambda.Runtime.PYTHON_3_7)

        create_handler = aws_lambda.Function(self, "TodoCreateFunction",
            code=aws_lambda.Code.asset("./lambda"),
            handler="create.create",
            timeout=Duration.minutes(5),
            runtime=aws_lambda.Runtime.PYTHON_3_7)
        
        get_handler = aws_lambda.Function(self, "TodoGetFunction",
            code=aws_lambda.Code.asset("./lambda"),
            handler="get.get",
            timeout=Duration.minutes(5),
            runtime=aws_lambda.Runtime.PYTHON_3_7)
        
        update_handler = aws_lambda.Function(self, "TodoUpdateFunction",
            code=aws_lambda.Code.asset("./lambda"),
            handler="update.update",
            timeout=Duration.minutes(5),
            runtime=aws_lambda.Runtime.PYTHON_3_7)
        
        delete_handler = aws_lambda.Function(self, "TodoDeleteFunction",
            code=aws_lambda.Code.asset("./lambda"),
            handler="delete.delete",
            timeout=Duration.minutes(5),
            runtime=aws_lambda.Runtime.PYTHON_3_7)

        # przekazanie nazwy tabeli do każdego handlera za pomocą zmiennej środowiskowej
        # i udzielenie handlerowi uprawnień do odczytu(zapisu) dla tej tabeli.
        handler_list = [
            list_handler, 
            create_handler, 
            get_handler, 
            update_handler, 
            delete_handler
        ]
        for handler in handler_list:
            handler.add_environment('DYNAMODB_TABLE', table.table_name)
            table.grant_read_write_data(handler)

        # define the API endpoint
        api = aws_apigateway.LambdaRestApi(self, "TodoApi",
            handler=list_handler,
            proxy=False)
        
        # definicja integracjj Lambda
        list_lambda_integration = \
            aws_apigateway.LambdaIntegration(list_handler)
        create_lambda_integration = \
            aws_apigateway.LambdaIntegration(create_handler)
        get_lambda_integration = \
            aws_apigateway.LambdaIntegration(get_handler)
        update_lambda_integration = \
            aws_apigateway.LambdaIntegration(update_handler)
        delete_lambda_integration = \
            aws_apigateway.LambdaIntegration(delete_handler)
        
        # definicja modelu API REST i powiązanie metod z integracjami Lambda
        api.root.add_method('ANY')
        todos = api.root.add_resource('todos')
        todos.add_method('GET', list_lambda_integration);    #GET /todos
        todos.add_method('POST', create_lambda_integration); #POST /todos

        todo = todos.add_resource('{id}')
        todo.add_method('GET', get_lambda_integration);      #GET /todos/{id}
        todo.add_method('PUT', update_lambda_integration);   #PUT /todos/{id}
        todo.add_method('DELETE', delete_lambda_integration);#DELETE /todos/{id}

