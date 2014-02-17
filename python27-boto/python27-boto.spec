Name: python27-boto
Version: 2.25.0
Release: 1
License: MIT License
Summary: A simple lightweight interface to Amazon Web Services
Group: Development/Libraries
URL: https://github.com/boto/boto
Source0: http://pypi.python.org/packages/source/b/boto/boto-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python2-devel >= %python_version

%description
Boto is a Python package that provides interfaces to Amazon Web Services.
It supports S3 (Simple Storage Service), SQS (Simple Queue Service) via
the REST API's provided by those services and EC2 (Elastic Compute Cloud)
via the Query API. The goal of boto is to provide a very simple, easy to
use, lightweight wrapper around the Amazon services.

%prep
%setup -q -n boto-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%exclude %{_bindir}/*
%{python_sitelib}/*

%changelog
* Thu Feb 13 2014 Paul Egan <paulegan@rockpack.com> - 2.25.0-1
- Bumped

* Mon Apr 22 2013 Paul Egan <paulegan@rockpack.com> - 2.9.0-1
- Bumped

* Tue Feb 19 2013 Paul Egan <paulegan@rockpack.com> - 2.8.0-1
- Bumped

* Thu Jan 10 2013 Paul Egan <paulegan@rockpack.com> - 2.6.0-1
- Initial release

