#!/usr/bin/env python3

import click
import os
import requests


API_TOKEN = os.environ['CLICKUP_API_TOKEN']
API_VERSION = 'v2'

URL_PREFIX = f'https://api.clickup.com/api/{API_VERSION}/'


@click.group()
@click.pass_context
def cli():
    """CLI tool for interacting with clickup"""
    return None


@cli.command()
def config():
    """Initialize config"""
    # todo
    return None


# todo impl detail
# todo impl --show-archived
# todo human readable format
@cli.command()
@click.option('--detail', '-d', default=False, help='show detail')
def teams(detail):
    """Get teams"""
    ret = requests.get(URL_PREFIX + f"/team", headers={'Authorization': API_TOKEN})
    print(ret.text)


@cli.command()
@click.argument("team_id")
@click.option('--detail', '-d', default=False, help='show detail')
@click.option('--show_archived', default=False, help='show archived')
def spaces(team_id, detail, show_archived):
    """Get team's spaces"""
    ret = requests.get(URL_PREFIX + f"team/{team_id}/list?archived={show_archived}",
                       headers={'Authorization': API_TOKEN})
    print(ret.text)


@cli.command()
@click.argument("space_id")
@click.option('--detail', '-d', default=False, help='show detail')
@click.option('--show_archived', default=False, help='show archived')
def folders(space_id, detail, show_archived):
    """Get space's folders"""
    ret = requests.get(URL_PREFIX + f"space/{space_id}/list?archived={show_archived}",
                       headers={'Authorization': API_TOKEN})
    print(ret.text)


@cli.command()
@click.argument('folder_id')
@click.option('--detail', '-d', default=False, help='show detail')
@click.option('--show_archived', default=False, help='show archived')
def lists(folder_id, detail, show_archived):
    """Get folder's Lists"""
    ret = requests.get(URL_PREFIX + f"folder/{folder_id}/list?archived={show_archived}",
                       headers={'Authorization': API_TOKEN})
    print(ret.text)


if __name__ == "__main__":
    cli()
