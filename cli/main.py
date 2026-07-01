import click
import os
from src.referee.core import AIReferee

@click.group()
def cli():
    """AI Referee Command Line Interface."""
    pass

@cli.command()
@click.argument('path', type=click.Path(exists=True))
def audit(path):
    """Run an automated audit on a file for Code Health and Security."""
    click.echo(f"Running referee audit on: {path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    referee = AIReferee()
    
    if str(path).endswith(".html"):
        result = referee.evaluate_accessibility(content)
    else:
        result = referee.evaluate_code_health(content)
        
    click.echo(f"Score:  {result['score']}")
    click.echo(f"Status: {result['status'].upper()}")
    for fb in result['feedback']:
        click.echo(f" - {fb}")

if __name__ == '__main__':
    cli()
