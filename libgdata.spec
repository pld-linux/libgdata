Summary:	GData access library
Name:		libgdata
Version:	0.13.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdata/0.13/%{name}-%{version}.tar.xz
# Source0-md5:	8790767a3700d146e859ce870229f8e7
URL:		http://live.gnome.org/libgdata
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.9
BuildRequires:	gcr-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.14
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common >= 3.6.0
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gobject-introspection-devel >= 0.9.7
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	intltool >= 0.40.0
BuildRequires:	liboauth-devel >= 0.9.4
BuildRequires:	libsoup-devel >= 2.38.0
BuildRequires:	libsoup-gnome-devel >= 2.38.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libsoup >= 2.38.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgdata is a GLib-based library for accessing online service APIs
using the GData protocol - most notably, Google's services. It
provides APIs to access the common Google services, and has full
asynchronous support.

%package devel
Summary:	Support files necessary to compile applications with libgdata
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libsoup-gnome-devel >= 2.38.0
Requires:	libxml2-devel >= 1:2.6.26

%description devel
Headers, and support files necessary to compile applications using
libgdata.

%package static
Summary:	libgdata static libraries
Summary(pl.UTF-8):	Statyczne biblioteki libgsf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Package contains static libraries.

%package apidocs
Summary:	libgdata API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgdata API documentation.

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
%doc AUTHORS README NEWS
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
