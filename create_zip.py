#!/usr/bin/env python3

# create_zip is free software: you can redistribute it and/or modify it under 
# the terms of the GNU General Public License as published by the Free Software 
# Foundation in version 2 of the License.

# file-roller-kde-desktop-entry is distributed in the hope that it will be 
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General 
# Public License for more details.

# You should have received a copy of the GNU General Public License along with
# file-roller-kde-desktop-entry. If not, see 
# <https://www.gnu.org/licenses/old-licenses>.

# Copyright (c) 2019 Florian Rademacher <florian.rademacher@fh-dortmund.de>

from pathlib import Path
import os
import sys

def zipCommandFor(path, addToZip=None):
    zipCommand = None

    if addToZip is not None:
        zipCommand = 'cd "%s"; zip -ur "%s".zip "%s"' % \
            (path.parent, addToZip, path.name)
    elif path.is_dir():
        zipCommand = 'cd "%s"; zip -r "%s".zip "%s"' % \
            (path.parent, path.name, path.name)
    elif path.is_file():
        zipCommand = 'cd "%s"; zip "%s".zip "%s"' % \
            (path.parent, path.name, path.name)

    return zipCommand
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(4)

    basePath = Path(sys.argv[1])
    zipCommand = zipCommandFor(basePath)
    if zipCommand is None:
        sys.exit(4)

    commands = [zipCommand]
    for arg in sys.argv[2:]:
        zipCommand = zipCommandFor(Path(arg), basePath)
        if zipCommand is None:
            sys.exit(4)

        commands.append(zipCommand)

    for command in commands:
        os.system(command)
