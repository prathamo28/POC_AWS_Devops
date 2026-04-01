import json
import time
import random


def handler(event, context):
    path = event.get("rawPath", "/")
    method = event.get("requestContext", {}).get("http", {}).get("method", "GET")

    if path == "/health":
        return _response(200, {"status": "ok", "service": "poc-devops-agent"})

    elif path == "/simulate-error":
        # Intentional error — triggers CloudWatch alarm → DevOps Agent investigation
        raise Exception("Simulated application error for DevOps Agent POC")

    elif path == "/simulate-latency":
        # Simulates slow response — useful for latency-based alarms
        delay = random.uniform(3, 6)
        time.sleep(delay)
        return _response(200, {"status": "ok", "latency_injected_seconds": round(delay, 2)})

    elif path == "/":
        return _response(200, {
            "service": "AWS DevOps Agent POC",
            "endpoints": {
                "GET /health": "Health check",
                "GET /simulate-error": "Triggers an exception (incident simulation)",
                "GET /simulate-latency": "Injects 3-6s delay (latency simulation)"
            }
        })

    return _response(404, {"error": "Route not found"})


def _response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }
