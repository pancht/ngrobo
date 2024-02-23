"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================


nRoBo file system utility.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmaill.com
"""
import os
import shutil
from pathlib import Path


def copy_dir(src, dst, symlinks=False, ignore=None, copy_function=shutil.copy2,
             ignore_dangling_symlinks=False, dirs_exist_ok=False) -> None:
    """
    Shadows shutil.copytree and its documentation.
    ----------------------------------------------------------------------

    Recursively copy a directory tree and return the destination directory.

    If exception(s) occur, an Error is raised with a list of reasons.

    If the optional symlinks flag is true, symbolic links in the
    source tree result in symbolic links in the destination tree; if
    it is false, the contents of the files pointed to by symbolic
    links are copied. If the file pointed by the symlink doesn't
    exist, an exception will be added in the list of errors raised in
    an Error exception at the end of the copy process.

    You can set the optional ignore_dangling_symlinks flag to true if you
    want to silence this exception. Notice that this has no effect on
    platforms that don't support os.symlink.

    The optional ignore argument is a callable. If given, it
    is called with the `src` parameter, which is the directory
    being visited by copytree(), and `names` which is the list of
    `src` contents, as returned by os.listdir():

        callable(src, names) -> ignored_names

    Since copytree() is called recursively, the callable will be
    called once for each directory that is copied. It returns a
    list of names relative to the `src` directory that should
    not be copied.

    The optional copy_function argument is a callable that will be used
    to copy each file. It will be called with the source path and the
    destination path as arguments. By default, copy2() is used, but any
    function that supports the same signature (like copy()) can be used.

    If dirs_exist_ok is false (the default) and `dst` already exists, a
    `FileExistsError` is raised. If `dirs_exist_ok` is true, the copying
    operation will continue if it encounters existing directories, and files
    within the `dst` tree will be overwritten by corresponding files from the
    `src` tree.
    """
    try:
        shutil.copytree(src, dst, symlinks=symlinks, ignore=ignore, copy_function=copy_function,
                        ignore_dangling_symlinks=ignore_dangling_symlinks, dirs_exist_ok=dirs_exist_ok)
    except FileExistsError as e:
        print(e)


def copy_file(src, dst, *, follow_symlinks=True):
    """Copy data from src to dst in the most efficient way possible.

        If follow_symlinks is not set and src is a symbolic link, a new
        symlink will be created instead of copying the file it points to.

    """
    try:
        shutil.copyfile(src, dst, follow_symlinks=follow_symlinks)
    except FileExistsError as e:
        print(e)


def remove_filetree(path, ignore_errors=False, onerror=None, *, onexc=None, dir_fd=None):
    """Recursively delete a directory tree.

        If dir_fd is not None, it should be a file descriptor open to a directory;
        path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
        If it is unavailable, using it will raise a NotImplementedError.

        If ignore_errors is set, errors are ignored; otherwise, if onexc or
        onerror is set, it is called to handle the error with arguments (func,
        path, exc_info) where func is platform and implementation dependent;
        path is the argument to that function that caused it to fail; and
        the value of exc_info describes the exception. For onexc it is the
        exception instance, and for onerror it is a tuple as returned by
        sys.exc_info().  If ignore_errors is false and both onexc and
        onerror are None, the exception is reraised.

        onerror is deprecated and only remains for backwards compatibility.
        If both onerror and onexc are set, onerror is ignored and onexc is used.
        """
    shutil.rmtree(path, ignore_errors=ignore_errors, onerror=onerror, onexc=onexc, dir_fd=dir_fd)


def remove_file(file_full_path: [str, Path]):
    """remove file"""
    if isinstance(file_full_path, Path):
        os.remove(str(file_full_path))
    else:
        os.remove(file_full_path)


def get_files_list(path: [str, Path], *, pattern: [str, None] = None, recursion: bool = False) -> [Path]:
    """Returns list of files from the given <path>.

        Return only list of files if a pattern is supplied.
        Return list of files from subdirectories too if recursion flag is True."""
    import re
    if isinstance(path, str):
        # covert string to path
        path = Path(path)

    _files = []  # start with empty list
    if pattern:
        # apply filter
        _files = [f for f in path.iterdir() if f.is_file() and re.match(pattern, str(f))]
    else:
        _files = [f for f in path.iterdir() if f.is_file()]

    # we got files from the path, now get list of directories at path
    sub_dirs = [f for f in path.iterdir() if f.is_dir()]

    # recursively iterate each directory
    if sub_dirs:
        for d in sub_dirs:
            _files = _files + get_files_list(d, pattern=pattern)
        return _files
    else:
        return _files


def move(src, dst, copy_function=shutil.copy2):
    """Recursively move a file or directory to another location. This is
    similar to the Unix "mv" command. Return the file or directory's
    destination.

    If the destination is a directory or a symlink to a directory, the source
    is moved inside the directory. The destination path must not already
    exist.

    If the destination already exists but is not a directory, it may be
    overwritten depending on os.rename() semantics.

    If the destination is on our current filesystem, then rename() is used.
    Otherwise, src is copied to the destination and then removed. Symlinks are
    recreated under the new name if os.rename() fails because of cross
    filesystem renames.

    The optional `copy_function` argument is a callable that will be used
    to copy the source or it will be delegated to `copytree`.
    By default, copy2() is used, but any function that supports the same
    signature (like copy()) can be used.

    A lot more could be done here...  A look at a mv.c shows a lot of
    the issues this implementation glosses over.

    """
    shutil.move(src=src, dst=dst, copy_function=copy_function)
