Summary: class library to create HTML documents from within Python  
Name: python-HTMLgen
Version: 2.1 
Release: 3
Copyright: distributable
Packager: Oliver Andrich <oli@andrich.net>
Group: Development/Languages/Python
Source0: HTMLgen.tar.gz 
Source1: HTMLgen.pth
Patch0: python-HTMLgen-fixpaths.patch
Icon: linux-python-small.gif 
BuildRoot: /tmp/py-root
Requires: python >= 1.5
BuildArchitectures: noarch

%changelog
* Sat Jun 30 1998 Oliver Andrich <oli@andrich.net>

- updated to the HTMLgen 2.1 final version

* Sat Jun 06 1998 Oliver Andrich <oli@andrich.net>

- added the new standard python icon. ;-)  

* Sat Jun 06 1998 Oliver Andrich <oli@andrich.net>

- initial release

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

%prep
%setup -n HTMLgen
%patch -p0

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/python1.5/site-packages/HTMLgen
install -m 555 $RPM_SOURCE_DIR/HTMLgen.pth $RPM_BUILD_ROOT/usr/lib/python1.5/site-packages/
install -m 555 *.py $RPM_BUILD_ROOT/usr/lib/python1.5/site-packages/HTMLgen

%clean
# Now we create the slackware packages
if [ ! -e /tmp/SLACKWARE ]; then
	mkdir /tmp/SLACKWARE
fi
cd $RPM_BUILD_ROOT
tar cvfz /tmp/SLACKWARE/python-HTMLgen-%{PACKAGE_VERSION}-%{PACKAGE_RELEASE}.tar.gz \
usr/lib/python1.5/site-packages/HTMLgen usr/lib/python1.5/site-packages/HTMLgen.pth
rm -rf $RPM_BUILD_ROOT
					
%files
%doc data html image README ChangeLog *.rc *.css
/usr/lib/python1.5/site-packages/HTMLgen
/usr/lib/python1.5/site-packages/HTMLgen.pth
