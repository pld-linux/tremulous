#
# Conditional build:
%bcond_with	altivec		# use altivec, no runtime detection
%bcond_without	openal		# don't use OpenAL

Summary:	First-person shooter with elements of strategy game
Summary(pl.UTF-8):	Strzelanina w pierwszej osobie z elementami strategii
Name:		tremulous
Version:	1.1.0
Release:	5
License:	GPL
Group:		X11/Applications/Games
Source0:	%{name}-%{version}-src.tar.gz
# Source0-md5:	13382bfd1c17677ff97109a457f4c488
Source2:	tremded.init
Source3:	tremded.sysconfig
Source4:	%{name}.desktop
Source5:	%{name}-smp.desktop
Patch0:		%{name}-backport.patch
Patch1:		%{name}-Makefile.patch
Patch2:		%{name}-LIBDIR.patch
Patch3:		%{name}-alpha.patch
URL:		http://www.tremulous.net/
%if %{with openal}
BuildRequires:	OpenAL-devel
%endif
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	curl-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
Requires:	%{name}-common = %{version}-%{release}
Requires:	OpenGL
Suggests:	curl-lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-ffast-math -funroll-loops -fomit-frame-pointer -fno-strict-aliasing
%define		specflags_ia32	-falign-loops=2 -falign-jumps=2 -falign-functions=2
%if %{with altivec}
%define		specflags_ppc	-maltivec -mabi=altivec
%endif
%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Tremulous is a free, open source game that blends a team based FPS
(first-person shooter) with elements of an RTS (real-time strategy).
Players can choose from 2 unique races, aliens and humans. Both teams
are able to build working structures in-game like an RTS. These
structures provide many functions, the most important being spawning.
The designated builders must ensure there are spawn structures or
other players will not be able to rejoin the game after death. Other
structures provide automated base defense (to some degree), healing
functions and much more...

Player advancement is different depending on which team you are on. As
a human, players are rewarded with credits for each alien kill. These
credits may be used to purchase new weapons and upgrades from the
"Armoury". The alien team advances quite differently. Upon killing a
human foe, the alien is able to evolve into a new class. The more
kills gained the more powerful the classes available.

The overall objective behind Tremulous is to eliminate the opposing
team. This is achieved by not only killing the opposing players but
also removing their ability to respawn by destroying their spawn
structures.

%description -l pl.UTF-8
Tremulous to wolnodostępna gra z otwartymi źródłami łącząca cechy
drużynowej FPS (strzelaniny widzianej oczami bohatera) z elementami
RTS (strategii w czasie rzeczywistym). Gracze mogą wybrać między dwoma
odmiennymi rasami: obcy lub ludzie. Obie drużyny mogą budować
funkcjonalne struktury jak w grach RTS. Struktury te udostępniają
wiele funkcji, najważniejszą jest "rodzenie". Wyznaczeni budowniczy
muszą muszą zapewnić istnienie "rodzących" struktur, w przeciwnym
przypadku gracze nie będą mogli powrócić do gry po śmierci. Inne
struktury zapewniają zautomatyzowaną obronę bazy (do pewnego stopnia),
funkcje leczenia i wiele więcej...

Wynagrodzenie graczy jest różne w zależności od drużyny. Jako ludzie
gracze otrzymują pieniądze za każdego zabitego obcego. Można je
przeznaczyć na zakup nowej broni lub ulepszenie zbroi. Obcy są
wynagradzani w inny sposób. Po zabiciu przeciwnika obcy może
przepoczwarzyć się w osobnika innej klasy. Im więcej ludzi się zabije
tym silniejszej klasy obcy są dostępni.

Ogólnym celem gry jest całkowite wyeliminowanie przeciwnej drużyny.
Osiąga się to nie tylko zabijając wszystkich jej graczy lecz także
niszcząc wszystkie "rodzące" struktury.

%package server
Summary:	Tremulous dedicated server
Summary(pl.UTF-8):	Serwer dedykowany Tremulousa
Group:		Applications/Games
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(triggerpostun):	/usr/sbin/usermod
Requires:	%{name}-common = %{version}-%{release}
Requires:	psmisc
Requires:	rc-scripts
Requires:	screen
Provides:	group(tremulous)
Provides:	user(tremulous)

%description server
Tremulous dedicated server.

%description server -l pl.UTF-8
Serwer dedykowany Tremulousa.

%package smp
Summary:	Tremulous for SMP
Summary(pl.UTF-8):	Tremulous dla SMP
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description smp
Tremulous is a free, open source game that blends a team based FPS
(first-person shooter) with elements of an RTS (real-time strategy).
Players can choose from 2 unique races, aliens and humans. Both teams
are able to build working structures in-game like an RTS. These
structures provide many functions, the most important being spawning.
The designated builders must ensure there are spawn structures or
other players will not be able to rejoin the game after death. Other
structures provide automated base defense (to some degree), healing
functions and much more...

Player advancement is different depending on which team you are on. As
a human, players are rewarded with credits for each alien kill. These
credits may be used to purchase new weapons and upgrades from the
"Armoury". The alien team advances quite differently. Upon killing a
human foe, the alien is able to evolve into a new class. The more
kills gained the more powerful the classes available.

The overall objective behind Tremulous is to eliminate the opposing
team. This is achieved by not only killing the opposing players but
also removing their ability to respawn by destroying their spawn
structures.

Version for multi processor machine.

