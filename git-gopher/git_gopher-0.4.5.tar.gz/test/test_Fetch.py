import unittest
from unittest.mock import MagicMock
from git_gopher.Fzf import Fzf
from git_gopher.GitDataGetter import GitDataGetter
from git_gopher.CommandRunner import CommandRunner
from git_gopher.Fetch import Fetch

class TestFetch(unittest.TestCase):

    def test_run(self):
        remote = 'foo'
        git_data_getter = GitDataGetter(Fzf())
        git_data_getter.get_remote_name = MagicMock(return_value=remote)
        command_runner = CommandRunner(git_data_getter)
        command_runner.run = MagicMock()
        fetch = Fetch(command_runner, git_data_getter)
        fetch.run()

        command_runner.run.assert_called_once_with(['git', 'fetch', remote])

if __name__ == '__main__':
    unittest.main()
