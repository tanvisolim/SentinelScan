HEADER_INFO = {

    "Strict-Transport-Security": {

        "name": "Strict Transport Security (HSTS)",

        "description":
            "Forces browsers to always use HTTPS.",

        "risk":
            "Without HSTS, users may be vulnerable to SSL stripping attacks."
    },


    "Content-Security-Policy": {

        "name": "Content Security Policy (CSP)",

        "description":
            "Helps protect against Cross-Site Scripting (XSS).",

        "risk":
            "Missing CSP increases the risk of XSS attacks."
    },


    "X-Frame-Options": {

        "name": "X-Frame-Options",

        "description":
            "Protects against clickjacking attacks.",

        "risk":
            "Attackers may embed your website inside malicious pages."
    },


    "X-Content-Type-Options": {

        "name": "X-Content-Type-Options",

        "description":
            "Prevents MIME type sniffing by browsers.",

        "risk":
            "Browsers may incorrectly interpret file types."
    },


    "Referrer-Policy": {

        "name": "Referrer-Policy",

        "description":
            "Controls what referrer information is shared.",

        "risk":
            "Sensitive URLs may leak to third-party websites."
    }

}