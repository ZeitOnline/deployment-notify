from .slack import Slack
import click
import json
import os
import logging


@click.group()
@click.pass_context
@click.option('--environment', required=True)
@click.option('--project')
@click.option('--version')
def cli(ctx, environment, project, version):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    ctx.ensure_object(dict)

    ctx.obj['environment'] = environment

    # https://lifecycle.keptn.sh/docs/implementing/tasks/#context
    if 'CONTEXT' in os.environ:
        keptn = json.loads(os.environ['CONTEXT'])
        ctx.obj['project'] = keptn['appName']
        ctx.obj['version'] = keptn['appVersion']

    if project:
        ctx.obj['project'] = project
    if version:
        ctx.obj['version'] = version


@cli.command()
@click.pass_context
@click.option('--channel-name', default='releases')
@click.option('--emoji')
@click.option('--vcs-url')
@click.option('--changelog-url')
def slack(ctx, channel_name, emoji, vcs_url, changelog_url):
    notify = Slack(**ctx.obj)
    notify(channel_name, os.environ['SLACK_HOOK_TOKEN'], emoji,
           vcs_url, changelog_url)
