import requests


def check_headers(url):

    try:

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        headers = response.headers

        return {
            "Strict-Transport-Security":
                headers.get("Strict-Transport-Security"),

            "Content-Security-Policy":
                headers.get("Content-Security-Policy"),

            "X-Frame-Options":
                headers.get("X-Frame-Options"),

            "X-Content-Type-Options":
                headers.get("X-Content-Type-Options"),

            "Referrer-Policy":
                headers.get("Referrer-Policy")
        }

    except Exception as e:

        return {
            "Error": str(e)
        }