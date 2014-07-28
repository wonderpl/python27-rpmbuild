Name: python27-pep8
Version: 1.5.7
Release: 1
Summary: Python style guide checker
Group: Development/Libraries
License: MIT
URL: http://pep8.readthedocs.org/
Source0: https://pypi.python.org/packages/source/p/pep8/pep8-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
pep8 is a tool to check your Python code against some of the style conventions
in PEP 8.

Features:
- Plugin architecture: Adding new checks is easy.
- Parseable output: Jump to error location in your editor.
- Small: Just one Python file, requires only stdlib. You can use just the
  pep8.py file for this purpose.
- Comes with a comprehensive test suite.

%prep
%setup -q -n pep8-%{version}

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
%{python_sitelib}/pep8*
%{_bindir}/pep8

%changelog
* Mon Jul 28 2014 Paul Egan <paulegan@rockpack.com> - 1.5.7-1
- Initial release
