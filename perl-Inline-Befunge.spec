%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pnam	Befunge
Summary:	Inline::Befunge perl module
Summary(pl):	Modu³ perla Inline::Befunge
Name:		perl-Inline-Befunge
Version:	0.04
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.43
BuildRequires:	perl-Language-Befunge >= 0.36
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
%{__make}

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
