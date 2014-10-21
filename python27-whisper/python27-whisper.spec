Name: python27-whisper
Version: 0.9.12
Release: 1
Summary: Simple database library for storing time-series data
Group: Development/Libraries
License: ASL 2.0
URL: http://graphite-project.github.com/
Source0: https://pypi.python.org/packages/source/w/whisper/whisper-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: python27-setuptools

%description
simple database library for storing time-series data (similar in design to RRD)

%prep
%setup -q -n whisper-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Temp mv to non .py locations
pushd %{buildroot}%{_bindir}
%{__mv} rrd2whisper.py rrd2whisper
%{__mv} whisper-create.py whisper-create
%{__mv} whisper-dump.py whisper-dump
%{__mv} whisper-fetch.py whisper-fetch
%{__mv} whisper-info.py whisper-info
%{__mv} whisper-merge.py whisper-merge
%{__mv} whisper-resize.py whisper-resize
%{__mv} whisper-set-aggregation-method.py whisper-set-aggregation-method
%{__mv} whisper-update.py whisper-update
popd

%files
%{python_sitelib}/*
%{_bindir}/whisper*
%{_bindir}/rrd2whisper
