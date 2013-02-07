Name: python27-ipython
Version: 0.13.1
Release: 1
Summary: IPython: Productive Interactive Computing
Group: Development/Libraries
License: BSD
URL: http://ipython.org
Source0: http://archive.ipython.org/release/%{version}/ipython-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
#Requires: python27-tornado python27-pygments python27-nose python27-sphinx python27-zmq

%description
IPython provides a replacement for the interactive Python interpreter with
extra functionality.

Main features:
 * Comprehensive object introspection.
 * Input history, persistent across sessions.
 * Caching of output results during a session with automatically generated
   references.
 * Readline based name completion.
 * Extensible system of 'magic' commands for controlling the environment and
   performing many tasks related either to IPython or the operating system.
 * Configuration system with easy switching between different setups (simpler
   than changing $PYTHONSTARTUP environment variables every time).
 * Session logging and reloading.
 * Extensible syntax processing for special purpose situations.
 * Access to the system shell with user-extensible alias system.
 * Easily embeddable in other Python programs.
 * Integrated access to the pdb debugger and the Python profiler.

%prep
%setup -q -n ipython-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man*/*
%{python_sitelib}/*
%exclude %{python_sitelib}/IPython/*/tests/
%exclude %{python_sitelib}/IPython/*/*/tests
%exclude %{_datadir}/doc/ipython

%changelog
* Thu Feb 07 2013 Paul Egan <paulegan@rockpack.com> - 0.13.1-1
- Initial release
