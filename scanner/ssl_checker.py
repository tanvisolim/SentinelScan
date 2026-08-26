import ssl
import socket

from datetime import datetime


def get_ssl_info(hostname):

    try:

        context = ssl.create_default_context()

        with socket.create_connection(
            (hostname, 443),
            timeout=5
        ) as sock:

            with context.wrap_socket(
                sock,
                server_hostname=hostname
            ) as secure_socket:

                cert = secure_socket.getpeercert()


        issuer = dict(
            x[0] for x in cert["issuer"]
        )


        valid_from = cert["notBefore"]

        valid_to = cert["notAfter"]


        expiry_date = datetime.strptime(
            valid_to,
            "%b %d %H:%M:%S %Y %Z"
        )


        days_remaining = (
            expiry_date - datetime.utcnow()
        ).days


        return {

            "status": "Valid",

            "issuer":
                issuer.get(
                    "organizationName",
                    "Unknown"
                ),

            "valid_from":
                valid_from,

            "valid_to":
                valid_to,

            "days_remaining":
                days_remaining
        }


    except Exception as e:

        return {

            "status": "Error",

            "error": str(e)
        }