"""Renders jinja2 template file with minimal context variables."""

# Standard library
import datetime
import logging
from pathlib import Path

# Third-party
from jinja2 import Environment
from jinja2 import FileSystemLoader


def render_namelist(jinja2_template, output_file, include_dir):
    """Render jinja2 template file with minimal context variables."""
    script_dir = Path(__file__).parent
    jinja2_template = Path(jinja2_template)
    if output_file is None:
        output_file = script_dir / "rendered/{}_rendered.nl".format(
            jinja2_template.name
        )
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    if include_dir is None:
        include_dir = script_dir
    include_dir = Path(include_dir)

    date = datetime.datetime.now()

    # Render the namelist template
    with open(str(jinja2_template), "r") as f:
        f_str = f.read()
        env = Environment(loader=FileSystemLoader(str(include_dir)))
        template = env.from_string(f_str)
        rtemplate = template.render(date=date)

    # Store rendered namelist
    with open(output_file, "w") as of:
        of.write(rtemplate)
    logger.info(f"Successfully rendered {jinja2_template} to {output_file}")
    return output_file
