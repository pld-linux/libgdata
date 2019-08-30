#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	GData access library
Summary(pl.UTF-8):	Biblioteka dostępu poprzez protokół GData
Name:		libgdata
Version:	0.17.11
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdata/0.17/%{name}-%{version}.tar.xz
# Source0-md5:	7b98e9059255d8a2fb147c4e727230a8
URL:		https://wiki.gnome.org/Projects/libgdata
BuildRequires:	gcr-devel >= 3
# for tests only
BuildRequires:	gdk-pixbuf2-devel >= 2.14
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-online-accounts-devel >= 3.8
BuildRequires:	gobject-introspection-devel >= 0.9.7
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	gtk-doc >= 1.25
BuildRequires:	json-glib-devel >= 0.15
BuildRequires:	liboauth-devel >= 0.9.4
BuildRequires:	libsoup-devel >= 2.56.0
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	uhttpmock-devel >= 0.5.0
BuildRequires:	vala
BuildRequires:	vala-gnome-online-accounts
BuildRequires:	xz
Requires:	glib2 >= 1:2.44.0
Requires:	gnome-online-accounts-libs >= 3.8
Requires:	json-glib >= 0.15
Requires:	liboauth >= 0.9.4
Requires:	libsoup >= 2.56.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgdata is a GLib-based library for accessing online service APIs
using the GData protocol - most notably, Google's services. It
provides APIs to access the common Google services, and has full
asynchronous support.

%description -l pl.UTF-8
libgdata to oparta na GLibie biblioteka służąca do dostępu do API
serwisów sieciowych przy użyciu protokołu GData - głównie serwisów
firmy Google. Biblioteka udostępnia API do popularnych serwisów Google
i ma pełną obsługę komunikacji asynchronicznej.

%package devel
Summary:	Header files for libgdata library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgdata
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gcr-devel >= 3
Requires:	glib2-devel >= 1:2.44.0
Requires:	gnome-online-accounts-devel >= 3.8
Requires:	json-glib-devel >= 0.15
Requires:	liboauth-devel >= 0.9.4
Requires:	libsoup-devel >= 2.56.0
Requires:	libxml2-devel >= 1:2.6.26

%description devel
Header files and support files necessary to compile applications using
libgdata.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz pomocnicze potrzebne do kompilowania aplikacji
wykorzystujących bibliotekę libgdata.

%package static
Summary:	libgdata static library
Summary(pl.UTF-8):	Statyczna biblioteka libgdata
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libgdata library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę libgdata.

%package apidocs
Summary:	libgdata API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgdata
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
libgdata API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgdata.

%package -n vala-libgdata
Summary:	libgdata API for Vala language
Summary(pl.UTF-8):	API libgdata dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.16
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-libgdata
libgdata API for Vala language.

%description -n vala-libgdata -l pl.UTF-8
API libgdata dla języka Vala.

%prep
%setup -q

%if %{with static_libs}
%{__sed} -i -e '/^libgdata_lib =/ s/shared_library/library/' gdata/meson.build
%endif

%build
%meson build \
	-Dinstalled_tests=false \
	-Dman=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang gdata

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f gdata.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libgdata.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdata.so.22
%{_libdir}/girepository-1.0/GData-0.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdata.so
%{_datadir}/gir-1.0/GData-0.0.gir
%{_includedir}/libgdata
%{_pkgconfigdir}/libgdata.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdata.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gdata

%files -n vala-libgdata
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libgdata.deps
%{_datadir}/vala/vapi/libgdata.vapi
