import sys
import traceback
from log import add as log

#WIP

def unknown_exception(what):
    what_str = str(what)
    try:
        what
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 01 - AssertionError on line {} in statement {}").format(line, text)
        log("Exception 01 - AssertionError on line {} in statement {}").format(line, text)
    except AttributeError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 02 - AttributeError on line {} in statement {}").format(line, text)
        log("Exception 02 - AttributeError on line {} in statement {}").format(line, text)
    except EOFError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 03 - EOFError on line {} in statement {}").format(line, text)
        log("Exception 03 - EOFError on line {} in statement {}").format(line, text)
    except FloatingPointError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 04 - FloatingPointError on line {} in statement {}").format(line, text)
        log("Exception 04 - FloatingPointError on line {} in statement {}").format(line, text)
    except GeneratorExit:
        print ("Exception 05 - GeneratorExit")
        log("Exception 05 - GeneratorExit")
    except IOError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 06 - IOError on line {} in statement {}").format(line, text)
        log("Exception 06 - IOError on line {} in statement {}").format(line, text)
    except ImportError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 07 - ImportError on line {} in statement {}").format(line, text)
    except IndexError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 08 - IndexError on line {} in statement {}").format(line, text)
        log("Exception 08 - IndexError on line {} in statement {}").format(line, text)
    except KeyError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 09 - KeyError on line {} in statement {}").format(line, text)
        log("Exception 09 - KeyError on line {} in statement {}").format(line, text)
    except KeyboardInterrupt:
        print "Exception 10 - KeyboardInterrupt"
        log("Exception 10 - KeyboardInterrupt")
    except MemoryError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 11 - MemoryError on line {} in statement {}").format(line, text)
        log("Exception 11 - MemoryError on line {} in statement {}").format(line, text)
    except NameError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 12 - NameError on line {} in statement {}").format(line, text)
        log("Exception 12 - NameError on line {} in statement {}").format(line, text)
    except NotImplementedError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 13 - NotImplementedError on line {} in statement {}").format(line, text)
        log("Exception 13 - NotImplementedError on line {} in statement {}").format(line, text)
    except OSError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 14 - OSError on line {} in statement {}").format(line, text)
        log("Exception 14 - OSError on line {} in statement {}").format(line, text)
    except OverflowError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 15 - OverflowError on line {} in statement {}").format(line, text)
        log("Exception 15 - OverflowError on line {} in statement {}").format(line, text)
    except ReferenceError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 16 - ReferenceError on line {} in statement {}").format(line, text)
        log("Exception 16 - ReferenceError on line {} in statement {}").format(line, text)
    except RuntimeError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 17 - RuntimeError on line {} in statement {}").format(line, text)
        log("Exception 17 - RuntimeError on line {} in statement {}").format(line, text)
    except StopIteration:
        print "Exception 18 - StopIteration"
        log("Exception 18 - StopIteration")
    except SyntaxError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 19 - SyntaxError on line {} in statement {}").format(line, text)
        logprint ("Exception 19 - SyntaxError on line {} in statement {}").format(line, text)
    except SystemError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 20 - SystemError on line {} in statement {}").format(line, text)
        log("Exception 20 - SystemError on line {} in statement {}").format(line, text)
    except SystemExit:
        print "Exception 21 - SystemExit"
        log("Exception 21 - SystemExit")
    except TypeError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 22 - TypeError on line {} in statement {}").format(line, text)
        log("Exception 22 - TypeError on line {} in statement {}").format(line, text)
    except UnboundLocalError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 23 - UnboundLocalError on line {} in statement {}").format(line, text)
        log("Exception 23 - UnboundLocalError on line {} in statement {}").format(line, text)
    except UnicodeError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 24 - UnicodeError on line {} in statement {}").format(line, text)
        log("Exception 24 - UnicodeError on line {} in statement {}").format(line, text)
    except ValueError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 25 - ValueError on line {} in statement {}").format(line, text)
        log("Exception 25 - ValueError on line {} in statement {}").format(line, text)
    except WindowsError:
        print "Windows Error - Use Linux"
        log("Logger thinks about commiting suicide")
    except ZeroDivisionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print ("Exception 26 - ZeroDivisionError on line {} in statement {}").format(line, text)
        log("Exception 26 - ZeroDivisionError on line {} in statement {}").format(line, text)
    except UserWarning:
        print ("Warning - User Warning")
        log("Warning - User Warning")
    except DeprecationWarning:
        print ("Warning - Deprecation Warning")
        log("Warning - Deprecation Warning")
    except PendingDeprecationWarning:
        print ("Warning - Pending Deprecation Warning")
        log("Warning - Pending Deprecation Warning")
    except SyntaxWarning:
        print ("Warning - Syntax Warning")
        log("Warning - Syntax Warning")
    except RuntimeWarning:
        print ("Warning - Runtime Warning")
        log("Warning - Runtime Warning")
    except ImportWarning:
        print ("Warning - Import Warning")
        log("Warning - Import Warning")
    except UnicodeWarning:
        print ("Warning - Unicode Warning")
        log("Warning - Unicode Warning")
    else:
        print "Unknown Exception"
        log("unknown exception happend")
