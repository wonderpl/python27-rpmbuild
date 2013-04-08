Name: python27-flask-debugtoolbar
Version: 0.8.0
Release: 1
Summary: A port of the Django debug toolbar to Flask
Group: Development/Libraries
License: BSD
URL: http://flask-debugtoolbar.rtfd.org/
Source0: http://pypi.python.org/packages/source/F/Flask-DebugToolbar/Flask-DebugToolbar-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools python27-itsdangerous
Requires: python27-flask python27-blinker python27-itsdangerous

%description
This is a port of the excellent django-debug-toolbar for Flask applications.

%prep
%setup -q -n Flask-DebugToolbar-%{version}

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
%doc README.rst LICENSE
%{python_sitelib}/*

%changelog
* Mon Apr 08 2013 Paul Egan <paulegan@rockpack.com> - 0.8.0-1
- Initial release
