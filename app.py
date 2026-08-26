from flask import Flask, render_template, request

from scanner.headers_checker import check_headers
from scanner.cookies_checker import check_cookies
from scanner.ssl_checker import get_ssl_info
from scanner.score_engine import calculate_score
from scanner.recommendations import HEADER_INFO


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():

    url = request.form.get("url", "").strip()

    if not url:
        return render_template("index.html")

    # Add HTTPS if user doesn't enter it
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # Get hostname
    hostname = (
        url.replace("https://", "")
           .replace("http://", "")
           .split("/")[0]
           .split(":")[0]
    )

    # Security headers
    header_results = check_headers(url)

    # Cookies
    cookie_info = check_cookies(url)

    # SSL
    ssl_info = get_ssl_info(hostname)

    # Score
    score = calculate_score(header_results)

    return render_template(
        "index.html",
        result=header_results,
        url=url,
        score=score,
        ssl_info=ssl_info,
        cookie_info=cookie_info,
        header_info=HEADER_INFO
    )


if __name__ == "__main__":
    app.run(debug=True)