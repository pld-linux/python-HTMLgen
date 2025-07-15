
%define		module	HTMLgen

Summary:	Class library to create HTML documents from within Python
Summary(pl.UTF-8):	Moduł do tworzenia dokumentów w HTML przy użyciu Pythona
Name:		python-%{module}
Version:	2.2.2
Release:	10
License:	distributable
Group:		Development/Languages/Python
Source0:	http://starship.python.net/crew/friedrich/%{module}.tgz
# Source0-md5:	cd20f8b63d3215e57289ddbf56c97f48
Patch0:		%{name}-fixpaths.patch
URL:		http://starship.python.net/crew/friedrich/HTMLgen/html/main.html
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTMLgen is a class library for the generation of HTML documents with
Python scripts. It's used when you want to create HTML pages
containing information which changes from time to time. For example
you might want to have a page which provides an overall system summary
of data collected nightly. Or maybe you have a catalog of data and
images that you would like formed into a spiffy set of web pages for
the world to browse. Python is a great scripting language for these
tasks and with HTMLgen it's very straightforward to construct objects
which are rendered out into consistently structured web pages. Of
course, CGI scripts written in Python can take advantage of these
classes as well.

This software should work on both Unix and Macintosh and Win32
platforms running Python 1.3 or greater. (HTMLcalendar.py requires
1.4) If you are running 1.5 the new re and string module enhancements
are used for performance.

%description -l pl.UTF-8
HTMLGen jest modułem do tworzenia dokumentów w HTML-u za pomocą
skryptów w Pythonie. Jest przydatny do generowania stron WWW
zawierających okresowo zmieniające sie informacje. Na przykład stronę
zawierającą dzienne podsumowania statystyki wykorzystania serwera.
Innym typowym zastosowaniem jest przygotowywanie strony zawierającej
opis i odnośniki do rysunków znajdujących sie w określonym katalogu,
tak aby można je było łatwo oglądać przez WWW. Python jest dobrym
językiem do programowania takich zadań, a wykorzystanie biblioteki
HTMLgen znacznie ułatwia konstruowanie obiektów, które po
przetworzeniu przez tę bibliotekę utworzą spójną stronę WWW.
Oczywiście skrypty CGI pisane w Pythonie również mogą robić użytek z
tej biblioteki.

%prep
%setup -q -n HTMLgen
%patch -P0 -p0

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/HTMLgen

mv -f *.py $RPM_BUILD_ROOT%{py_sitescriptdir}/HTMLgen
echo %{module} > $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}.pth

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog data html image *.rc
%{py_sitescriptdir}/HTMLgen
%{py_sitescriptdir}/HTMLgen.pth
