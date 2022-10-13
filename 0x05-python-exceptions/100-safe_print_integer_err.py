#!/usr/bin/python3i
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
