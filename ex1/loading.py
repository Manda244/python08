import importlib.util
from importlib.metadata import version, PackageNotFoundError
from typing import Optional
try:
    import numpy as np
    import pandas as pd
except ImportError:
    pass


def check_dependencies(package_name: str) -> Optional[str]:
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        return None
    else:
        try:
            return version(package_name)
        except PackageNotFoundError:
            return None


def print_dependency_status(dependencies: dict[str, str]) -> dict[str, bool]:
    print("Checking dependencies:")
    status: dict[str, bool] = {}
    for name, message in dependencies.items():
        resultat = check_dependencies(name)
        if resultat is None:
            print(f"[MISSING] {name} - not {message}")
            status[name] = False
        else:
            print(f"[OK] {name} ({resultat}) - {message}")
            status[name] = True
    return status


def print_installation_instruction(missing: list[str]) -> None:
    print("Missing dependencies detected!")
    print()
    print("Install with pip:")
    print(" pip install -r requirements.txt")
    print()
    print("Or Install with poetry:")
    print(" poetry install")


def simulate_matrix_data(n_points: int = 1000) -> "np.ndarray":
    if "np" not in globals():
        return None
    data = np.random.randn(n_points)
    return data


def analyze_data(data: "np.ndarray") -> "pd.DataFrame":
    if "pd" not in globals():
        return None
    print(f"Processing {len(data)} data points...")
    df = pd.DataFrame({"value": data})
    df.describe()
    return df


def visualize_data(
    df: "pd.DataFrame",
    output_path: str = "matrix_analysis.png"
) -> None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        plt.figure()
        plt.hist(df["value"], bins=30)
        plt.title("matrix_analysis")
        plt.xlabel("___")
        plt.ylabel("___")
        plt.savefig(output_path)
        plt.close()
    except ImportError:
        pass


def main() -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    deps = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
    }
    status = print_dependency_status(deps)
    missing = [name for name, ok in status.items() if not ok]
    if missing:
        print()
        print_installation_instruction(missing)
    print()
    print("Analyzing Matrix data...")
    data = simulate_matrix_data(1000)
    df = analyze_data(data)
    visualize_data(df)
    print("Generating visualization...")
    print()
    print("Analysis complete!")
    if missing:
        print("Results not saved to: matrix_analysis.png")
    else:
        print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
