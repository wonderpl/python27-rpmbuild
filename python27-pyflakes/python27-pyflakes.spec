Name: python27-pyflakes
Version: 0.8.1
Release: 1
Summary: passive checker of Python programs
Group: Development/Libraries
License: MIT
URL: https://launchpad.net/pyflakes
Source0: https://pypi.python.org/packages/source/p/pyflakes/pyflakes-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
A simple program which checks Python source files for errors.

Pyflakes analyzes programs and detects various errors.  It works by parsing the
source file, not importing it, so it is safe to use on modules with side
effects.  It's also much faster.

%prep
%setup -q -n pyflakes-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%check
%{__python} setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst
%{python_sitelib}/pyflakes*
%{_bindir}/pyflakes

%changelog
* Mon Jul 28 2014 Paul Egan <paulegan@rockpack.com> - 0.8.1-1
- Initial release
