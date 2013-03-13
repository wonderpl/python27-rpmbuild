Name: python27-mako
Version: 0.7.3
Release: 1
Summary: A super-fast templating language that borrows the  best ideas from the existing templating languages
Group: Development/Libraries
License: MIT
URL: http://www.makotemplates.org/
Source0: http://pypi.python.org/packages/source/M/Mako/Mako-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-markupsafe

%description
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi.

%prep
%setup -q -n Mako-%{version}

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
%{_bindir}/*

%changelog
* Wed Mar 13 2013 Paul Egan <paulegan@rockpack.com> - 0.7.3-1
- Initial release
