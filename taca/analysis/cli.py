""" CLI for the analysis subcommand
"""
import click
from taca.analysis import analysis as an


@click.group()
def analysis():
	""" Analysis methods entry point """
	pass

# analysis subcommands
@analysis.command()
@click.option('-r', '--run', type=click.Path(exists=True), default=None,
				 help='Demultiplex only a particular run')
@click.option('--force', is_flag=True, help='If specified tranfers always the runs, despite they fail QC. Mail is sent anyway' )

def demultiplex(run, force):
	""" Demultiplex all runs present in the data directories
	"""
	an.run_preprocessing(run, force_trasfer=force)

@analysis.command()
@click.option('-a','--analysis', is_flag=False, help='Trigger the analysis for the transferred flowcell')
@click.option('--runfolder', is_flag=False, help='Project ID for runfolder transfer')
@click.argument('rundir')

def transfer(rundir, analysis, runfolder):
    """Transfers the run without qc"""
    if not runfolder:
            an.transfer_run(rundir, analysis=analysis)
    else:
            an.transfer_runfolder(rundir, pid=runfolder)
@analysis.command()
@click.argument('rundir')
def updatedb(rundir):
    """saves the run to statusdb"""
    an.upload_to_statusdb(rundir)
