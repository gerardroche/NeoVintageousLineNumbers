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
