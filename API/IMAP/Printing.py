import os
from API.IMAP.Setup import log_path, p_logs, f___log, f__warn, f_error, f_debug

class Printable(object):

    @property
    def printable(self) -> str:
        _string = ""  # type: str
        for key, value in vars(self).items():
            _string += "\t" + key + "\t=\t" + str(value) + "\n"
        return _string


def make_dirs_if_missing():
    if not os.path.exists(log_path):
        os.makedirs(log_path)


def p(filename: str=None, mode: str=None, _ps: str=None, *args):
    _M_WARNING = 'WARNING'
    _M_ERROR = 'ERROR'
    _M_DEBUG = 'DEBUG'
    _M_NONE = ''
    allowed_modes = [_M_WARNING, _M_ERROR, _M_DEBUG, _M_NONE]
    filename_debug = None
    filename_warning = None
    filename_error = None
    # TODO: add support for directories and store logs in the log_directory

    mode_str = _M_NONE

    if mode not in allowed_modes:
        mode_str = _M_NONE
    if mode == _M_WARNING:
        mode_str = '\tWARNING\t'
        filename_warning = p_logs+"WARNING.txt"
    elif mode == _M_ERROR:
        mode_str = '\tERROR\t'
        filename_error = p_logs+"ERROR.txt"
    elif mode == _M_DEBUG:
        mode_str = '\tDEBUG\t'
        filename_debug = p_logs+"DEBUG.txt"

    if mode is None:
        mode_str = ""

    _ps = mode_str + _ps

    if args is None:
        print(_ps)
        # in case there are errors...
        if filename_error is not None:
            with open(filename_error, 'a') as file:
                file.write(_ps+"\n")
        # in case there are warnings...
        if filename_warning is not None:
            with open(filename_warning, 'a') as file:
                file.write(_ps+"\n")
        # in case there are debug messages...
        if filename_debug is not None:
            with open(filename_debug, 'a') as file:
                file.write(_ps+"\n")
        # in case of regular output
        if filename is not None:
            with open(filename, 'a') as file:
                file.write(_ps+"\n")
    else:
        print(_ps.format(args))
        if filename is not None:
            with open(filename, 'a') as file:
                file.write(_ps.format(args)+"\n")


def write_to_file(_filename: str = None, _print_string: str = None):
    make_dirs_if_missing()
    with open(_filename, 'w') as f:
        f.write(_print_string+"\n")


def append_to_file(_filename: str = None, _print_string: str = None):
    make_dirs_if_missing()
    with open(_filename, 'a') as f:
        f.write(_print_string+"\n")


# Log messages
def log(_ps: str=None):
    print(_ps)
    append_to_file(_filename=f___log, _print_string=_ps)


# Print a warning
def p_w(_ps: str=None):
    _ps = "\tWARNING\t"+_ps
    print(_ps)
    append_to_file(_filename=f__warn, _print_string=_ps)
    append_to_file(_filename=f___log, _print_string=_ps)


# Print an error
def p_e(_ps: str=None):
    _ps = "\tERROR\t"+_ps
    print(_ps)
    append_to_file(_filename=f_error, _print_string=_ps)
    append_to_file(_filename=f___log, _print_string=_ps)


# Print a debug message
def p_d(_ps: str=None):
    _ps = "\tDEBUG\t"+_ps
    print(_ps)
    append_to_file(_filename=f_debug, _print_string=_ps)
    append_to_file(_filename=f___log, _print_string=_ps)


# Print an assertion message
def p_a(_ps: str=None):
    _ps = "\tASSERTION\t"+_ps
    print(_ps)
    append_to_file(_filename=f___log, _print_string=_ps)


# Print an assertion message
def p_assert(assertion: bool, message: str=None, ticket: str=None, soft: bool=False) -> bool:
    """
        Handles assertions and logging of results
    :param assertion: what is to be asserted
    :param message: how is it to be described
    :param ticket: which ticket does this refer to
    :param soft: should the assert continue or interrupt the test
    :return: what is the result of the assertion
    """
    if soft:
        message = "\tCHECK\t" + message
    else:
        message = "\tASSERTION\t" + message

    if ticket is not None:
        message += "\tTICKET https://jira.office.ottonova.de/browse/{0}".format(ticket)
    print(message)
    append_to_file(_filename=f___log, _print_string=message)

    if soft:
        try:
            assert assertion
            return True
        except AssertionError:
            p_e("\t\tFAILED!")
            return False
    else:
        assert assertion
        return True


# replace_str method is used to overwrite special characters that corrupt the tests' result by simpler ones
def replace_str(string: str) -> str:

    if '/' in string:
        string = string.replace('/', ' ')
    if ('ä' or 'Ä' or 'Å' or 'å') in string:
        string = string.replace('ä' or 'Ä' or 'Å' or 'å', 'a')
    if ('ö' or 'Ö' or 'ø' or 'Ø') in string:
        string = string.replace('ö' or 'Ö' or 'ø' or 'Ø', 'o')
    if ('ü' or 'Ü') in string:
        string = string.replace('ü' or 'Ü', 'u')
    if ('è' or 'é' or 'È' or 'É' or 'ê' or 'Ê') in string:
        string = string.replace('è' or 'é' or 'È' or 'É' or 'ê' or 'Ê', 'e')
        # TODO: check if there are any other special signs that can corrupt the tests' result
    return string
