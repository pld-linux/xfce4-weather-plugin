%define		_name	xfce4-weather
Summary:	A weather plugin for the Xfce panel
Summary(pl):	Wtyczka panelu Xfce pokazuj±ca pogodê
Name:		xfce4-weather-plugin
Version:	0.4.9
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://download.berlios.de/xfce-goodies/%{name}-%{version}.tar.gz
# Source0-md5:	1d5ba253c8eae5a9ad5e3d7002a0dae0
URL:		http://xfce-goodies.berlios.de/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 4.1.90
Requires:	xfce4-panel >= 4.1.90
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A weather plugin for the Xfce panel.

%description -l pl
Wtyczka dla panelu Xfce wy¶wietlaj±ca pogodê.

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

%find_lang %{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/*.so
%{_datadir}/xfce4/weather
