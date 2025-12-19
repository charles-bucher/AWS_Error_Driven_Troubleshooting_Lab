"""
Intentionally break Lambda by deploying a function with too short timeout and missing log permissions.
"""
import time

def handler(event, context):
    # Sleep longer than timeout to force failure
    time.sleep(3)
    return {"ok": True}