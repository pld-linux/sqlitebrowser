# TODO:	use system-wide QCustomPlot
Summary:	DB Browser for SQLite
Name:		sqlitebrowser
Version:	3.7.0
Release:	1
License:	MPLv2/GPLv3
Group:		Applications/Databases/Interfaces
Source0:	https://github.com/sqlitebrowser/sqlitebrowser/archive/v%{version}.tar.gz
# Source0-md5:	1033f076944316a713d4831bf581cf3a
URL:		http://sqlitebrowser.org/
#BuildRequires:	QCustomPlot-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	antlr
BuildRequires:	cmake >= 2.8.7
BuildRequires:	qscintilla2-qt4-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQLite Database Browser is a freeware, public domain, open source
visual tool used to create, design and edit database files compatible
with SQLite. It is meant to be used for users and developers that want
to create databases, edit and search data using a familiarspreadsheet-
-like interface, without the need to learn complicated SQL commands.

%prep
%setup -q
# use system-wide qscintilla2
sed -e '/QSCINTILLA_DIR[ }][^"]/d' -e 's/qcustomplot qscintilla2/qcustomplot/' -i CMakeLists.txt

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
