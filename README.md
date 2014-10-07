python27-rpmbuild
=================

RPM spec files and build configuration for Python 2.7 packages on Amazon Linux.

To use:

    git clone git@github.com:wonderpl/python27-rpmbuild.git ~/rpmbuild
    ln -s ~/rpmbuild/macros ~/.rpmmacros
    cd ~/rpmbuild/PACKAGE
    make
