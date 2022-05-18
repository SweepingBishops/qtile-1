# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import subprocess
from itertools import cycle

from libqtile.widget import base


class Load(base.ThreadPoolText):
    """A small widget to show the load averages of the system."""

    defaults = [
        ("update_interval", 1.0, "The update interval for the widget"),
        ("format", "Load({time}):{load}", "The format in which to display the results."),
    ]
    times = ["1m", "5m", "15m"]

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(Load.defaults)
        self.add_callbacks({"Button1": self.next_load})
        self.cycled_times = cycle(Load.times)
        self.next_load()

    def next_load(self):
        self.time = next(self.cycled_times)

    def poll(self):
        loads = {}
        uptime = subprocess.check_output("uptime").decode("utf-8").strip()
        loads["1m"], loads["5m"], loads["15m"] = eval(
            uptime[uptime.index("load") + 13 :]
        )  # Gets the load averages as a dictionary.
        load = loads[self.time]
        return self.format.format(time=self.time, load=load)
