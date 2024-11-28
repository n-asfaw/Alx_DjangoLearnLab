"Introduction to django"

## Security Measures Implemented

### Secure Settings:
- `DEBUG` is set to `False` in production to prevent exposure of sensitive data.
- Browser security headers (`X_FRAME_OPTIONS`, `SECURE_BROWSER_XSS_FILTER`, `SECURE_CONTENT_TYPE_NOSNIFF`) are configured to prevent common attacks.
- CSRF and session cookies are configured to be transmitted only over HTTPS.

### CSRF Protection:
- All forms include `{% csrf_token %}` to prevent CSRF attacks.

### SQL Injection Prevention:
- All database queries use Django’s ORM, avoiding raw SQL queries.
- User input is validated and sanitized using Django forms.

### Content Security Policy:
- A restrictive Content Security Policy is enforced using the `django-csp` middleware.
