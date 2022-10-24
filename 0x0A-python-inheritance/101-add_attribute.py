#!/usr/bin/python3

def foo():
    try:
        raise TypeError('cant add new attribute')
    except:
        raise

def bar(arg1):
    try:
        foo()
    except Exception as e:
        raise type(e)(e.message + ' happens at %s' % arg1)

bar('arg1')
