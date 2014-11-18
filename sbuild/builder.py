from BalabitBuilder import BalabitBuilder
import Utils
import os

class LibnetBuilder(BalabitBuilder):

    def bootstrap(self):
        Utils.ensure_directory(os.path.join(self.source_dir,"m4"))
        return super(LibnetBuilder, self).bootstrap()
       

def get_builder():
    return LibnetBuilder(get_default_config_opts())

def get_default_config_opts():
    try:
        import configure_opts
    except ImportError:
        return None
    else:
        return configure_opts.default_opts
