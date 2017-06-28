# file-roller-kde-desktop-entry
Configuration file for adding "Extract here" desktop entry to KDE applications' context menus. file-roller is used for the extraction process.

## Installation

1. Determine KDE services directories with `kde4-config --path services`.

2. Create sub-directory "ServiceMenus" in one of KDE's services directories, e.g. in "~/.kde/share/kde4/services": `mkdir ~/.kde/share/kde4/services/ServiceMenus`.

3. Copy "extractHere.desktop" file to the "ServiceMenus" sub-directory.

4. Restart KDE applications, which now should contain a context menu entry "Extract here" for files with an archive MIME type, e.g. `application/zip` or `application/x-rar-compressed`.

Tested with [krusader 2.4.0-beta3](https://www.krusader.org) on [Linux Mint 18.1](http://www.linuxmint.com) with [file-roller 3.16.5](https://github.com/GNOME/file-roller).