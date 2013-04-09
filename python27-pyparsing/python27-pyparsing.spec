Name: python27-pyparsing
Version: 1.5.7
Release: 1
Summary: Python parsing module
Group: Development/Libraries
License: MIT
URL: http://pyparsing.wikispaces.com/
Source0: http://pypi.python.org/packages/source/p/pyparsing/pyparsing-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
The pyparsing module is an alternative approach to creating and executing
simple grammars, vs. the traditional lex/yacc approach, or the use of regular
expressions. The pyparsing module provides a library of classes that client
code uses to construct the grammar directly in Python code.

%prep
%setup -q -n pyparsing-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc examples/0README.html LICENSE
%{python_sitelib}/pyparsing*

%changelog
* Mon Apr 08 2013 Paul Egan <paulegan@rockpack.com> - 2.0.0-1
- Initial release
