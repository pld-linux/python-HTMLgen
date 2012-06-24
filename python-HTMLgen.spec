Summary: class library to create HTML documents from within Python  
Name: python-HTMLgen
Version: 2.1 
Release: 3
Copyright: distributable
Group: Development/Languages/Python
Group(pl): Programowanie/J�zyki/Python
Source0: HTMLgen.tar.gz 
Source1: HTMLgen.pth
Patch0: python-HTMLgen-fixpaths.patch
Icon: linux-python-small.gif 
BuildRoot:	/tmp/%{name}-%{version}-root
Requires: python >= 1.5
BuildArchitectures: noarch
Summary(pl): Modul do tworzenia domument�w w HTML przy uzyciu Pythona  

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
HTMLGen jest modu�em do tworzenia dokument�w w HTML'u za pomoc� skrypt�w
w Pythonie. Jest przydatny do generowania stron WWW zawieraj�cych okresowo
zmieniaj�ce sie informacje. Na przyk�ad stron� zawieraj�c� dzienne 
podsumowania statystyki wykorzystania serwera. Innym typowym zastosowaniem 
jest przygotowywanie strony zawieraj�cej opis i odnosniki do rysunk�w 
znajduj�cych sie w okreslonym katalogu, tak aby mo�na je by�o �ato ogl�da� 
przez www. Python jest dobrym j�zykiem do programowania takich zada�,
a wyko�ystanie biblioteki HTMLGen znacznie u�atwia konstruowanie obiekt�w
kt�re po przetwo�eniu przez t� bibliotek� utworz� sp�jn� stron� www.
Oczywi�cie sktypty CGI pisane w Pythonie r�wnie� mog� robi� u�ytek z tej 
bilioteki.

%prep
%setup -n HTMLgen
%patch -p0

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/HTMLgen
install -m 555 $RPM_SOURCE_DIR/HTMLgen.pth $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/
install -m 555 *.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/HTMLgen

%clean
rm -rf $RPM_BUILD_ROOT
					
%files
%doc data html image README ChangeLog *.rc *.css
%{_libdir}/python1.5/site-packages/HTMLgen
%{_libdir}/python1.5/site-packages/HTMLgen.pth
