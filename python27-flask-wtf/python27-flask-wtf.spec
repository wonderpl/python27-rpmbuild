Name: python27-flask-wtf
Version: 0.10.2
Release: 1
Summary: Simple integration of Flask and WTForms
Group: Development/Libraries
License: BSD
URL: https://github.com/ajford/flask-wtf
Source0: http://pypi.python.org/packages/source/F/Flask-WTF/Flask-WTF-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-wtforms python27-flask

%description
Simple integration of Flask and WTForms, including CSRF, file upload
and Recaptcha integration.

%prep
%setup -q -n Flask-WTF-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE PKG-INFO docs/*.rst
%{python_sitelib}/*

%changelog
* Tue Oct 22 2013 Paul Egan <paulegan@rockpack.com> - 0.9.3-1
- Latest release

* Fri Jan 11 2013 Paul Egan <paulegan@rockpack.com> - 0.8.2-1
- Initial release
