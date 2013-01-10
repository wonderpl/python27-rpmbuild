Name: s3cmd
Version: 1.0.1
Release: 2
Summary: Command line tool for managing Amazon S3 and CloudFront services
Group: Networking
License: GPL
Url: http://s3tools.org/s3cmd
Source: http://prdownloads.sourceforge.net/s3tools/s3cmd-%{version}.tar.gz
Patch1: aws_env.patch
Patch2: headers.patch

BuildArch: noarch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python2-devel >= %python_version

%description
S3cmd lets you copy files from/to Amazon S3
(Simple Storage Service) using a simple to use
command line client. Supports rsync-like backup,
GPG encryption, and more. Also supports management
of Amazon's CloudFront content delivery network.

%prep
%setup
%patch1 -p0
%patch2 -p1

%build
export S3CMD_PACKAGING=1
%{__python} setup.py build

%install
export S3CMD_PACKAGING=1
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README PKG-INFO NEWS
%{_bindir}/*
%{python_sitelib}/*

%changelog
* Thu Jan 10 2013 Paul Egan <paulegan@rockpack.com> - 1.0.1-2
- Initial release

