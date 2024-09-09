def camel_case_to_snake_case(input_str: str) -> str:
    """
    >>> camel_case_to_snake_case("SomeSDK")
    'some_sdk'
    >>> camel_case_to_snake_case("RServoDrive")
    'r_servo_drive'
    >>> camel_case_to_snake_case("SDKDemo")
    'sdk_demo'
    """
    result = []
    for i, char in enumerate(input_str):
        if char.isupper():
            if i > 0 and (i + 1 == len(input_str) or input_str[i + 1].isupper()):
                result.append(char.lower())
            else:
                if i > 0:
                    result.append("_")
                result.append(char.lower())
        else:
            result.append(char)
    return "".join(result)
