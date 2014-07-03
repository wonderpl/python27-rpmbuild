Name: python27-mailchimp
Version: 2.0.8
Release: 1
Summary: A CLI client and Python API library for the MailChimp email platform
Group: Development/Libraries
License: MIT
URL: https://bitbucket.org/mailchimp/mailchimp-api-python/
Source0: https://pypi.python.org/packages/source/m/mailchimp/mailchimp-%{version}.tar.gz
Patch1: docopt.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: python27-setuptools
Requires: python27-requests
#Requires: python27-docopt

%description
A Python client for v2 of the MailChimp API. Please note that we generate this
client/wrapper, so while we're happy to look at any pull requests, ultimately
we can't technically accept them. We will, however comment on any additions or
changes made due to them before closing them.

%prep
%setup -q -n mailchimp-%{version}
%patch1 -p0

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
%doc 
%{python_sitelib}/mailchimp*

%changelog
* Wed Mar 19 2014 Paul Egan <paulegan@rockpack.com> - 2.0.7-1
- Initial release
