# AI Usage Report
## Generated on 2025-05-17 13:14

## Search Results:

## 0001_initial.py
- Line : ('email', models.EmailField(max_length=254)),

## 0001_initial.py

## settings.py
- Line : ACCOUNT_EMAIL_VERIFICATION = 'none'

## global_settings.py
- Line : # [('Full Name', 'email@example.com'), ('Full Name', 'anotheremail@example.com')]
- Line : # Hosts/domain names that are valid for this site.
- Line : # "*" matches anything, ".example.com" matches example.com and all subdomains
- Line : ("az", gettext_noop("Azerbaijani")),
- Line : ("th", gettext_noop("Thai")),
- Line : ("uk", gettext_noop("Ukrainian")),
- Line : LANGUAGE_COOKIE_DOMAIN = None
- Line : # notifications and other various emails.
- Line : # Email address that error messages come from.
- Line : SERVER_EMAIL = "root@localhost"
- Line : # The email backend to use. For possible shortcuts see django.core.mail.
- Line : # to a module that defines an EmailBackend class.
- Line : EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
- Line : # Host for sending email.
- Line : EMAIL_HOST = "localhost"
- Line : # Port for sending email.
- Line : EMAIL_PORT = 25
- Line : EMAIL_USE_LOCALTIME = False
- Line : # Optional SMTP authentication information for EMAIL_HOST.
- Line : EMAIL_HOST_USER = ""
- Line : EMAIL_HOST_PASSWORD = ""
- Line : EMAIL_USE_TLS = False
- Line : EMAIL_USE_SSL = False
- Line : EMAIL_SSL_CERTFILE = None
- Line : EMAIL_SSL_KEYFILE = None
- Line : EMAIL_TIMEOUT = None
- Line : # Default email address to use for various automated correspondence from
- Line : DEFAULT_FROM_EMAIL = "webmaster@localhost"
- Line : # Subject-line prefix for email messages send with django.core.mail.mail_admins
- Line : # or ...mail_managers.  Make sure to include the trailing space.
- Line : EMAIL_SUBJECT_PREFIX = "[Django] "
- Line : # Whether to append trailing slashes to URLs.
- Line : # Whether to prepend the "www." subdomain to URLs that don't have it.
- Line : #         re.compile(r'^EmailSiphon.*'),
- Line : # be reported by BrokenLinkEmailsMiddleware. Here are a few examples:
- Line : # hashing algorithms. Set this in your settings, or Django will complain
- Line : # read before a SuspiciousOperation (RequestDataTooBig) is raised.
- Line : # SuspiciousOperation (TooManyFieldsSent) is raised.
- Line : # before a SuspiciousOperation (TooManyFilesSent) is raised.
- Line : # The directory where this setting is pointing should contain subdirectories
- Line : # named as the locales, containing a formats.py file
- Line : # Default formatting for date objects. See all available format strings here:
- Line : # Default formatting for datetime objects. See all available format strings here:
- Line : # Default formatting for time objects. See all available format strings here:
- Line : # See all available format strings here:
- Line : # See all available format strings here:
- Line : # Default short formatting for date objects. See all available format strings here:
- Line : # See all available format strings here:
- Line : # See all available format string here:
- Line : # See all available format string here:
- Line : # See all available format string here:
- Line : # A string like "example.com", or None for standard domain cookie.
- Line : SESSION_COOKIE_DOMAIN = None
- Line : CSRF_FAILURE_VIEW = "django.views.csrf.csrf_failure"
- Line : CSRF_COOKIE_DOMAIN = None
- Line : SECURE_HSTS_INCLUDE_SUBDOMAINS = False

