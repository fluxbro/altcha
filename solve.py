import hashlib
import json
import base64


def Altcha(cdata: dict) -> str:
    salt      = cdata["salt"]
    target    = cdata["challenge"]
    max_num   = cdata.get("max_number", 100000)
    algorithm = cdata.get("algorithm", "SHA-256")
    signature = cdata["signature"]

    for num in range(max_num + 1):
        digest = hashlib.sha256(f"{salt}{num}".encode()).hexdigest()
        if digest == target:
            payload = {
                "algorithm": algorithm,
                "challenge":  target,
                "number":     num,
                "salt":       salt,
                "signature":  signature,
                "verified":   True,
            }
            return base64.b64encode(json.dumps(payload).encode()).decode()

    raise ValueError("solve error")