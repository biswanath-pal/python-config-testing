from config import load_config


def main():
    config = load_config()

    print("Starting application...")
    print(f"Application: {config['app_name']}")
    print(f"Environment: {config['environment']}")
    print(f"Debug mode: {config['debug']}")


if __name__ == "__main__":
    main()
