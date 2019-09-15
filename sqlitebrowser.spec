# TODO:	use system-wide QCustomPlot and QHexEdit
Summary:	DB Browser for SQLite
Name:		sqlitebrowser
Version:	3.11.2
Release:	1
License:	MPLv2/GPLv3
Group:		Applications/Databases/Interfaces
Source0:	https://github.com/sqlitebrowser/sqlitebrowser/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9991541d1f93ebcd7769ac8e15475c71
Patch0:		system-libs.patch
URL:		http://sqlitebrowser.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	antlr
BuildRequires:	cmake >= 2.8.7
BuildRequires:	qscintilla2-qt5-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	sqlite3-devel
Requires:	desktop-file-utils
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQLite Database Browser is a freeware, public domain, open source
visual tool used to create, design and edit database files compatible
with SQLite. It is meant to be used for users and developers that want
to create databases, edit and search data using a familiarspreadsheet-
-like interface, without the need to learn complicated SQL commands.

%prep
%setup -q
%patch0 -p1

%{__rm} -r libs/{antlr-*,qscintilla}

%build
mkdir build
cd build
%cmake ../ \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DQT_INCLUDE_DIR:PATH=%{_includedir}/qt5
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/appdata/sqlitebrowser.desktop.appdata.xml
