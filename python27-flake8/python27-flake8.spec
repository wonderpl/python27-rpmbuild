Name: python27-flake8
Version: 2.2.4
Release: 1
Summary: the modular source code checker: pep8, pyflakes and co
Group: Development/Libraries
License: MIT
URL: http://bitbucket.org/tarek/flake8
Source0: https://pypi.python.org/packages/source/f/flake8/flake8-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools python27-pyflakes python27-pep8
Requires: python27-pyflakes python27-pep8 python27-mccabe

%description
Flake8 is a wrapper around these tools:
- PyFlakes
- pep8
- Ned Batchelder's McCabe script

Flake8 runs all the tools by launching the single flake8 script.  It displays
the warnings in a per-file, merged output.

%prep
%setup -q -n flake8-%{version}

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
%{python_sitelib}/flake8*
%{_bindir}/flake8

%changelog
* Mon Jul 28 2014 Paul Egan <paulegan@rockpack.com> - 2.2.2-1
- Initial release
