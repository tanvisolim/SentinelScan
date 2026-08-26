import requests
from http.cookies import SimpleCookie


def check_cookies(url):

    try:

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        cookies = []

        # Get all Set-Cookie headers
        try:
            set_cookie_headers = response.raw.headers.get_all("Set-Cookie")
        except Exception:
            set_cookie_headers = []

        # Fallback
        if not set_cookie_headers:
            header = response.headers.get("Set-Cookie")

            if header:
                set_cookie_headers = [header]

        for header in set_cookie_headers:

            simple_cookie = SimpleCookie()

            try:
                simple_cookie.load(header)
            except Exception:
                continue

            for name, morsel in simple_cookie.items():

                secure = bool(morsel["secure"])
                httponly = bool(morsel["httponly"])
                samesite = morsel["samesite"]

                domain = morsel["domain"]

                if not domain:
                    domain = hostname_from_url(url)

                path = morsel["path"]

                if not path:
                    path = "/"

                recommendations = []

                # Secure
                if not secure:
                    recommendations.append(
                        "Enable the Secure flag."
                    )

                # HttpOnly
                if not httponly:
                    recommendations.append(
                        "Enable the HttpOnly flag."
                    )

                # SameSite
                if not samesite:
                    recommendations.append(
                        "Set the SameSite attribute."
                    )

                # Security level
                if secure and httponly and samesite:
                    security = "Good"

                elif secure or httponly or samesite:
                    security = "Medium"

                else:
                    security = "Weak"

                cookies.append({
                    "name": name,
                    "domain": domain,
                    "path": path,
                    "secure": secure,
                    "httponly": httponly,
                    "samesite": samesite,
                    "security": security,
                    "recommendations": recommendations
                })

        return cookies

    except Exception:
        return []


def hostname_from_url(url):

    hostname = (
        url.replace("https://", "")
           .replace("http://", "")
           .split("/")[0]
           .split(":")[0]
    )

    return hostname