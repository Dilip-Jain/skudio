"""Console entry point: ``python -m skudio``."""

from skudio.cli import main

if __name__ == "__main__":
    # `main` is a click.Command; click injects arguments from sys.argv.
    main() # pylint: disable=no-value-for-parameter
