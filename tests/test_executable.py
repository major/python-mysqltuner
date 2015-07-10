import click
from click.testing import CliRunner


from mysqltuner import executable

class TestExecutable(object):

    def test_executable(self):
        runner = CliRunner()
        result = runner.invoke(executable.run_mysqltuner, input='Hello World!\n')
        assert not result.exception
        assert result.output == 'Running MySQLTuner\n'