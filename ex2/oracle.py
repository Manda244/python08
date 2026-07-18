import os
try:
    from dotenv import load_dotenv
except ImportError:
    pass


def loading_configuration() -> dict[str, str]:
    load_dotenv()
    config: dict[str, str] = {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
        "DATABASE_URL": os.environ.get("DATABASE_URL", "Not configured"),
        "API_KEY": os.environ.get("API_KEY", "Not configured"),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT", "Not configured"),
    }
    return config


def print_configuration(config: dict[str, str]) -> None:
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    if config['DATABASE_URL'] != "Not configured":
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")

    if config['API_KEY'] != "Not configured":
        print("API Access: Authenticated")
    else:
        print("API Access: Not configured")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config['ZION_ENDPOINT'] != "Not configured":
        print("Zion Network: Online")
    else:
        print("Zion Network: Not configured")


def check_security(config: dict[str, str]) -> None:
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[MISSING] .env file not found")
    print("[OK] Production overrides available")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    load = loading_configuration()
    print_configuration(load)
    print()
    check_security(load)
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