## hashers.py
- Line : # If the hasher didn't change (we don't protect against enumeration if it
- Line : Turn a plain-text password into a hash for database storage
- Line : which disallows logins. Additional random string reduces chances of gaining
- Line : raise TypeError(
- Line : raise ImproperlyConfigured(
- Line : raise ValueError(
- Line : get_hasher() to return hasher. Raise ValueError if
- Line : # Ancient versions of Django created plain MD5 passwords and accepted
- Line : raise ValueError(
- Line : raise ValueError(
- Line : raise NotImplementedError(
- Line : raise TypeError("password must be provided.")
- Line : raise ValueError("salt must be provided and cannot contain $.")
- Line : raise NotImplementedError(
- Line : The result is a dictionary and should contain `algorithm`, `hash`, and
- Line : raise NotImplementedError(
- Line : raise NotImplementedError(
- Line : Taking PBKDF2 as an example, if `encoded` contains 20000 iterations and
- Line : raise ValueError("salt must be empty.")
- Line : raise ValueError("salt must be empty.")
- Line : raise ValueError("salt must be of length 2.")
- Line : raise TypeError("hash must be provided.")

## views.py
- Line : if timezone.is_naive(new_lastmod):
- Line : absolute_url = "%s://%s%s" % (protocol, req_site.domain, sitemap_url)
- Line : raise Http404("No sitemap available for section: %r" % section)
- Line : raise Http404("Page %s empty" % page)
- Line : raise Http404("No page '%s'" % page)

## makemessages.py
- Line : raise CommandError(
- Line : def __init__(self, command, domain, translatable):
- Line : self.domain = domain
- Line : if self.domain == "djangojs":
- Line : elif self.domain == "django":
- Line : }.get(self.domain)
- Line : if self.domain == "djangojs":
- Line : elif self.domain == "django":
- Line : "--domain",
- Line : help='The domain of the message files (default: "django").',
- Line : 'if the domain is "djangojs"). Separate multiple extensions with '
- Line : self.domain = options["domain"]
- Line : raise CommandError(
- Line : if self.domain not in ("django", "djangojs"):
- Line : raise CommandError(
- Line : "currently makemessages only supports domains "
- Line : if self.domain == "djangojs":
- Line : if (not locale and not exclude and not process_all) or self.domain is None:
- Line : raise CommandError(
- Line : if self.settings_available:
- Line : raise CommandError("Unable to get gettext version. Is it installed?")
- Line : def settings_available(self):
- Line : potfile = os.path.join(path, "%s.pot" % self.domain)
- Line : raise CommandError(
- Line : pot_path = os.path.join(path, "%s.pot" % self.domain)
- Line : if self.settings_available:
- Line : if self.domain not in ("djangojs", "django"):
- Line : build_file = self.build_file_class(self, self.domain, translatable)
- Line : raise
- Line : if self.domain == "djangojs":
- Line : self.domain,
- Line : elif self.domain == "django":
- Line : self.domain,
- Line : raise CommandError(
- Line : raise CommandError(
- Line : potfile = os.path.join(locale_dir, "%s.pot" % self.domain)
- Line : Create or update the PO file for self.domain and `locale`.
- Line : pofile = os.path.join(basedir, "%s.po" % self.domain)
- Line : raise CommandError(
- Line : "#. #-#-#-#-#  %s.pot (PACKAGE VERSION)  #-#-#-#-#\n" % self.domain, ""
- Line : raise CommandError(
- Line : if self.domain == "djangojs":
- Line : domains = ("djangojs", "django")
- Line : domains = ("django",)
- Line : for domain in domains:
- Line : django_dir, "conf", "locale", locale, "LC_MESSAGES", "%s.po" % domain

## paginator.py
- Line : raise ValueError
- Line : raise PageNotAnInteger(_("That page number is not an integer"))
- Line : raise EmptyPage(_("That page number is less than 1"))
- Line : raise EmptyPage(_("That page contains no results"))
- Line : raise TypeError(

## creation.py
- Line : Encapsulate backend-specific differences pertaining to creation and
- Line : self.mark_expected_failures_and_skips()
- Line : # Disable constraint checks, because some databases (MySQL) doesn't
- Line : with self.connection.constraint_checks_disabled():
- Line : # because constraint checks were disabled.
- Line : self.connection.check_constraints(table_names=table_names)
- Line : # give it the keepdb param. See create_test_db for details.
- Line : raise NotImplementedError(
- Line : def mark_expected_failures_and_skips(self):
- Line : Mark tests in Django's test suite which are expected failures on this
- Line : from unittest import expectedFailure, skip
- Line : for test_name in self.connection.features.django_test_expected_failures:
- Line : # Importing a test app that isn't installed raises RuntimeError.
- Line : setattr(test_case, test_method_name, expectedFailure(test_method))
- Line : # Importing a test app that isn't installed raises RuntimeError.

## compiler.py
- Line : # DELETE FROM cannot be used when filtering against aggregates or
- Line : # Ignore ordering if it contains joined fields, because
- Line : raise FieldError
- Line : # Ignore ordering if it contains annotations, because they're

## base.py
- Line : raise ImproperlyConfigured(
- Line : raise ImproperlyConfigured("Error loading cx_Oracle module: %s" % e)
- Line : # cx_Oracle raises a cx_Oracle.DatabaseError exception with the
- Line : #            'ORA-02291: integrity constraint (TEST_DJANGOTEST.SYS
- Line : #            'ORA-00001: unique constraint (DJANGOTEST.DEFERRABLE_
- Line : #               PINK_CONSTRAINT) violated
- Line : raise IntegrityError(*tuple(e.args))
- Line : raise
- Line : raise AttributeError("operators not available as class attribute")
- Line : # types, as strings. Column-type strings can contain format strings; they'll
- Line : # be interpolated against the values of Field.__dict__ before being output.
- Line : data_type_check_constraints = {
- Line : "contains": (
- Line : "icontains": (
- Line : "contains": "LIKEC %s ESCAPE '\\'",
- Line : "icontains": "LIKEC UPPER(%s) ESCAPE '\\'",
- Line : "contains": "'%%' || {} || '%%'",
- Line : "icontains": "'%%' || UPPER({}) || '%%'",
- Line : % self._standard_operators["contains"],
- Line : def check_constraints(self, table_names=None):
- Line : Check constraints by setting them to immediate. Return them to deferred
- Line : cursor.execute("SET CONSTRAINTS ALL IMMEDIATE")
- Line : cursor.execute("SET CONSTRAINTS ALL DEFERRED")
- Line : # Try dict handling; if that fails, treat as sequence
- Line : # Try dict handling; if that fails, treat as sequence
- Line : # cx_Oracle wants no trailing ';' for SQL statements.  For PL/SQL, it
- Line : # it does want a trailing ';' but not a trailing '/'.  However, these

## base.py
- Line : raise ImproperlyConfigured("Error loading psycopg2 or psycopg module")
- Line : raise ImproperlyConfigured(
- Line : raise ImproperlyConfigured(
- Line : # types, as strings. Column-type strings can contain format strings; they'll
- Line : # be interpolated against the values of Field.__dict__ before being output.
- Line : data_type_check_constraints = {
- Line : "contains": "LIKE %s",
- Line : "icontains": "LIKE UPPER(%s)",
- Line : "contains": "LIKE '%%' || {} || '%%'",
- Line : "icontains": "LIKE '%%' || UPPER({}) || '%%'",
- Line : raise ImproperlyConfigured(
- Line : raise ImproperlyConfigured(
- Line : # - after connecting to the database in order to obtain the database's
- Line : raise ImproperlyConfigured(
- Line : def check_constraints(self, table_names=None):
- Line : Check constraints by setting them to immediate. Return them to deferred
- Line : cursor.execute("SET CONSTRAINTS ALL IMMEDIATE")
- Line : cursor.execute("SET CONSTRAINTS ALL DEFERRED")
- Line : raise
- Line : "to avoid running initialization queries against the production "
- Line : raise

## schema.py
- Line : # Setting all constraints to IMMEDIATE to allow changing data in the same
- Line : "; SET CONSTRAINTS ALL IMMEDIATE"
- Line : # Setting the constraint to IMMEDIATE to allow changing data in the same
- Line : "CONSTRAINT %(name)s REFERENCES %(to_table)s(%(to_column)s)%(deferrable)s"
- Line : "; SET CONSTRAINTS %(namespace)s%(name)s IMMEDIATE"
- Line : # Setting the constraint to IMMEDIATE runs any deferred checks to allow
- Line : "SET CONSTRAINTS %(name)s IMMEDIATE; "
- Line : "ALTER TABLE %(table)s DROP CONSTRAINT %(name)s"

## writer.py
- Line : # Only iterate over remaining arguments
- Line : if arg_name in kwargs:  # Don't sort to maintain signature order
- Line : raise ValueError(
- Line : raise ValueError(

## datastructures.py
- Line : the SQL domain.
- Line : # Add a join condition for each pair of joining columns.
- Line : raise ValueError(

## expressions.py
- Line : raise NotImplementedError(
- Line : raise NotImplementedError(
- Line : raise NotImplementedError(
- Line : raise NotImplementedError(
- Line : raise NotImplementedError(
- Line : raise NotImplementedError(
- Line : Where `sql` is a string containing ordered sql parameters to be
- Line : raise NotImplementedError("Subclasses must implement as_sql()")
- Line : def contains_aggregate(self):
- Line : expr and expr.contains_aggregate for expr in self.get_source_expressions()
- Line : def contains_over_clause(self):
- Line : expr and expr.contains_over_clause for expr in self.get_source_expressions()
- Line : def contains_column_references(self):
- Line : expr and expr.contains_column_references
- Line : def contains_subquery(self):
- Line : expr and (getattr(expr, "subquery", False) or expr.contains_subquery)
- Line : raise FieldError("Cannot resolve expression type, unknown output_field")
- Line : raise
- Line : If all sources are None, then an error is raised higher up the stack in
- Line : raise FieldError(
- Line : "Expression contains mixed types: %s, %s. You must "
- Line : if not self.contains_aggregate:
- Line : # i.e. if one of the supported databases is raising an error (rather than
- Line : # return NULL) for `val <op> NULL`, then Django raises FieldError.
- Line : raise FieldError(
- Line : raise DatabaseError(
- Line : An object that contains a reference to an outer query.
- Line : contains_aggregate = False
- Line : contains_over_clause = False
- Line : raise ValueError(
- Line : "This queryset contains a reference to an outer query and may "
- Line : if col.contains_over_clause:
- Line : raise NotSupportedError(
- Line : contains_aggregate = False
- Line : contains_over_clause = False
- Line : raise TypeError(
- Line : raise
- Line : contains_column_references = True
- Line : An expression containing multiple expressions. Can be used to provide a
- Line : raise ValueError(
- Line : raise TypeError("Cannot negate non-conditional expressions.")
- Line : raise TypeError(
- Line : raise ValueError("An empty Q() can't be used as a When() condition.")
- Line : raise TypeError("Positional arguments must all be When objects.")
- Line : An explicit subquery. It may contain OuterRef() references to the outer
- Line : contains_aggregate = False
- Line : raise ValueError("nulls_first and nulls_last are mutually exclusive")
- Line : # raise ValueError(
- Line : raise ValueError("expression must be an expression type")
- Line : # Although the main expression may either be an aggregate or an
- Line : contains_aggregate = False
- Line : contains_over_clause = True
- Line : raise ValueError(
- Line : raise ValueError(
- Line : raise NotSupportedError("This backend does not support window expressions.")
- Line : raise NotImplementedError("Subclasses must implement window_frame_start_end().")

## models.py
- Line : from itertools import chain
- Line : Return a dict containing the data in ``instance`` suitable for passing as
- Line : for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
- Line : Return a dictionary containing form fields for the given model.
- Line : chain(opts.concrete_fields, sortable_private_fields, opts.many_to_many)
- Line : raise FieldError(
- Line : raise TypeError("formfield_callback must be a function or callable")
- Line : raise TypeError(msg)
- Line : raise ImproperlyConfigured(
- Line : raise FieldError(message)
- Line : raise ValueError("ModelForm has no model class specified.")
- Line : # It is False by default so overriding self.clean() and failing to call
- Line : # Exclude fields that failed form validation. There's no need for
- Line : # from raising a required error. Note: don't exclude the field from
- Line : # Allow the model generated by construct_instance() to raise
- Line : validation errors if any were raised.
- Line : for f in chain(opts.many_to_many, opts.private_fields):
- Line : raise ValueError(
- Line : Return a ModelForm containing form fields for the given model. You can
- Line : raise ImproperlyConfigured(
- Line : include_meta_constraints=True,
- Line : # if we've already seen it then we have a uniqueness failure
- Line : # if we've already seen it then we have a uniqueness failure
- Line : raise ValidationError(errors)
- Line : raise ImproperlyConfigured(
- Line : def _get_foreign_key(parent_model, model, fk_name=None, can_fail=False):
- Line : (return None if can_fail is True and no such field exists). If fk_name is
- Line : provided, assume it is the name of the ForeignKey field. Unless can_fail is
- Line : True, raise an exception if there isn't a ForeignKey from model to
- Line : raise ValueError(
- Line : raise ValueError(
- Line : if can_fail:
- Line : raise ValueError(
- Line : raise ValueError(
- Line : raise ValidationError(
- Line : "Select a valid choice. That choice is not one of the available choices."
- Line : raise ValidationError(
- Line : "Select a valid choice. %(value)s is not one of the available choices."
- Line : raise ValidationError(self.error_messages["required"], code="required")
- Line : raise ValidationError(
- Line : corresponding objects. Raise a ValidationError if a given value is
- Line : raise ValidationError(
- Line : raise ValidationError(
- Line : raise ValidationError(

## client.py
- Line : self.redirect_chain = last_response.redirect_chain
- Line : ), "Cannot read more than the available bytes from the HTTP incoming data."
- Line : ), "Cannot read more than the available bytes from the HTTP incoming data."
- Line : raise ValueError("Unable to write a payload after it's been read")
- Line : # settings weren't available.
- Line : if self._middleware_chain is None:
- Line : # required for backwards compatibility with external tests against
- Line : # settings weren't available.
- Line : if self._middleware_chain is None:
- Line : await sync_to_async(request_started.send, thread_sensitive=False)(
- Line : # for backwards compatibility with external tests against admin views.
- Line : response = await self.get_response_async(request)
- Line : await sync_to_async(response.close, thread_sensitive=False)()
- Line : raise TypeError(
- Line : get_request = await rf.get('/hello/')
- Line : post_request = await rf.post('/submit/', {'foo': 'bar'})
- Line : data, re-raise the signaled exception, and clear the signaled exception
- Line : if self.raise_request_exception:
- Line : raise exc_value
- Line : # Create a fake request to store login details.
- Line : "domain": settings.SESSION_COOKIE_DOMAIN,
- Line : raise ValueError(
- Line : obtain the response that the server gave to those requests.
- Line : The server Response objects are annotated with the details
- Line : Client objects are stateful - they will retain cookie (and
- Line : thus session) details for the lifetime of the Client instance.
- Line : the like - it is here to allow testing against the
- Line : raise_request_exception=True,
- Line : self.raise_request_exception = raise_request_exception
- Line : # Add any rendered template detail to the response.
- Line : response.redirect_chain = []
- Line : redirect_chain = response.redirect_chain
- Line : redirect_chain.append((response_url, response.status_code))
- Line : response.redirect_chain = redirect_chain
- Line : if redirect_chain[-1] in redirect_chain[:-1]:
- Line : raise RedirectCycleError(
- Line : if len(redirect_chain) > 20:
- Line : # Such a lengthy chain likely also means a loop, but one with
- Line : raise RedirectCycleError("Too many redirects.", last_response=response)
- Line : raise_request_exception=True,
- Line : self.raise_request_exception = raise_request_exception
- Line : raise NotImplementedError(
- Line : response = await self.handler(scope)
- Line : # Add any rendered template detail to the response.

## glibc.py
- Line : # os.confstr() or CS_GNU_LIBC_VERSION not available (or a bad value)...
- Line : # main program". This way we can let the linker do the work to figure out
- Line : in case the lookup fails.

## langthaimodel.py
- Line : THAI_LANG_MODEL = {
- Line : # 255: Undefined characters that did not exist in training text
- Line : TIS_620_THAI_CHAR_TO_ORDER = {
- Line : TIS_620_THAI_MODEL = SingleByteCharSetModel(charset_name='TIS-620',
- Line : language='Thai',
- Line : char_to_order_map=TIS_620_THAI_CHAR_TO_ORDER,
- Line : language_model=THAI_LANG_MODEL,

## sbcsgroupprober.py
- Line : # Lesser General Public License for more details.
- Line : from .langthaimodel import TIS_620_THAI_MODEL
- Line : #       and several tests failed that did not before. Some thought
- Line : #       after we retrain model.
- Line : SingleByteCharSetProber(TIS_620_THAI_MODEL),

## idnadata.py

## uts46data.py

## connection.py
- Line : from .wait import NoWayToWaitForSocketError, wait_for_read
- Line : return wait_for_read(sock, timeout=0.0)
- Line : except NoWayToWaitForSocketError:  # Platform-specific: AppEngine
- Line : # Using the value from allowed_gai_family() in the context of getaddrinfo lets
- Line : family = allowed_gai_family()
- Line : return six.raise_from(
- Line : raise err
- Line : raise socket.error("getaddrinfo returns an empty list")
- Line : def allowed_gai_family():

## labels.py
- Line : :license: BSD, see LICENSE for details.
- Line : 'x-mac-ukrainian':     'x-mac-cyrillic',

## mklabels.py
- Line : :license: BSD, see LICENSE for details.
- Line : :license: BSD, see LICENSE for details.
- Line : if __name__ == '__main__':

## sdist.py
- Line : log.warn("data_files contains unexpected objects")
- Line : # The manifest must contain UTF-8. See #303.

## sdist.py
- Line : "List of available source distribution formats:")
- Line : "list available distribution formats", show_formats),
- Line : raise DistutilsOptionError(
- Line : # 'filelist' contains the list of files that will make up the
- Line : # plain file
- Line : # the call above can raise a DistutilsTemplateError for
- Line : log.info("not writing to manually maintained "
- Line : (if hard linking is unavailable) those files into place.
- Line : directory named after the distribution, containing only the files