%description smp -l pl.UTF-8
Tremulous to wolnodostępna gra z otwartymi źródłami łącząca cechy
drużynowej FPS (strzelaniny widzianej oczami bohatera) z elementami
RTS (strategii w czasie rzeczywistym). Gracze mogą wybrać między dwoma
odmiennymi rasami: obcy lub ludzie. Obie drużyny mogą budować
funkcjonalne struktury jak w grach RTS. Struktury te udostępniają
wiele funkcji, najważniejszą jest "rodzenie". Wyznaczeni budowniczy
muszą muszą zapewnić istnienie "rodzących" struktur, w przeciwnym
przypadku gracze nie będą mogli powrócić do gry po śmierci. Inne
struktury zapewniają zautomatyzowaną obronę bazy (do pewnego stopnia),
funkcje leczenia i wiele więcej...

Wynagrodzenie graczy jest różne w zależności od drużyny. Jako ludzie
gracze otrzymują pieniądze za każdego zabitego obcego. Można je
przeznaczyć na zakup nowej broni lub ulepszenie zbroi. Obcy są
wynagradzani w inny sposób. Po zabiciu przeciwnika obcy może
przepoczwarzyć się w osobnika innej klasy. Im więcej ludzi się zabije
tym silniejszej klasy obcy są dostępni.

Ogólnym celem gry jest całkowite wyeliminowanie przeciwnej drużyny.
Osiąga się to nie tylko zabijając wszystkich jej graczy lecz także
niszcząc wszystkie "rodzące" struktury.

Wersja dla maszyny wieloprocesorowej.

%package common
Summary:	Common files for Tremulous
Summary(pl.UTF-8):	Pliki wspólne dla Tremulousa
Group:		Applications/Games
Requires(triggerpostun):	/usr/sbin/groupdel
Requires(triggerpostun):	/usr/sbin/userdel
Requires:	%{name}-data = %{version}

%description common
Common files for Tremulous server and player game.

%description common -l pl.UTF-8
Pliki wspólne Tremulous dla serwera i trybu gracza.

%prep
%setup -q -n %{name}-%{version}-src
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%{__sed} -i -e 's/-Werror//' src/tools/asm/Makefile
%{__sed} -i -e '/OP_BLOCK_COPY not dword aligned/s#^#//#' src/qcommon/vm_interpreted.c
%{__sed} -i -e 's/^all:.*/all: makedirs tools targets/' Makefile
%{__sed} -i -e 's/$(CC)  -o $@/$(CC) -o $@ $(REAL_LDFLAGS)/' Makefile

%build
cat << 'EOF' > Makefile.local
BUILD_CLIENT    = 1
BUILD_CLIENT_SMP= 1
BUILD_SERVER    = 1
BUILD_GAME_SO   = 1
BUILD_GAME_QVM  = 0
%if !%{with openal}
USE_OPENAL      = 0
%endif

USE_LOCAL_HEADERS = 0
USE_CURL_DLOPEN = 1

override BR = rel
override B = rel

override CFLAGS := %{rpmcflags} \
	-DDEFAULT_BASEDIR=\"%{_datadir}/games/%{name}\" \
	-DLIBDIR=\"%{_libdir}/%{name}\" \
	-Wall -Wimplicit -Wstrict-prototypes \
	-DUSE_SDL_VIDEO=1 -DUSE_SDL_SOUND=1 %(sdl-config --cflags) \
	-DUSE_CURL=1 -DUSE_CURL_DLOPEN=1 \
%if %{with openal}
	-DUSE_OPENAL=1 \
%endif
%ifnarch %{ix86} %{x8664}
	-DNO_VM_COMPILED \
%endif  
	-DNDEBUG -MMD

override LCC_CFLAGS := $(CFLAGS) -MMD
override Q3ASM_CFLAGS := $(CFLAGS)

REAL_LDFLAGS := %{rpmldflags}

override CC := %{__cc}
EOF

%{__make} -j1 all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/%{name}/base} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_libdir}/%{name}/base} \
	$RPM_BUILD_ROOT/var/games/tremulous

install rel/%{name}.* $RPM_BUILD_ROOT%{_bindir}/%{name}
install rel/%{name}-smp.* $RPM_BUILD_ROOT%{_bindir}/%{name}-smp
install rel/tremded.* $RPM_BUILD_ROOT%{_bindir}/tremded
install rel/base/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}/base

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/tremded
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/tremded
install misc/%{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}/%{name}-smp.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%pre server
%groupadd -P %{name}-server -g 38 tremulous
%useradd -P %{name}-server -u 124 -d /var/games/tremulous -s /bin/sh -c "Tremulous" -g tremulous tremulous

%post server
/sbin/chkconfig --add tremded
%service tremded restart "Tremulous server"

%preun server
if [ "$1" = "0" ]; then
	%service tremded stop
	/sbin/chkconfig --del tremded
fi

%postun server
if [ "$1" = "0" ]; then
	%userremove tremulous
	%groupremove tremulous
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop

%files common
%defattr(644,root,root,755)
%doc ChangeLog COPYING
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/base
%{_pixmapsdir}/%{name}.xpm
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/base
%attr(755,root,root) %{_libdir}/%{name}/base/*.so

%files server
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/tremded
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/tremded
%attr(755,root,root) %{_bindir}/tremded
%attr(750,tremulous,tremulous) /var/games/tremulous

%files smp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-smp
%{_desktopdir}/%{name}-smp.desktop
