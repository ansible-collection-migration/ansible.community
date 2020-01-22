import pytest

from ansible_collections.ansible.community.plugins.shell.cmd import ShellModule


@pytest.mark.parametrize('s, expected', [
    ['arg1', 'arg1'],
    [None, '""'],
    ['arg1 and 2', '^"arg1 and 2^"'],
    ['malicious argument\\"&whoami', '^"malicious argument\\^"^&whoami^"'],
    ['C:\\temp\\some ^%file% > nul', '^"C:\\temp\\some ^^^%file^% ^> nul^"']
])
def test_quote_args(s, expected):
    cmd = ShellModule()
    actual = cmd.quote(s)
    assert actual == expected
