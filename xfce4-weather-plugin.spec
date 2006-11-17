Summary:	A weather plugin for the Xfce panel
Summary(pl):	Wtyczka panelu Xfce pokazuj±ca pogodê
Name:		xfce4-weather-plugin
Version:	0.5.99.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-weather-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	dfc5b89a173b7da6fabe56bf73d41321
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-weather-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.3.99.1
BuildRequires:	xfce4-panel-devel >= 4.3.99.1
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A weather plugin for the Xfce panel.

%description -l pl
Wtyczka dla panelu Xfce wy¶wietlaj±ca pogodê.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-weather-plugin
%{_datadir}/xfce4/panel-plugins/weather.desktop
%{_datadir}/xfce4/weather
%{_iconsdir}/hicolor/*/*/xfce4-weather.png
