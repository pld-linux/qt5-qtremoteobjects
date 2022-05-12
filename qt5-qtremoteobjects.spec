#
# Conditional build:
%bcond_without	doc	# Documentation

%define		orgname		qtremoteobjects
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qttools_ver		%{version}
Summary:	The Qt5 RemoteObjects library
Summary(pl.UTF-8):	Biblioteka Qt5 RemoteObjects
Name:		qt5-%{orgname}
Version:	5.15.4
Release:	2
License:	LGPL v3 or GPL v2+ or commercial
Group:		X11/Libraries
Source0:	https://download.qt.io/official_releases/qt/5.15/%{version}/submodules/%{orgname}-everywhere-opensource-src-%{version}.tar.xz
# Source0-md5:	8f1d4530535e8a7aae7391906895f479
URL:		https://www.qt.io/
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Network-devel >= %{qtbase_ver}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	pkgconfig
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_ver}
BuildRequires:	qt5-doc-common >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 RemoteObjects library.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera bibliotekę Qt5 RemoteObjects.

%package -n Qt5RemoteObjects
Summary:	The Qt5 RemoteObjects library
Summary(pl.UTF-8):	Biblioteka Qt5 RemoteObjects
Group:		X11/Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}

%description -n Qt5RemoteObjects
Qt5 RemoteObjects library.

%description -n Qt5RemoteObjects -l pl.UTF-8
Biblioteka Qt5 RemoteObjects.

%package -n Qt5RemoteObjects-devel
Summary:	Qt5 RemoteObjects - development files
Summary(pl.UTF-8):	Biblioteka Qt5 RemoteObjects - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Network-devel >= %{qtbase_ver}
Requires:	Qt5RemoteObjects = %{version}-%{release}

%description -n Qt5RemoteObjects-devel
Qt5 RemoteObjects - development files.

%description -n Qt5RemoteObjects-devel -l pl.UTF-8
Biblioteka Qt5 RemoteObjects - pliki programistyczne.

%package doc
Summary:	Qt5 RemoteObjects documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 RemoteObjects w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc
Qt5 RemoteObjects documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do biblioteki Qt5 RemoteObjects w formacie HTML.

%package doc-qch
Summary:	Qt5 RemoteObjects documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 RemoteObjects w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc-qch
Qt5 RemoteObjects documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do biblioteki Qt5 RemoteObjects w formacie QCH.

%package examples
Summary:	Qt5 RemoteObjects examples
Summary(pl.UTF-8):	Przykłady do biblioteki Qt5 RemoteObjects
Group:		X11/Development/Libraries
BuildArch:	noarch

%description examples
Qt5 RemoteObjects examples.

%description examples -l pl.UTF-8
Przykłady do biblioteki Qt5 RemoteObjects.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version}

%build
%{qmake_qt5}
%{__make}
%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.??
# obsoleted by pkg-config; Qt5RepParser.la is bogus (header only library)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5RemoteObjects -p /sbin/ldconfig
%postun	-n Qt5RemoteObjects -p /sbin/ldconfig

%files -n Qt5RemoteObjects
%defattr(644,root,root,755)
%doc LICENSE.GPL3-EXCEPT dist/changes-*
# R: Qt5Core Qt5Network
%attr(755,root,root) %{_libdir}/libQt5RemoteObjects.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5RemoteObjects.so.5
# R: Qt5Core
%attr(755,root,root) %{qt5dir}/bin/repc
%dir %{qt5dir}/qml/QtQml/RemoteObjects
# R: Qt5Core Qt5Qml Qt5RemoteObjects
%attr(755,root,root) %{qt5dir}/qml/QtQml/RemoteObjects/libqtqmlremoteobjects.so
%{qt5dir}/qml/QtQml/RemoteObjects/plugins.qmltypes
%{qt5dir}/qml/QtQml/RemoteObjects/qmldir
%dir %{qt5dir}/qml/QtRemoteObjects
# R: Qt5Core Qt5Qml Qt5RemoteObjects
%attr(755,root,root) %{qt5dir}/qml/QtRemoteObjects/libqtremoteobjects.so
%{qt5dir}/qml/QtRemoteObjects/plugins.qmltypes
%{qt5dir}/qml/QtRemoteObjects/qmldir

%files -n Qt5RemoteObjects-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5RemoteObjects.so
%{_libdir}/libQt5RemoteObjects.prl
%{_libdir}/libQt5RepParser.prl
%{_includedir}/qt5/QtRemoteObjects
%{_includedir}/qt5/QtRepParser
%{_pkgconfigdir}/Qt5RemoteObjects.pc
%{_pkgconfigdir}/Qt5RepParser.pc
%{_libdir}/cmake/Qt5RemoteObjects
%{_libdir}/cmake/Qt5RepParser
%{qt5dir}/mkspecs/features/remoteobjects_repc.prf
%{qt5dir}/mkspecs/features/repc*.pri
%{qt5dir}/mkspecs/features/repparser.prf
%{qt5dir}/mkspecs/modules/qt_lib_remoteobjects.pri
%{qt5dir}/mkspecs/modules/qt_lib_remoteobjects_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_repparser.pri
%{qt5dir}/mkspecs/modules/qt_lib_repparser_private.pri

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtremoteobjects

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtremoteobjects.qch
%endif

%files examples
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
%{_examplesdir}/qt5/remoteobjects
