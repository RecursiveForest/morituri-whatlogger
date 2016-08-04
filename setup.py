from setuptools import setup, find_packages

setup(
    name="morituri-whatlogger",
    version="0.2.1",
    description="""morituri what.cd-enhanced EAC-style logger""",
    author="superveloman",
    maintainer="Samantha Baldwin",
    packages=[
        'whatlogger',
        'whatlogger.logger'],
    entry_points="""
  [morituri.logger]
  what = whatlogger.logger.what:WhatLogger
  """)
