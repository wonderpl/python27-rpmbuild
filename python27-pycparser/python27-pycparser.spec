Name: python27-pycparser
Version: 2.10
Release: 1
Summary: C parser in Python
Group: Development/Libraries
License: BSD
URL: https://github.com/eliben/pycparser
Source0: https://pypi.python.org/packages/source/p/pycparser/pycparser-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
pycparser is a complete parser of the C language, written in pure Python using
the PLY parsing library.  It parses C code into an AST and can serve as a
front-end for C compilers or analysis tools.

%prep
%setup -q -n pycparser-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE
%{python_sitelib}/*

%changelog
* Thu Jul 03 2014 Paul Egan <paulegan@rockpack.com> - 2.10-1
- Initial release
