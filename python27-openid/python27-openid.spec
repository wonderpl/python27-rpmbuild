Name: python27-openid
Version: 2.2.5
Release: 1
Summary: OpenID support for servers and consumers
Group: Development/Libraries
License: ASL
URL: http://github.com/openid/python-openid
Source0: http://pypi.python.org/packages/source/p/python-openid/python-openid-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
This is a set of Python packages to support use of the OpenID decentralized
identity system in your application.  Want to enable single sign-on for your
web site?  Use the openid.consumer package.  Want to run your own OpenID
server? Check out openid.server.  Includes example code and support for a
variety of storage back-ends.

%prep
%setup -q -n python-openid-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{python_sitelib}/*

%changelog
* Wed Apr 10 2013 Paul Egan <paulegan@rockpack.com> - 2.2.5-1
- Initial release
