Summary:	A weather plugin for the XFce4 panel
Summary(pl):	Wtyczka panelu XFce4 pokazuj±ca pogodê
Name:		xfce4-weather-plugin
Version:	0.3.9.1
Release:	2
License:	BSD
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.bz2
# Source0-md5:	a124a22ba65d0667f513ad6fae83c626
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 4.0.0
Requires:	xfce4-panel >= 4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A weather plugin for the XFce4 panel.

%description -l pl
Wtyczka dla panelu XFce4 wy¶wietlaj±ca pogodê.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I %{_datadir}/xfce4/m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
%{_datadir}/xfce4/weather
