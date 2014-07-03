Name: python27-six
Version: 1.7.3
Release: 1
Summary: Python 2 and 3 compatibility utilities
Group: Development/Libraries
License: MIT
URL: http://pypi.python.org/pypi/six/
Source0: https://pypi.python.org/packages/source/s/six/six-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
Six is a Python 2 and 3 compatibility library.  It provides utility functions
for smoothing over the differences between the Python versions with the goal of
writing Python code that is compatible on both Python versions.  See the
documentation for more information on what is provided.

%prep
%setup -q -n six-%{version}

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
%doc 
%{python_sitelib}/six*

%changelog
* Tue Mar 18 2014 Paul Egan <paulegan@rockpack.com> - 1.6.1-1
- Initial release
