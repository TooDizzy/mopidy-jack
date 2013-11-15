****************************
Mopidy-Jack
****************************

.. image:: https://pypip.in/v/Mopidy-Jack/badge.png
    :target: https://crate.io/packages/Mopidy-Jack/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/Mopidy-Jack/badge.png
    :target: https://crate.io/packages/Mopidy-Jack/
    :alt: Number of PyPI downloads

.. image:: https://travis-ci.org/TooDizzy/mopidy-jack.png?branch=master
    :target: https://travis-ci.org/TooDizzy/mopidy-jack
    :alt: Travis CI build status

.. image:: https://coveralls.io/repos/TooDizzy/mopidy-jack/badge.png?branch=master
   :target: https://coveralls.io/r/TooDizzy/mopidy-jack?branch=master
   :alt: Test coverage

Try to keep a set of predefined jack batchbay connection during playback.


Installation
============

Install by running::

	A prerequisite for this plugin is JACK (naturally) and the JACK headers.
	For JACK1 these can be installed by:
	sudo apt-get install libjack-dev
	
	And for JACK2 these can be installed by:
	sudo apt-get install libjack-jackd2-dev

	And in order for us to build py-jack we need to install a few dependencies: NumPy, python-dev. 

	You should also install NumPy:
	
	sudo apt-get install python-numpy
	sudo apt-get install python-dev
	
	Then it's just to run:
	
    pip install Mopidy-Jack

Or, if available, install the Debian/Ubuntu package from `apt.mopidy.com
<http://apt.mopidy.com/>`_.


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-Jack to your Mopidy configuration file::

    [jack]
    # TODO: Add example of extension config


Project resources
=================

- `Source code <https://github.com/TooDizzy/mopidy-jack>`_
- `Issue tracker <https://github.com/TooDizzy/mopidy-jack/issues>`_
- `Download development snapshot <https://github.com/TooDizzy/mopidy-jack/tarball/master#egg=Mopidy-Jack-dev>`_


Changelog
=========

v0.1.0 (UNRELEASED)
----------------------------------------

- Initial release.