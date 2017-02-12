def unknown_exception(what):
    what_str = str(what)
    try:
        what
    except AssertionError:
        print "Exception 01 - AssertionError"
    except AttributeError:
        print "Exception 02 - AttributeError"
    except EOFError:
        print "Exception 03 - EOFError"
    except FloatingPointError:
        print "Exception 04 - FloatingPointError"
    except GeneratorExit:
        print "Exception 05 - GeneratorExit"
    except IOError:
        print "Exception 06 - IOError"
    except ImportError:
        print "Exception 07 - ImportError"
    except IndexError:
        print "Exception 08 - IndexError"
    except KeyError:
        print "Exception 09 - KeyError"
    except KeyboardInterrupt:
        print "Exception 10 - KeyboardInterrupt"
    except MemoryError:
        print "Exception 11 - MemoryError"
    except NameError:
        print "Exception 12 - NameError"
    except NotImplementedError:
        print "Exception 13 - NotImplementedError"
    except OSError:
        print "Exception 14 - OSError"
    except OverflowError:
        print "Exception 15 - OverflowError"
    except ReferenceError:
        print "Exception 16 - ReferenceError"
    except RuntimeError:
        print "Exception 17 - RuntimeError"
    except StopIteration:
        print "Exception 18 - StopIteration"
    except SyntaxError:
        print "Exception 19 - SyntaxError"
    except SystemError:
        print "Exception 20 - SystemError"
    except SystemExit:
        print "Exception 21 - SystemExit"
    except TypeError:
        print "Exception 22 - TypeError"
    except UnboundLocalError:
        print "Exception 23 - UnboundLocalError"
    except UnicodeError:
        print "Exception 24 - UnicodeError"
    except ValueError:
        print "Exception 25 - ValueError"
    except WindowsError:
        print "Windows Error - Use linux"
    except ZeroDivisionError:
        print "Exception 26 - ZeroDivisionError"
    except UserWarning:
        return "Warning - User Warning"
    except DeprecationWarning:
        return "Warning - Deprecation Warning"
    except PendingDeprecationWarning:
        return "Warning - Pending Deprecation Warning"
    except SyntaxWarning:
        return "Warning - Syntax Warning"
    except RuntimeWarning:
        return "Warning - Runtime Warning"
    except ImportWarning:
        return "Warning - Import Warning"
    except UnicodeWarning:
        return "Warning - Unicode Warning"
