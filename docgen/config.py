"""


"""
from declib import DeclibConfig


class DocgenConfig(DeclibConfig):

    def __init__(self, log, renderer_name):

        extra_defaults = {
            'tmpl_dir': f"~/.config/{renderer_name}/templates",
            'data_dir': f"~/.config/{renderer_name}/data",
            'out_dir': f"~/.config/{renderer_name}/out"
        }
        path_opts = ['tmpl_dir', 'data_dir', 'out_dir']

        super().__init__(log, extra_defaults, path_opts)
