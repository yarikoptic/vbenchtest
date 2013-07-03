#!/usr/bin/python
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: t -*-
# vi: set ft=python sts=4 ts=4 sw=4 noet :

# This is just a test repository for vbench

from distutils.core import setup

setup(
	name = "vbenchtest",
	version = '0.0.1',
	description = "Test repository for vbench",
	author = "Yaroslav Halchenko",
	author_email = "debian@onerussian.com",
 	license = "MIT",
	packages =	['vbenchtest'],
)
