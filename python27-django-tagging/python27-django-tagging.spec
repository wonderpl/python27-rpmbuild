Name: python27-django-tagging
Version: 0.3.1
Release: 1
Summary: Generic tagging application for Django
Group: Development/Libraries
License: BSD
URL: http://code.google.com/p/django-tagging/
Source0: http://pypi.python.org/packages/source/d/django-tagging/django-tagging-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
A generic tagging application for Django projects, which allows association of
a number of tags with any Model instance and makes retrieval of tags simple.

%prep
%setup -q -n django-tagging-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt LICENSE.txt
%{python_sitelib}/*

%changelog
* Tue Apr 09 2013 Paul Egan <paulegan@rockpack.com> - 0.3.1-1
- Initial release
