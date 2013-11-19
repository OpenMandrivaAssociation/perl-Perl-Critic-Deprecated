%define upstream_name    Perl-Critic-Deprecated
%define upstream_version 1.119

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Write C<$my_variable = 42> instead of C<$MyVariable = 42>
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl/Perl-Critic-Deprecated-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(English)
BuildRequires:	perl(Perl::Critic::Policy)
BuildRequires:	perl(Perl::Critic::TestUtils)
BuildRequires:	perl(Perl::Critic::Utils)
BuildRequires:	perl(Readonly)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(base)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
The included policies are:

* Perl::Critic::Policy::NamingConventions::ProhibitMixedCaseSubs

  Write '$my_variable = 42' instead of '$MyVariable = 42'. [Severity 1]

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
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.108.0-2mdv2011.0
+ Revision: 655608
- rebuild for updated spec-helper

* Wed Aug 25 2010 Jérôme Quelin <jquelin@mandriva.org> 1.108.0-1mdv2011.0
+ Revision: 573222
- import perl-Perl-Critic-Deprecated


