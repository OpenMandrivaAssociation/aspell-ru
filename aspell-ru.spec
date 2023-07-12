%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.99f7-1
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Russian
%define languagecode ru
%define lc_ctype ru_RU

Summary:	%{languageenglazy} files for aspell
Summary(ru):	Русская проверка орфографии
Name:		aspell-%{languagecode}
Version:	0.99.f7.1
Release:	1
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspell.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= %{aspell_ver}
Requires:	aspell >= %{aspell_ver}
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	spell-ru
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} doc/*

%files
%doc README.%{languagecode} Copyright doc/*
%{_libdir}/aspell-%{aspell_ver}/*

