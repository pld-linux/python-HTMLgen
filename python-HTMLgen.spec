
%define		module	HTMLgen

Summary:	Class library to create HTML documents from within Python
Summary(pl):	Modu³ do tworzenia dokumentów w HTML przy u¿yciu Pythona
Name:		python-%{module}
Version:	2.2.2
Release:	6
License:	distributable
Group:		Development/Languages/Python
Source0:	http://starship.python.net/crew/friedrich/%{module}.tgz
# Source0-md5:	cd20f8b63d3215e57289ddbf56c97f48
Patch0:		%{name}-fixpaths.patch
URL:		http://starship.python.net/crew/friedrich/HTMLgen/html/main.html
BuildRequires:	python-devel >= 2.2.1
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

%description -l pl
HTMLGen jest modu³em do tworzenia dokumentów w HTML-u za pomoc±
skryptów w Pythonie. Jest przydatny do generowania stron WWW
zawieraj±cych okresowo zmieniaj±ce sie informacje. Na przyk³ad stronê
zawieraj±c± dzienne podsumowania statystyki wykorzystania serwera.
Innym typowym zastosowaniem jest przygotowywanie strony zawieraj±cej
opis i odnosniki do rysunków znajduj±cych sie w okreslonym katalogu,
tak aby mo¿na je by³o ³atwo ogl±daæ przez WWW. Python jest dobrym
jêzykiem do programowania takich zadañ, a wykorzystanie biblioteki
HTMLgen znacznie u³atwia konstruowanie obiektów, które po
przetworzeniu przez tê bibliotekê utworz± spójn± stronê WWW.
Oczywi¶cie sktypty CGI pisane w Pythonie równie¿ mog± robiæ u¿ytek z
tej bilioteki.

%prep
%setup -q -n HTMLgen
%patch -p0

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
