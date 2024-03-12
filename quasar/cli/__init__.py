import click
# from quasar.algorithm import MainDetector

from quasar._version import __version__ as _version
from quasar.utils import ASCII_ART
from quasar.utils import analyse
from quasar.algorithm.detector import MainDetector, detect_smell


class ASCIICommandClass(click.Group):
    def get_help(self, ctx):
        return ASCII_ART + '\n' + super().get_help(ctx)


@click.group(name='cli', cls=ASCIICommandClass)
@click.version_option(_version, prog_name='Quasar')
@click.help_option('-h', '--help')
def cli() -> None:
    pass


@cli.command(name='detect', help='Detect code smells')
@click.option('--path', '-p')
@click.option('--format', '-f',
              type=click.Choice(['json']))
@click.option('--solution', '-s', is_flag=True, help='Provide solutions for detected code smells')
def detect(path, format, solution) -> None:
    """
    Detects the specified type of object in the given path and formats the output.

    Args:
        type (str): The type of object to detect.
        path (str): The path to the file or directory to be analyzed.
        format (str): The desired output format ('json' or 'xml').
        solution (bool): Whether to provide solutions for the detected code smells.

    Raises:
        ValueError('Path is required'): If the path is not provided.

    Returns:
        None
    """

    if solution:
        raise NotImplementedError('Solution flag not implemented yet')
    else:
        try:
            if path:
                data_json = analyse([path])
                if format == 'json':
                    # Here we are using the detect_smell function to detect the smell in the combined_json
                    try:
                        detector = MainDetector()
                        print(detect_smell(data_json, detector))
                    except Exception as e:
                        raise e
                    click.echo(data_json)

                else:
                    NotImplementedError('Other format not implemented yet')
            else:
                raise ValueError('Path is required')
        except Exception as e:
            raise e


if __name__ == '__main__':
    cli()
