"""Command line interface of nl_rendering."""
# Standard library
import logging

# Third-party
import click

# Local
from . import __version__
from .nl_rendering import render_namelist
from .utils import count_to_log_level


@click.command()
@click.option(
    "--dry-run",
    "-n",
    flag_value="dry_run",
    default=False,
    help="Perform a trial run with no changes made",
)
@click.option(
    "--verbose",
    "-v",
    count=True,
    help="Increase verbosity (specify multiple times for more)",
)
@click.option(
    "--version",
    "-V",
    is_flag=True,
    help="Print version",
)
@click.argument("jinja2_template", type=click.Path(exists=True))
@click.option("--output-file", type=str, default=None, help="Location of output file")
@click.option(
    "--include-dir",
    type=str,
    default=None,
    help="Set directory from where subtemplates can be loaded",
)
def main(*, dry_run: bool, verbose: int, version: bool) -> None:
    logging.basicConfig(level=count_to_log_level(verbose))

    if version:
        click.echo(__version__)
        return

    if dry_run:
        click.echo("Is dry run")
        return

    render_namelist(jinja2_template, output_file, include_dir)
