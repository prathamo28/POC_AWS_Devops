output "api_url" {
  description = "API Gateway endpoint URL"
  value       = aws_apigatewayv2_stage.default_stage.invoke_url
}

output "lambda_function_name" {
  description = "Lambda function name"
  value       = aws_lambda_function.app.function_name
}

output "cloudwatch_alarm_name" {
  description = "CloudWatch alarm name"
  value       = aws_cloudwatch_metric_alarm.lambda_errors.alarm_name
}
