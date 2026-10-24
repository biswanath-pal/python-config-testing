import os

from dotenv import load_dotenv

load_dotenv()

def load_config():
    app_name = os.getenv(
        "APP_NAME", "Task Management Service"
    ).strip()

    environment = os.getenv(
        "APP_ENV", "development"
    ).strip().lower()

    debug_value = os.getenv(
        "APP_DEBUG", "false"
    ).strip().lower()

    allowed_environments = {
        "development", "testing", "production"
    }

    if not app_name:
        raise ValueError("APP_NAME cannot be empty")
    if environment not in allowed_environments:
        raise ValueError(f"Invalid APP_ENV: {environment}")
    if debug_value not in {
        "true", "false", "1", "0", "yes", "no"
    }:
        raise ValueError("APP_DEBUG must be a valid Boolean value")
    debug = debug_value in {"true", "1", "yes"}
    if environment == "production" and debug:
        raise ValueError("Debug mode must be disabled in production")
    return {
        "app_name": app_name,
        "environment": environment,
        "debug": debug,
    }