# Copyright (C) 2023 Gerard Roche
#
# This file is part of NeoVintageousLineNumbers.
#
# NeoVintageousLineNumbers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NeoVintageousLineNumbers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NeoVintageousLineNumbers.  If not, see <https://www.gnu.org/licenses/>.

import sublime
import sublime_plugin

# Relative line numbers is supported >= 4074.

if int(sublime.version()) >= 4050:
    def _is_normal_view(view) -> bool:
        return view and view.element() is None
else:
    def _is_normal_view(view) -> bool:
        if not view:
            return False

        settings = view.settings()

        return settings and not settings.get('is_widget', False)


def _is_command_mode(view) -> bool:
    return _is_normal_view(view) and view.settings().get('command_mode')


class NeoVintageousLineNumbers(sublime_plugin.EventListener):

    def on_post_text_command(self, view, command_name, args):
        if view.settings().get('line_numbers'):
            if _is_command_mode(view):
                view.settings().set('relative_line_numbers', True)
            else:
                view.settings().set('relative_line_numbers', False)
