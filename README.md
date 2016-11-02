## morituri-whatlogger

morituri-whatlogger is an EAC-like logger module for [whipper](), a cdda extraction tool favoring accuracy over speed.
morituri-whatlogger is a backwards incompatible set of enhancements over the [morituri-eaclogger]().
Despite the name, the logger is incompatible with morituri and only targets whipper.

## Improvements on morituri-eaclogger

- Superior pre-emphasis support

## Status
[![Build Status](https://travis-ci.org/RecursiveForest/morituri-whatlogger.svg?branch=master)](https://travis-ci.org/RecursiveForest/morituri-whatlogger)

## Using

To use this plugin:

* build it:

        git clone git://github.com/RecursiveForest/morituri-whatlogger.git
        cd morituri-whatlogger
        python2 setup.py bdist_egg

* copy it to your plugin directory:

        export XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-"${HOME}/.config"}
        mkdir -p $XDG_CONFIG_HOME/.whipper/plugins
        cp dist/morituri_*egg $XDG_CONFIG_HOME/.whipper/plugins

* verify that it gets recognized:

        rip cd rip --help

   You should see 'what' as a possible logger.

* use it:

        rip cd rip -L what

## Developers

To use the plugin while developing uninstalled:

    python2 setup.py develop --install-dir=path/to/checkout/of/morituri
