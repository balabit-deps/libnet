from BalabitBuilder import BalabitBuilder
import Utils

def get_builder():
    Utils.ensure_directory("m4")
    return BalabitBuilder(get_default_config_opts())

def get_default_config_opts():
    try:
        import configure_opts
    except ImportError:
        return None
    else:
        return configure_opts.default_opts
