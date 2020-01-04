%define	oname	QuiteRSS
%define lname %(echo %oname | tr [:upper:] [:lower:])

Summary:	RSS/Atom feed reader written on Qt
Name:		%{lname}
Version:	0.19.1
Release:	1
License:	GPLv3+
Group:		Networking/News
URL:		https://quiterss.org/
Source0:	https://quiterss.org/files/%{version}/%{oname}-%{version}-src.tar.gz

BuildRequires:  qt5-linguist-tools	
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  qtsingleapplication-qt5-devel
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qtbase-devel
Requires:       qt5-database-plugin-sqlite3

%description
QuiteRSS is RSS/Atom feed reader written on Qt.

%files -f %{name}.lang
%doc AUTHORS CHANGELOG COPYING README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/sound/notification.wav
%{_datadir}/%{name}/style/*.qss
%{_datadir}/%{name}/style/*.css

#----------------------------------------------------------------------------

%prep
%setup -q -c -n %{oname}-%{version}-src

%build
%qmake_qt5 CONFIG+=release PREFIX=%{_prefix} SYSTEMQTSA=1 %{oname}.pro
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%find_lang %{name} --with-qt --without-mo

%files -f %{name}.lang
%doc AUTHORS CHANGELOG README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/sound/
%{_datadir}/%{name}/style/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png

