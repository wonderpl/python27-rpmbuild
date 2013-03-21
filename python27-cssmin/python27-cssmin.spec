Name: python27-cssmin
Version: 0.1.4
Release: 1
Summary: A Python port of the YUI CSS compression algorithm
Group: Development/Libraries
License: MIT
URL: http://github.com/zacharyvoase/cssmin
Source0: http://pypi.python.org/packages/source/c/cssmin/cssmin-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
CssMin is a css parser and minfier. It minifies css by removing unneeded whitespace
character, comments, empty blocks and empty declarations. In addition declaration
values can get rewritten to shorter notation if available.

%prep
%setup -q -n cssmin-%{version}

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
%doc PKG-INFO
%{python_sitelib}/cssmin*
%{_bindir}/*

%changelog
* Thu Mar 21 2013 Paul Egan <paulegan@rockpack.com> - 0.1.4-1
- Initial release
