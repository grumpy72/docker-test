#!/usr/bin/perl

use HTTP::Negotiate;
use Template::Multilingual;
use Date::Calc;
use CGI;
use CGI::Carp qw(fatalsToBrowser); # show errors in browser
use CGI::Session;

# new query object
my $q = CGI->new();

# new session object, will get session ID from the query object
# # will restore any existing session with the session ID in the query object
my $s = CGI::Session->new($q);

# print the HTTP header and set the session ID cookie
print $s->header();


# print some info
print "<pre>\n";

print "Hello!\n\n";
printf "Your session ID is: %s\n", $s->id;
printf "This sessin is: %s\n", $s->is_new ? 'NEW': 'old';
printf "Stored session 'test' value: '%s'\n", $q->escapeHTML($s->param('test'));
printf "CGI Params: %s\n", join ', ', $q->param;


# handle the form submit
if(defined $q->param('save')){
    # save param value in the session
    $s->param('test', $q->param('test'));
    printf "Set session value: '%s'\n", $q->escapeHTML($s->param('test'));
}
elsif(defined $q->param('delete')){
    # delete session
    $s->delete;
    print "Session will be deleted.\n";
}

print "\n</pre>\n";


# simple HTML form
printf <<'_HTML_', $q->escapeHTML($s->param('test'));
<hr/>
<form>
Session value "test": <input type="text" value="%s" name="test"/>
<button type="submit" name="save">Save Value</button>
<button type="submit" name="delete">Delete session</button>
</form>
_HTML_

__END__
