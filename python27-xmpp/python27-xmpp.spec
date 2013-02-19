Name: python27-xmpp
Version: 0.5.0rc1
Release: 1
Summary: XMPP-IM-compliant library for jabber instant messenging
Group: Development/Libraries
License: GPL
URL: http://xmpppy.sourceforge.net/
Source0: http://downloads.sourceforge.net/project/xmpppy/xmpppy/0.5.0-rc1/xmpppy-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
This library provides functionality for writing xmpp-compliant
clients, servers and/or components/transports.

It was initially designed as a "rework" of the
jabberpy library but has become a separate product.

%prep
%setup -q -n xmpppy-%{version}

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
%{python_sitelib}/xmpp*

%changelog
* Tue Feb 19 2013 Paul Egan <paulegan@rockpack.com> - 0.5.0rc1-1
- Initial release
