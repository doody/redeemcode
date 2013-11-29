import uuid
import base64


DEFAULT_CODE_LENGTH = 8


def get_redeem_code(length=DEFAULT_CODE_LENGTH, base64encode=False):
    generated_code = str(uuid.uuid4())
    if base64encode:
        generated_code = base64.b64encode(generated_code)

    stripped_code = generated_code[:length]
    return stripped_code