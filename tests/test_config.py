import pytest

from config import load_config


@pytest.mark.parametrize(
        "value, expected",
        [
            ("true", True),
            ("1", True),
            ("yes", True),
            ("false", False),
            ("0", False),
            ("no", False),
        ],
)
def test_debug_boolean_value(monkeypatch, value, expected):
    monkeypatch.setenv("APP_DEBUG", value)
    monkeypatch.setenv("APP_ENV", "development")
    config = load_config()
    assert config["debug"] is expected

@pytest.mark.parametrize(
        "value, expected",
        [
            ("TRUE", True),
            ("YES", True),
            ("FALSE", False),
            ("NO", False),
            ("True", True),
            ("False", False),
        ],
)    
def test_debug_boolean_case_and_spaces(
    monkeypatch, value, expected
):
    monkeypatch.setenv("APP_DEBUG", value)
    monkeypatch.setenv("APP_ENV", "development")
    config = load_config()
    assert config["debug"] is expected
    
def test_load_config_defaults(monkeypatch):
    monkeypatch.delenv("APP_NAME", raising=False)
    monkeypatch.delenv("APP_ENV", raising=False)
    monkeypatch.delenv("APP_DEBUG", raising=False)

    config = load_config()
    assert config["app_name"] == "Task Management Service"
    assert config["environment"] == "development"
    assert config["debug"] is False

def test_rejects_empty_app_name(monkeypatch):
    monkeypatch.setenv("APP_NAME", "")
    with pytest.raises(ValueError, match="APP_NAME cannot be empty"):
        load_config()

def test_rejects_invalid_environment(monkeypatch):
    monkeypatch.setenv("APP_ENV", "invalid")
    with pytest.raises(ValueError, match="Invalid APP_ENV"):
        load_config()

def test_rejects_invalid_debug_value(monkeypatch):
    monkeypatch.setenv("APP_DEBUG", "maybe")
    with pytest.raises(ValueError, match="APP_DEBUG"):
        load_config()

def test_rejects_debug_in_production(monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    monkeypatch.setenv("APP_DEBUG", "true")
    with pytest.raises(ValueError, match="Debug mode must be disabled"):
        load_config()        