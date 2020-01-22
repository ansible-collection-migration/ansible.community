# This code is part of Ansible, but is an independent component.
# This particular file snippet, and this file snippet only, is BSD licensed.
# Modules you write using this snippet, which is embedded dynamically by Ansible
# still belong to the author of the module, and may assign their own license
# to the complete work.
#
# (c) 2017 Red Hat Inc.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible_collections.ansible.community.plugins.module_utils.facts.other.facter import FacterFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.other.ohai import OhaiFactCollector

from ansible_collections.ansible.community.plugins.module_utils.facts.system.apparmor import ApparmorFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.caps import SystemCapabilitiesFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.chroot import ChrootFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.cmdline import CmdLineFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.distribution import DistributionFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.date_time import DateTimeFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.env import EnvFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.dns import DnsFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.fips import FipsFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.local import LocalFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.lsb import LSBFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.pkg_mgr import OpenBSDPkgMgrFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.platform import PlatformFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.python import PythonFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.selinux import SelinuxFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.service_mgr import ServiceMgrFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.ssh_pub_keys import SshPubKeyFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.system.user import UserFactCollector

from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.base import HardwareCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.aix import AIXHardwareCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.darwin import DarwinHardwareCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.dragonfly import DragonFlyHardwareCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.freebsd import FreeBSDHardwareCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.hpux import HPUXHardwareCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.hurd import HurdHardwareCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.linux import LinuxHardwareCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.netbsd import NetBSDHardwareCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.openbsd import OpenBSDHardwareCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.hardware.sunos import SunOSHardwareCollector

from ansible_collections.ansible.community.plugins.module_utils.facts.network.base import NetworkCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.network.aix import AIXNetworkCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.network.darwin import DarwinNetworkCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.network.dragonfly import DragonFlyNetworkCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.network.fc_wwn import FcWwnInitiatorFactCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.network.freebsd import FreeBSDNetworkCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.network.hpux import HPUXNetworkCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.network.hurd import HurdNetworkCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.network.linux import LinuxNetworkCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.network.iscsi import IscsiInitiatorNetworkCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.network.nvme import NvmeInitiatorNetworkCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.network.netbsd import NetBSDNetworkCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.network.openbsd import OpenBSDNetworkCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.network.sunos import SunOSNetworkCollector

from ansible_collections.ansible.community.plugins.module_utils.facts.virtual.base import VirtualCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.virtual.dragonfly import DragonFlyVirtualCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.virtual.hpux import HPUXVirtualCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.virtual.linux import LinuxVirtualCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.virtual.netbsd import NetBSDVirtualCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.virtual.openbsd import OpenBSDVirtualCollector
from ansible_collections.ansible.community.plugins.module_utils.facts.virtual.sunos import SunOSVirtualCollector

# these should always be first due to most other facts depending on them
_base = [
    PlatformFactCollector,
    DistributionFactCollector,
    LSBFactCollector
]

# These restrict what is possible in others
_restrictive = [
    SelinuxFactCollector,
    ApparmorFactCollector,
    ChrootFactCollector,
    FipsFactCollector
]

# general info, not required but probably useful for other facts
_general = [
    PythonFactCollector,
    SystemCapabilitiesFactCollector,
    PkgMgrFactCollector,
    OpenBSDPkgMgrFactCollector,
    ServiceMgrFactCollector,
    CmdLineFactCollector,
    DateTimeFactCollector,
    EnvFactCollector,
    SshPubKeyFactCollector,
    UserFactCollector
]

# virtual, this might also limit hardware/networking
_virtual = [
    VirtualCollector,
    DragonFlyVirtualCollector,
    FreeBSDVirtualCollector,
    LinuxVirtualCollector,
    OpenBSDVirtualCollector,
    NetBSDVirtualCollector,
    SunOSVirtualCollector,
    HPUXVirtualCollector
]

_hardware = [
    HardwareCollector,
    AIXHardwareCollector,
    DarwinHardwareCollector,
    DragonFlyHardwareCollector,
    FreeBSDHardwareCollector,
    HPUXHardwareCollector,
    HurdHardwareCollector,
    LinuxHardwareCollector,
    NetBSDHardwareCollector,
    OpenBSDHardwareCollector,
    SunOSHardwareCollector
]

_network = [
    DnsFactCollector,
    FcWwnInitiatorFactCollector,
    NetworkCollector,
    AIXNetworkCollector,
    DarwinNetworkCollector,
    DragonFlyNetworkCollector,
    FreeBSDNetworkCollector,
    HPUXNetworkCollector,
    HurdNetworkCollector,
    IscsiInitiatorNetworkCollector,
    NvmeInitiatorNetworkCollector,
    LinuxNetworkCollector,
    NetBSDNetworkCollector,
    OpenBSDNetworkCollector,
    SunOSNetworkCollector
]

# other fact sources
_extra_facts = [
    LocalFactCollector,
    FacterFactCollector,
    OhaiFactCollector
]

# TODO: make config driven
collectors = _base + _restrictive + _general + _virtual + _hardware + _network + _extra_facts
