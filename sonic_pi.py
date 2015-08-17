import sublime, sublime_plugin, shlex
from subprocess import Popen

def sonic_pi(command):
    print(shlex.quote(command))
    Popen("sonic_pi " + shlex.quote(command),shell=True)

class SonicPiRun(sublime_plugin.TextCommand):

    def run(self, edit):
        print("run")
        r = sublime.Region(0,self.view.size())
        s = self.view.substr(r)
        sonic_pi(s)

class SonicPiStop(sublime_plugin.TextCommand):

    def run(self, edit):
        print("stop")
        sonic_pi("stop")

class SonicPiSelection(sublime_plugin.TextCommand):

    def line(self):
        for region in self.view.sel():
            if region.empty():
                line = self.view.line(region)
                line_contents = self.view.substr(line)
                line_below = sublime.Region(line.b+1)
                self.view.sel().clear()
                self.view.sel().add(line_below)
                return line_contents
            else:
                return self.view.substr(region)

    def run(self, edit):
        print("selection")
        sonic_pi(self.line())
