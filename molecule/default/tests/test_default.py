import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_external_socket(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening
    assert not host.socket("tcp://0.0.0.0:443").is_listening