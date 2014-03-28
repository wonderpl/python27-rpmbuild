Name: python27-asn1
Version: 0.1.7
Release: 1
Summary: ASN.1 types and codecs
Group: Development/Libraries
License: BSD
URL: http://pyasn1.sf.net
Source0: https://pypi.python.org/packages/source/p/pyasn1/pyasn1-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
This is an implementation of ASN.1 types and codecs in Python programming
language. It has been first written to support particular protocol (SNMP) but
then generalized to be suitable for a wide range of protocols based on ASN.1
specification.

%prep
%setup -q -n pyasn1-%{version}

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
%doc README
%{python_sitelib}/pyasn1*

%changelog
* Fri Mar 28 2014 Paul Egan <paulegan@rockpack.com> - 0.1.7-1
- Initial release
