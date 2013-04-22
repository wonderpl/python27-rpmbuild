Name: python27-gunicorn
Version: 0.17.2
Release: 1
Summary: WSGI HTTP Server for UNIX
Group: Development/Libraries
License: MIT
URL: http://gunicorn.org
Source0: http://pypi.python.org/packages/source/g/gunicorn/gunicorn-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork
worker model ported from Ruby's Unicorn project. The Gunicorn server is broadly
compatible with various web frameworks, simply implemented, light on server
resources, and fairly speedy.

%prep
%setup -q -n gunicorn-%{version}

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
%{python_sitelib}/gunicorn*
%{_bindir}/gunicorn*

%changelog
* Mon Apr 22 2013 Paul Egan <paulegan@rockpack.com> - 0.17.2-1
- Initial release
