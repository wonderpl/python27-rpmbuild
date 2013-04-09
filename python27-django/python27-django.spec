Name: python27-django
Version: 1.5.1
Release: 1
Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design
Group: Development/Libraries
License: BSD
URL: http://www.djangoproject.com/
Source0: http://pypi.python.org/packages/source/D/Django/Django-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
Django is a high-level Python Web framework that encourages rapid
development and a clean, pragmatic design. It focuses on automating as
much as possible and adhering to the DRY (Don't Repeat Yourself)
principle.

%prep
%setup -q -n Django-%{version}

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
* Tue Apr 09 2013 Paul Egan <paulegan@rockpack.com> - 1.5.1-1
- Initial release
