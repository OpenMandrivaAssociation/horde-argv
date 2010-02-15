%define prj    Argv

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-argv
Version:       0.1.0
Release:       %mkrel 1
Summary:       Horde command-line argument parsing package
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): %{_bindir}/pear
Requires:      php-pear
Requires:      php-pear-channel-horde
BuildRequires: horde-framework
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This package provides classes for parsing command line arguments with
various actions, providing help, grouping options, and more.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package*.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Argv
%{peardir}/Horde/Argv/AmbiguousOptionException.php
%{peardir}/Horde/Argv/BadOptionException.php
%{peardir}/Horde/Argv/Exception.php
%{peardir}/Horde/Argv/HelpFormatter.php
%{peardir}/Horde/Argv/IndentedHelpFormatter.php
%{peardir}/Horde/Argv/Option.php
%{peardir}/Horde/Argv/OptionConflictException.php
%{peardir}/Horde/Argv/OptionContainer.php
%{peardir}/Horde/Argv/OptionException.php
%{peardir}/Horde/Argv/OptionGroup.php
%{peardir}/Horde/Argv/OptionValueException.php
%{peardir}/Horde/Argv/Parser.php
%{peardir}/Horde/Argv/TitledHelpFormatter.php
%{peardir}/Horde/Argv/Values.php

