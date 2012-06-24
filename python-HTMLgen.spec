%define module HTMLgen

Summary:	Class library to create HTML documents from within Python  
Summary(pl):	Modul do tworzenia domument�w w HTML przy uzyciu Pythona  
Name:		python-%{module}
Version:	2.2.2
Release:	4
Copyright:	Distributable
Group:		Development/Languages/Python
Group(pl):	Programowanie/J�zyki/Python
Source:		%{module}.tgz 
Patch:		%{name}-fixpaths.patch
Requires:	python >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTMLgen is a class library for the generation of HTML documents with Python
scripts. It's used when you want to create HTML pages containing
information which changes from time to time. For example you might want to
have a page which provides an overall system summary of data collected
nightly. Or maybe you have a catalog of data and images that you would like
formed into a spiffy set of web pages for the world to browse. Python is a
great scripting language for these tasks and with HTMLgen it's very
straightforward to construct objects which are rendered out into
consistently structured web pages. Of course, CGI scripts written in Python
can take advantage of these classes as well.

This software should work on both Unix and Macintosh and Win32 platforms
running Python 1.3 or greater. (HTMLcalendar.py requires 1.4) If you are
running 1.5 the new re and string module enhancements are used for
performance.

%description -l pl 
HTMLGen jest modu�em do tworzenia dokument�w w HTML'u za pomoc� skrypt�w w
Pythonie. Jest przydatny do generowania stron WWW zawieraj�cych okresowo
zmieniaj�ce sie informacje. Na przyk�ad stron� zawieraj�c� dzienne
podsumowania statystyki wykorzystania serwera. Innym typowym zastosowaniem
jest przygotowywanie strony zawieraj�cej opis i odnosniki do rysunk�w
znajduj�cych sie w okreslonym katalogu, tak aby mo�na je by�o �atwo ogl�da�
przez WWW. Python jest dobrym j�zykiem do programowania takich zada�, a
wykorzystanie biblioteki HTMLGen znacznie u�atwia konstruowanie obiekt�w,
kt�re po przetworzeniu przez t� bibliotek� utworz� sp�jn� stron� WWW.
Oczywi�cie sktypty CGI pisane w Pythonie r�wnie� mog� robi� u�ytek z tej
bilioteki.

%prep
%setup -q -n HTMLgen
%patch -p0

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/HTMLgen

mv *.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/HTMLgen
echo %{module} > $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/%{module}.pth

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT
					
%files
%defattr(644,root,root,755)
%doc {README,ChangeLog}.gz data html image *.rc
%{_libdir}/python1.5/site-packages/HTMLgen
%{_libdir}/python1.5/site-packages/HTMLgen.pth
