Summary:	SQLite Database Browser
Name:		sqlitebrowser
Version:	1.3
Release:	1
License:	Public domain
Group:		Applications/Databases/Interfaces
Source0:	http://dl.sourceforge.net/sqlitebrowser/%{name}-%{version}-src.tar.gz
# Source0-md5:	d4dc8c6a95d5f005e493f3a5a2a10491
URL:		http://sqlitebrowser.sourceforge.net/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQLite Database Browser is a freeware, public domain, open source
visual tool used to create, design and edit database files compatible
with SQLite. It is meant to be used for users and developers that want
to create databases, edit and search data using a familiarspreadsheet-
-like interface, without the need to learn complicated SQL commands.

%prep
%setup -q -n %{name}

%build
export QTDIR="%{_prefix}"
export QMAKESPEC="linux-g++"

qmake sqlitedbbrowser.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install sqlitebrowser/sqlitebrowser $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc sqlitebrowser/LICENSING
%attr(755,root,root) %{_bindir}/*
