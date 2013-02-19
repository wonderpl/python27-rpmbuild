Name: python27-jabberbot
Version: 0.15
Release: 1
Summary: A framework for writing Jabber/XMPP bots and services
Group: Development/Libraries
License: GNU General Public License version 3 or later
URL: http://thp.io/2007/python-jabberbot/
Source0: http://pypi.python.org/packages/source/j/jabberbot/jabberbot-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools

%description
The JabberBot framework allows you to easily write bots
that use the XMPP protocol. You can create commands by
decorating functions in your subclass or customize the
bot's operation completely. MUCs are also supported.

%prep
%setup -q -n jabberbot-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/jabberbot*

%changelog
* Tue Feb 19 2013 Paul Egan <paulegan@rockpack.com> - 0.15-1
- Initial release
