Summary:	GData access library
Summary(pl.UTF-8):	Biblioteka dostępu poprzez protokół GData
Name:		libgdata
Version:	0.14.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdata/0.14/%{name}-%{version}.tar.xz
# Source0-md5:	0442d97eb76294a1e7629decbe7aa2fa
URL:		http://live.gnome.org/libgdata
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.9
BuildRequires:	gcr-devel >= 3
BuildRequires:	gdk-pixbuf2-devel >= 2.14
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common >= 3.6.0
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gobject-introspection-devel >= 0.9.7
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	intltool >= 0.40.0
BuildRequires:	liboauth-devel >= 0.9.4
BuildRequires:	libsoup-devel >= 2.38.0
BuildRequires:	libsoup-gnome-devel >= 2.38.0
BuildRequires:	libtool >= 2:2
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.32.0
Requires:	gnome-online-accounts >= 3.2.0
Requires:	liboauth >= 0.9.4
Requires:	libsoup >= 2.38.0
Requires:	libsoup-gnome >= 2.38.0
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
Requires:	glib2-devel >= 1:2.32.0
Requires:	gnome-online-accounts-devel >= 3.2.0
Requires:	liboauth-devel >= 0.9.4
Requires:	libsoup-devel >= 2.38.0
Requires:	libsoup-gnome-devel >= 2.38.0
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

%description -n vala-libgdata
libgdata API for Vala language.

%description -n vala-libgdata -l pl.UTF-8
API libgdata dla języka Vala.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgdata.la

%find_lang gdata

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f gdata.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgdata.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdata.so.13
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
