%define upstream_name    DateTime-Event-ICal
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.11
Release:	3

Summary:	Perl DateTime extension for computing rfc2445 recurrences
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/DateTime-Event-ICal-0.11.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Event::Recurrence)
BuildArch:	noarch

%description
This module provides convenience methods that let you easily create
'DateTime::Set' objects for rfc2445 style recurrences.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 653402
- rebuild for updated spec-helper

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 542972
- import perl-DateTime-Event-ICal


* Thu May 06 2010 cpan2dist 0.10-1mdv
- initial mdv release, generated with cpan2dist

