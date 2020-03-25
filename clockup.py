#!/usr/bin/env python3

import click
import os
from clockup.client import Client


API_TOKEN = os.environ['CLICKUP_API_TOKEN']
API_VERSION = 'v2'

URL_PREFIX = f'https://api.clickup.com/api/{API_VERSION}/'


@click.group()
@click.pass_context
def cli(ctx):
    """CLI tool for interacting with clickup"""
    ctx.obj = Client(API_TOKEN, API_VERSION)

    return None


@cli.command()
def config():
    """Initialize config"""
    # todo
    return None


# todo impl detail
# todo human readable format
@cli.command()
@click.option('--detail', '-d', default=False, help='show detail')
@click.pass_context
def teams(ctx, detail):
    """Get teams"""
    ret = ctx.obj.get_teams()
    print(ret)


@cli.command()
@click.argument("team_id")
@click.option('--detail', '-d', default=False, help='show detail')
@click.option('--show_archived', default=False, help='show archived')
@click.pass_context
def spaces(ctx, team_id, detail, show_archived):
    """Get team's spaces"""
    ret = ctx.obj.get_spaces(team_id, show_archived)
    print(ret)


@cli.command()
@click.argument("space_id")
@click.option('--detail', '-d', default=False, help='show detail')
@click.option('--show_archived', default=False, help='show archived')
@click.pass_context
def folders(ctx, space_id, detail, show_archived):
    """Get space's folders"""
    ret = ctx.obj.get_folders(space_id, show_archived)
    print(ret)


@cli.command()
@click.argument('folder_id')
@click.option('--detail', '-d', default=False, help='show detail')
@click.option('--show_archived', default=False, help='show archived')
@click.pass_context
def lists(ctx, folder_id, detail, show_archived):
    """Get folder's Lists"""
    ret = ctx.obj.get_lists(folder_id, show_archived)
    print(ret)


if __name__ == "__main__":
    cli()
