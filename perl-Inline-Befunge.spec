#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Befunge
Summary:	Inline::Befunge Perl module
Summary(cs):	Modul Inline::Befunge pro Perl
Summary(da):	Perlmodul Inline::Befunge
Summary(de):	Inline::Befunge Perl Modul
Summary(es):	Módulo de Perl Inline::Befunge
Summary(fr):	Module Perl Inline::Befunge
Summary(it):	Modulo di Perl Inline::Befunge
Summary(ja):	Inline::Befunge Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Inline::Befunge ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Inline::Befunge
Summary(pl):	Modu³ Perla Inline::Befunge
Summary(pt):	Módulo de Perl Inline::Befunge
Summary(pt_BR):	Módulo Perl Inline::Befunge
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Inline::Befunge
Summary(sv):	Inline::Befunge Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Inline::Befunge
Summary(zh_CN):	Inline::Befunge Perl Ä£¿é
Name:		perl-Inline-Befunge
Version:	0.04
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-Language-Befunge >= 0.36
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Befunge - write Perl subs in Befunge.

%description -l pl
Modu³ Inline::Befunge - pozwalaj±cy na pisanie procedur Perla w jêzyku
Befunge.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Inline/Befunge.pm
%{_mandir}/man3/*
