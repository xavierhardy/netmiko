from __future__ import unicode_literals
import time
from select import select

from netmiko.cisco_base_connection import CiscoSSHConnection


class ExtremeWingSSH(CiscoSSHConnection):
    """Extreme WiNG support."""
    def session_preparation(self):
        self.set_base_prompt(pri_prompt_terminator='>',
                             alt_prompt_terminator='#',
                             delay_factor=2)
        self.disable_paging(command="no page")
        self.set_terminal_width(command='terminal width 512')
        # Clear the read buffer
        select([self.remote_conn], [], [], .3 * self.global_delay_factor)
        self.clear_buffer()
