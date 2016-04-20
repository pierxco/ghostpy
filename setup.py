#!/usr/bin/env python
#
# Copyright (c) 2015 Will Bond, 2012 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 only.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# GNU Lesser General Public License version 3 (see the file LICENSE).


from setuptools import setup


setup(name='ghostpy',
      version='0.9.1',
      description='Ghost templating for Python 3 and 2',
      long_description='Documentation is maintained at https://github.com/ticklemepierce/pybars3#readme',
      author='ticklemepierce',
      author_email='pierce.tickle@gmail.com',
      url='https://github.com/ticklemepierce/pybars3',
      packages=['ghostpy', 'ghostpy._templates'],
      package_dir={'': '.'},
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4'
          ],
      install_requires=[
          'PyMeta3>=0.5.1',
          'beautifulsoup4==4.4.1',
          'bleach==1.4.2',
          ],
      )
