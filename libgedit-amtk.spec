#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	libgedit-amtk - Actions, Menus and Toolbars Kit for GTK+ applications
Summary(pl.UTF-8):	libgedit-amtk - zestaw akcji, menu i pasków narzędzi dla aplikacji GTK+
Name:		libgedit-amtk
Version:	5.9.0
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://download.gnome.org/sources/libgedit-amtk/5.9/%{name}-%{version}.tar.xz
# Source0-md5:	b48befe78b0be18d8300de52d4119067
URL:		https://gedit-technology.github.io/
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= 1:2.56
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-doc >= 1.25
BuildRequires:	meson >= 0.64
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.56
Requires:	gtk+3 >= 3.22
Obsoletes:	amtk < 5.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgedit-amtk is part of Gedit Technology
<https://gedit-technology.github.io/>.

Amtk is the acronym for "Actions, Menus and Toolbars Kit". It is a
basic GtkUIManager replacement based on GAction. It is suitable for
both a traditional UI or a modern UI with a GtkHeaderBar.

%description -l pl.UTF-8
libgedit-amtk to część projektu Gedit Technology
<https://gedit-technology.github.io/>.

Amtk to krót od "Actions, Menus and Toolbars Kit" (zestaw akcji, menu
i pasków narzędziowych). Jest to podstawowy zamiennik GtkUIManagera
oparty na GAction. Nadaje się zarówno dla tradycyjnych, jak i
nowoczesnych interfejsów użytkownika z GtkHeaderBarem.

%package devel
Summary:	Header files for Amtk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Amtk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.56
Requires:	gtk+3-devel >= 3.22
Obsoletes:	amtk-devel < 5.8

%description devel
Header files for Amtk library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Amtk.

%package static
Summary:	Static Amtk library
Summary(pl.UTF-8):	Statyczna biblioteka Amtk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	amtk-static < 5.8

%description static
Static Amtk library.

%description static -l pl.UTF-8
Statyczna biblioteka Amtk.

%package apidocs
Summary:	API documentation for Amtk library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Amtk
Group:		Documentation
Obsoletes:	amtk-apidocs < 5.8
BuildArch:	noarch

%description apidocs
API documentation for Amtk library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Amtk.

%prep
%setup -q

%build
%meson \
	%{!?with_static_libs:--default-library=shared}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang libgedit-amtk-5

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libgedit-amtk-5.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libgedit-amtk-5.so.0
%{_libdir}/girepository-1.0/Amtk-5.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgedit-amtk-5.so
%{_includedir}/libgedit-amtk-5
%{_datadir}/gir-1.0/Amtk-5.gir
%{_pkgconfigdir}/libgedit-amtk-5.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgedit-amtk-5.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgedit-amtk-5
