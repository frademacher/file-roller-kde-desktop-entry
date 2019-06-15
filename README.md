# file-roller-kde-desktop-entry
Configuration files and scripts for adding "Extract here" and "Compress" desktop entries to KDE applications' context menus. `file-roller` and `zip` are used for extraction and compression, respectively.

## Installation

1. Determine KDE services directories, e.g., with `kde4-config --path services` on KDE 4. For KDE 5, one of the directories is `~/.local/share/kservices5/ServiceMenus`.

2. Create sub-directory "ServiceMenus" in one of KDE's services directories, e.g., in `~/.local/share/kservices5/ServiceMenus` via `mkdir ~/.kde/share/kde4/services/ServiceMenus`.

3. Copy the `desktop` files and Python scripts in this repository to the created `ServiceMenus` sub-directory.

4. Restart KDE applications, which now should contain two context menu entries, i.e., `Extract here` (for files with an archive MIME type) and `Compress` (for arbitrary files and directories).

Note that the `create_zip` Python script contained in this repository is used by the `Compress` entry to create a ZIP archive. The script creates a ZIP archive that contains all files and/or folders passed to it.

Tested with [krusader 2.6.0](https://www.krusader.org) on [Linux Mint 19.1](http://www.linuxmint.com) with [file-roller 3.28](https://github.com/GNOME/file-roller) and [zip 3.0](http://www.info-zip.org).
